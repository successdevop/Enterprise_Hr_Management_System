from src.hr_system.repositories.leave_repo import LeaveRepo
from src.hr_system.models.employee import Employee
from src.hr_system.models.leave import LeaveRequest
from src.hr_system.models.role import Role
from src.hr_system.storage.logger import Logger
from src.hr_system.storage.config import LOGS_FILE
from src.hr_system.utils.exceptions import ValidationError, AuthorizationError
from src.hr_system.services.permision_service import PermissionService


class LeaveServices:
    def __init__(self, leave_repo: LeaveRepo):
        self.leave_repo = leave_repo
        self.leave_balance = {}

    def _approvable_leave_days(self, employee: Employee):
        if employee.role.value == "Employee":
            self.leave_balance[employee.employee_id] = 14
        else:
            self.leave_balance[employee.employee_id] = 21

    def apply_for_leave(self, employee: Employee, days: int):
        self._approvable_leave_days(employee)

        balance = self.leave_balance.get(employee.employee_id, 0)

        if days > balance:
            raise ValidationError("Exceeded your approvable leave days")

        leave_request = LeaveRequest(employee, days)
        self.leave_repo.save_leave_request(leave_request)
        Logger.info(f"{employee.employee_id} applied for {days} days leave request", LOGS_FILE)

        return leave_request

    def approve_leave(self, executive: Employee, leave: LeaveRequest):
        PermissionService.required_role(executive, [Role.ADMIN, Role.HR, Role.MANAGER])

        if executive.role == Role.MANAGER:
            if executive.department[0] not in leave.employee.department:
                raise AuthorizationError("You can only approve your team member's leave")

        leave.approve_leave(executive)
        self.leave_balance[leave.employee.employee_id] -= leave.days
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




