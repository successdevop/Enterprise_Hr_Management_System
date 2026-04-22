from src.hr_system.models.employee import Employee
from src.hr_system.utils.exceptions import ValidationError, NotFoundError
from typing import List


class Department:
    def __init__(self, name: str, manager: Employee):
        if not name:
            raise ValidationError("Department must have a name")

        if manager.role.value != "Manager":
            raise ValidationError("Department manager must have a Manager role")

        self._name = name
        self._manager = manager
        self._dept_employees: List[Employee] = []

    @property
    def name(self):
        return self._name

    @property
    def manager(self):
        return self._manager

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
            raise NotFoundError("Employee not found in department")

    def view_department(self):
        for emp in self._dept_employees:
            print(emp)

    def to_dict(self):
        # return {
        #     "name": self._name,
        #     "manager": self._manager.to_dict() if self._manager else None,
        #     "dept_employees": [emp.to_dict() for emp in self._dept_employees]
        # }
        return {
            "name": self._name,
            "manager": self._manager.name,
            "dept_employees": [
                {"name": emp.name, "email": emp.email, "role": emp.role.value}
                for emp in self._dept_employees
            ]
        }

    @classmethod
    def from_to_dict(cls, data) -> "Department":
        department = cls(
            name=data["name"],
            manager=data["manager"]
        )
        department._dept_employees = [Employee.from_dict_to_object(emp) for emp in data.get("dept_employees", [])]
        return department

    def __repr__(self):
        return f"<Department name: {self._name} | manager: {self._manager.name}>"
