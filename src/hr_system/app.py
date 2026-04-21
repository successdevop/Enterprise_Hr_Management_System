from repositories.employee_repo import EmployeeRepository
from services.auth_service import AuthService
from models.role import Role
from storage.config import EMPLOYEE_DATABASE


def main():
    repo = EmployeeRepository(EMPLOYEE_DATABASE)
    auth = AuthService(repo)

    # employee_1 = auth.register(
    #     "Success raphael ifeanyi",
    #     "SUCcess@gmail.com",
    #     30,
    #     "imo state, Nigeria",
    #     Role.ADMIN,
    #     50000,
    #     "echezPay123@/.com"
    # )

    # employee_2 = auth.register(
    #     "Tobi",
    #     "TOBI@gmail.com",
    #     25,
    #     "ogun state, Nigeria",
    #     Role.EMPLOYEE,
    #     4000,
    #     "tobiPass123@/.com"
    # )

    # employee_3 = auth.register(
    #     "favour",
    #     "umah@gmail.com",
    #     27,
    #     "ebonyi, Nigeria",
    #     Role.EMPLOYEE,
    #     15000,
    #     "umahPass123@/.com"
    # )

    #
    employee_4 = auth.register(
        "Oluchi Raphael",
        "oluchi@gmail.com",
        24,
        "Enugu state, Nigeria",
        Role.HR,
        10000,
        "olu123@/.com"
    )

    # auth.login("SUccess@gmail.com", "echezPay123@/.com")
    # auth.login("umah@gmail.com", "umahPass123@/.com")
    # repo.get_all()


main()
