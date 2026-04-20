import json

from src.hr_system.models.employee import Employee
from src.hr_system.storage.config import EMPLOYEE_DATABASE_BY_ID, EMPLOYEE_DATABASE_BY_EMAIL
from src.hr_system.storage.json_operator import save_to_jason_database
from typing import Dict


class EmployeeRepository:
    def __init__(self, storage_file: str):
        self._database = storage_file
        self._employees_by_id: Dict[str, Employee] = {}
        self._employees_by_email: Dict[str, Employee] = {}
        self._load_database()

    def _load_database(self):
        try:
            with open(self._database, mode="r", encoding="utf-8") as file_reader:
                data = json.load(file_reader)
                print(data)

                # self._employees_by_email = {
                #     email: Employee.to_dict(emp)
                #
                #     for email, emp in data.items()
                # }
        except FileNotFoundError:
            self._employees_by_email = {}

    def _save_to_database(self):
        serializable_data = {
            email: employee.to_dict()
            for email, employee in self._employees_by_email.items()
        }

        save_to_jason_database(serializable_data, self._database)

    def save_employee(self, employee: Employee):
        self._employees_by_email[employee.email] = employee
        self._save_to_database()

    def get_by_id(self, emp_id: str) -> Employee | None:
        return self._employees_by_id.get(emp_id)

    def get_by_email(self, email: str) -> Employee | None:
        return self._employees_by_email.get(email)

    def get_all(self) -> list:
        return list(self._employees_by_id)

    def count(self) -> int:
        return len(self._employees_by_id)

