#write a program to find 2 digit numbers in a list
list=[11,2,3,4,5,11,33,11]
empty_list=[]
for i in list:
    if i>=10:
        empty_list.append(i)
print(empty_list)

##write a program to find 3 digit numbers in a list
list=[11,111,222,34,56,56,777,168]
empty=[]
for i in list:
    if i>=100:
        empty.append(i)
print(empty)
