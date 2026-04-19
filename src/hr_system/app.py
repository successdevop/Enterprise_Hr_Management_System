from repositories.employee_repo import EmployeeRepository
from services.auth_service import AuthService
from models.role import Role


def main():
    repo = EmployeeRepository()
    auth = AuthService(repo)

    employee_1 = auth.register(
        "Success",
        "success@.com", 16,
        "imo state, Nigeria",
        "Manage", 50000,
        "echezPay123@/.com"
    )

    employee_2 = auth.register(
        "Tobi",
        "tobi@gmail.com", 25,
        "ogun state, Nigeria",
        Role.EMPLOYEE.value,
        4000,
        "tobiPass123@/.com"
    )


main()
