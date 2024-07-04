import random
# random : order to choose
# on random words fro ma list

name = input("What is your name: ")

print("Good luck", name)

words = ["rainbow", "computer", "science", "programming", "python","mathmatics","player" , "board",
         "tree", "muscle"]
word = random.choice(words)
