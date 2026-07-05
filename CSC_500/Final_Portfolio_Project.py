"""Online Shopping Cart - Portfolio Project.

Author: Ogbebor Osariemen
Course: CSC 500
Date: July 4th 2026

A menu-driven shopping cart program. The user enters their name and
today's date, then can add, remove, and modify items, and print the
cart's contents and item descriptions.
"""


class ItemToPurchase:
    """A single item in the cart: name, price, quantity, description."""

    def __init__(self, item_name="none", item_price=0.0, item_quantity=0,
                 item_description="none"):
        """Initialize an item, using default values if none are given."""
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def get_cost(self):
        """Return the total cost of this item (price x quantity)."""
        return self.item_price * self.item_quantity

    def print_item_cost(self):
        """Print this item's cost line, e.g. 'Milk 2 @ $3.00 = $6.00'."""
        print(f"{self.item_name} {self.item_quantity} "
              f"@ ${self.item_price:.2f} = ${self.get_cost():.2f}")


class ShoppingCart:
    """A customer's cart: holds items and prints totals and descriptions."""

    def __init__(self, customer_name="none", current_date="none"):
        """Initialize a cart for the given customer and date."""
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def find_item(self, item_name):
        """Return the cart item matching item_name, or None if not found."""
        for item in self.cart_items:
            if item.item_name == item_name:
                return item
        return None

    def add_item(self, item):
        """Add an ItemToPurchase to the cart."""
        self.cart_items.append(item)

    def remove_item(self, item_name):
        """Remove the named item, or print a message if it is not found."""
        item = self.find_item(item_name)
        if item is None:
            print("Item not found in cart.")
        else:
            self.cart_items.remove(item)

    def modify_item(self, modified_item):
        """Update an item's quantity, or print a not-found message.

        A quantity of 0 on modified_item means "leave the quantity as is".
        """
        item = self.find_item(modified_item.item_name)
        if item is None:
            print("Item not found in cart.")
        elif modified_item.item_quantity != 0:
            item.item_quantity = modified_item.item_quantity

    def get_num_items_in_cart(self):
        """Return the total quantity of all items in the cart."""
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        """Return the total cost of all items in the cart."""
        return sum(item.get_cost() for item in self.cart_items)

    def print_total(self):
        """Print the cart header, each item's cost line, and the total."""
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
        """Print the cart header and each item's description."""
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()
        print("Item Descriptions")
        if not self.cart_items:
            print("CART IS EMPTY")
        else:
            for item in self.cart_items:
                print(f"{item.item_name}: {item.item_description}")


# Menu text shown before each prompt; one letter per option.
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
    """Prompt for a new item's details and add it to the cart."""
    print("\nADD ITEM TO CART")
    name = input("Enter the item name: ")
    description = input("Enter the item description: ")
    price = float(input("Enter the item price: "))
    quantity = int(input("Enter the item quantity: "))
    cart.add_item(ItemToPurchase(name, price, quantity, description))


def remove_item_from_cart(cart):
    """Prompt for an item name and remove that item from the cart."""
    print("\nREMOVE ITEM FROM CART")
    item_name = input("Enter name of item to remove: ")
    cart.remove_item(item_name)


def change_item_quantity(cart):
    """Prompt for an item name and new quantity, then update the cart."""
    print("\nCHANGE ITEM QUANTITY")
    item_name = input("Enter the item name: ")
    new_quantity = int(input("Enter the new quantity: "))
    cart.modify_item(ItemToPurchase(item_name, item_quantity=new_quantity))


def print_menu(cart):
    """Show the menu and handle the user's choices until they quit."""
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
    # Get the customer's info, echo it back, then start the menu loop.
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    print()
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)
