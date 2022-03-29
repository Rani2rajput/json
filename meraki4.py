import json
dict={'4': 5,'6': 7,'1': 3,'2': 4}
a=list(dict.values())
a.sort()
m={}
for i in a:
    for j in dict:
        if i==dict[j]:
            m[j]=i
            k=json.dumps(m)
print(k)
            
            
    
