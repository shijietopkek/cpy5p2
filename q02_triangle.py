#q02_triangle.py

#get input

sides = [int(input("Enter side 1:")), int(input("Enter side 2:")), int(input("Enter side 3:"))]
sides.sort()
                                         
#calculation
perimeter = sides[0] + sides[1] + sides[2]
                                         
#generate output
if sides[2] > (sides[0] + sides[1]):
    print("Invalid triangle!")
else:
    print("perimeter = {0}".format(perimeter))
             
