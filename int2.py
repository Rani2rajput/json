dict={"name":"priya","age":21,"clg":"ssism"}
m=[]
for i in dict.items():
    for j in i:
        m.append(j)
print(m)