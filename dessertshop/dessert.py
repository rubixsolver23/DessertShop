from receipt import make_receipt
from dessertshop import (
    Order,
    DessertItem,
    Candy,
    Cookie,
    IceCream,
    Sundae
)


def main():
    order1 = Order()
    order1.add(Candy("Candy Corn", 1.5, .25))
    order1.add(Candy("Gummy Bears", .25, .35))
    order1.add(Cookie("Chocolate Chip", 6, 3.99))
    order1.add(IceCream("Pistachio", 2, .79))
    order1.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    order1.add(Cookie("Oatmeal Raisin", 2, 3.45))

    order_list = []
    order_list.append(["Name", "Item Cost", "Tax"])
    for item in order1.order:
        price = item.calculate_cost()
        tax = item.calculate_tax()
        order_list.append([item.name, "$%.2f"%(price), "$%.2f"%(tax)])
    order_list.append(["Order Subtotals", "$%.2f" %(order1.order_cost()), "$%.2f"%(order1.order_tax())])
    order_list.append(["Order Total", "", "$"+str(round(order1.order_cost() + order1.order_tax(), 2))])
    order_list.append(["Total items in the order", "", str(len(order1))])
    make_receipt(order_list, "receipt")

main()