list = []
number = 1

print(f"The list is now {list}")

while True:
    letter = input("a(d)d, (r)emove or e(x)it: ")

    if letter == 'x':
        print("Bye!")
        break

    if letter == 'd':
        list.append(number)
        number += 1

        print(f"The list is now {list}")

    if letter == 'r':
        list.pop()
        number -= 1

        print(f"The list is now {list}")