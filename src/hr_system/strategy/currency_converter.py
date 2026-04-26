class CurrencyConverter:
    def __init__(self):
        self.rates = {
            "NGN": 1,
            "USD": 0.0013,
            "EUR": 0.0012
        }

    def convert(self, amount, from_currency, to_currency):
        if from_currency not  in self.rates or to_currency not in self.rates:
            raise ValueError("Unsupported currency")

        base = amount / self.rates[from_currency]
        return base * self.rates[to_currency]