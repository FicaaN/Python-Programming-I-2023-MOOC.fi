def everything_reversed(strings: list):
    new_strings = []
    for string in reversed(strings):
        r_string = string[::-1]
        new_strings.append(r_string)

    return new_strings

if __name__ == "__main__":

    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)