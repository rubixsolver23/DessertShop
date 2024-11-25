from abc import ABC, abstractmethod
from packaging import Packaging

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
                price_per_pound = float(input("What is the price per pound of the candy?: ").strip())
                valid = True
            except ValueError:
                print("That's not a valid price. Must be a float.")

        return Candy(name, candy_weight, price_per_pound)
    
    def user_prompt_cookie(self):

        name = input("What is the name of the cookie?: ").strip()
        
        valid = False
        while not valid:
            try:
                cookie_count = int(input("How many cookies?: ").strip())
                valid = True
            except ValueError:
                print("That's not a valid weight. Must be an integer.")

        valid = False
        while not valid:
            try:
                price_per_dozen = float(input("What is the price per dozen of the cookie?: ").strip())
                valid = True
            except ValueError:
                print("That's not a valid price. Must be a float.")

        return Cookie(name, cookie_count, price_per_dozen)

    def user_prompt_icecream(self):

        name = input("What is the name of the ice cream?: ").strip()
        
        valid = False
        while not valid:
            try:
                scoop_count = int(input("How many scoops?: ").strip())
                valid = True
            except ValueError:
                print("That's not a valid amount. Must be an integer.")

        valid = False
        while not valid:
            try:
                price_per_scoop = float(input("What is the price per scoop of the ice cream?: ").strip())
                valid = True
            except ValueError:
                print("That's not a valid price. Must be a float.")

        return IceCream(name, scoop_count, price_per_scoop)

    def user_prompt_sundae(self):
        name = input("What is the name of the sundae?: ").strip()
        
        valid = False
        while not valid:
            try:
                scoop_count = int(input("How many scoops?: ").strip())
                valid = True
            except ValueError:
                print("That's not a valid amount. Must be an integer.")

        valid = False
        while not valid:
            try:
                price_per_scoop = float(input("What is the price per scoop?: ").strip())
                valid = True
            except ValueError:
                print("That's not a valid price. Must be a float.")

        topping_name = input("What is the name of the topping?: ").strip()

        valid = False
        while not valid:
            try:
                topping_price = float(input("What is the price of the topping?: ").strip())
                valid = True
            except ValueError:
                print("That's not a valid price. Must be a float.")
        
        return Sundae(name, scoop_count, price_per_scoop, topping_name, topping_price)


class DessertItem(ABC, Packaging):
    def __init__(self, name, tax_percent=7.25, packaging=None):
        super().__init__(packaging)
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
        self.packaging = "Bag"

    def calculate_cost(self):
        return self.candy_weight * self.price_per_pound
    
    def __str__(self):
        return f"{self.name} ({self.packaging}), {self.candy_weight}lbs, ${self.price_per_pound}/lb, ${round(self.calculate_cost(), 2)}, ${round(self.calculate_tax(), 2)}"

class Cookie(DessertItem):
    def __init__(self, name, cookie_quantity, price_per_dozen):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
        self.packaging = "Box"
    
    def calculate_cost(self):
        return self.cookie_quantity/12 * self.price_per_dozen
    
    def __str__(self):
        return f"{self.name} ({self.packaging}), {self.cookie_quantity} cookies, ${self.price_per_dozen}/dozen, ${round(self.calculate_cost(), 2)}, ${round(self.calculate_tax(), 2)}"
        
class IceCream(DessertItem):
    def __init__(self, name, scoop_count, price_per_scoop):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        self.packaging = "Bowl"
    
    def calculate_cost(self):
        return self.price_per_scoop * self.scoop_count
    
    def __str__(self):
        return f"{self.name} ({self.packaging}), {self.scoop_count} scoops, ${self.price_per_scoop}/scoop, ${round(self.calculate_cost(), 2)}, ${round(self.calculate_tax(), 2)}"
        
class Sundae(IceCream):
    def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price
        self.packaging = "Boat"
    
    def calculate_cost(self):
        return super().calculate_cost() + self.topping_price
    
    def __str__(self):
        return f"{self.name} ({self.packaging}), {self.scoop_count} scoops, ${self.price_per_scoop}/scoop, ${self.topping_price} of {self.topping_name}, ${round(self.calculate_cost(), 2)}, ${round(self.calculate_tax(), 2)}"


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

    def __str__(self):
        string_repr = "----------------------------------------------Receipt---------------------------"
        for item in self.order:
            if isinstance(item, Candy):
                string_repr += f"\n{item.name} ({item.packaging})"
                string_repr += f"\n      {item.candy_weight} lbs. @ ${item.price_per_pound}/lb.:"
                string_repr += " "*(54-len(f"      {item.candy_weight} lbs. @ ${item.price_per_pound}/lb.:"))
                string_repr += f"${round(item.calculate_cost(), 2)}           [Tax: ${round(item.calculate_tax(), 2)}]"

            elif isinstance(item, Cookie):
                string_repr += f"\n{item.name} ({item.packaging})"
                string_repr += f"\n      {item.cookie_quantity} cookies @ ${item.price_per_dozen}/dozen:"
                string_repr += " "*(54-len(f"      {item.cookie_quantity} cookies @ ${item.price_per_dozen}/dozen:"))
                string_repr += f"${round(item.calculate_cost(), 2)}           [Tax: ${round(item.calculate_tax(), 2)}]"

            elif isinstance(item, Sundae):
                string_repr += f"\n{item.name} ({item.packaging})"
                string_repr += f"\n      {item.scoop_count} scoops @ ${item.price_per_scoop}/scoop"
                string_repr += f"\n      {item.topping_name} topping @ ${item.topping_price}:"

                string_repr += " "*(54-len(f"      {item.topping_name} topping @ ${item.topping_price}:"))
                string_repr += f"${round(item.calculate_cost(), 2)}           [Tax: ${round(item.calculate_tax(), 2)}]"
            
            elif isinstance(item, IceCream):
                string_repr += f"\n{item.name} ({item.packaging})"
                string_repr += f"\n      {item.scoop_count} scoops @ ${item.price_per_scoop}/scoop:"
                string_repr += " "*(54-len(f"      {item.scoop_count} scoops @ ${item.price_per_scoop}/scoop:"))
                string_repr += f"${round(item.calculate_cost(), 2)}           [Tax: ${round(item.calculate_tax(), 2)}]"
            
        string_repr += "---------------------------------------------------------------------------------"
        string_repr += f"Total number of items in the order: {len(self)}"
        return string_repr[:-2]