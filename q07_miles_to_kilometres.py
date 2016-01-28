#q07_miles_to_kilometres.py

#print table headings 
print("Miles Kilometres Kilometres Miles")

#conversion
miles_to_kilometres = 1.609
kilometres_to_miles = 1/miles_to_kilometres

#print conversion values
for i in range (1,11):
    print("{0:<6}{1:<11.3f}{2:<11}{3:.3f}".format(i, miles_to_kilometres * i, (i + 3) * 5, kilometres_to_miles * ((i+3) * 5)))
