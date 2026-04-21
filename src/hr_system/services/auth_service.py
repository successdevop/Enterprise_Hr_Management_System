from src.hr_system.repositories.employee_repo import EmployeeRepository
from src.hr_system.utils.utils import Utils
from src.hr_system.utils.exceptions import UserAlreadyExistError, AuthenticationError
from src.hr_system.storage.logger import Logger
from src.hr_system.storage.config import LOGS_FILE
from src.hr_system.models.role import Role


class AuthService:
    def __init__(self, employee_repo: EmployeeRepository):
        self._employee_repo = employee_repo
        self._current_user = None

    def register(self, name: str, email: str, age: int, origin: str, role: Role, salary: float, password: str):
        from src.hr_system.models.employee import Employee

        email = email.lower().strip()
        Utils.validate_email(email)

        if self._employee_repo.get_by_email(email):
            raise UserAlreadyExistError(f"{email} already exists")

        employee = Employee(name, email, age, origin, role, salary)

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
        email = email.lower().strip()
        user = self._employee_repo.get_by_email(email)

        if not user:
            Logger.error(f"Login Failed: {email} not found")
            raise AuthenticationError("user not found")

        if not user.check_password(password):
            Logger.error(f"Login Failed: wrong password for {email}")
            raise AuthenticationError("invalid email or password")

        if not user.isActive:
            Logger.error(f"Login Failed: Account is deactivated ({email})")
            raise AuthenticationError("Account is deactivated")

        self._current_user = user
        Logger.info(f"Login successful: {email}", LOGS_FILE)
        print(f"Login successful: {email}")
        return user

    def logout(self):
        if self._current_user:
            Logger.info(f"User logged out: {self._current_user.email}", LOGS_FILE)
            print(f"User logged out: {self._current_user.email}")
            self._current_user = None

