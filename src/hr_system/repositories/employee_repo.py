from ..models.employee import Employee
from typing import Dict


class EmployeeRepository:
    def __init__(self):
        self._employees: Dict[str, Employee] = {}

    def save_employee(self, employee: Employee):
        self._employees[employee.employee_id] = employee

    def get_by_id(self, emp_id: str) -> Employee | None:
        return self._employees.get(emp_id)

    def get_by_email(self, email: str) -> Employee | None:
        return next((email == emp.email for emp in self._employees.values()))

    def get_all(self) -> list:
        return list(self._employees)

    def count(self) -> int:
        return len(self._employees)

