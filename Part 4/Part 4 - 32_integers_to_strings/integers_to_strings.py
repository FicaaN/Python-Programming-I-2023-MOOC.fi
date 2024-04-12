def formatted(list: list):
    new_list = []
    
    for number in list:
        f_number = f"{number:.2f}"
        new_list.append(f_number)
    return new_list

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)