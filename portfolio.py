from money import Money


class Portfolio:
    def __init__(self):
        self.moneys = []
        self._conversion_rates = {"EUR->USD": 1.08, "EUR->CZK": 25.3}

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, currency):
        total = 0
        failures = []

        for m in self.moneys:
            try:
                total += self.convert(m, currency)
            except KeyError as ke:
                failures.append(ke)

        if len(failures) == 0:
            return Money(total, currency)

        # ["Nemas franky", "Nemas zlote"]
        # "Nemas franky, nemas zlote"

        failure_message = ", ".join(str(f) for f in failures)
        raise Exception(f"Chybejici kurzy: [{failure_message}]")

    def convert(self, money, currency):
        if money.currency == currency:
            return money.amount

        key = f"{money.currency}->{currency}"
        return money.amount * self._conversion_rates[key]
