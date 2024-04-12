wage = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
day = input("Day of the week: ")

if day == "Sunday":
    print(f"Daily wages: {wage * hours_worked * 2} euros")
else:
    print(f"Daily wages: {wage * hours_worked} euros")