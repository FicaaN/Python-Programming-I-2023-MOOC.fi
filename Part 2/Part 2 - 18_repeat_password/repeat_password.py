password = input("Password: ")

while True:

    password1 = input("Repeat password: ")

    if password1 == password:
        break
    else:
        print("They do not match!")

print("User account created!")