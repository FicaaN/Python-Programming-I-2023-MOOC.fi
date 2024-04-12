string = input("Please type in a string: ")
char = input("Please type in a character: ")

index = 0

while index < len(string) - 2:
    if string[index] == char:
        print(string[index:index + 3])
    index += 1