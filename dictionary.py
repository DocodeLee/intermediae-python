# max_di = {"name": "Max", "age": 28, "city":"NewYork"}
# print(max_di)

# marydi = dict( name = "marry", age = 29) # Key : Value
# print(marydi)
# print(marydi["name"])

# value = dictionary["key"]

#------------------------------

# max_di = {"name": "Max", "age": 28, "city":"NewYork"}
# max_di["email"] = "max@email.com" #adding
# print(max_di)

# del max_di["name"]
# print(max_di)

# max_di.pop("age")
# print(max_di)

# if "name" in max_di:
#     print(max_di["name"])
# else:
#     print("Error")

#-----------------------------
# max_di = {"name": "Max", "age": 28, "city":"NewYork"}
# for key in max_di:
#     print(key)
    
# for value in max_di: 
#     # print(value)  # you cannot get value like this
#     print(max_di[value]) # it gives the value

# for value in max_di.values():
#     print(value)

# for key, value in max_di.items():
#     print(key,value)

## when you want to copy better to use copy()

#----------------
# max_di = {"name": "Max", "age": 28, "city":"NewYork"}
# marydi = dict( name = "marry", age = 29)

# max_di.update(marydi) #change the all the items to marydi
# print(max_di)

#-----
## Dictionary is unordered
# num_di = {3 : 9, 6 : 36 , 9 : 81}
# # value = num_di[0] # doesnt work
# value = num_di[3]
# print(value)