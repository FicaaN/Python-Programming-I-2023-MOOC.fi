number = int(input("Please type in a number: "))

for i in range(1, (number // 2) + 1):
    print(i)
    print(number - i + 1)

if number % 2 == 1:
    print((number // 2) + 1)