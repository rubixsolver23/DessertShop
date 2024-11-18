from dessertshop.dessertshop import Cookie

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