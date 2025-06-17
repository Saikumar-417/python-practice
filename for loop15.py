
name ="saikumar"
vowels="aeiouAEIOU"
vowelsstr=""
vowelslist=[]
for char in name:
    if char in vowels:
        vowelsstr+=char
        vowelslist.append(char)
print(vowelsstr)
print(vowelslist)
