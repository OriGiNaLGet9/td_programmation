import tkinter as tk
from random import random
import numpy as np
from math import *

HEIGHT = 600
WIDTH = 600
graph = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0], [3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]
k = 0.5
dt = 0.1
l0 = 100
frottements = 0.05
repulsion_coefficient = 5000


class Graph:

    def __init__(self):
        self.root = tk.Tk()
        self.height = HEIGHT
        self.width = WIDTH
        self.graph = graph 
        self.pos = np.array([(random()*self.width, random()*self.height) for i in range(len(graph))])
        self.vit = np.array([((random()-0.5)*10, (random()-0.5)*10) for i in range(len(graph))])
        self.root.bind("<f>", lambda e : self.is_pressed_f(e))
        self.root.bind('<s>', lambda f : self.is_pressed_g(f))
        self.after = None

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

    def is_pressed_f(self, e):
        self.ressort()

    def is_pressed_g(self, f):
        self.stop()

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
                self.repulsion = [0, 0]
                self.pos[s][0] += dt*self.vit[s][0] + self.repulsion[0]
                self.pos[s][1] += dt*self.vit[s][1] + self.repulsion[1]
#force de répulsion entre tous les noeuds
        for i in range(len(self.graph)):
            for j in range(i + 1, len(self.graph)):
                dx = self.pos[j][0] - self.pos[i][0]
                dy = self.pos[j][1] - self.pos[i][1]
                distance = sqrt(dx**2 + dy**2)
                if distance == 0:
                    continue
                force = repulsion_coefficient / (distance**2)
                u = [dx / distance, dy / distance]
                self.vit[i][0] -= dt * force * u[0]
                self.vit[i][1] -= dt * force * u[1]
                self.vit[j][0] += dt * force * u[0]
                self.vit[j][1] += dt * force * u[1]
#ajout de frottements pour que le graph s'arrete progressivement de bouger
            self.vit[i][0] *= (1 - frottements)
            self.vit[i][1] *= (1 - frottements)
            self.pos[i][0] += dt * self.vit[i][0]
            self.pos[i][1] += dt * self.vit[i][1]
#ajout de rebonds sur les bords pour que le graph ne sorte pas du canva
            if self.pos[i][0] < 0:
                self.pos[i][0] = 0
                self.vit[i][0] = -self.vit[i][0]  
            elif self.pos[i][0] > self.width:
                self.pos[i][0] = self.width
                self.vit[i][0] = -self.vit[i][0]
            if self.pos[i][1] < 0:
                self.pos[i][1] = 0
                self.vit[i][1] = -self.vit[i][1] 
            elif self.pos[i][1] > self.height:
                self.pos[i][1] = self.height
                self.vit[i][1] = -self.vit[i][1] 
        self.draw()
        self.after = self.root.after(80, self.ressort)

    def stop(self):
        self.root.after_cancel(self.after)

    def run(self):
        self.canva()
        self.draw()
        self.root.mainloop()

if __name__ == '__main__':
    Graph().run()