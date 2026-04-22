from repositories.employee_repo import EmployeeRepository
from repositories.department_repo import DepartmentRepo
from services.auth_service import AuthService
from services.department_service import DepartmentService
from models.role import Role
from storage.config import EMPLOYEE_DATABASE, DEPARTMENT_DATABASE


def main():
    emp_repo = EmployeeRepository(EMPLOYEE_DATABASE)
    dept_repo = DepartmentRepo(DEPARTMENT_DATABASE)
    auth = AuthService(emp_repo)
    dept_service = DepartmentService(dept_repo)

    # employee_1 = auth.register(
    #     "Success raphael ifeanyi",
    #     "SUCcess@gmail.com",
    #     30,
    #     "imo state, Nigeria",
    #     Role.ADMIN,
    #     50000,
    #     "echezPay123@/.com"
    # )
    #
    # employee_2 = auth.register(
    #     "Tobi",
    #     "TOBI@gmail.com",
    #     25,
    #     "ogun state, Nigeria",
    #     Role.MANAGER,
    #     4000,
    #     "tobiPass123@/.com"
    # )
    #
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
    # employee_4 = auth.register(
    #     "Oluchi Raphael",
    #     "oluchi@gmail.com",
    #     24,
    #     "Enugu state, Nigeria",
    #     Role.HR,
    #     10000,
    #     "olu123@/.com"
    # )

    auth.login("success@gmail.com", "echezPay123@/.com")

    # dept_service.create_department(auth.current_user, "Engineering", emp_repo.get_by_email("TOBI@gmail.com"))
    # dept_service.assign_employee(auth.current_user, "Engineering", emp_repo.get_by_email("umah@gmail.com"))
    # dept_service.remove_employee(auth.current_user, "Engineering", emp_repo.get_by_email("umah@gmail.com"))
    # dept_service.delete_dept(auth.current_user, "Engineering")
    print(dept_repo.get_all_dept())



if __name__ == "__main__":
    main()
