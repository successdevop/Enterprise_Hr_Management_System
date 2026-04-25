from datetime import datetime
from src.hr_system.models.employee import Employee


class Payslip:
    def __init__(self, employee: Employee, base_salary: float, net_salary: float, deductions: float, bonuses:float):
        self.employee = employee
        self.base_salary = base_salary
        self.net_salary = net_salary
        self.deductions = deductions
        self.bonuses = bonuses
        self.generated_at = datetime.now()

    def __repr__(self):
        return f"<Payslip(name: {self.employee.name} | net_salary: {self.net_salary} | role: {self.employee.role.value})>"