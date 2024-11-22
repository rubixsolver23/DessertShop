from receipt import make_receipt
from dessertshop import (
    Order,
    DessertItem,
    DessertShop,
    Candy,
    Cookie,
    IceCream,
    Sundae
)


def main():
    shop = DessertShop()
    order = Order()
    """
    order.add(Candy("Candy Corn", 1.5, .25))
    order.add(Candy("Gummy Bears", .25, .35))
    order.add(Cookie("Chocolate Chip", 6, 3.99))
    order.add(IceCream("Pistachio", 2, .79))
    order.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    order.add(Cookie("Oatmeal Raisin", 2, 3.45))
    """
    done: bool = False

    prompt = "\n".join([ "\n", 
                        "1: Candy", 
                        "2: Cookie", 
                        "3: Ice Cream", 
                        "4: Sundae", 
                        "\nWhat would you like to add to the order? (1-4, Enter for done): "])


    while not done:
        choice = input(prompt)
        match choice:
            case "":
                done = True
            case "1":
                item = shop.user_prompt_candy()
                order.add(item)
                print(f"{item.name} has been added to your order.")
            case '2':
                item = shop.user_prompt_cookie()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '3':
                item = shop.user_prompt_icecream()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '4':
                item = shop.user_prompt_sundae()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case _:
                print("Invalid response: Please enter a choice from the menu (1-4) or Enter")


    # Create the receipt
    order_list = []
    order_list.append(["Name", "Item Cost", "Tax"])
    for item in order.order:
        price = item.calculate_cost()
        tax = item.calculate_tax()
        order_list.append([item.name, "$%.2f"%(price), "$%.2f"%(tax)])
    order_list.append(["Order Subtotals", "$%.2f" %(order.order_cost()), "$%.2f"%(order.order_tax())])
    order_list.append(["Order Total", "", "$"+str(round(order.order_cost() + order.order_tax(), 2))])
    order_list.append(["Total items in the order", "", str(len(order))])
    make_receipt(order_list, "receipt")

    #print("\nThank you for your order! Have a nice day!")

main()