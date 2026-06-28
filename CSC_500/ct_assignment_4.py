class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
        
    def get_cost(self):
        return self.item_price * self.item_quantity

    def print_item_cost(self):
        cost_of_item = self.get_cost()
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.1f} = ${cost_of_item:.1f}")

def main():
    
    items = []
    total_cost = 0
    while True:
        item = ItemToPurchase()
        item.item_name = input("Enter item name or input quit to finish:\n")
        if item.item_name.lower() == "quit":
            break
        item.item_price = float(input("Enter the price of item:\n"))
        item.item_quantity = int(input("Enter the quantity of item:\n"))
        items.append(item)

    print("TOTAL COST")
    for item in items:
        item.print_item_cost()
        total_cost += item.get_cost()
    print(f"Total: ${total_cost:.1f}")

if __name__ == "__main__":
    main()
    