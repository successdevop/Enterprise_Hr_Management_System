from src.hr_system.models.employee import Employee
from typing import Dict


class EmployeeRepository:
    def __init__(self):
        self._employees_by_id: Dict[str, Employee] = {}
        self._employees_by_email: Dict[str, Employee] = {}

    def save_employee(self, employee: Employee):
        self._employees_by_id[employee.employee_id] = employee
        self._employees_by_email[employee.email] = employee

    def get_by_id(self, emp_id: str) -> Employee | None:
        return self._employees_by_id.get(emp_id)

    def get_by_email(self, email: str) -> Employee | None:
        return self._employees_by_email.get(email)

    def get_all(self) -> list:
        return list(self._employees_by_id)

    def count(self) -> int:
        return len(self._employees_by_id)

