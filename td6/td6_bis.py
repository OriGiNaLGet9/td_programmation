import tkinter as tk
from random import random
import numpy as np
from math import *

HEIGHT = 600
WIDTH = 600
graph = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0], [3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]
k = 1
dt = 0.1
l0 = 100


class Graph:

    def __init__(self):
        self.root = tk.Tk()
        self.height = HEIGHT
        self.width = WIDTH
        self.graph = graph 
        self.pos = np.array([(random()*self.width, random()*self.height) for i in range(len(graph))])
        self.vit = np.array([((random()-0.5)*10, (random()-0.5)*10) for i in range(len(graph))])
        self.root.bind("<f>", lambda e : self.is_pressed(e))

    def canva(self): 
        self.can = tk.Canvas(self.root, height=self.height, width=self.width)
        self.can.pack()

    def draw(self):
        self.can.delete("all")
        for i in range(len(self.graph)):
            for j in graph[i]:  # sucs de i a j
                self.can.create_line(self.pos[i][0], self.pos[i][1], self.pos[j][0], self.pos[j][1])
        for (x, y) in self.pos:
            self.can.create_oval(x-4,y-4,x+4,y+4,fill="#f3e1d4")

    def is_pressed(self, e):
        self.ressort()

    def ressort(self): 
        global k
        for i in range(len(graph)):
            for s in graph[i]:
                dx = self.pos[s][0]-self.pos[i][0]
                dy = self.pos[s][1]-self.pos[i][1]
                distance = sqrt(dx**2+dy**2)
                force = -k*(distance-l0)
                u = [dx/distance, dy/distance]
                self.vit[s][0] += dt*force*u[0]
                self.vit[s][1] += dt*force*u[1]
                self.pos[s][0] += dt*self.vit[s][0]
                self.pos[s][1] += dt*self.vit[s][1]
        self.draw()
        self.root.after(300, self.ressort)

    def run(self):
        self.canva()
        self.draw()
        self.root.mainloop()

if __name__ == '__main__':
    Graph().run()