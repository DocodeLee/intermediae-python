import random

num = random.randrange(100000,1000000)

n = int(input("Guess the 6 digits : "))

if(n== num):
    print("Great! You guessed at 1 try you are master mind")
else:
    ctr = 0
    
    while (n != num) :
        ctr += 1
        
        count = 0
        
        n = str(n)
        num = str(num)
        
        correct = ['X']*6
        for i in range(0,6):
            if (n[i] == num[i]):
                count += 1
                correct[i] = n[i]
            else:
                continue
        
        if (count < 4) and (count != 0):
            print("Not quite but you did get", count, "digits correct")
            print("Also these numbers in you input were correct")
            
            for k in correct:
                print(k, end= " ")
            
            print("\n")
            n = int(input("Enter your next chocie : "))
        elif(count == 0):
            print("None of the numbers in your input match")
            n = int(input("Enter your next choice of number : "))
    if n == num:
        print("You've become a master mind")
        print("It took you only",ctr,"tries.")