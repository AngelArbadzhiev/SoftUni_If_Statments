dayOfTheWeek = str(input())
if dayOfTheWeek == 'Monday' or dayOfTheWeek == 'Tuesday' or dayOfTheWeek == 'Wednesday' or dayOfTheWeek == 'Thursday' or dayOfTheWeek == 'Friday':
    print("Working day")
elif dayOfTheWeek == 'Saturday' or dayOfTheWeek == 'Sunday':
    print("Weekend")
else:
    print("Error")
