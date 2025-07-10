#Perfect Number Check
num=int(input("enter number:"))
add=0
for i in range(1,num,1):
    if num%i==0:
        add+=i
print(add)
if num==add:
    print("it is a perfect number:")
else:
    print("it is not a perfect number:")
