def largest():

    with open("numbers.txt") as file:
            
            numbers = [float(line.strip()) for line in file]
        
    max_number = max(numbers)

    return int(max_number)