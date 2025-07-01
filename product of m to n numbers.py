#for loop
n=int(input("enter number:"))
m=int(input("enter number:"))
product=1
for i in range(n,m+1,1):
    print(i)
    product*=i
print("product of numbers:",product)

#while loop
n=int(input("enter number:"))
m=int(input("enter number:"))
product=1
i=n
while i<=m:
    print(i)
    product*=i
    i+=1
print("product of numbers:",product)
