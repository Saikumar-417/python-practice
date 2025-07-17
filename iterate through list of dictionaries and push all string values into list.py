# write a program to iterate list of dictionaries and push all str values of all keys into a new list but not pushing digit values or list values or dict values and find the length of that resulted list.
list=[{"name":"sai","age":30},{"name":"ganesh","age":25}]
result=[]
for item in list:
    for k in item.values():
        if type(k)==str and not k.isdigit():
            result.append(k)
print("result :", result)
print("length :", len(result))
