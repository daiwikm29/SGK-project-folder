food_info_hamburg = {"size":2, "price":5, "veg":False}
food = {"hamburger":food_info_hamburg, }
#print(food["hamburger"])

for item in food["hamburger"]:
    print(item)
    
for value in food["hamburger"].values():
    print(value)
    
food["fries"] = {23}    
    
for k,v in food["hamburger"].items():
    print(k,v)
    
print(food)