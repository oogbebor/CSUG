# Portfolio Project Updated- Multiple Item Entry using loops.
total_cost = 0.0
item_count = 0

while True:
    item_name = input("Enter name of item or type 'quit' to finish: ")

    if item_name.lower() == "quit":
        break

    item_price = float(input("Enter item price: "))
    item_quantity = int(input("Enter item quantity: "))
    item_description = input("Enter item description: ")

    subtotal = item_price * item_quantity
    total_cost += subtotal
    item_count += 1

    print("======================================")
    print(f"Item: {item_name}")
    print(f"Price: ${item_price:.2f}")
    print(f"Quantity: {item_quantity}")
    print(f"Description: {item_description}")
    print(f"Subtotal: ${subtotal:.2f}")
    print("======================================")

print("Summary")
print("======================================")
print(f"Total number of items entered: {item_count}")
print(f"Total cost of all items: ${total_cost:.2f}")
