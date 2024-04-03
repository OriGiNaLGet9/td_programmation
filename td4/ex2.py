import matplotlib.pyplot as plt
path = "frenchssaccent.dic"

# CLASS

class Hashtable:
    
    def __init__(self, h, N):
        self.hachage = h
        self.number = N
        self.table = []
        for i in range(0, N):
            self.table.append([])

    def put(self, key, value): 
        position = self.hachage(key) % self.number
        for i in range(0,len(self.table[position])):
            if self.table[position][i][0] == key:
                self.table[position][i] = (key, value)
                return self.table
        self.table[position].append((key, value))
        return self.table
    
    def get(self, key): 
        position = self.hachage(key) % self.number
        for i in range(0, len(self.table[position])):
            if self.table[position][i][0] == key:
                return (position, i)
        return None

    def repartition(self):
        y = []
        for i in range(0, len(self.table)):
            y.append(len(self.table[i]))
        N = len(y)
        x = range(N)
        width = 1/1.5
        plt.bar(x, y, width, color="blue")
        plt.show()
                
# FUNCTION 
        
def h(x):
    value = 0 
    value = sum([ord(c) for c in x])
    return value

def read_file(p):
    f = open(p, 'r')
    liste=list()
    for ligne in f: 
        mot = ligne[0:len(ligne)-1]
        liste.append(mot)
    f.close()
    return liste    

# MAIN

hashtable = Hashtable(h, 500)
"""
ici j'a mis entre quotes pour faire le test des fonctions suivantes, mais ces trois la fonctionnent!
hashtable.put('abc', 3)
hashtable.put('abc', 2)
hashtable.put('acb', 5)
"""

print(hashtable.table)
print(hashtable.get('aaa'))
print(hashtable.get('abc'))

liste_mots = read_file(path)
for mot in liste_mots:
    hashtable.put(mot, len(mot))

hashtable.repartition()

