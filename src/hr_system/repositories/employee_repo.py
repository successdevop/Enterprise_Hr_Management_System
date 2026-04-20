import json
from src.hr_system.models.employee import Employee
from src.hr_system.utils.utils import Utils
from typing import Dict


class EmployeeRepository:
    def __init__(self, storage_file: str):
        self._json_file_database = storage_file
        self._employees_by_id_database: Dict[str, Employee] = {}
        self._employees_by_email_database: Dict[str, Employee] = {}
        self._load_employee_database()

    def _load_employee_database(self):
        self._employees_by_email_database.clear()
        self._employees_by_id_database.clear()

        try:
            with open(self._json_file_database, mode="r", encoding="utf-8") as file_reader:
                data = json.load(file_reader)
                print(data)

                for email, emp_obj in data.items():
                    employee = Employee.from_dict_to_object(emp_obj)
                    self._employees_by_email_database[email] = employee
                    self._employees_by_id_database[employee.employee_id] = employee

        except Exception as e:
            print(e)
            Utils.logger(f"{e}")
            self._employees_by_email_database = {}
            self._employees_by_id_database = {}

    def save_employee(self, employee: Employee):
        self._employees_by_email_database[employee.email] = employee
        self._employees_by_id_database[employee.employee_id] = employee

        with open(self._json_file_database, mode="a", encoding="utf-8") as file_writer:
            file_writer.write(json.dumps(employee.to_dict(), indent=4))

    def update_employee(self, employee: Employee):
        emp = self._employees_by_email_database.get(employee.email)

        if not emp:
            print(f"Staff with ID {employee.employee_id} not found")
            return

        self._employees_by_email_database[employee.email] = employee
        self._employees_by_id_database[employee.employee_id] = employee

        with open(self._json_file_database, mode="w", encoding="utf-8") as file_writer:
            for employee in self._employees_by_email_database.values():
                file_writer.write(json.dumps(employee.to_dict(), indent=4))

    def get_by_id(self, emp_id: str) -> Employee | None:
        return self._employees_by_id_database.get(emp_id)

    def get_by_email(self, email: str) -> Employee | None:
        return self._employees_by_email_database.get(email)

    def get_all(self) -> list:
        return list(self._employees_by_email_database)

    def count(self) -> int:
        return len(self._employees_by_email_database)
