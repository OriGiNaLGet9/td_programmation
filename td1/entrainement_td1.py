paths = "frenchssaccent.dic"
s = {'?':0, 
    'a': 1, 'e': 1, 'i': 1, 'l': 1, 'n': 1, 'o': 1, 'r': 1, 's': 1, 't': 1, 'u': 1,
    'd': 2, 'g': 2, 'm': 2,
    'b': 3, 'c': 3, 'p': 3,
    'f': 4, 'h': 4, 'v': 4,
    'j': 8, 'q': 8,
    'k': 10, 'w': 10, 'x': 10, 'y': 10, 'z': 10}

########## FONCTIONS

def read_file(path):
    f = open(path, 'r')
    mots_possibles = []
    for ligne in f: 
        if len(ligne[0:len(ligne)-1])<=8:
            mots_possibles.append(ligne[0:len(ligne)-1])
    f.close()
    return mots_possibles

def lettres_ds_tirage(tirage, mot):
    copie_tirage = list(tirage)
    joker = 0 
    for lettre in mot:
        if lettre in copie_tirage:
            copie_tirage.remove(lettre)
        else:
            if joker == 0:
                joker = 1
            else:
                return False
    return True

def mots_faisables(tirage, path):
    mots_faisable = []
    mots_possibles = read_file(path)
    for mot in mots_possibles:
        if lettres_ds_tirage(tirage, mot):
            mots_faisable.append(mot)
    return mots_faisable

def mot_plus_long(tirage, path):
    mots_possibles = mots_faisables(tirage, path)
    if len(mots_possibles)>0:
        plus_long = mots_possibles[0]
        for mot in mots_possibles:
            if len(mot)>len(plus_long):
                plus_long = mot
        return plus_long
    else : 
        return 0

def score(mot, tirage):
    score = 0
    for lettre in mot:
        if lettre in tirage: 
            score += int(s[lettre])
    return score

def max_score(tirage, path):
    mots = mots_faisables(tirage, path)
    if len(mots)>0:
        score_max = score(mots[0], tirage)
        mot_max = mots[0]
        for mot in mots:
            if score_max<score(mot, tirage):
                score_max = score(mot, tirage)
                mot_max = mot
        return (mot_max, score_max)
    else:
        return 0

########## MAIN

if __name__ == '__main__':
    
    tirage = []
    for i in range(8):
        tirage.append(input(f"donnez une {i+1}ème lettre : "))

    plus_long = mot_plus_long(tirage, paths)
    if plus_long != 0:
        print("le mot le plus long est : ", plus_long)
    else : 
        print("il n'y a pas de mots correspondant aux lettres")
    
    score_max = max_score(tirage, paths)
    print("le mot faisant le meilleur score est :", score_max[0], "\nle score de ce mot est : ",score_max[1])

