# """we need to write a program to find the position of a given number

cards = [13,11,10,7,4,3,1,0]
query = 7
output = 3

def locate_card(cards, query):
    pass

#lets make as dictionary
tests = list()
tests.append ( {
    'input' :{
        'cards' : [13,12,10,7,4,3,1,0],
        'query' : 7
    },
    'output' : 3
})
#expecting result
# locate_card(test['input']['card'], test['input']['query']) == test['output']


## need to find all the edge case
#somewhere / first or last / middle 
# cards could be only one
# cards could be empty
# it could have repeating num


# case for in the middle
tests.append({
    'input' :{
        'cards' : [13,11,10,6,3,1,0],
        'query' : 6
    },
    'output' : 3
})

# case for first element
tests.append({
    'input' :{
        'cards' : [4,2,1,-1],
        'query' : 4
    },
    'output' : 0
})

# case for last
tests.append({
    'input' :{
        'cards' : [4,2,1,-1],
        'query' : -1
    },
    'output' : 3
})
# when card is only one
tests.append({
    'input' :{
        'cards' : [5],
        'query' : 5
    },
    'output' : 0
})

# when card doesnt contian query
tests.append({
    'input' :{
        'cards' : [4,2,1,-1],
        'query' : 5
    },
    'output' : -1
})

#when numverc are repeated
tests.append({
    'input' :{
        'cards' : [4,4,4,4,4,3,2,2,2,2,1,-1],
        'query' : 3
    },
    'output' : 5
})
#when the querys are repeated
tests.append({
    'input' :{
        'cards' : [4,4,4,4,2,2,2,2,1,-1],
        'query' : 2
    },
    'output' : 4
})

print(tests)