import random
import re


class Utils:
    """ this class provides the functions/methods that serves as helper function to our application"""
    @staticmethod
    def generate_nin(employee_database: list) -> str:
        while True:
            nin = "".join(str(random.randint(1, 9)) for _ in range(10))
            if not any(person.nin == nin for person in employee_database):
                return nin

    @staticmethod
    def validate_name(name: str) -> str:
        name = name.strip().title()
        if name and len(name) >= 3:
            return name
        else:
            print("Name value cannot be empty and must be at-least 3 characters")

    @staticmethod
    def validate_email(email: str) -> str:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return email
        print("Invalid email")

    @staticmethod
    def validate_age(age: int) -> int:
        if isinstance(age, int):
            if age >= 18:
                return age
            else:
                print("You must be at-least 18 years")
        else:
            print("Invalid age value")