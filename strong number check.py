#Strong Number Check

num=input("enter number:")
sum_of_factorials=0
for digit in str(num):
    digit=int(digit)
    fact=1
    for i in range(1,digit+1):
        fact*=i
    sum_of_factorials+=fact
        
if num==sum_of_factorials:
    print("it is a strong number:")
else:
    print("it is not a strong number:")
