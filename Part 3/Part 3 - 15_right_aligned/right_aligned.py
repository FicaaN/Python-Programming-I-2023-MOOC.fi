string = input("Please type in a string: ")

if len(string) == 20:
    print(string)
else:
    fill = 20 - len(string)
    print('*' * fill + string)