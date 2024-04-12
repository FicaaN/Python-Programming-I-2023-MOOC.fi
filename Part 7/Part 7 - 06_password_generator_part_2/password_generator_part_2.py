import random
import string

def generate_strong_password(length: int, include_numbers: bool, include_special_chars: bool):

    lowercase_alphabet = random.choice(string.ascii_lowercase)

    remaining_length = max(length - 1, 1)

    char_set = set(lowercase_alphabet)

    if include_numbers:
        char_set.add(random.choice(string.digits))
        remaining_length -= 1

    if include_special_chars:
        char_set.add(random.choice('!?=+-()#'))
        remaining_length -= 1

    if remaining_length > 0:
        additional_chars = string.ascii_lowercase
        if include_numbers:
            additional_chars += string.digits
        if include_special_chars:
            additional_chars += '!?=+-()#'

        char_set.update(random.sample(additional_chars, remaining_length))

    password_list = list(char_set)
    random.shuffle(password_list)

    password = ''.join(password_list)

    while len(password) < length:
        return generate_strong_password(length, include_numbers, include_special_chars)

    return password

if __name__ == "__main__":

    for i in range(10):
        print(generate_strong_password(12, False, False))