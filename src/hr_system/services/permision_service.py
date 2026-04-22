from src.hr_system.models.role import Role
from src.hr_system.models.employee import Employee
from src.hr_system.utils.exceptions import AuthorizationError, ValidationError
from typing import List


class PermissionService:
    @staticmethod
    def required_role(user: Employee, allowed_role: List[Role]):
        if not isinstance(user, Employee):
            raise ValidationError("Invalid user")

        if user.role not in allowed_role:
            raise AuthorizationError(f"{user.role.value} is not allowed to perform his action")
