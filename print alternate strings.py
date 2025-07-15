#write a program to print alternative chars
str=input("enter str:")
for i in range(len(str)):
    if i%2!=0:
        print(str[i])


#write a program to print alternative chars and concate all chars into empty strings and find the length of the concate string       
str=input("enter str:")
empty_str=""
for i in range(len(str)):
    if i%2!=0:
        print(str[i])
        empty_str+=str[i]
l=len(empty_str)
print(l)
    
