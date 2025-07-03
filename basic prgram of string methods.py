#str methods
#lower , upper
str=input("enter str:-")
result=str.lower()
print(result)
result2=result.upper()
print(result2)

#title
str=input("enter str:-")
result=str.title()
print(result)

#capitalize
str=input("enter str:-")
result=str.capitalize()
print(result)

#find()
str=input("enter str:-")
result=str.find("a")
print(result)
#or find() in for loop
for char in range(0,len(str)):
   if str[char]=="a":
  #      print(char)
   #     break
   

#count()
str=input("enter str:-")
result=str.count("a")
print(result)


#split()
name="sai,kumar,ganesh"
result=name.split(",")
print(result)
result2=result[2].split("a")
print(result2)
