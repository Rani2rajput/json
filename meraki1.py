import json
dict={"name":"David","job":"iter","age":6,"salary":50000}
print(type(dict))
b=json.dumps(dict)
print(b)