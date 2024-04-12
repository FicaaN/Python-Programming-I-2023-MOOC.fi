import random

def words(n: int, beginning: str):

    with open("words.txt") as file:
        all_words = [line.strip() for line in file if line.startswith(beginning)]
    
    if len(all_words) < n:
        raise ValueError("not enough words beginning with the specified string")
    
    return random.sample(all_words, n)

if __name__ == "__main__":

    word_list = words(3, "ca")
    for word in word_list:
        print(word)