# q04_determine_leap_year.py
from q04_determine_leap_year import check_leap

while True:
    #get input
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))

    #formula
    month_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month_name = month_name[month-1]

    #range limit
    if year < 0:
        print("Invalid value!")

    # leap year
    if month == 2:
        if check_leap(year):
            print("Number of days: 29")

        else:
            print("Number of days: 28")

    elif month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        print("Number of days: 31")

    elif month == 4 or 6 or 9 or 11:
        print("Number of days: 30")

    else:
        print("Error! Please enter a number from 1 to 12.")





