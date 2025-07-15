str=input("enter str:")
new_list1=[]
list=[]
for char in str:
    if char.isdigit() or char.isspace():
        print(char)
        list.append(char)
print(list)
new_list=[1,2,3,10,12,30]

for i in new_list:
    if i >= 10:
        new_list1.append(i)
print(new_list1)
