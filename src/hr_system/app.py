from repositories.employee_repo import EmployeeRepository
from services.auth_service import AuthService
from models.role import Role


def main():
    repo = EmployeeRepository()
    auth = AuthService(repo)

    employee_1 = auth.register(
        "Success raphael ifeanyi",
        "SUCcess@gmail.com",
        19,
        "imo state, Nigeria",
        Role.ADMIN,
        50000,
        "echezPay123@/.com"
    )

    employee_2 = auth.register(
        "Tobi",
        "TOBI@gmail.com", 25,
        "ogun state, Nigeria",
        Role.EMPLOYEE,
        4000,
        "tobiPass123@/.com"
    )

    auth.login("SUCcess@gmail.com", "echezPay123@/.com")

    auth.logout()

    repo.get_all()


main()
