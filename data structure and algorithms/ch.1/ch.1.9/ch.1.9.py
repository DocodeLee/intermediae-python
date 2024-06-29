wordlist = ["cat","dog","rabbit"]
letterlist = []
for word in wordlist:
    for letter in word:
        letterlist.append(letter)
print(letterlist)

#Selection statement allow programmer to ask questions and then, based on the result perform different actions

uniquelist = []
for x in letterlist:
    #check if iexists in unique list or not
    if x not in uniquelist:
        uniquelist.append(x)
print(uniquelist)

sqlist  = [x*x for x in range(1,11)]
print(sqlist)

sqlisteven = [x*x for x in range(1,11) if x%2 != 0]
print(sqlisteven)

print([ch.upper() for ch in 'comprehension' if ch not in 'aeiou'])

#-paractice
newletterlist = [ letter for word in wordlist for letter in word]
print(newletterlist)
new_unique = set([ letter for word in wordlist for letter in word])
print(sorted(list(new_unique)))

