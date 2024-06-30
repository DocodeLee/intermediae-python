class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
        self.show()

    def show(self):
        print(self.num , "/", self.den)

Fraction(3,5)

def gcd(m,n):
        while m % n !=0: # m= 22 n= 26
            oldm = m    # old m = 22
            oldn =n     #old n = 26
            
            m =oldn     # m = 26
            n = oldm % oldn #n = 22 % 26
            
        return n

class Fraction2:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
    
    def __str__(self): # run without execution
        return str(self.num) + "/" + str(self.den)
    
    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den*otherfraction.den
        common = gcd(newnum,newden)
        
        return Fraction2(newnum//common , newden //common)
    
    
            
    
    def show(self):
        print(self.num , "/", self.den)

a = Fraction2(3,5)
print(a)

f1 = Fraction2(1,4)
f2 = Fraction2(1,2)
f3 = f1+f2
print(f3)

