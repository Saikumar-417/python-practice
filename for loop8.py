evnsum=0
oddsum=0
for num in range(1,11,1):
    if num%2==0:
        print(num, end=" ")
        evnsum+=num
    else:
        print(num, end=" ")
        oddsum+=num
print()        
print(evnsum,"evnsum")
print(oddsum,"oddsum")
