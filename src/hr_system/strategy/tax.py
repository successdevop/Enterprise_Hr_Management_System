from abc import ABC, abstractmethod


class TaxStrategy(ABC):
    @abstractmethod
    def calculate_tax(self, salary):
        pass


class NigerianTaxStrategy(TaxStrategy):
    def calculate_tax(self, salary):
        if salary <= 3000:
            return salary * 0.1
        elif salary <= 10000:
            return salary * 0.15
        else:
            return salary * 0.2


class PensionClaculator:
    @staticmethod
    def calculate(salary):
        employee_contribution = salary * 0.8
        employer_contribution = salary * 1.0
        total_pension_contribution = employee_contribution + employer_contribution
        return total_pension_contribution
