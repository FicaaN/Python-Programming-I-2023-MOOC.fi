def read_fruits():
    
    fruits_dict = {}

    with open("fruits.csv") as file:

        for line in file:
            fruit_name, price = line.strip().split(';')
            fruits_dict[fruit_name] = float(price)

    return fruits_dict