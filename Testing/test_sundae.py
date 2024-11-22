from dessertshop.dessert import Sundae

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