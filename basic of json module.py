#built in module - json
import json
a=[{"name":"sai","age":22,"city":"vizag"},{"name":"kumar","age":32,"city":"vizianagaram"},{"name":"ganesh","age":42,"city":"chennai"}]
result=json.dumps(a)
print(type(result))
result2=json.loads(result)
print(type(result2))
