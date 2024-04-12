temp = int(input("Please type in a temperature (F): "))

new_temp = (temp - 32) / 1.8

if new_temp < 0:
    print(f"{temp} degrees Fahrenheit equals {new_temp} degrees Celsius")
    print("Brr! It's cold in here!")
else: 
    print(f"{temp} degrees Fahrenheit equals {new_temp} degrees Celsius")