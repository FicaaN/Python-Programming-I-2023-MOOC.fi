number = int(input("Please type in a number: "))
i = 1
j = 1

while number > 0 and i <= number:
    if j <= number:
        print(f"{i} x {j} = {i * j}")
        j += 1
    elif j > number:
        i += 1
        j = 1