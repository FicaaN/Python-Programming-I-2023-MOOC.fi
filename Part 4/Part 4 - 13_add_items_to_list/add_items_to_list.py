items = int(input("How many items: "))

list = []

for item in range(items):
    list.append(int(input(f"Item {item + 1}: ")))

print(list)