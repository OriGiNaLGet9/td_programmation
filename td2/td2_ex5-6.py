#======== CLASSES 

class polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients
    
    def __str__(self):
        r = ""
        for i in range(len(self.coefficients)):
            if i == 0:
                if self.coefficients[i]!=0:
                    r += f"{self.coefficients[i]}"
            elif i == 1: 
                if self.coefficients[i] !=0:
                    r += f"{self.coefficients[i]}X"
            else:
                if self.coefficients[i] !=0:
                    r += f"{self.coefficients[i]}X**{i}"
            if (i != len(self.coefficients)-1) and (self.coefficients[i+1]!=0):
                    r += " + "            
        return r 
    
    def add(self, obj):
        i = 0
        while True:
            if (i<len(self.coefficients)) and (i<len(obj.coefficients)):
                self.coefficients[i] += obj.coefficients[i]
            elif i<len(obj.coefficients): 
                self.coefficients.append(obj.coefficients[i])
            else: # On ne fait pas le dernier cas car pas besoin de modifier self.coefficients pour les remettre dedans
                break
            i += 1
            
    def deriv(self):
        for i in range(0,len(self.coefficients)-1):
            self.coefficients[i] = self.coefficients[i+1]*(i+1)
        self.coefficients[len(self.coefficients)-1]=0
        
    def integrate(self, K):
        L = [K]
        for i in range(0, len(self.coefficients)):
            L.append(self.coefficients[i]/(i+1))
        self.coefficients = L
    
#========== MAIN

p = polynomial([1,0,3,4,0])
q = polynomial([1,5,2])
p.add(q)
print (p)

q_p = polynomial([1,2,5])
q_p.deriv()
print(q_p)

q_i = polynomial([3,1])
q_i.integrate(2)
#for i in range(0,2):
    #print(q_i.coefficients[i])
print(q_i)