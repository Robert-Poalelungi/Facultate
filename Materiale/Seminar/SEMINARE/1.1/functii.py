import math


def calcul_indicatori(tabel,variabile_numerice):
    assert isinstance(tabel,dict)
    t={}
    for i in range(len(variabile_numerice)):
        x = []
        for v in tabel.keys():
            x.append(tabel[v][i+2])
        media=sum(x)/len(x)
        std = math.sqrt(sum([(v - media) * (v - media) for v in x]) / len(x))
        cvar=std/media
        t[variabile_numerice[i]]=(media,std,cvar)
    return t

def functie_filtru(t):
    if t[7]>0:
        return True
    else:
        return False

def functie_lambda(t,k,valoare):
    if t[k]>valoare:
        return True
    else:
        return False

def functie_lambda_dict(t,k,valoare):
    if t[1][k]>valoare:
        return True
    else:
        return False

def sortare(t,k):
    return t[1][k]

def selector(t):
    return(t[0],t[1][8:])

def salvare(tabel, variabile, nume_index="", nume_fisier="out.csv"):
    fisier = open(nume_fisier, mode="w")
    fisier.write(nume_index + "," + ",".join(variabile) + "\n")
    for v in tabel:
        fisier.write(str(v) + "," + ",".join([str(val) for val in tabel[v]]) + "\n")
    fisier.close()



