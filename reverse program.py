num = input("enter a number:=")
revnum=""
for char in range(len(num)-1,-1,-1):
    revnum+=num[char]
num=int(num)
if int(num)==int(revnum):
     print("yes")
else:
    print("no")
