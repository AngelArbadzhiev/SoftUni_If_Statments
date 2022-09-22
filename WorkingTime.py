
time = int(input())
dayOfTheWeek = str(input())
if dayOfTheWeek == "Monday" or dayOfTheWeek == "Tuesday" or dayOfTheWeek == "Wednesday" or dayOfTheWeek == "Thursday" or dayOfTheWeek == "Friday" or dayOfTheWeek == "Saturday":
    if 18 >= time >= 10:
        print("open")
    else:
        print("closed")
else:
    print("closed")
