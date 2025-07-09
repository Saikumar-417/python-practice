num=input("enter number:")
revnum=""
l=len(num)
for i in range(l-1,-1,-1):
    revnum+=num[i]
print(revnum)
if num==revnum:
    print("it is a palindrome number")
else:
    print("it is not a palindrome number")
