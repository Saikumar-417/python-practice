#using for loop
n=int(input("enter number:"))
add=0
for i in range(1,n+1,1):
    print(i)
    add+=i
print(add)

#using while loop
n=int(input("enter number:"))
add=0
i=1
while i<=n:
  
     add+=i
     i+=1
   
print(add)
