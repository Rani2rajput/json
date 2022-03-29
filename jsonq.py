import json
dict=[["g","f","g"],["i","s"],["b","e","s","t"]]
sum=""
m={}
i=0
while i<len(dict):
    j=0
    while j<len(dict[i]):
        sum=sum+dict[i][j]
        m["rani"]=sum
        b=json.dumps(m)
        j=j+1
    i=i+1
print(b)
print(m)
print(sum)
        
        
