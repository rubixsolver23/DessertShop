from dessertshop.dessertshop_part3 import (
    DessertItem,
    Candy,
    Cookie,
    IceCream,
    Sundae
)

def test_candy():
    candy1 = Candy("Tootsie roll", 6, 2)
    candy2 = Candy("Twix", 10, 3)
    candy3 = Candy("DiabEATies", 100, 9999)

    assert candy1.name == "Tootsie roll"
    assert candy1.candy_weight == 6
    assert candy1.price_per_pound == 2

    assert candy2.name == "Twix"
    assert candy2.candy_weight == 10
    assert candy2.price_per_pound == 3

    assert candy3.name == "DiabEATies"
    assert candy3.candy_weight == 100
    assert candy3.price_per_pound == 9999

def test_cookie():
    cookie1 = Cookie("Chocolate", 7, 3)
    cookie2 = Cookie("Peanut Butter", 11, 4)
    cookie3 = Cookie("Diamond", 101, 10000)

    assert cookie1.name == "Chocolate"
    assert cookie1.cookie_quantity == 7
    assert cookie1.price_per_dozen == 3

    assert cookie2.name == "Peanut Butter"
    assert cookie2.cookie_quantity == 11
    assert cookie2.price_per_dozen == 4

    assert cookie3.name == "Diamond"
    assert cookie3.cookie_quantity == 101
    assert cookie3.price_per_dozen == 10000

def test_icecream():
    icecream1 = IceCream("Mint", 5, 1)
    icecream2 = IceCream("Rocky Road", 9, 2)
    icecream3 = IceCream("Titanium", 99, 9998)

    assert icecream1.name == "Mint"
    assert icecream1.scoop_count == 5
    assert icecream1.price_per_scoop == 1

    assert icecream2.name == "Rocky Road"
    assert icecream2.scoop_count == 9
    assert icecream2.price_per_scoop == 2

    assert icecream3.name == "Titanium"
    assert icecream3.scoop_count == 99
    assert icecream3.price_per_scoop == 9998

def test_sundae():
    sundae1 = Sundae("OreoSundae", 8, 1.5, "Oreo", 0.5)
    sundae2 = Sundae("FruityBlast", 12, 22, "Strawberry", 0.6)
    sundae3 = Sundae("GoldFlaked", 1000, 9999999, "Gold Flakes", 9999)

    assert sundae1.name == "OreoSundae"
    assert sundae1.scoop_count == 8
    assert sundae1.price_per_scoop == 1.5
    assert sundae1.topping_name == "Oreo"
    assert sundae1.topping_price == 0.5

    assert sundae2.name == "FruityBlast"
    assert sundae2.scoop_count == 12
    assert sundae2.price_per_scoop == 22
    assert sundae2.topping_name == "Strawberry"
    assert sundae2.topping_price == 0.6

    assert sundae3.name == "GoldFlaked"
    assert sundae3.scoop_count == 1000
    assert sundae3.price_per_scoop == 9999999
    assert sundae3.topping_name == "Gold Flakes"
    assert sundae3.topping_price == 9999

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
