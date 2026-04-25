from src.hr_system.models.employee import Employee
from src.hr_system.models.payslip import Payslip
from src.hr_system.models.role import Role
from src.hr_system.utils.exceptions import NotFoundError
from src.hr_system.repositories.payroll_repo import PayrollRepo
from src.hr_system.strategy.salary import SalaryStrategy
from src.hr_system.storage.logger import Logger
from src.hr_system.storage.config import LOGS_FILE
from src.hr_system.services.permision_service import PermissionService


class PayrollService:
    def __init__(self, payroll_repo: PayrollRepo):
        self._payroll_repo = payroll_repo

    def process_salary(self, current_user,  employee: Employee, strategy: SalaryStrategy,
                       net_salary: float, deductions: float = 0, bonuses: float = 0):
        PermissionService.required_role(current_user, [Role.ADMIN, Role.HR])

        base_salary = employee.salary

        net_salary, tax = strategy.calculate(base_salary)
        total_deduction = deductions + tax
        final_salary = net_salary + bonuses - deductions

        payslip = Payslip(
            base_salary=base_salary,
            net_salary=final_salary,
            deductions=total_deduction,
            bonuses=bonuses,
            employee=employee
        )

        self._payroll_repo.save_payslip(payslip)
        Logger.info(f"Payroll processed for {employee.name}", LOGS_FILE)
        return payslip

    def get_payslip_by_employee(self,current_user,  employee: Employee):
        PermissionService.required_role(current_user, [Role.ADMIN, Role.HR])
        payslip = self._payroll_repo.get_employee_payslip(employee)
        if not payslip:
            raise NotFoundError("Employee not found")
        print(payslip)

    def view_all_pays(self, current_user):
        PermissionService.required_role(current_user, [Role.ADMIN, Role.HR])
        self._payroll_repo.view_all_payslip()

    def get_all_payslip(self, current_user):
        PermissionService.required_role(current_user, [Role.ADMIN, Role.HR])
        self._payroll_repo.get_all_payslip()