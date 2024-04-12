cafeteria = int(input("How many times a week do you eat at the student cafeteria? "))
lunch = float(input("The price of a typical student lunch? "))
money = float(input("How much money do you spend on groceries in a week? "))
print("\n")

print("Average food expenditure:")
print(f"Daily: {((cafeteria * lunch) + money) / 7} euros")
print(f"Weekly: {(cafeteria * lunch) + money} euros")