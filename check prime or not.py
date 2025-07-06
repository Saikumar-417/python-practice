
num=int(input("enter num:"))
factors=0
for i in range(1,num+1):
    if num%i == 0 :
        factors+=1
print(factors)
if factors==2:
    print("it is a prime number")
else:
    print("not a prime number")
