count = 0
summ = 0
mean = 0
positive = 0
negative = 0

while True:

    print("Please type in integer numbers. Type in 0 to finish.")
    number = int(input("Number: "))
    count += 1
    summ += number
    mean = summ / count

    if number > 0:
        positive += 1
    else:
        negative += 1

    if number == 0:
        break
    else:
        print(f"Numbers typed in {count}")
        print(f"The sum of the numbers is {summ}")
        print(f"The mean of the numbers is {mean}")
        print(f"Positive numbers {positive}")
        print(f"Negative numbers {negative}")