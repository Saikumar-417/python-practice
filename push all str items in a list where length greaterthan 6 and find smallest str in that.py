#WAP to push all str items in a list where length >=6 to a list and find the smallest lengthed str in that resulted list


list=["sai","kumar","indu","gaanesh","vamsikrishna","durgaprasad","harsha","ramnarayana"]
new_list=[]
for i in list:
    if len(i)>=6:
        new_list.append(i)
print(new_list)
smallest=new_list[0]
for k in new_list:
    if len(k)<len(smallest):
        smallest=k
print(smallest)
