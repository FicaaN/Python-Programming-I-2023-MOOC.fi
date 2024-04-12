def range_of_list(list: list) -> int:
    max_list = max(list)
    min_list = min(list)
    return max_list - min_list

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)