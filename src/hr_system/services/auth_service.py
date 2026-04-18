from ..repositories.employee_repo import EmployeeRepository
from ..utils.utils import Utils


class AuthService:
    def __init__(self, employee_repo: EmployeeRepository):
        self.employee_repo = employee_repo
        self.current_user = None

    def register(self, name, email, age, origin, role, salary, password):
        from ..models.employee import Employee

        if self.employee_repo.get_by_email(email):
            raise ValueError("User already exist")

        employee = Employee(name, email, age, origin, role, salary)
        employee.set_password(password)

        self.employee_repo.save_employee(employee)
        Utils.logger(f"User Registered: {email}")
        return employee

    def login(self, email, password):
        user = self.employee_repo.get_by_email(email.strip().lower())

        if not user:
            raise ValueError("Invalid password or email")

        if user.password == password:
            raise ValueError("invalid email or password")

        if not user.is_active:
            raise ValueError("Account is deactivated")

        self.current_user = user
        Utils.logger("Login successful")
        return user

    def logout(self):
        if self.current_user:
            Utils.logger(f"User logged out: {self.current_user.email}")
            self.current_user = None

