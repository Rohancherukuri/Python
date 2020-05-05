# Creating an armstrong number in python
n=int(input("Enter a number: "))
r=0
temp=n
while n>0:
    i=n%10
    r=r+ i**3
    n//=10

if temp==r:
    print("The number ",temp," is an Armstrong number")
else:
    print("The number ",temp," is not am Armstrong number")

