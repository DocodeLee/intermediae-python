# mytuple = "max",39,"Boston",
# # mytuple = ("max",39,"Boston",)
# print(mytuple)

#--------------------
# mytuple = tuple(["Max",39,"LA"]) #change lsit to tuple
# print(mytuple)

# item = mytuple[0] # index is also working at tuple
# print(item)

# mytuple[0] = "tim" # we cannot change the item

# for x in mytuple: #for and if statement is also work
#     print(x)

#---------------------------
# mytuple = ("a","b","c","c")
# print(len(mytuple)) # check length
# print(mytuple.count("c")) # you can use count in tuple 
# print(mytuple.index("b"))

# mylist = list(mytuple) # change to list
# print(mylist)

# b = mytuple[0:3]    #slicing the tuple [2:] , [::1] /every [::2] /2,4,6 th
# print(b)

#----------------
# mytuple = tuple(["Max",39,"LA"])
# name, age, city = mytuple # give variable
# print(name)
# print(age)

#---------------------------
# my_tuple = [0,1,2,3,4]
# i1, *i2= my_tuple #sorting them 
# print(i1)
# print(i2)

import sys
my_list = [0,1,2]
my_tuple = (0,1,2)
print(sys.getsizeof(my_list),"bytes")
print(sys.getsizeof(my_tuple),"bytes") # tuple is small so could be fast
## working with tuple will be more efficient then list