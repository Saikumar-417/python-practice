m=int(input("enter a number:"))
n=int(input("enter a number:"))
even_count=0
odd_count=0
for i in range(m,n+1):
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("even_count",even_count)
print('odd_count',odd_count)
