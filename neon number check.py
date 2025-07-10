#Neon Number Check
num=int(input("enter number:"))
square=num**2
print(square)
add=0
for digit in str(square) :
    add+= int(digit)
if num==add:
    print("it is a neon number:")
else:
    print("it is not a neon number:")
