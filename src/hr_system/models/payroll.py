from datetime import datetime
from src.hr_system.models.employee import Employee


class Payslip:
    def __init__(self, employee: Employee, base_salary: float, net_salary: float, deductions: float, bonuses: float):
        self.employee = employee
        self.base_salary = base_salary
        self.net_salary = net_salary
        self.deductions = deductions
        self.bonuses = bonuses
        self.generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self) -> dict:
        return {
            "base_salary": self.base_salary,
            "net_salary": self.net_salary,
            "deductions": self.deductions,
            "bonuses": self.bonuses,
            "generated_at": self.generated_at,
            "employee": self.employee.to_dict(show_all=False) if self.employee else None
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Payslip":
        payslip = cls(
            base_salary=data.get("base_salary"),
            net_salary=data.get("net_salary"),
            deductions=data.get("deductions"),
            bonuses=data.get("bonuses"),
            employee=Employee.from_dict_to_object(data.get("employee"))
        )
        payslip.generated_at = data.get("generated_at")
        return payslip

    def __repr__(self):
        return f"<Payslip(name: {self.employee.name} | net_salary: {self.net_salary} | role: {self.employee.role.value})>"