from dessertshop.dessert import IceCream

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