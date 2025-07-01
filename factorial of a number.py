#using for loop
n=int(input("enter number:"))
mul=1
for i in range(1,n+1,1):
    print(i)
    mul=mul*i
print(mul)

#using while loop
n=int(input("enter number:"))
mul=1
i=1
while i<=n:
    print(i)
    mul*=i
    i+=1
print(mul)
