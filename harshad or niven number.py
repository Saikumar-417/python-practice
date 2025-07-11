#Harshad Number Check
num=input("enter number:")
sum=0
for digit in num:
    sum+=int(digit)
if int(num)%int(sum)==0:
    print("it is a Harshad Number ")
else:
    print("it is not a Harshad Number ")
