import random

def square(n):
    print(n**2)
    
def squareroot(n):
    root = n/2
    for k in range(20):
        root = (1/2)*(root + (n / root))
        
    
    return root
print(0.5*6.5)

#------------------- exercise -----------------


def generateOne(strlen):
    # going to use this strings
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(strlen):
        #editing string
        res = res + alphabet[random.randrange(27)]
        
    return res

def score(goal, teststring):
    same = 0
    for i in range(len(goal)):
        
        if goal[i] == teststring[i]:
            same = same + 1
        
    return same / len(goal)

def testing():
    goalstring = "methinks it is like a weasel"
    newstring = generateOne(28)
    best = 0
    count = 0
    newscore = score(goalstring,newstring) 
    while newscore < 1:
        count = count + 1
        if newscore >=  best:
            best = newscore
        if count % 100000 == 0 :
           print(best, newstring, count) 
        newstring =generateOne(28)
        newscore = score(goalstring,newstring)     
        if count == 5000000 :
            break;   
    print(newstring, count)
            
        
testing()