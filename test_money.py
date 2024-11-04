from money import Money

def test_multiplication():
    amount = Money(10, "EUR")
    double = amount.times(2)
    # assert double.amount == 20
    # assert double.currency == "EUR"
    assert double == Money(20, "EUR")
