def even_numbers(list: list):
    list1 = []
    for i in list:
        if i % 2 == 0:
            list1.append(i)
    return list1

if __name__ == "__main__":
    my_list = [1, 2, 3, 4 ,5]
    new_list = even_numbers(my_list)
    print(f"original {my_list}")
    print(f"new {new_list}")