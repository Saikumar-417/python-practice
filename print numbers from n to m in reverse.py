#using for loop
n=int(input("enter number:"))
m=int(input("enter number:"))
for i in range(n,m-1,-1):
    print(i)
    
#using while loop
n=int(input("enter number:"))
m=int(input("enter number:"))
i=m
while n>=i:
    print(n)
    n-=1
