num=input("enter number:")
l=len(num)
result=0
for i in num:
    if int(i)**l:
        result+=(int(i)**l)
 
print(result)
if result==int(num):
    print("it is a armstrong number")
else:
    print("it is not a armstrong number")
