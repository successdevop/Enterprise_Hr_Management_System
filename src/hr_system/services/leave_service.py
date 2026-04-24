from src.hr_system.repositories.leave_repo import LeaveRepo
from src.hr_system.models.employee import Employee
from src.hr_system.models.leave import LeaveRequest, LeaveType
from src.hr_system.models.role import Role
from src.hr_system.storage.logger import Logger
from src.hr_system.storage.config import LOGS_FILE
from src.hr_system.utils.exceptions import ValidationError, AuthorizationError
from src.hr_system.services.permision_service import PermissionService


class LeaveServices:
    def __init__(self, leave_repo: LeaveRepo):
        self.leave_repo = leave_repo

    def apply_for_leave(self, employee: Employee, days: int, leave_t: LeaveType):
        if employee.role.value in [Role.ADMIN, Role.HR]:
            balance = 30
        else:
            balance = 21

        if days > balance:
            raise ValidationError("Exceeded your approvable leave days")

        leave_request = LeaveRequest(employee, days, leave_t)
        self.leave_repo.save_leave_request(leave_request)
        Logger.info(f"{employee.employee_id} applied for {days} days of {LeaveType.ANNUAL.value} leave request", LOGS_FILE)
        return leave_request

    def approve_leave(self, executive: Employee, leave: LeaveRequest):
        PermissionService.required_role(executive, [Role.ADMIN, Role.HR, Role.MANAGER])

        if executive.role == Role.MANAGER:
            if executive.department[0] not in leave.employee.department:
                raise AuthorizationError("You can only approve your team member's leave")

        leave.approve_leave(executive)
        self.leave_repo.save_leave_request(leave)
        Logger.info(f"{leave.employee.name} leave request approved by {executive.role.value} {executive.name}",
                    LOGS_FILE)

    def reject_leave(self, executive: Employee, leave: LeaveRequest):
        PermissionService.required_role(executive, [Role.ADMIN, Role.HR, Role.MANAGER])

        if executive.role == Role.MANAGER:
            if executive.department[0] not in leave.employee.department:
                raise AuthorizationError("You can only approve your team member's leave")

        leave.reject_leave(executive)
        Logger.info(f"{leave.employee.name} leave request rejected by {executive.role.value} {executive.name}",
                    LOGS_FILE)

    def view_all_pending_request(self, executive: Employee):
        PermissionService.required_role(executive, [Role.ADMIN, Role.HR])
        request = self.leave_repo.get_all_pending_leave_request()
        print(request)

    def view_all_request(self, executive: Employee):
        PermissionService.required_role(executive, [Role.ADMIN, Role.HR])
        request = self.leave_repo.get_all_leave_request()
        print(request)

    def view_employee_leave_request(self, executive: Employee, employee: Employee):
        PermissionService.required_role(executive, [Role.ADMIN, Role.HR])
        request = self.leave_repo.get_request_by_employee(employee)
        print(request.to_dict())




