#Sets : unordered, mutable, no duplicates

# myset = {1,2,3,1,2}
# print(myset) #1,2,3 because set doesn't allow duplicates
# -------------------------

# myset = set('hello')
# print(myset)

#--------------------

# myset = set()

# myset.add(1)
# myset.add(2)
# myset.remove(2) # myset.discard(2)
# myset.add(3)

#myset.clear() # myset.pop()

# print(myset)
# print(type(myset))

#------------------
# myset = {1,2,2,3,3,4}

# for x in myset: 
#     print(x)   #1,2,3,4

#--------------------
# odds = {1,3,5,7,9}
# evens = {0,2,4,6,8}
# primes = {2,3,5,7}

# u = odds.union(evens)  ## get plus
# print(u)

# i = odds.intersection(primes) # minus the elements in primes
# print(i)

#-------------
# setA = {1,2,3,4,5,6,7,8,9}
# setB = {1,2,3,10,11,12}

# diff = setA.difference(setB) #get the different 
# print(diff)

# setA.update(setB) # update for set is same with add
# print(setA)

# setA.intersection_update(setB) #show the same items
# print(setA)

# setA.difference_update(setB) # show the difference
# print(setA)
# setA.symmetric_difference_update(setB) #add all the different item
# print(setA)

# setA.issubset(setB) # checking the all the element is in set B
## superset() is only true when all the element is there

#------------------------------
# setA = {1,2,3,4,5}
# setB = {1,2,3}
# setC = {8,9}
# print(setA.isdisjoint(setC)) # if no relation will be true

#-------------
# setA = {1,2,3,4,5}
# setB = setA
# setB.add(7)
# print(setA) # the result change all around

## use copy or / setB = set(setA)

# a = frozenset([1,2,3,4])
# a.add (2) # you cannot add to frozenset


