def first_word(sentence1):
    words = sentence1.split()
    return words[0]

def second_word(sentence1):
    words = sentence1.split()
    return words[1]

def last_word(sentence1):
    words = sentence1.split()
    return words[-1]

if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))