from src.hr_system.repositories.department_repo import DepartmentRepo
from src.hr_system.services.permision_service import PermissionService
from src.hr_system.models.employee import Employee
from src.hr_system.models.role import Role
from src.hr_system.utils.utils import Utils
from src.hr_system.models.department import Department
from src.hr_system.storage.logger import Logger
from src.hr_system.storage.config import LOGS_FILE
from src.hr_system.utils.exceptions import UserAlreadyExistError, NotFoundError


class DepartmentService:
    def __init__(self, department_repo: DepartmentRepo):
        self.__department_repo = department_repo

    def create_department(self, current_user, dept_name: str, manager: Employee):

        PermissionService.required_role(current_user, [Role.ADMIN, Role.HR])
        Utils.validate_name(dept_name)

        if self.__department_repo.get_department_by_name(dept_name):
            raise UserAlreadyExistError("Department already exist")

        department = Department(dept_name, manager)

        self.__department_repo.save_department(department)
        Logger.info(f"[{dept_name} department] created by {current_user.name}", LOGS_FILE)
        return department

    def assign_employee(self, current_user, dept_name: str, employee: Employee):
        PermissionService.required_role(current_user, [Role.HR, Role.ADMIN])

        department = self.__department_repo.get_department_by_name(dept_name)
        if not department:
            raise NotFoundError("Department not found")

        department.add_employee(employee)
        self.__department_repo.save_department(department)

    def remove_employee(self, current_user, dept_name: str, employee: Employee):
        PermissionService.required_role(current_user, [Role.HR, Role.ADMIN])

        department = self.__department_repo.get_department_by_name(dept_name)
        if not department:
            raise NotFoundError("Department not found")

        department.remove_employee(employee)
        self.__department_repo.save_department(department)

    def delete_dept(self, current_user, dept_name: str):
        PermissionService.required_role(current_user, [Role.ADMIN])

        self.__department_repo.delete_department(dept_name)

    def get_department(self, current_user, dept_name: str):
        PermissionService.required_role(current_user, [Role.ADMIN])

        department = self.__department_repo.get_department_by_name(dept_name)
        print(department.to_dict())

    def get_all_dept(self, current_user):
        PermissionService.required_role(current_user, [Role.ADMIN])

        department = self.__department_repo.get_all_dept()
        print(department)

    def count_department(self, current_user):
        PermissionService.required_role(current_user, [Role.ADMIN])
        print(self.__department_repo.count_dept())

    def view_department_employees(self, current_user, dept_name: str):
        PermissionService.required_role(current_user, [Role.ADMIN])
        department = self.__department_repo.get_department_by_name(dept_name)
        if not department:
            raise NotFoundError("Department not found")
        department.view_department()

    def delete_all_department(self, current_user):
        PermissionService.required_role(current_user, [Role.ADMIN])
        self.__department_repo.delete_all_department()
        print(f"{current_user.name} deleted all department")



