import time
from random import randrange

numbers = [10,5,4,2,1,0,3]
numbers2 = [0,1,2,3,4,5,6,7,8]
numbers3 = [10,9,8,0,7,6,5,4,3,2,1]

def findminimum(list) :
    a = list[0]
    for i in range(len(list)):
        if a > list[i]:
            a = list[i] 
            
            
    print("The smallest one is",a)



# why O(n^2)
for listSize in range(1000,10001,1000):
    alist = [randrange(10000) for x in range(listSize)]
    start = time.time()
    print(findminimum(alist))
    end = time.time()
    print("size : %d time : %f" %(listSize, end-start))