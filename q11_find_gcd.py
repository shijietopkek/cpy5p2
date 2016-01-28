#q11_find_gcd.py

#get input
numbers = [int(input("Enter the first integer: ")),int(input("Enter the second integer: "))]

numbers.sort()

d = numbers[0]

#while loop
while (numbers[0] % d != 0) or (numbers[1] % d != 0):
    d = d-1

#generate output
print("Greatest common divisor: {0}".format(d))
