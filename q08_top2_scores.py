#q08_top2_scores.py

number_of_students = int(input("Enter no. of students: "))

students = [(str(input("Enter name of student: ")), int(input("Enter score of student: "))) for i in range(number_of_students)]

#sort the tuple
students.sort(key=lambda tup: tup[1], reverse = True)

#2 top scorers
top_scorer = students[0]
runner_up = students[1]

#print top 2 scorer
print("Top scorer: {0}".format(students[0]3))
print("2nd Top scorer: {0}".format(students[1]))
                                  





    

    
