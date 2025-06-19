abc = [1000,1,2,3,10,11,200,500]
minnum=abc[0]
maxnum=abc[0]
for i in abc:
    if minnum>i:
        minnum=i
    if maxnum<i:
        maxnum=i
print(minnum)
print(maxnum)
