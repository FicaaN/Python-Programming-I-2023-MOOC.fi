string = input("Please type in a string: ")

index = 0
length = 1 + len(string)

for index in range(length):
    print(string[0:index])
    index += 1