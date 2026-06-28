# Using the latest version of Python, write a single program that performs basic arithmetic. Your program must prompt the user to input two numbers ($num1$ and $num2$) and then calculate and display the results for:

# Addition ($num1 + num2$)
# Subtraction ($num1 - num2$)
# Multiplication ($num1 \times num2$)
# Division ($num1 / num2$)

num1 = int(input("Enter first number:", ))
num2 = int(input("Enter second number:", ))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)