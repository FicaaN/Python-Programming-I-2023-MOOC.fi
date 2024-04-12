def all_the_longest(string_list):
    max_length = len(max(string_list, key=len))
    longest_strings = [s for s in string_list if len(s) == max_length]

    return longest_strings

if __name__ == "__main__":

    my_list1 = ["first", "second", "fourth", "eleventh"]
    result1 = all_the_longest(my_list1)
    print(result1) 

    my_list2 = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result2 = all_the_longest(my_list2)
    print(result2) 