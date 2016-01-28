# q04_determine_leap_year.py

#determine leap year
def check_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    #get input
    input_year = int(input("Enter year: "))

    #range limit
    if input_year < 0:
        print("Invalid value!")
        
    elif check_leap(input_year):
        print("Leap")
    else:
        print("Non-Leap")
    
