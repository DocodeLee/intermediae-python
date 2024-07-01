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
    
    def __eq__(self,other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum == secondnum
    
    def show(self):
        print(self.num , "/", self.den)

a = Fraction2(3,5)
print(a)

f1 = Fraction2(1,4)
f2 = Fraction2(1,2)
f3 = f1+f2
print(f3)
print(f1 == f2)

print("--------------------------")
# inheritence hierarchy for python
# list, string tuple is sequential collection
# dictionaries are nonsequential collection

#Logic gate : Binary gate, Unary gate

class LogicGate:
    def __init__(self,n):
        self.label = n
        self.output = None
    
    def getLabel(self):
        return self.label
    
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
    
class BinaryGate(LogicGate):
    
    def __init__(self,n):
        LogicGate.__init__(self,n)
        
        self.pinA = None
        self.pinB = None
    
    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter a Pin A input for gate" + self.getLabel() + "-->"))
        else:
            return self.pinA.getFrom().getOutput()
    
    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter a Pin B input for gate" + self.getLabel() + " -->"))
        else:
            return self.pinB.getFrom().getOutput()
    
    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error : No empty Pins")

class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pin  = None
        
    def getPin(self):
        return int(input("Enter a pin input for a gate" + self.getLabel() + "-->"))
    
    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot connect: NO empty Pins on this gate")

class AndGate(BinaryGate):
    def __init__(self,n):
        super(AndGate,self).__init__(n)
    
    def performGateLogic(self):
        
        a = self.getPinA()
        b = self.getPinB()
        
        if a == 1 and b ==1:
            return 1
        elif a==1 and b ==0:
            return 0
        elif a ==0 and b ==1:
            return 0
        elif a ==0 and b ==0:
            return 0
        else:
            print("insert only 0 or 1")
            
class Halfadd(BinaryGate):
    def __init__(self,n):
        super(Halfadd,self).__init__(n)
        self.c = 0
    
    def performGateLogic(self):
        
        a = self.getPinA()
        b = self.getPinB()
        
        if a == 0 and b == 0:
            return 0 , self.c == 0
        elif a ==0 and b == 1:
            return 1 ,self.c == 0
        elif a ==1 and b == 0 :
            return 1, self.c == 0
        elif a ==1 and b == 1 :
            return 0, self.c == 1
        else:
            print("Insert only 0 or 1")

class OrGate(BinaryGate):
    def __init__(self,n):
        super(OrGate,self).__init__(n)
    
    def performGateLogic(self):
        
        a = self.getPinA()
        b = self.getPinB()
        
        if a == 0 and b == 0 :
            return 0
        elif a == 0 and b == 1:
            return 1
        elif a == 1 and b == 0:
            return 1
        elif a == 1 and b == 1:
            return 1
        else:
            print("Insert only 0 or 1")
        
            

class NotGate(UnaryGate):
    def __init__(self,n):
        super(NotGate,self).__init__(n)
    
    def performGateLogic(self):
        
        a = self.getPin()
        
        if a == 1:
            return 0
        elif a == 0:
            return 1
        else:
            print("insert 0 or 1 please")


class Connector:
    
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        
        tgate.setNextPin(self)
        
    def getFrom(self):
        return self.fromgate
    
    def getTo(self):
        return self.togate

def main():
    g1 = AndGate(" G1")
    g2 = AndGate(" G2")
    g3 = OrGate(" G3")
    g4 = NotGate(" G4")
    c1 = Connector(g1,g3)
    c2 = Connector(g2,g3)
    c3 = Connector(g3,g4)
    print()
    

g5 = Halfadd(" G5")
s