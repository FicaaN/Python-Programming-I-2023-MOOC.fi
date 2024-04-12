import random
import string

def generate_password(length: int):

    password = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    return password

if __name__ == "__main__":

    for i in range(10):
        print(generate_password(i))