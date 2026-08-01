import random


number = 1000
i = 0
file_name = "file2.txt"
while i < number:
    with open(file_name, "a") as f:
        print(random.randint(1, 1000), file=f)
    i += 1

print("Done!")