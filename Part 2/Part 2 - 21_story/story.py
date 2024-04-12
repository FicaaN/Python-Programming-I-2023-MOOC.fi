sentence = ""
word1 = None

while True:
    word = input("Please type in a word: ")

    if word == "end":
        print(sentence)
        break
    elif word == word1:
        print(sentence)
        break
    else:
        sentence += word + " "
        word1 = word