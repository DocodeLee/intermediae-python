import random

class Fraction:
    def __init__(self,top,bottom):
        # The isinstance(object, type) function returns True if the specified object is of the specified type, 
        if isinstance(top,int):
            self.num = top
        else:
            raise RuntimeError("Please enter the right value")
        
        if isinstance(bottom,int):
            self.den = bottom
        else:
            raise ValueError("Bottom is not an int")
        
        common = gcd(top,bottom)
        
        self.num = self.num // common
        self.den = self.den // common
        
    def __str__(self): # run without execution
        return str(self.num) + "/" + str(self.den)
    
    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den*otherfraction.den
        return Fraction(newnum,newden)
    
    def __radd__(self,other):
        return __add__(other)
    
    def __sub__(self,other):
        newnum = self.num*other.den - self.den*other.num
        newden = self.den*other.den
        return Fraction(newnum,newden)
    
    def __mul__(self,other):
        newnum = self.num*other.num
        newden = self.den*other.den
        return Fraction(newnum,newden)
    
    def __truediv__(self,other):
        newnum = self.num * other.den
        newden = self.den * other.num
        return Fraction(newnum, newden)
    
    def __eq__(self,other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum == secondnum
    
    def __gt__(self,other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum > secondnum
    
    def __ge__(self,other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum >= secondnum
    
    def __lt__(self,other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum < secondnum
    
    def __le__(self,other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum <= secondnum
    
    def __ne__(self,other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum != secondnum
    
    def show(self):
        print(self.num , "/", self.den)
    def getNum(self):
        return self.num
    def getDen(self):
        return self.den


def gcd(m,n):
        while m % n !=0: # m= 22 n= 26
            oldm = m    # old m = 22
            oldn =n     #old n = 26
            
            m =oldn     # m = 26
            n = oldm % oldn #n = 22 % 26
            
        return n
    
f1 = Fraction(1,4)
f2 = Fraction(1,2)
f3 = f1+ f2
f4 = f2 - f1
f5 = f1 * f2
f6 = f1 / f2

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def __eq__(self, other):
        return self.rank == other.rank
    def  __lt__(self, other):
        return self.rank < other.rank

class Deck:
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [Card(suit,rank) for suit in self.suits for rank in self.ranks]
        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal_card(self):
        if len(self.cards) ==0:
            return None
        return self.cards.pop(0)
    
    def cards_left(self):
        return len(self.cards)
    
def play_war_game():
    deck = Deck()
    deck.shuffle()
    
    p1_cards = []
    p2_cards = []
    
    #deal cards to players
    while deck.cards_left() > 0:
        p1_cards.append(deck.deal_card())
        p2_cards.append(deck.deal_card())
        
    rounds = 0
    
    while len(p1_cards) > 0 and len(p2_cards) > 0:
        rounds += 1
        card1 = p1_cards.pop(0)
        card2 = p2_cards.pop(0)
    
        print(f"Round {rounds} :")
        print(f"Player 1 : {card1}")
        print(f"Player 2 : {card2}")
        
        if card1> card2:
            print("Player 1 wins this round \n ")
            p1_cards.extend([card1, card2])
        elif card2 > card1:
            print("Player 2 wins this round \n ")
            p2_cards.extend([card1, card2])
        else:
            print("It's a tie! \n ")
            p1_cards.append(card1)
            p2_cards.append(card2)
    
    if len(p1_cards) > len(p2_cards):
        print("player 1 win ")
    elif len(p1_cards) < len(p2_cards):
        print("player 2 win ")
    else:
        print("It's a draw")

# play_war_game()

print("--------------Sudoku----------------")
board = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]]

def is_valid_move(board, row, col, number):
    
    for x in range(9):
        if board[row][x] == number :
            return False
    
    for x in range(9):
        if board[x][col] == number :
            return False
        
    corner_row = row - row % 3
    corner_col = col - col % 3
    
    for x in range(3):
        for y in range(3):
            if board[corner_row + x][corner_col + y] == number:
                return False
    return True
def solve(board, row, col):
    
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0
    
    if board[row][col] > 0 :
        return solve(board, row, col +1 )
    
    for num in range(1,10) : # 1 ~ 9
        
        if is_valid_move(board, row, col, num):
            
            board[row][col] = num
            
            if solve(board, row, col + 1):
                return True
            
        board[row][col] = 0
    
    return False

if solve(board, 0, 0):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end = " ")
        print()
else:
    print("No solution")
    
