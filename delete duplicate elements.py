abc = [1,1,2,2,2,5,4,9,9,6,8,8]
result=[]
for i in abc:
    if i not in result:
        result.append(i)
print(result)
