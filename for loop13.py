abc = [10,100,20,11,0,5,-2,11]
evesum=0
oddsum=0
for i in abc:
    if i%2==0:
        evesum+=i
    else:
        oddsum+=i
print("sum of even numbers:",evesum)
print("sum of odd numbers:",oddsum)
