from money import Money
from portfolio import Portfolio

def test_convert_eur_to_usd():
    portfolio = Portfolio()

    portfolio.add(Money(10.3, "EUR"), Money(20.5, "EUR"))
    usd = portfolio.evaluate("USD")

    assert usd == Money(33.264, "USD")