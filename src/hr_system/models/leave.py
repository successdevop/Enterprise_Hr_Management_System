from datetime import datetime
from enum import Enum
from src.hr_system.models.employee import Employee
from src.hr_system.utils.exceptions import ValidationError
from src.hr_system.models.employee import Role


class LeaveStatus(Enum):
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class LeaveType(Enum):
    ANNUAL = "Annual_leave"
    SICK = "Sick_leave"
    PATERNITY_MATERNITY = "Parental_leave"
    UNPAID = "Unpaid_leave"
    EMMERGENCY = "Emergency_leave"


class LeaveRequest:
    def __init__(self, employee: Employee, days: int, leave_type: LeaveType):
        if days <= 0:
            raise ValidationError("Leave days must be greater than 0")

        if employee.role.value in [Role.ADMIN, Role.HR]:
            self.total_approvable_year_leave = 30
        else:
            self.total_approvable_year_leave = 21

        self.days = days
        self.employee = employee
        self.status = LeaveStatus.PENDING
        self.type = leave_type
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_approved = None
        self.leave_balance = self.total_approvable_year_leave - self.days
        self.reviewed_by = []

    def approve_leave(self, manager: Employee):
        if self.status != LeaveStatus.PENDING:
            raise ValidationError("Leave request already processed")

        self.status = LeaveStatus.APPROVED
        self.reviewed_by.append({"name": manager.name, "role": manager.role.value})

    def reject_leave(self, manager: Employee):
        if self.status != LeaveStatus.PENDING:
            raise ValidationError("Leave request already processed")

        self.status = LeaveStatus.REJECTED
        self.reviewed_by.append({"name": manager.name, "role": manager.role.value})

    def increase_total_leave_days(self, days):
        self.total_approvable_year_leave += days

    def to_dict(self):
        return {
            "days": self.days,
            "total_leave_in_a_year": self.total_approvable_year_leave,
            "total_leave_balance": self.leave_balance,
            "leave_type": self.type.value,
            "status": self.status.value if hasattr(self.status, "value") else self.status,
            "created_at": self.created_at,
            "employee": self.employee.to_dict(show_all=False) if self.employee else None,
            "time_approved": self.time_approved,
            "leave_reviewed_by": self.reviewed_by
        }

    @classmethod
    def from_dict(cls, data: dict) -> "LeaveRequest":
        status = data.get("status")
        if isinstance(status, str) and hasattr(LeaveStatus, status.upper()):
            status = Role[status.upper()]

        leaverequest = cls(
            days=data["days"],
            leave_type=data["leave_type"],
            employee=Employee.from_dict_to_object(data["employee"])
        )
        leaverequest.total_approvable_year_leave = data.get("total_leave_in_a_year")
        leaverequest.leave_balance = data.get("total_leave_balance")
        leaverequest.status = status
        leaverequest.reviewed_by = data.get("leave_reviewed_by", [])
        leaverequest.created_at = data.get("created_at")
        leaverequest.time_approved = data.get("time_approved")
        return leaverequest

    def __repr__(self):
        return f"<LeaveRequest name:{self.employee.name} | days_of_leave:{self.days} | status:{self.status.value}>"
