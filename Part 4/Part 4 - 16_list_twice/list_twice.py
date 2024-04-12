list1 = []
list2 = []

while True:
    item = int(input("New item: "))

    if item == 0:
        print("Bye!")
        break

    list1.append(item)
    list2.append(item)

    list2.sort()

    print(f"The list now: {list1}")
    print(f"The list in order: {list2}")