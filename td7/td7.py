##-----importation des modules-----##
import tkinter as tk
from random import randint
from random import random


##-----parametres-----##

#COLORS = ['antiquewhite', 'aqua', 'aquamarine',  'bisque', 'black',  'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgrey', 'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen']
#graph = [[2, 7], [3], [5, 8], [10], [3, 1], [], [3, 10, 4], [], [], [10, 1], [3, 1], [0]]
#pos = ([131, 352], [464, 315], [254, 211], [393, 346], [381, 432], [343,  98], [298, 326], [187, 475], [245, 407], [483, 212], [365, 216], [149, 198])
#graph = [[2], [], [4], [1], [6], [3], [7], [5]]
#pos = [[100, 200], [450, 200], [150, 200], [400, 200], [200, 200], [350, 200], [250, 200], [300, 200]]
HEIGHT = 600
WIDTH = 600
LINES = 50
COLUMS = 50
rayon_cercle = 5

##-----classes-----##
class fenetre:
    def __init__(self):
        self.root = tk.Tk()
        self.height = HEIGHT
        self.width = WIDTH
        [self.graph, self.pos] = self.graph_al()
        self.col_index = [i for i in range(len(self.graph))]
        self.root.bind("<f>", lambda e : self.is_pressed(e)) #permet de propager le minimum
        self.COLORS = [color_generator() for i in range(50**2)]

    def canva(self):
        self.can = tk.Canvas(self.root, height=self.height, width=self.width)
        self.can.grid()

    def draw(self):
        N = len(self.graph)
        for e in self.can.find_all():
            self.can.delete(e)
        for i in range(N):
            for j in self.graph[i]:  # sucs de i a j
                self.can.create_line(self.pos[i][0], self.pos[i][1], self.pos[j][0], self.pos[j][1])
        for i in range(N):
            x, y = self.pos[i]
            self.can.create_oval(x-3, y-3, x+3, y+3, fill=self.COLORS[self.col_index[i]])
            #self.can.create_text(x-12,y,text=f"{i}")

    def change_color(self):
        for i in range(len(self.graph)):
            self.min_local(i)

    def min_local(self, i):
        min = self.col_index[i]
        self.voisins = self.graph[i]+[j for j in range(len(self.graph)) if i in self.graph[j]]
        for v in range(len(self.voisins)):
            if self.col_index[self.voisins[v]]<min:
                min = self.col_index[self.voisins[v]]
        self.col_index[i]=self.col_index[min]

    def is_pressed(self, e):
        self.change_color()
        self.draw()

    def graph_al(self):
        graph = [[] for i in range(LINES * COLUMS)]
        pos = []
        for i in range(LINES):
            for j in range(COLUMS):
                index = i * COLUMS + j
                pos.append([10 + j * 10, 10 + i * 10])
                if j < COLUMS - 1 and random() < 0.4:
                    graph[index].append(index + 1) 
                if i < LINES - 1 and random() < 0.4:
                    graph[index].append(index + COLUMS)
        return graph, pos
    
    def run(self):
        self.canva()
        self.draw()
        self.root.mainloop()


##-----fonctions-----##
def color_generator():
    r, g, b = randint(0,255), randint(0,255),randint(0,255)
    return f"#{r:02x}{g:02x}{b:02x}"


##-----main-----##
if __name__=='__main__':
    fenetre().run()
    """
    autour de p=0.5 on remarque qu'une couleur devient grandement majoritaire à chaque fois
    """