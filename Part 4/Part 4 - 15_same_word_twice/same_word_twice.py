list = []
sum = 0

while True:
    word = input("Word: ")

    list.append(word)
    sum += 1

    if list.count(word) == 2:
        print(f"You typed in {sum - 1} different words")
        break