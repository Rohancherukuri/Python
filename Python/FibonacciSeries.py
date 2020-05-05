# Implemeting Fibonacci Series
n=int(input("Enter the series range: "))
a=-1
c=0
b=1
print("The Fibonacci Series is: ")
for i in range(0,n):
    c=a+b
    print(c," ")
    a=b
    b=c
    c=a
