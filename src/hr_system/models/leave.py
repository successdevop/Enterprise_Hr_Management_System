from datetime import datetime
from enum import Enum
from src.hr_system.models.employee import Employee
from src.hr_system.utils.exceptions import ValidationError


class LeaveStatus(Enum):
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class LeaveRequest:
    def __init__(self, employee: Employee, days: int):
        if days <= 0:
            raise ValidationError("Leave days must be greater than 0")

        self.days = days
        self.employee = employee
        self.status = LeaveStatus.PENDING
        self.created_at = datetime.now()
        self.reviewed_by = None

    def approve_leave(self, manager: Employee):
        if self.status != LeaveStatus.PENDING:
            raise ValidationError("Leave request already processed")

        self.status = LeaveStatus.APPROVED
        self.reviewed_by = {manager.name, manager.role}

    def reject_leave(self, manager: Employee):
        if self.status != LeaveStatus.PENDING:
            raise ValidationError("Leave request already processed")

        self.status = LeaveStatus.REJECTED
        self.reviewed_by = {manager.name, manager.role}

    def to_dict(self):
        return {
            "days": self.days,
            "employee": self.employee.to_dict(show_all=False) if self.employee else None,
            "status": self.status.value if hasattr(self.status, "value") else self.status,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data: dict) -> "LeaveRequest":
        leaverequest = cls(
            days=data["days"],
            employee=Employee.from_dict_to_object(data["employee"])
        )
        leaverequest.status = data["status"]
        leaverequest.created_at = data["created_at"]
        return leaverequest

    def __repr__(self):
        return f"<LeaveRequest name:{self.employee.name} | days_of_leave:{self.days} | status:{self.status.value}>"
