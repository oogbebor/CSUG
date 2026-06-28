# String new_paint is read from input and assigned to the element at index 2 of list paint_list. 
# Complete the for loop so that for each value in paint_list, "Input: " is output, followed by the value on the same line.

paint_list = ["fuchsia", "lemon", "magenta", "red"]

new_paint = input()
paint_list[2] = new_paint

print(f"List has {len(paint_list)} elements:")
for value in paint_list:
    print(f"Input: {value}")