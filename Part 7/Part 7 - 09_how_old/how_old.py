from datetime import datetime

def calculate_age(year: int, month: int, day: int):
    
    birthday = datetime(year, month, day)
    millennium = datetime(1999, 12, 31)
    difference = millennium - birthday

    return difference.days

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

age_by_millennium = calculate_age(year, month, day)

if age_by_millennium > 0:
    print(f"You were {age_by_millennium} days old on the eve of the new millennium.")
else:
    print(f"You weren't born yet on the eve of the new millennium.")