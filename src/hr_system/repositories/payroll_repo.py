import json
from typing import Dict, Optional
from src.hr_system.models.payroll import Payslip
from src.hr_system.models.employee import Employee
from src.hr_system.storage.logger import Logger


class PayrollRepo:
    def __init__(self, payroll_json_file_storage):
        self.payroll_json_file_storage = payroll_json_file_storage
        self._payroll_database: Dict[str, Payslip] = {}
        self._load_payroll_database()

    def get_employee_payslip(self, employee: Employee) -> Optional[Employee]:
        return self._payroll_database.get(employee.employee_id)

    def get_all_payslip(self):
        return list(self._payroll_database.values())

    def view_all_payslip(self):
        for payslip in self._payroll_database.values():
            print(payslip)

    def save_payslip(self, payslip: Payslip):
        self._payroll_database[payslip.employee.employee_id] = payslip

        savable_data = {
            emp_id: payslip.to_dict()
            for emp_id, payslip in self._payroll_database.items()
        }

        try:
            with open(self.payroll_json_file_storage, mode="w", encoding="utf-8") as pay_writer:
                json.dump(savable_data, pay_writer, indent=4)
        except Exception as e:
            Logger.error(f"Error loading payslip_database | {e}")
            raise

    def _load_payroll_database(self):
        self._payroll_database.clear()

        try:
            with open(self.payroll_json_file_storage, mode="r", encoding="utf-8") as pay_reader:
                data = json.load(pay_reader)
                print(data)

                if isinstance(data, dict):
                    for emp_id, payslip in data.items():
                        if isinstance(payslip, dict):
                            payslip_data = Payslip.from_dict(payslip)
                        else:
                            payslip_data = payslip
                        self._payroll_database[emp_id] = payslip_data
        except FileNotFoundError:
            # First run - file doesn't exist yet
            Logger.error("Payroll_database file not found, starting fresh")
            self._payroll_database = {}
        except json.JSONDecodeError:
            # File exits but empty or corrupted
            Logger.error("JSON Decode Error for Payroll database")
            self._payroll_database = {}
        except Exception as e:
            Logger.error(f"Error loading payroll database | {e}")
            self._payroll_database = {}