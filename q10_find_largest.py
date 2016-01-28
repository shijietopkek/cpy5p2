#q10_find_largest.py
#while loop
n = 1
while n * n * n < 12000:
    n = n + 1

#print output
print("Greatest integer n, n^3 < 12000: ",(n-1))
