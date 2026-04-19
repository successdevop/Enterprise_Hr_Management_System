from src.hr_system.repositories.employee_repo import EmployeeRepository
from src.hr_system.utils.utils import Utils


class AuthService:
    def __init__(self, employee_repo: EmployeeRepository):
        self._employee_repo = employee_repo
        self._current_user = None

    def register(self, name, email, age, origin, role, salary, password):
        from src.hr_system.models.employee import Employee

        email = email.lower().strip()
        if not Utils.validate_email(email):
            return

        if self._employee_repo.get_by_email(email):
            raise ValueError("User already exist")

        employee = Employee(name, email, age, origin, role, salary)

        if (not Utils.validate_name(name) or not Utils.validate_age(age)
                or not Utils.validate_name(origin) or not Utils.validate_amount_input(salary)):
            return

        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters")
        employee.set_password(password)

        self._employee_repo.save_employee(employee)
        Utils.logger(f"Registration Successful! ({email})")
        return employee

    def login(self, email, password):
        user = self._employee_repo.get_by_email(email.strip().lower())

        if not user:
            raise ValueError("Invalid email or password")

        if not user.check_password(password):
            raise ValueError("invalid email or password")

        if not user.is_active:
            raise ValueError("Account is deactivated")

        self._current_user = user
        Utils.logger(f"Login successful: {email}")
        return user

    def logout(self):
        if self._current_user:
            Utils.logger(f"User logged out: {self._current_user.email}")
            self._current_user = None

