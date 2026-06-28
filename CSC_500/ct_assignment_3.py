# Get user input for the food charge
food_cost = float(input("Enter cost of food: "))
tip = food_cost * 0.18
tax = food_cost * 0.07
total_cost = food_cost + tip + tax

# Display the results
print(f"Tip amount: ${tip:.2f}")
print(f"Sales tax: ${tax:.2f}")
print(f"Total cost: ${total_cost:.2f}")