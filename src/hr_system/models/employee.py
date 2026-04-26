import datetime
import hashlib
import uuid
from typing import List
from src.hr_system.models.person import Person
from src.hr_system.models.role import Role
from src.hr_system.utils.utils import Utils
from src.hr_system.utils.exceptions import ValidationError


class Employee(Person):
    def __init__(self, name: str, email, age, origin, role: Role, salary: float):
        super().__init__(name=name, email=email, age=age, state_of_origin=origin)
        self._emp_id = str(uuid.uuid4())
        self.role = role
        self._salary = salary
        self.type = None
        self.isActive = True
        self._password = None
        self.department: List[str] = []
        self.onboarding_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def set_password(self, password):
        if password and len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long")

        self._password = hashlib.sha256(password.encode()).hexdigest()

    def _get_password(self):
        return self._password

    def check_password(self, password) -> bool:
        test = hashlib.sha256(password.encode()).hexdigest()
        return test == self._get_password()

    @property
    def employee_id(self):
        return self._emp_id

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = Utils.validate_amount_input(salary)

    def deactivate(self):
        self.isActive = False

    def to_dict(self, show_all: bool = True) -> dict:
        if show_all:
            return {
                "employee_id": self.employee_id,
                "name": self.name,
                "email": self.email,
                "age": self.age,
                "origin": self.origin,
                "role": self.role.value if hasattr(self.role, "value") else self.role,
                "salary": self.salary,
                "isActive": self.isActive,
                "password": self._password,
                "department": self.department,
                "onboarding_date": self.onboarding_date
            }
        else:
            return {
                "employee_id": self.employee_id,
                "name": self.name,
                "role": self.role.value if hasattr(self.role, "value") else self.role,
            }

    @classmethod
    def from_dict_to_object(cls, data: dict) -> "Employee":

        role = data.get("role")
        if isinstance(role, str) and hasattr(Role, role.upper()):
            role = Role[role.upper()]

            employee = cls(
                name=data.get("name"),
                email=data.get("email"),
                age=data.get("age"),
                origin=data.get("origin"),
                role=role,
                salary=data.get("salary"),
            )
            employee._emp_id = data.get("employee_id")
            employee.isActive = data.get("isActive")
            employee._password = data.get("password")
            employee.department = data.get("department")
            employee.onboarding_date = data.get("onboarding_date")
            return employee

    def __eq__(self, other):
        if not isinstance(other, Employee):
            return False
        return self.employee_id == other.employee_id

    def __hash__(self):
        return hash(self.employee_id)

    def __repr__(self):
        return f"<Employee id: {self._emp_id} | name: {self.name} | role: {self.role.value} >"
