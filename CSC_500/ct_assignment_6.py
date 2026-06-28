class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description = "none"

    def get_cost(self):
        return self.item_price * self.item_quantity

    def print_item_cost(self):
        cost_of_item = self.get_cost()
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${cost_of_item:.2f}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="none"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart.")

    def modify_item(self, modified_item):
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                return
        print("Item not found in cart.")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.get_cost()
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        print()
        if not self.cart_items:
            print("CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            print()
            print(f"Total: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()
        print("Item Descriptions")
        if not self.cart_items:
            print("CART IS EMPTY")
        else:
            for item in self.cart_items:
                print(f"{item.item_name}: {item.item_description}")


def print_menu(cart):
    menu = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
    )
    while True:
        print(menu)
        choice = input("Choose an option: ")

        if choice == "a":
            print("\nADD ITEM TO CART")
            item = ItemToPurchase()
            item.item_name = input("Enter the item name: ")
            item.item_description = input("Enter the item description: ")
            item.item_price = float(input("Enter the item price: "))
            item.item_quantity = int(input("Enter the item quantity: "))
            cart.add_item(item)

        elif choice == "r":
            print("\nREMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove: ")
            cart.remove_item(item_name)

        elif choice == "c":
            print("\nCHANGE ITEM QUANTITY")
            item_name = input("Enter the item name: ")
            new_quantity = int(input("Enter the new quantity: "))
            modified = ItemToPurchase()
            modified.item_name = item_name
            modified.item_quantity = new_quantity
            cart.modify_item(modified)

        elif choice == "i":
            print("\nOUTPUT DESCRIPTIONS")
            cart.print_descriptions()

        elif choice == "o":
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()

        elif choice == "q":
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    print()
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)