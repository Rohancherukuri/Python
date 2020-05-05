# Checking the number if it is prime or not
n=int(input("Enter a number: "))
count=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
if count==2:
    print ("The number ",n," is a prime number")
else:
    print ("The number ",n," is a composite number")
