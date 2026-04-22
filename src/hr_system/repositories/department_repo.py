import json
from typing import Dict, Optional, List
from src.hr_system.models.department import Department
from src.hr_system.models.employee import Employee
from src.hr_system.storage.logger import Logger
from src.hr_system.utils.exceptions import NotFoundError


class DepartmentRepo:
    def __init__(self, storage_file: str):
        self._dept_json_database = storage_file
        self._dept_database: Dict[str, Department] = {}
        self._load_dept_database()

    def save_department(self, dept: Department):
        self._dept_database[dept.name] = dept

        savable_data = {
            name: dept.to_dict()
            for name, dept in self._dept_database.items()
        }

        try:
            with open(self._dept_json_database, mode="w", encoding="utf-8") as file_writer:
                json.dump(savable_data, file_writer, indent=4)
        except Exception as e:
            Logger.error(f"Error saving department | {e}")

    def get_department_by_name(self, dept_name: str) -> Optional[Department]:
        return self._dept_database.get(dept_name)

    def get_department_by_manager(self, manager: Employee):
        for dept in self._dept_database.values():
            if dept.manager == manager.role:
                return dept
        raise NotFoundError("Manager not found")

    def get_all_dept(self) -> List[Department]:
        return list(self._dept_database.values())

    def count_dept(self) -> int:
        return len(self._dept_database)

    def _load_dept_database(self):
        self._dept_database.clear()

        try:
            with open(self._dept_json_database, mode="r", encoding="utf-8") as file_reader:
                data = json.load(file_reader)

                if isinstance(data, dict):
                    for name, department in data.items():
                        if isinstance(department, dict):
                            dept = Department.from_to_dict(department)
                        else:
                            dept = department
                        self._dept_database[name] = dept

        except FileNotFoundError:
            # First run - File doesn't exist yet
            Logger.error("Database file not found, starting fresh")
            self._dept_database = {}
        except json.JSONDecodeError as e:
            # File exists but is empty or corrupted
            Logger.error(f"JSON decode error: {e}")
            self._dept_database = {}
        except Exception as e:
            Logger.error(f"Error loading database: {e}")
            self._dept_database = {}
