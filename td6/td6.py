import tkinter as tk
import numpy as np
from random import random 
from math import *

dt = 0.1
k = 0.1


class noeud:

    def __init__(self, x, x0, y0, y, vx, vy, sucs):
        self.x = x
        self.x0 = x0
        self.y = y
        self.y0 = y0
        self.vx = ((random()-0.5)*10)
        self.vy = ((random()-0.5)*10)
        self.sucs = sucs

    def deplacement(self):
        global dt
        self.x += dt**2*self.vx*self.ressort[0]
        self.y += dt**2*self.vx*self.ressort[1]
        return(self.x, self.y)
    
    def ressort(self, n2):
        global k
        global dt
        dx0 = self.x0-n2.x0
        dy0 = self.y0-n2.y0
        l0 =dx0**2+dy0**2
        force_vect = [0, 0]
        dx = self.x-n2.x
        dy = self.y-n2.y
        distance = dx**2+dy**2
        force = -k*(distance-l0)
        angle = atan2(dx, dy)
        force_vect[0] = force * cos(angle)
        force_vect[1] = force * sin(angle)
        return (force_vect)


def draw(can, graph, pos):
    can.delete("all")
    for i in range(len(graph)):
        for j in graph[i]:  # sucs de i a j
            can.create_line(pos[i][0], pos[i][1], pos[j][0], pos[j][1])
    for (x, y) in pos:
        can.create_oval(x-4,y-4,x+4,y+4,fill="#f3e1d4")


def is_pressed(e):
    global can, graph, pos, n
    pos = np.array([n.deplacement(n.ressort(n2)) for i in range(len(graph))])
    draw(can, graph, pos)


if __name__=='__main__':
    WIDTH = 600
    HEIGHT = 600
    root = tk.Tk()
    can = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    can.pack()
    graph = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0], [3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]
    pos = np.array([(random()*WIDTH, random()*HEIGHT) for i in range(len(graph))])
    draw(can, graph, pos)
    n = noeud(0, 0, 0, 0, 0, 0, [])
    root.bind("<f>", lambda e : is_pressed(e))
    root.mainloop()

