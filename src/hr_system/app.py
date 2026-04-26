from repositories.employee_repo import EmployeeRepository
from repositories.department_repo import DepartmentRepo
from repositories.leave_repo import LeaveRepo
from repositories.payroll_repo import PayrollRepo
from services.auth_service import AuthService
from services.department_service import DepartmentService
from services.leave_service import LeaveServices
from services.payroll_service import PayrollService
from strategy.salary import ContractStrategy, FullTimeStrategy
from models.role import Role
from models.leave import LeaveType
from storage.config import EMPLOYEE_DATABASE, DEPARTMENT_DATABASE, LEAVE_DATABASE, PAYROLL_DATABASE


def main():
    emp_repo = EmployeeRepository(EMPLOYEE_DATABASE)
    # dept_repo = DepartmentRepo(DEPARTMENT_DATABASE)
    # leave_repo = LeaveRepo(LEAVE_DATABASE)
    payroll_repo = PayrollRepo(PAYROLL_DATABASE)

    auth = AuthService(emp_repo)
    # dept_service = DepartmentService(dept_repo)
    # leave_service = LeaveServices(leave_repo)
    payroll_service = PayrollService(payroll_repo)

    # auth.login("kelechigd@gmail.com", "kel123@/.com")
    # leave_1 = leave_service.apply_for_leave(auth.current_user, 15, LeaveType.EMMERGENCY)

    auth.login("success@gmail.com", "echezPay123@/.com")
    strategy = FullTimeStrategy()
    payroll_service.process_salary(auth.current_user, emp_repo.get_by_email("success@gmail.com"), strategy)
    # leave_service.reject_leave(auth.current_user, leave_1)
    # leave_service.view_all_pending_request(auth.current_user)
    # leave_service.view_all_request(auth.current_user)
    # leave_service.view_employee_leave_request(auth.current_user, auth.get_employee_repo().get_by_email("kelechigd@gmail.com"))
    # print(leave_repo.get_all_leave_request())

if __name__ == "__main__":
    main()

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
    #     "kelechi gold",
    #     "kelechigd@gmail.com",
    #     22,
    #     "Abia state, Nigeria",
    #     Role.EMPLOYEE,
    #     15000,
    #     "kel123@/.com"
    # )
    # employee_5 = auth.register(
    #     "Folakemi Oladimeji",
    #     "folak.ola@gmail.com",
    #     29,
    #     "Oyo state, Nigeria",
    #     Role.MANAGER,
    #     8000,
    #     "folakiss123@/.com"
    # )
    #
    # employee_6 = auth.register(
    #     "Oluchi Raphael",
    #     "oluchi@gmail.com",
    #     24,
    #     "Enugu state, Nigeria",
    #     Role.HR,
    #     10000,
    #     "olY123_@/.com"
    # )

# dept_service.create_department(auth.current_user, "Engineering", auth.get_employee_repo().get_by_email('TOBI@gmail.com'))
# dept_service.create_department(auth.current_user, "Engineering", emp_repo.get_by_email('TOBI@gmail.com'))
# dept_service.assign_employee(auth.current_user, "Engineering", emp_repo.get_by_email("umah@gmail.com"))
# dept_service.remove_employee(auth.current_user, "Engineering", emp_repo.get_by_email("umah@gmail.com"))
# dept_service.assign_employee(auth.current_user, "Engineering", emp_repo.get_by_email("kelechigd@gmail.com"))
# dept_service.delete_dept(auth.current_user, "Engineering")
# dept_service.view_department_employees(auth.current_user, "Engineering")
# dept_service.get_all_dept(auth.current_user)
# dept_service.get_department(auth.current_user, "Engineering")
# dept_service.count_department(auth.current_user)
# dept_service.delete_all_department(auth.current_user)
# dept_service.delete_dept(auth.current_user, "Engineering")
# dept_service.create_department(auth.current_user, "Marketing", emp_repo.get_by_email('folak.ola@gmail.com'))
# dept_service.assign_employee(auth.current_user, "Marketing", emp_repo.get_by_email("umah@gmail.com"))
# dept_service.remove_employee(auth.current_user, "Marketing", emp_repo.get_by_email("umah@gmail.com"))
# dept_service.delete_dept(auth.current_user, "Marketing")