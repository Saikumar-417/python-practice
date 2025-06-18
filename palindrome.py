str=input("enter a name:")
revstr=""
for char in range(len(str)-1,-1,-1):
    revstr+=str[char]
if (str==revstr):
    print( "given str is palindrome")
else:
    print(" it is not palindrome")
