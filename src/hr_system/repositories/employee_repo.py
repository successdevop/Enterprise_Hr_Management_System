from ..models.employee import Employee


class EmployeeRepository:
    def __init__(self):
        self._employees = []

    def save_employee(self, employee: Employee):
        self._employees.append(employee)

    def get_by_id(self, emp_id: str) -> Employee | None:
        for employee in self._employees:
            if emp_id == employee.employee_id:
                return employee
        return None

    def get_by_email(self, email):
        employee = next((email == employee.email for employee in self._employees), None)
        return employee

    def get_all(self):
        return self._employees

    def count(self):
        return len(self._employees)

