from employee import Employee
from src.hr_system.utils.exceptions import ValidationError, NotFoundError
from typing import List


class Department:
    def __init__(self, name: str, manager: Employee):
        if not name:
            raise ValidationError("Department must have a name")

        if manager.role.value != "Manager":
            raise ValidationError("Department manager must have a Manager role")

        self.name = name
        self.manager = manager
        self._dept_employees: List[Employee] = []

    def add_employee(self, employee: Employee):
        if employee in self._dept_employees:
            raise ValidationError("Employee already in the department")
        self._dept_employees.append(employee)
        print("Employee added to department")

    def remove_employee(self, employee: Employee):
        if employee in self._dept_employees:
            self._dept_employees.remove(employee)
            print("Employee removed from department")
        else:
            raise NotFoundError("Employee not in department")

    def view_department(self):
        for emp in self._dept_employees:
            print(emp)

    def to_dict(self):
        return {
            "name": self.name,
            "manager": self.manager,
            "dept_employees": self._dept_employees
        }

    @classmethod
    def from_to_dict(cls, data) -> "Department":
        department = cls(
            name=data["name"],
            manager=data["manager"],
        )
        department._dept_employees = data["dept_employees"]
        return department

    def __repr__(self):
        return f"<Department name: {self.name} | manager: {self.manager.name}>"
