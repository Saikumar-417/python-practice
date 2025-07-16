# WAP to find falsy values in the list[{},[],0,0,"","False",False] and concate all of them to empty str and find the length of the concated str.
list=[{},[],0,0,"","False",False]
newstr=""
for item in list:
    if not item:
        newstr+=str(item)
print(newstr)
print(len(newstr))
