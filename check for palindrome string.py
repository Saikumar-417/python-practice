str=input("enter a string:")
reverse=""
for i in range(len(str)-1,-1,-1):
    reverse+=str[i]
if str==reverse: 
    print("it is a palindrome")
else:
    print("it is not palindrome")
