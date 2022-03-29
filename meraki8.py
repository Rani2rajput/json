
import json
a=["neelam","programer","24","2400"]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"]
e=["name","designation","age","salary"]
f=[a,b,c,d]
g=["emp1","emp2","emp3","emp4"]
dict={}
i=0
while i<len(f):
    j=0
    dict1={}
    while j<len(f[i]):
        if j==0:
            dict1[e[j]]=f[i][j]
        elif j==1:
            dict1[e[j]]=f[i][j]
        elif j==2:
            dict1[e[j]]=f[i][j]
        elif j==3:
            dict1[e[j]]=f[i][j]
        j=j+1
        dict[g[i]]=dict1
    i=i+1
print(dict)
            
        