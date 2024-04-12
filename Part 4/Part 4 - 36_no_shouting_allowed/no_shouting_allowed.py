def no_shouting(list_strings: list):
    new_list = []

    for strings in list_strings:
        if strings.isupper():
            continue
        else:
            new_list.append(strings)
    
    return new_list

if __name__ == "__main__":

    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)