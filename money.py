from __future__ import annotations

class Money:
    def __init__(self, amount: int, currency: str):
        self.amount = amount
        self.currency = currency

    def times(self, multiplier: int) -> Money:
        return Money(self.amount * multiplier, self.currency)

    def __eq__(self, other: Money):
        if not isinstance(other, Money):
            raise Exception("Invalid class")

        return self.amount == other.amount and self.currency == other.currency