from dessertshop.dessertshop import (
    Candy,
    Cookie,
    IceCream,
    Sundae
)

def test_tax_percent():
    candy1 = Candy("Tootsie roll", 6, 2)
    candy2 = Candy("Twix", 10, 3)
    candy3 = Candy("DiabEATies", 100, 9999)

    assert candy1.tax_percent == 7.25
    assert candy2.tax_percent == 7.25
    assert candy3.tax_percent == 7.25

def test_calculate_cost():
    candy = Candy("Tootsie roll", 6, 2)
    cookie = Cookie("Chocolate", 7, 3)
    icecream = IceCream("Mint", 5, 1)
    sundae = Sundae("OreoSundae", 8, 1.5, "Oreo", 0.5)

    assert candy.calculate_cost() == 12
    assert cookie.calculate_cost() == 1.75
    assert icecream.calculate_cost() == 5
    assert sundae.calculate_cost() == 12.5
