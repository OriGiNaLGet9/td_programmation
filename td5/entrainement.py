import tkinter as tk
from tkinter import ttk
from random import randint
from math import sqrt


class fenetre:
    def __init__(self):
        self.root = tk.Tk()
        self.score = 0
        self.nb_tirs = 0
        self.root.bind("<f>", lambda e : self.feu_unique(e))
        self.mire_x = randint(50, 350)
        self.mire_y = randint(50,350)

    def canva(self):
        self.can = tk.Canvas(self.root, height=400, width=400, background='red')
        self.can.grid(row=0, column=0, columnspan=3)

    def cible(self):
        for i in range (0, 6):
            if i != 4:
                cercle(self.can, 200, 200, 180-i*30, "ivory", "red")
                self.can.create_text(200, 35+i*30, text=i+1, font=('Times', '20', 'bold'), fill="red")
            else:
                cercle(self.can, 200, 200, 180-i*30, "red", "red")
                self.can.create_text(200, 35+i*30, text=i+1, font=('Times', '20', 'bold'), fill="ivory")
        self.can.create_line(0,200,400, 200, fill="red")
        self.can.create_line(200, 0, 200, 400, fill="red")
        self.mire_act = self.mire()

    def display(self):
        self.bouton_feu = tk.Button(self.root, text='Feu!', command=self.feu)
        self.bouton_quitter = ttk.Button(self.root, text='Quitter', command=self.root.destroy)
        self.bouton_feu.grid(row=1, column=0)
        self.bouton_quitter.grid(row=1, column=2)
        self.label = ttk.Label(self.root, text=f"Score : {self.score}")
        self.label.grid(row=1, column=1)

    def feu(self):
        while self.nb_tirs <5:
            x = randint(0,400)
            y = randint(0, 400)
            cercle(self.can, x, y, 5, "black", "black")
            self.score += score(x, y)
            self.nb_tirs += 1
        self.label['text'] = f"Score : {self.score}"
        self.label['text'] = f"Score : {self.score}"
        self.bouton_feu.config(state='disabled')

    def feu_unique(self, e):
        if self.nb_tirs<5:
            cercle(self.can, self.mire_x, self.mire_y, 5, "black", "black")
            self.score += score(self.mire_x, self.mire_y)
            self.nb_tirs += 1
            if self.nb_tirs == 5:
                self.bouton_feu.config(state='disabled')
        self.label['text'] = f"Score : {self.score}"

    def mire(self):
        return cercle(self.can, self.mire_x, self.mire_y, 5, "green", "yellow")
    
    def dep_mire(self):
        self.can.delete(self.mire_act)
        self.mire_x += randint(-20, 20)
        self.mire_y += randint(-20, 20)
        self.mire_act = self.mire()
        self.root.after(300, self.dep_mire)

    def run(self):
        self.canva()
        self.cible()
        self.display()
        self.dep_mire()
        self.root.mainloop()


def cercle(can, x, y, r, c_i, c_o):
    return can.create_oval(x-r, y-r, x+r, y+r, outline=c_o, fill=c_i)

def score(x, y):
    s = 0
    d = sqrt((x-200)**2+(y-200)**2)
    zone = min(6, int(d/30))
    s += 6-zone
    return s


fenetre().run()