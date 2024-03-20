from math import gcd
from math import pi

#=============== CLASSES

class Fraction:
    def __init__(self, a, b):
            self.numerateur = a
            self.denominateur = b 
            
    def __repr__(self):
        self.simplification()
        if self.denominateur==1:
            return f"{self.numerateur}"
        else:
            return f"{self.numerateur}/{self.denominateur}"        
   
   
    def simplification(self):
        self.numerateur,self.denominateur =int(self.numerateur/gcd(self.numerateur, self.denominateur)),int(self.denominateur/gcd(self.numerateur, self.denominateur))
    
    def ecriture_fractionnaire(self): 
        self.simplification()
        if self.denominateur==1:
            return f"{self.numerateur}"
        else:
            return f"{self.numerateur}/{self.denominateur}"
    
    def add(self, obj):
        num = self.numerateur*obj.denominateur+self.denominateur*obj.numerateur
        den = self.denominateur*obj.denominateur
        self.numerateur = num
        self.denominateur = den
        
    def mult(self, obj):
        num = self.numerateur*obj.numerateur
        den = self.denominateur*obj.denominateur
        self.numerateur = num
        self.denominateur = den
    
    
#============== FONCTIONS


def H(n):
    somme = Fraction(1,1)
    for i in range(2, n+1):
        f = Fraction(1,i)
        somme.add(f) 
        #print(somme)
        #input()
        somme.simplification() 
        #print(somme)
        #input()
    return somme
    
def Leibniz(n):
    somme = Fraction(1,1)
    for i in range(1, n+1):
        f = Fraction((-1)**i,2*i+1)
        somme.add(f) 
        somme.simplification() 
    return somme    


#============== MAIN



f1=Fraction(1, 2)
print(f1.ecriture_fractionnaire())

f2=Fraction(3,2)
f1.add(f2)
print (f1.ecriture_fractionnaire())

f = H(10000)
print(f)

f = Leibniz(10000)
print(f)
print (pi/4)