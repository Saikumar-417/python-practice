# write a program to print vowels in your village name and print count of vowels
str=input("enter str:")
count=0
vowels="aeiouAEIOU"
for i in str:
    if i in vowels:
        print(i)
        count+=1
print("count:",count)

# write a program to print consonants in your village name and print count of consonants
str=input("enter str:")
count=0
vowels="aeiouAEIOU"
for i in str:
    if i not in vowels:
        print(i)
        count+=1
print("count:",count)
