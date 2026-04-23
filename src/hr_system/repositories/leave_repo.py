import json
from typing import List, Optional
from src.hr_system.models.leave import LeaveRequest
from src.hr_system.storage.logger import Logger
from src.hr_system.models.employee import Employee
from src.hr_system.utils.exceptions import NotFoundError


class LeaveRepo:
    def __init__(self, leave_storage_file: str):
        self._leave_json_document = leave_storage_file
        self._leave_database: List[LeaveRequest] = []
        self._load_leave_request_database()

    def get_request_by_employee(self, employee: Employee) -> Optional[LeaveRequest]:
        for leave_request in self._leave_database:
            if leave_request.employee == employee:
                return leave_request
        raise NotFoundError(f"Employee {employee.name} not found")

    def get_all_leave_request(self):
        return self._leave_database

    def get_all_pending_leave_request(self):
        return [request for request in self._leave_database if request.status.PENDING]

    def save_leave_request(self, leave: LeaveRequest):
        self._leave_database.append(leave)

        savable_data = [leave.to_dict() for leave in self._leave_database]

        try:
            with open(self._leave_json_document, mode="w", encoding="utf-8") as leave_writer:
                json.dump(savable_data, leave_writer, indent=4)
        except Exception as e:
            Logger.error(f"Error saving Request | {e}")
            raise

    def _load_leave_request_database(self):
        try:
            with open(self._leave_json_document, mode="r", encoding="utf-8") as leave_reader:
                leave_data = json.load(leave_reader)

                for leave_request in leave_data:
                    self._leave_database.append(leave_request.from_dict())

        except Exception as e:
            print(f"Error with loading Leave Request database: {e}")
            Logger.error(f"Error with loading Leave Request database: {e}")
            self._leave_database = []

