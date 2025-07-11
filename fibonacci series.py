#Print the Fibonacci series up to n terms. Explanation: Start with 0, 1 and continue with sum of last two. - Input: n = 5 - Output: 0 1 1 2 3

num=int(input("enter number:"))


a, b = 0, 1

for i in range(num):
    print(a, end=' ')
    a,b=b,a+b
