fruit = str(input())
dayOfTheWeek = str(input())
quantity = float(input())
price = 0.00
if dayOfTheWeek == "Monday" or dayOfTheWeek == "Tuesday" or dayOfTheWeek == "Wednesday" or dayOfTheWeek == "Thursday" or dayOfTheWeek == "Friday":
    if fruit == "banana":
        price = 2.50
    if fruit == "apple":
        price = 1.20
    if fruit == "orange":
        price = 0.85
    if fruit == "grapefruit":
        price = 1.45
    if fruit == "kiwi":
        price = 2.70
    if fruit == "pineapple":
        price = 5.50
    if fruit == "grapes":
        price = 3.85
if dayOfTheWeek == "Saturday" or dayOfTheWeek == "Sunday":
    if fruit == "banana":
        price = 2.70
    if fruit == "apple":
        price = 1.25
    if fruit == "orange":
        price = 0.90
    if fruit == "grapefruit":
        price = 1.60
    if fruit == "kiwi":
        price = 3.00
    if fruit == "pineapple":
        price = 5.60
    if fruit == "grapes":
        price = 4.20
total = format(price * quantity, '.2f')
print(total)
