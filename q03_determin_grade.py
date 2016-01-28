#q03_determine_grade.py

#get input

score = int(input("Enter score: "))

#corresponding grades
if score < 0 or score > 100:
    print("Invalid! Score must be within 0 - 100.")
elif score >= 70:
    print("Grade: A")
elif score >= 60:
    print("Grade: B")
elif score >= 55:
    print("Grade: C")
elif score >= 50:
    print("Grade: D")
elif score >= 45: 
    print("Grade: E")
elif score >= 35:
    print("Grade: S")
else:
    print("Grade: U")


              
            
