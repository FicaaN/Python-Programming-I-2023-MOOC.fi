sentence = input("Please type in a sentence: ")

i = 0
length = len(sentence)

while i < length:
    while i < length and sentence[i] == " ":
        i += 1
    
    if i < length:
        print(sentence[i])
    
    while i < length and sentence[i] != " ":
        i += 1