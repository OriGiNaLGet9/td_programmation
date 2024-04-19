from tkinter import *
from tkinter import ttk
from random import randint
from math import sqrt

#FONCTIONS
def cercle(x , y, r, c_exte, c_inte):
    can.create_oval(x-r, y-r, x+r, y+r, outline=c_exte, fill=c_inte)


def cible(can):
    for i in range(6):
        if i !=4:
            cercle(200, 200, 180-i*30, "red", "ivory")
            can.create_text(200, 35+i*30, text=i+1, font=('Times','25','bold'),fill='red')
        else:
            cercle(200, 200, 180-i*30, "red", "red")
            can.create_text(200, 35+i*30, text=i+1, font=('Times','25','bold'),fill='ivory')
    can.create_line(0,200,400, 200, fill='red')
    can.create_line(200,0,200, 400, fill='red')


score = 0
nb_tirs = 0


def tirs():
    global nb_tirs
    global score
    while nb_tirs<=4:
        x = randint(0, 400)
        y = randint(0, 400)
        cercle(x, y, 5, 'black', 'black')
        nb_tirs +=1
        d = sqrt((x-200)**2+(y-200)**2)
        zone = min(6, int(d/30))
        score += 6-zone
    feu["state"]=DISABLED
    label_score['text'] = f"Score : {score}"


def tir_unique():
    global nb_tirs
    global score
    if nb_tirs<=4:
        nb_tirs +=1
        x = randint(0, 400)
        y = randint(0, 400)
        cercle(x, y, 5, 'black', 'black')
        d = sqrt((x-200)**2+(y-200)**2)
        zone = min(6, int(d/30))
        score += 6-zone
        label_score['text'] = f"Score : {score}"
    

def is_clicked(event, nb_tirs):
    if event.char == 'f':
        tir_unique()
        nb_tirs+=1


#creer la fenetre
w = Tk()

#faire la fenetre de 400x400 rouge
can = Canvas(w, width=400, height=400, bg='red')
can.pack(side=TOP)

#creation de la cible
cible(can)

#creation des boutons
feu = ttk.Button(w, text='Feu!', command=tirs)
quit = ttk.Button(w, text='Quitter', command=w.destroy)
quit.pack(side=RIGHT)
feu.pack(side=LEFT)

#creation du score au centre
label_score = ttk.Label(w, text="Score : 0")
label_score.pack()

w.bind("<Key>", lambda event: is_clicked(event, can))

w.mainloop()
