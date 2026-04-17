class _Person:
    def __int__(self, name: str, email: str, age: int, nin: str, state_of_origin: str):
        self.__name = name
        self.__email = email
        self.__age = age
        self.__NIN = nin
        self.__origin = state_of_origin

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        new_name =
