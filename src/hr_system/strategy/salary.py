from abc import ABC, abstractmethod


class SalaryStrategy(ABC):
    @abstractmethod
    def calculate(self, base_salary):
        pass


class FullTimeStrategy(SalaryStrategy):
    def calculate(self, base_salary):
        tax = base_salary * 0.2
        return base_salary - tax, tax


class ContractStrategy(SalaryStrategy):
    def calculate(self, base_salary):
        return base_salary, 0
