import random
# random : order to choose
# on random words fro ma list

name = input("What is your name: ")

print("Good luck", name)

words = ["rainbow", "computer", "science", "programming", "python","mathmatics","player" , "board",
         "tree", "muscle"]
word = random.choice(words)

print("guess the characters")

guesses = ""
turns = 12

while turns > 0 :
    failed = 0
    for char in word:
        
        if char in guesses:
            print(char, end= " ")
        
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break
    print()
    guess = input("Guess a character: ")
    
    guesses += guess
    
    if guess not in word:
        turns -= 1
        
        print("Wrong")
        print("you have", turns, "more guesses")
    if turns == 0:
        print("You loose")        