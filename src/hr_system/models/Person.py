from ..utils.utils import Utils


class Person:
    def __init__(self, name: str, email: str, age: int, state_of_origin: str):
        self._name = Utils.validate_name(name)
        self._email = Utils.validate_email(email)
        self._age = Utils.validate_age(age)
        self._origin = Utils.validate_name(state_of_origin)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = Utils.validate_name(name)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = Utils.validate_email(email)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = Utils.validate_age(age)

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, state_of_origin):
        self._origin = Utils.validate_name(state_of_origin)
