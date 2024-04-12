limit = int(input("Limit: "))

summ = 0
number = 1
end = "The consecutive sum:"

while limit > summ:
    end += f" {number}"
    summ = summ + number
    number += 1

    if limit > summ:
        end += " +"

print(end + f" = {summ}")