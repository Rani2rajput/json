import json 
dict=[["priya","Bscmpc",20,"qualification","age"],["rani","intermediate","age","qualifications",20]]
m=[]
k={}
for i in dict:
    for j in i:
        m.append(j)
        k["name"]=m
        b=json.dumps(k)
print(b)
print(type(b))

