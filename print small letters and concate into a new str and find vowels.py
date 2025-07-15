#write a program to print small letters in a str and concate to empty string and iterate that concated string for finding no.of vowels in it.
str=input("enter str:")
vowels="aeiouAEIOU"
count=0
new_str=""
for char in str:
    if char.islower():
        print(char)
        new_str+=char
print(new_str)
for char in new_str:
    if char in vowels:
        print(char)
        count+=1
print("count:",count)
