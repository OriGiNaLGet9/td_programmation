#========== Variables globales 

tirage = ["z", "x", "c", "v", "r", "r", "t", "?"]
path = "frenchssaccent.dic"


#========== Fonctions 


def read_file(path):
    f = open(path, 'r')
    liste=list()
    for ligne in f: 
        mot = ligne[0:len(ligne)-1]
        if len(mot)<=8:
            liste.append(ligne[0:len(ligne)-1]) #ou liste.append(ligne.replace("\n", "")
    f.close()
    return liste

def is_not_possible (tirage, mot): # renvoie true si le mot peut s'écrire avec les lettres
    copie_tirage = list(tirage)
    compteur_joker = 0
    for lettre in mot: # pour chaque lettre dans le mot, on regarde si elle est dans la liste de lettres
        if lettre in copie_tirage:
            copie_tirage.remove(lettre)# on enleve la lettre si elle est dans la liste
        else: 
            if (copie_tirage.count('?')>0)&(compteur_joker==0):
                copie_tirage.remove('?')
                compteur_joker=1
            else:
                return False # on renvoie faux si la lettre n'est pas dans la liste
    return True
    
def score(mot, T):
    score = 0
    for lettre in mot:
        if lettre in T: #il faut que la lettre soit dans le tirage en plus d'être dans le mot maintenant
            if lettre in "aeilnorstu":
                score = score+1
            elif lettre in "dgm":
                score = score+2
            elif lettre in "bcp":
                score = score+3
            elif lettre in "fhv":
                score = score+4
            elif lettre in "jq":
                score = score+8
            elif lettre in "kwxyz":
                score = score+10
    return score

        
def max_score(liste_mots, T):
    score_max=0
    mot_max=liste_mots[0]
    for mot in liste_mots:
        if score(mot_max, T)<score(mot, T):
            mot_max=mot
            score_max=score(mot, T)
    return mot_max,score_max


#=========== Main


liste_mots = read_file(path) # on crée la liste de mots dans la librairie
mots_possible = list()
for mot in liste_mots:
    if is_not_possible(tirage, mot):
        mots_possible.append(mot) # on construit la liste de mots possibles dans la librairie

if len(mots_possible)==0:
    print("aucun mot n'est possible") # on s'assure qu'il y a bien un mot possible
else:
    mot_plus_long = mots_possible[0] 
    for mot in mots_possible:
        if len(mot)>len(mot_plus_long):
            mot_plus_long = mot
    print (mots_possible)
    print(mot_plus_long)

if len(mots_possible)!=0: #partie de la fonction main dans laquelle on teste la fonction score
    meilleur_score = score(mots_possible[0], tirage) 
    for mot in mots_possible:
        if meilleur_score<score(mot, tirage):
            meilleur_score = score(mot, tirage)
    print(meilleur_score)
    
print(max_score(mots_possible, tirage))