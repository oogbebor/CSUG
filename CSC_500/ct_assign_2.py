item_name_1 = input("Enter name of item: ")
item_price_1 = float(input("Enter item price: "))
item_quantity_1 = int(input("Enter item quantity: "))
item_description_1 = input("Enter item description: ")
subtotal_item_1 = item_quantity_1 * item_price_1
print("======================================")
item_name_2 = input("Enter name of item: ")
item_price_2 = float(input("Enter item price: "))
item_quantity_2 = int(input("Enter item quantity: "))
item_description_2 = input("Enter item description: ")
subtotal_item_2 = item_quantity_2 * item_price_2
print("======================================")
total_cost = subtotal_item_1 + subtotal_item_2

print(f"Item 1: {item_name_1}\nPrice: {item_price_1:.2f}\nQuantity: {item_quantity_1}\nDescription: {item_description_1}\nSubtotal: {subtotal_item_1:.2f}")
print("======================================")
print(f"Item 2: {item_name_2}\nPrice: {item_price_2:.2f}\nQuantity: {item_quantity_2}\nDescription: {item_description_2}\nSubtotal: {subtotal_item_2:.2f}")
print("======================================")
print(f"Total cost of items: {total_cost:.2f}")