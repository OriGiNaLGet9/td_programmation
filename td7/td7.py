##-----importation des modules-----##
import tkinter as tk
from random import randint


##-----parametres-----##

COLORS = ['antiquewhite', 'aqua', 'aquamarine',  'bisque', 'black',  'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgrey', 'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen']
graph = [[2, 7], [3], [5, 8], [10], [3, 1], [], [3, 10, 4], [], [], [10, 1], [3, 1], [0]]
pos = ([131, 352], [464, 315], [254, 211], [393, 346], [381, 432], [343,  98], [298, 326], [187, 475], [245, 407], [483, 212], [365, 216], [149, 198])
HEIGHT = 600
WIDTH = 600


##-----classes-----##
class fenetre:
    def __init__(self):
        self.root = tk.Tk()
        self.height = HEIGHT
        self.width = WIDTH
        self.graph = graph
        self.pos = pos
        self.col_index = [i for i in range(len(self.graph))]

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
            self.min_local(i)
            self.can.create_oval(x-6, y-6, x+6, y+6, fill=COLORS[self.col_index[i]])
            self.can.create_text(x-12,y,text=f"{i}")

    def min_local(self, i):
        min = i
        self.voisins = self.graph[i]+[j for j in range(len(self.graph)) if i in self.graph[j]]
        for v in range(len(self.voisins)):
            if self.voisins[v]<min:
                min = self.voisins[v]
        self.col_index[i]=self.col_index[min]

    def run(self):
        self.canva()
        self.draw()
        self.root.mainloop()


##-----main-----##
if __name__=='__main__':
    fenetre().run()