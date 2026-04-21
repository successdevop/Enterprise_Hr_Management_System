import json
from src.hr_system.models.employee import Employee
from src.hr_system.storage.json_operator import logger
from src.hr_system.storage.config import LOGS_FILE
from typing import Dict, Optional, List


class EmployeeRepository:
    def __init__(self, storage_file: str):
        self._json_file_database = storage_file
        self._employees_by_id_database: Dict[str, Employee] = {}
        self._employees_by_email_database: Dict[str, Employee] = {}
        self._load_employee_database()

    def save_employee(self, employee: Employee):
        # Add to in-memory databases
        self._employees_by_email_database[employee.email] = employee
        self._employees_by_id_database[employee.employee_id] = employee

        # Prepare data for JSON serialization
        savable_data = {
            email: employee.to_dict()
            for email, employee in self._employees_by_email_database.items()
        }

        try:
            with open(self._json_file_database, mode="a", encoding="utf-8") as file_writer:
                json.dump(savable_data, file_writer, indent=4)
        except Exception as e:
            logger(f"Error saving employee: {e}", LOGS_FILE)
            raise

    def get_by_id(self, emp_id: str) -> Optional[Employee]:
        return self._employees_by_id_database.get(emp_id)

    def get_by_email(self, email: str) -> Optional[Employee]:
        return self._employees_by_email_database.get(email)

    def get_all(self) -> List[Employee]:
        return list(self._employees_by_email_database.values())

    def update_employee(self, employee: Employee):
        """Update an existing employee"""
        if employee.email in self._employees_by_email_database:
            self.save_employee(employee)
        else:
            raise ValueError(f"Staff with ID {employee.employee_id} not found")

    def delete_employee(self, employee: Employee):
        """Delete an employee"""
        if employee.email in self._employees_by_email_database:
            del self._employees_by_email_database[employee.email]
            del self._employees_by_id_database[employee.employee_id]
            self._save_all()
        else:
            raise ValueError(f"Staff with ID {employee.employee_id} not found")

    def count(self) -> int:
        return len(self._employees_by_email_database)

    def _save_all(self):
        """Save entire database to file"""
        savable_data = {
            email: employee.to_dict()
            for email, employee in self._employees_by_email_database.items()
        }

        with open(self._json_file_database, mode="w", encoding="utf-8") as file_writer:
            json.dump(savable_data, file_writer, indent=4)

    def _load_employee_database(self):
        self._employees_by_email_database.clear()
        self._employees_by_id_database.clear()

        try:
            with open(self._json_file_database, mode="r", encoding="utf-8") as file_reader:
                data = json.load(file_reader)
                print(data)

                if isinstance(data, dict):
                    for email, emp_obj in data.items():
                        if isinstance(emp_obj, dict):
                            employee = Employee.from_dict_to_object(emp_obj)
                        else:
                            employee = emp_obj

                        self._employees_by_email_database[email] = employee
                        self._employees_by_id_database[employee.employee_id] = employee
        except FileNotFoundError:
            # First run - file doesn't exist yet
            logger(f"Database file not found, starting fresh", LOGS_FILE)
            self._employees_by_email_database = {}
            self._employees_by_id_database = {}
        except json.JSONDecodeError as e:
            # File exists but is empty or corrupted
            logger(f"JSON decode error: {e}", LOGS_FILE)
            self._employees_by_email_database = {}
            self._employees_by_id_database = {}
        except Exception as e:
            logger(f"Error loading database: {e}", LOGS_FILE)
            self._employees_by_email_database = {}
            self._employees_by_id_database = {}
