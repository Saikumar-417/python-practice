abc=[1,2,"sai","indu",True]
index=len(abc)-1
result=[]
while index>=0:
    if type(abc[index])==str:
        result.append(abc[index])
    index-=1    
print(result)
