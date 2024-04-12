def distinct_numbers(lst):
    sorted_list = sorted(lst)
    unique_list = [sorted_list[i] for i in range(len(sorted_list) - 1) if sorted_list[i] != sorted_list[i + 1]]
    unique_list.append(sorted_list[-1])
    return unique_list

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))