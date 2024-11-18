from abc import ABC, abstractmethod

class DessertShop:
    def __init__(self):
        pass

    def user_prompt_candy(self):

        name = input("What is the name of the candy?: ").strip()
        
        valid = False
        while not valid:
            try:
                candy_weight = float(input("What is the weight of the candy?: ").strip())
                valid = True
            except ValueError:
                print("That's not a valid weight. Must be a float.")

        valid = False
        while not valid:
            try:
                candy_weight = float(input("What is the price per pound of the candy?: ").strip())
                valid = True
            except ValueError:
                print("That's not a valid weight. Must be a float.")

    def user_prompt_cookie(self):
        pass

    def user_prompt_icecream(self):
        pass

    def user_prompt_sundae(self):
        pass


class DessertItem(ABC):
    def __init__(self, name, tax_percent=7.25):
        self.name = name
        self.tax_percent = tax_percent

    def calculate_tax(self):
        return self.calculate_cost() * (self.tax_percent/100)

    @abstractmethod
    def calculate_cost(self):
        pass

class Candy(DessertItem):
    def __init__(self, name, candy_weight, price_per_pound):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

    def calculate_cost(self):
        return self.candy_weight * self.price_per_pound

class Cookie(DessertItem):
    def __init__(self, name, cookie_quantity, price_per_dozen):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
    
    def calculate_cost(self):
        return self.cookie_quantity/12 * self.price_per_dozen
        
class IceCream(DessertItem):
    def __init__(self, name, scoop_count, price_per_scoop):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
    
    def calculate_cost(self):
        return self.price_per_scoop * self.scoop_count
        
class Sundae(IceCream):
    def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price
    
    def calculate_cost(self):
        return super().calculate_cost() + self.topping_price


class Order:
    def __init__(self):
        self.order = []
    
    def add(self, item):
        self.order.append(item)
        return self
    
    def __len__(self):
        return len(self.order)

    def order_cost(self):
        total_cost = 0
        for item in self.order:
            total_cost += item.calculate_cost()
        return round(total_cost, 2)
    
    def order_tax(self):
        total_tax = 0
        for item in self.order:
            total_tax += item.calculate_tax()
        return round(total_tax, 2)
