#Count consonants in String

str=input("enter str:")
count=0
vowels="aeiouAEIOU"
for char  in str:
    if char not in vowels:
        count+=1
print(count)
