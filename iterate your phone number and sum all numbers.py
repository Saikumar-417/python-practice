#write a program to iterate your phone number add sum all digits which are>5 in your phone number.
num=8677162099
pno=str(num)
sum=0
for digit in pno:
    if int(digit)>=5:
        sum+=int(digit)
print(sum)
