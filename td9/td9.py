## ----- CLASSES ----- ##

class polynome:
    def __init__(self, coefs, q, n):
        self.q = q
        self.n = n
        self.coefs = coefs
        self.modulo_degre()
        self.modulo_coef()

    def modulo_degre(self):
        for i in range (self.n, len(self.coefs)):
            self.coefs[i%self.n] -= self.coefs[i]
        self.coefs = self.coefs[:self.n]

    def modulo_coef(self):
        for i in range (len(self.coefs)):
            self.coefs[i] = self.coefs[i]%self.q

    def __str__(self):
        l = ""
        for i in range(len(self.coefs)):
            if self.coefs[i] != 0:
                if i == 0:
                    l += f"{self.coefs[i]}"
                elif i == 1:
                    if self.coefs[i] > 0:
                        l += f"+{self.coefs[i]}X"
                    else:
                        l += f"{self.coefs[i]}X"
                else:
                    if self.coefs[i] > 0:
                        l += f"+{self.coefs[i]}X**{i}"
                    else:
                        l += f"{self.coefs[i]}X**{i}"
        if l == "":
            l = "0"
        return l

    def __add__(self, other):
        assert self.q == other.q
        assert self.n == other.n
        coefficient = [0]*max(len(self.coefs), len(other.coefs))
        for i in range(max(len(self.coefs), len(other.coefs))):
            coef1 = self.coefs[i] if i<len(self.coefs) else 0
            coef2 = other.coefs[i] if i<len(other.coefs) else 0
            coefficient[i] = coef1+coef2
        nv_polyn = polynome(coefficient, self.q, self.n)
        return nv_polyn
    
    def mul(self, other): 
        coeficients = [0 for i in range(2*len(self.coefs))]
        for i in range(len(self.coefs)):
            for j in range(len(other.coefs)):
                coeficients[i+j] += self.coefs[i]*other.coefs[j]
        c = polynome(coeficients, self.q, self.n)
        return c

    def scalar(self, c):
        coef = []
        for i in range(len(self.coefs)):
            coef.append(self.coefs[i]*c)
        p = polynome(coef, self.q, self.n)
        return p
        
    def rescale(self, r):
        p = polynome(self.coefs, r, self.n)
        return p
    
    def fscalar(self, r, alpha):
        q = self
        for i in range(len(q.coefs)):
            q.coefs[i] = round(q.coefs[i]*alpha)
        q = q.rescale(r)
        return q


## ----- MAIN ----- ##
a = polynome([0, 8], 5, 3)
b = polynome([0, 1, -6, 4, 5], 5, 3)

print(a)
print(b, "\n")

c = a+b
print(c, "\n")

d = a.mul(b) 
print(d, "\n")

e = a.scalar(2)
f = b.scalar(2)
print(e)
print(f, "\n")

g = a.rescale(2)
h = b.rescale(2)
print(g)
print(h, "\n")

k = b.fscalar(3, 2)
print(k)