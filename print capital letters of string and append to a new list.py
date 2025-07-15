#write a program to print capital letters in a str and arrange them into a list and find length of list
str=input("enter str:")
list=[]
for char in str:
    if char.isupper():
        print(char)
        list.append(char)
print(len(list))
print(list)
