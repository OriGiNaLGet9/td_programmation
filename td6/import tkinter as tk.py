import tkinter as tk
import numpy as np
from random import random
from math import cos, sin, atan2

dt = 0.1
k = 0.1

class Application(tk.Tk):
    def __init__(self, graph, pos):
        tk.Tk.__init__(self)
        self.canvas = tk.Canvas(self, width=600, height=600, bg="white")
        self.canvas.pack()
        self.graph = graph
        self.pos = pos
        self.draw_graph()
        self.bind("<KeyPress-f>", self.move_nodes)

    def draw_graph(self):
        for i in range(len(self.graph)):
            for j in self.graph[i]:
                self.canvas.create_line(self.pos[i][0], self.pos[i][1], self.pos[j][0], self.pos[j][1])
        for (x, y) in self.pos:
            self.canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill="#f3e1d4")

    def move_nodes(self, event):
        for _ in range(10):
            self.update_positions()
            self.draw_graph()

    def update_positions(self):
        global dt
        global k
        vit = np.array([((random()-0.5)*10, (random()-0.5)*10) for i in range(len(self.graph))])
        forces = np.zeros_like(vit)
        for i in range(len(self.graph)):
            for j in self.graph[i]:
                dx = self.pos[i][0] - self.pos[j][0]
                dy = self.pos[i][1] - self.pos[j][1]
                distance = np.sqrt(dx**2 + dy**2)
                force = -k * (distance - 100)  # 100 est la longueur de repos du ressort
                angle = atan2(dy, dx)
                forces[i][0] += force * cos(angle)
                forces[i][1] += force * sin(angle)
        vit += dt * forces
        self.pos += dt * vit

if __name__ == "__main__":
    graph = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0], [3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]
    pos = np.array([(random() * 600, random() * 600) for i in range(len(graph))])

    app = Application(graph, pos)
    app.mainloop()