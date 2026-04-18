import uuid
from person import Person
from role import Role


class Employee(Person):
    def __init__(self, name, email, age, origin, role: Role, salary: float):
        super().__init__(name=name, email=email, age=age, state_of_origin=origin)
        self._emp_id = str(uuid.uuid4())
        self._role = role
        self._salary = salary
        self._isActive = True
        self.password = None

    def set_password(self, password):
        self.password = password

    def check_password(self, password) -> bool:
        return self.password == password

    @property
    def employee_id(self):
        return self._emp_id

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary > 0:
            self._salary = salary
        else:
            print("salary must be greater than zero")

    @property
    def is_active(self):
        return self._isActive

    def deactivate(self):
        self._isActive = False


# class Manager(Employee):
#     def __init__(self, name, email, age, emp_id, salary, origin):
#         super().__init__(name, email, age, emp_id, origin, role="Manager", salary=salary)
#         self.team = []
#
#     def add_team_member(self, employee):
#         self.team.append(employee)
#
#
# class Hr(Employee):
#     def __init__(self, name, email, age, origin, emp_id, salary):
#         super().__init__(name, email, age, origin, emp_id, role="HR", salary=salary)


