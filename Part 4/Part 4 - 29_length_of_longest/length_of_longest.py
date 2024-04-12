def length_of_longest(string_list):
    max_length = len(string_list[0])

    for s in string_list[1:]:
        current_length = len(s)
        if current_length > max_length:
            max_length = current_length

    return max_length

if __name__ == "__main__":

    my_list1 = ["first", "second", "fourth", "eleventh"]
    result1 = length_of_longest(my_list1)
    print(result1)  

    my_list2 = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result2 = length_of_longest(my_list2)
    print(result2) 