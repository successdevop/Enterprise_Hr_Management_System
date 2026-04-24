from typing import Optional
from src.hr_system.repositories.employee_repo import EmployeeRepository
from src.hr_system.utils.utils import Utils
from src.hr_system.utils.exceptions import UserAlreadyExistError, AuthenticationError
from src.hr_system.storage.logger import Logger
from src.hr_system.storage.config import LOGS_FILE
from src.hr_system.models.role import Role
from src.hr_system.models.employee import Employee
from src.hr_system.services.permision_service import PermissionService


class AuthService:
    def __init__(self, employee_repo: EmployeeRepository):
        self._employee_repo = employee_repo
        self.current_user = Optional[Employee]

    def get_employee_repo(self):
        PermissionService.required_role(self.current_user, [Role.ADMIN])
        return self._employee_repo

    def register(self, name: str, email: str, age: int, origin: str, role: Role, salary: float, password: str):
        from src.hr_system.models.employee import Employee
        Utils.validate_email(email)

        if self._employee_repo.get_by_email(email):
            raise UserAlreadyExistError(f"{email} already exists")

        employee = Employee(name.strip().title(), email.strip().lower(), age, origin.strip().title(), role, salary)

        Utils.validate_name(name)
        Utils.validate_age(age)
        Utils.validate_name(origin)
        Utils.validate_amount_input(salary)

        employee.set_password(password)

        self._employee_repo.save_employee(employee)

        Logger.info(f"Congratulations {name}, registration successful", LOGS_FILE)
        print(f"Registration Successful! ({email})")
        return employee

    def login(self, email, password):
        user = self._employee_repo.get_by_email(email)

        if not user:
            Logger.error(f"Login Failed: {email} not found")
            raise AuthenticationError("user not found")

        if not user.check_password(password):
            Logger.error(f"Login Failed: wrong password for {email}")
            raise AuthenticationError("invalid email or password")

        if not user.isActive:
            Logger.error(f"Login Failed: Account is deactivated (email:{email}, name:{user.name})")
            raise AuthenticationError("Account is deactivated")

        self.current_user = user
        Logger.info(f"Login successful: {email.lower()}", LOGS_FILE)
        print(f"Login successful: {email.lower()}")
        return user

    def logout(self):
        if self.current_user:
            Logger.info(f"User logged out: {self.current_user.email}", LOGS_FILE)
            print(f"User logged out: {self.current_user.email}")
            self.current_user = None
