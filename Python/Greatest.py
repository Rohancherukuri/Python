# Checking the greatest number
n=int(input("Enter first  number: "))
a=int(input("Enter second number: "))
b=int(input("Enter third number: "))
if n>a and n>b:
    print n," is the greatest number"
elif a>b:
    print a," is the greatest number"
else:
    print b," is the greates number"
