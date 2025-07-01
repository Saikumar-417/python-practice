#for loop
n=int(input("enter number:"))
count=0
for i in range(1,n+1,1):
    if n%i==0:
        print(i)
        count+=1
print("total factors count:",count)

#while loop
n=int(input("enter number:"))
count=0
i=1
while i<=n:
    if n%i==0:
        print(i)
        count+=1
    i+=1
print("total factors count:",count)
