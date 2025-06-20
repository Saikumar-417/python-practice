abc=[1,"indu","sai","true",True,False,[True,10,10.5],{"id":1,"name":"indu"}]
index=0
result=[]
while index<len(abc):
    if type(abc[index])==list or type(abc[index]) ==dict:
        result.append(abc[index])
    index+=1
print(result)
