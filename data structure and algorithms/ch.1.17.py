class Fraction:
    def __init__(self,top,bottom):
        # The isinstance(object, type) function returns True if the specified object is of the specified type, 
        if top and bottom > 0:
            self.num = top
            self.den = bottom
        else:
            raise RuntimeError("Please enter the right value")
        
        common = gcd(top,bottom)
        
        self.num = self.num // common
        self.den = self.den // common
        
    def __str__(self): # run without execution
        return str(self.num) + "/" + str(self.den)
    
    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den*otherfraction.den
        return Fraction(newnum,newden)
    
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
    
f1 = Fraction(1,2)
f2 = Fraction(1,4)
f3 = f1 + f2
f4 = f2 - f1
f5 = f1 * f2
f6 = f1 / f2
print(f6)