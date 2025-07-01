#for loop
n=int(input("enter number:"))
m=int(input("enter number:"))
sum=0
for i in range(n,m+1,1):
    print(i)
    sum+=i
print("total:",sum)

#while loop
n=int(input("enter number:"))
m=int(input("enter number:"))
sum=0
i=n
while i<=m:
    print(i)
    sum=sum+i
    i=i+1
print("total:",sum)
