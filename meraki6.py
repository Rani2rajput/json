import json
dict='{"a":  1,"a":  2,"a":  3,"a": 4,"b": 1,"b": 2}'
b=json.loads(dict)
print(b)
print(type(b))