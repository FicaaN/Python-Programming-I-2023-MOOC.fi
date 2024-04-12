import csv

def is_valid_line(line):
    try:
        week, numbers = line.strip().split(';')
        week_number = int(week.split()[1])
        number_list = [int(num) for num in numbers.split(',')]

        if len(number_list) != 7 or not all(1 <= num <= 39 for num in number_list) or len(set(number_list)) != 7:
            return False
    except (ValueError, IndexError):
        return False

    return True

def filter_incorrect():
    input_file = 'lottery_numbers.csv'
    output_file = 'correct_numbers.csv'

    try:
        with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
            reader = csv.reader(infile, delimiter=';')
            writer = csv.writer(outfile, delimiter=';')

            for line in reader:
                if is_valid_line(';'.join(line)):
                    writer.writerow(line)

        print(f"Filtered and saved correct lines to {output_file}")

    except FileNotFoundError:
        print(f"Error: File not found - {input_file}")