def shortest(string_list):
    shortest_str = string_list[0]

    for s in string_list[1:]:
        if len(s) < len(shortest_str):
            shortest_str = s

    return shortest_str

if __name__ == "__main__":
    
    my_list1 = ["first", "second", "fourth", "eleventh"]
    result1 = shortest(my_list1)
    print(result1) 

    my_list2 = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result2 = shortest(my_list2)
    print(result2)