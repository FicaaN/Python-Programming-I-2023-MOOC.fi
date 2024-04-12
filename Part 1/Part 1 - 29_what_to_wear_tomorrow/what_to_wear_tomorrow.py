print("What is the weather forecast for tomorrow?")

temperature = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")

clothing_suggestions = ["Wear jeans and a T-shirt"]
if temperature > 20:
    clothing_suggestions.append("")
elif temperature > 10:
    clothing_suggestions.append("I recommend a jumper as well.")
elif temperature > 5:
    clothing_suggestions.extend(["I recommend a jumper as well.", "Take a jacket with you"])
else:
    clothing_suggestions.extend(["I recommend a jumper as well.", "Take a jacket with you", "Make it a warm coat, actually.", "I think gloves are in order."])

if rain == 'yes':
    clothing_suggestions.extend(["Don't forget your umbrella!"])

print("\n".join(clothing_suggestions))