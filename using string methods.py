#write a program to print upper,lower,digits,even,odd,prime,special characters print all are in separate list.
input_str=input("enter str:-")
lowercase=[]
uppercase=[]
digits=[]
even=[]
odd=[]
schar=[]
prime=[]
for char in input_str:
    if char.isalpha():
        if char.isupper():
            uppercase.append(char)
        if char.islower():
            lowercase.append(char)
    if char.isdigit():
        digits.append(char)
        if int(char)%2==0:
            even.append(char)
        if int(char)%2!=0:
            odd.append(char)
    if not char.isalnum() and not char.isdigit():
        schar.append(char)
    if char.isdigit():
        
        if int(char) in [2,3,5,7]:
            
            prime.append(char)
            
        
       
            
            
print(lowercase)
print(uppercase)
print(digits)
print(even)
print(odd)
print(schar)
print(prime)
