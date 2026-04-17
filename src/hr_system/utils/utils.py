import random
import re


class Utils:
    """ this class provides the functions/methods that serves as helper function to our application"""
    @staticmethod
    def generate_nin(employee_database):
        while True:
            nin = "".join(str(random.randint(1, 9)) for _ in range(10))
            if not any(person.nin == nin for person in employee_database):
                return nin

    @staticmethod
    def validate_name(name):
        name = name.strip()
        if name and len(name) >= 3:
            return name
        else:
            print("Name value cannot be empty and must be at-least 3 characters")

    @staticmethod
    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return email
        print("Invalid email")

    @staticmethod
    def validate_age(age):
        if isinstance(age, int):
            if age >= 18:
                return age
            else:
                print("You must be at-least 18 years")
        else:
            print("Invalid age value")


# util_ch = Utils()
# # util_ch.generate_nin(["1234567890", "2345678901", "3456789012", "4567890123", "5678901234"])
# util_ch.validate_age("32")
# util_ch.validate_name("er")
# print(util_ch.validate_email("success.@gmail.com"))

