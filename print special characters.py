#write a program to print special symbols in str
str=input("enter number:")
for char in str:
    if not char.isalnum() and not char.isspace():
        print(char)
