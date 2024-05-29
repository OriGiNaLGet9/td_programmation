##-----importation des modules-----##

import struct 

path = "the_wall.wav"

##-----fonctions-----#

def recup_data(path):
    f = open(path, "rb")
    data = f.read()   
    header = data[:44]
    return data, header

def recup_echant(data):
    voie1 = []
    voie2 = []
    i = 44
    while i<len(data):
        v = struct.unpack_from("hh", data, i)
        voie1.append(v[0])
        voie2.append(v[1])
        i = i+4
    return voie1, voie2

def recreer_music(header, voie1, voie2):
    with open("test.wav", "wb") as f: #ouvre un fichier et le crée si il n'existe pas
        f.write(header)
        for i in range(len(voie1)):
            f.write(struct.pack("h", voie1[i]))
            f.write(struct.pack("h", voie2[i]))

def recup_enchant2(data):
    voie1 = []
    voie2 = []
    i = 44
    while i<len(data):
        v = struct.unpack_from("hh", data, i)
        voie1.append(v[0])
        voie2.append(v[1])
        i = i+8
    return voie1, voie2

def recreer_music2(header, voie1, voie2):
    with open("test_q3.wav", "wb") as f: #ouvre un fichier et le crée si il n'existe pas
        f.write(header)
        for i in range(len(voie1)):
            f.write(struct.pack("h", voie1[i]))
            f.write(struct.pack("h", voie2[i]))

##-----main-----##

data = recup_data(path)[0]
header = recup_data(path)[1]
print(len(recup_echant(data)[0]))
recreer_music(header, recup_echant(data)[0], recup_echant(data)[1])
recreer_music2(header, recup_enchant2(data)[0], recup_enchant2(data)[1])