#for loop
n=int(input("enter number:"))

for i in range(1,n+1,1):
    if n%i==0:
        print(i)


#while loop
n=int(input("enter number:"))

i=1
while i<=n:
    if n%i==0:
        print(i)
    i+=1
