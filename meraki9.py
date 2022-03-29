import json
dict={"shopping_list":{"chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20",}}
with open ("rani.json","w") as file:
    json.dump(dict,file,indent=6)
    print(dict)
