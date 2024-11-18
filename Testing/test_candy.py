from dessertshop.dessertshop import Candy

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