phone_book = {}

while True:

    command = int(input("command (1 search, 2 add, 3 quit): "))

    if command == 3:
        print("quitting...")
        break
    elif command == 2:
        name = input("name: ")
        number = input("number: ")

        phone_book[name] = number

        print("ok!")
    elif command == 1:
        name1 = input("name: ")

        if name1 in phone_book:
            print(phone_book[name1])
        else:
            print("no number")       