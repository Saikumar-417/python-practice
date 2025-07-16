# WAP to find all falsy values in list [0,0,1,19,True,False,"","sai"] and push all of them into new list
list= [0,0,1,19,True,False,"","sai"] 
new_list=[]
for item in list:
    if not item:
        new_list.append(item)
print(new_list)
