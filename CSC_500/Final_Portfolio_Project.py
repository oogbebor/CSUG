class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0,
                 item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def get_cost(self):
        return self.item_price * self.item_quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} "
              f"@ ${self.item_price:.2f} = ${self.get_cost():.2f}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="none"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def find_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                return item
        return None

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item is None:
            print("Item not found in cart.")
        else:
            self.cart_items.remove(item)

    def modify_item(self, modified_item):
        item = self.find_item(modified_item.item_name)
        if item is None:
            print("Item not found in cart.")
        elif modified_item.item_quantity != 0:
            item.item_quantity = modified_item.item_quantity

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.get_cost() for item in self.cart_items)

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


MENU = (
    "\nMENU\n"
    "a - Add item to cart\n"
    "r - Remove item from cart\n"
    "c - Change item quantity\n"
    "i - Output descriptions\n"
    "o - Output shopping cart\n"
    "q - Quit\n"
)


def add_item_to_cart(cart):
    print("\nADD ITEM TO CART")
    name = input("Enter the item name: ")
    description = input("Enter the item description: ")
    price = float(input("Enter the item price: "))
    quantity = int(input("Enter the item quantity: "))
    cart.add_item(ItemToPurchase(name, price, quantity, description))


def remove_item_from_cart(cart):
    print("\nREMOVE ITEM FROM CART")
    item_name = input("Enter name of item to remove: ")
    cart.remove_item(item_name)


def change_item_quantity(cart):
    print("\nCHANGE ITEM QUANTITY")
    item_name = input("Enter the item name: ")
    new_quantity = int(input("Enter the new quantity: "))
    cart.modify_item(ItemToPurchase(item_name, item_quantity=new_quantity))


def print_menu(cart):
    while True:
        print(MENU)
        choice = input("Choose an option: ")

        if choice == "a":
            add_item_to_cart(cart)
        elif choice == "r":
            remove_item_from_cart(cart)
        elif choice == "c":
            change_item_quantity(cart)
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
