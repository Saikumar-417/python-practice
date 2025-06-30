a=int(input("enter number:"))
b=int(input("enter number:"))
c=int(input("enter number:"))
if a>b and a<c or a<b and a>c:
    print("a is second greater")
if b>a and b<c or b<a and b>c:
    print("b is second greater")
if c<a and c>b or c>a and c<b:
    print("c is second greater")
