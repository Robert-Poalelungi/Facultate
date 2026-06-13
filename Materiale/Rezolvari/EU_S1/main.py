# importam librarii
import pandas as pd
from pandas.api.types import is_numeric_dtype #functie care verifica daca o variabila e numerica


# functie care inlocuieste valorile NaN
def nan_replace_t(t): #functie cu un parametru t
    assert isinstance(t, pd.DataFrame) #verificam daca parametrul t este data frame
    for v in t.columns: #iteram prin numele fiecarei coloane
        if any(t[v].isna()): #true daca exista un NaN in coloana
            if is_numeric_dtype(t[v]): #true daca coloana are date numerice
                t[v].fillna(t[v].mean(), inplace=True) #NaN e inlocuit cu media
            else:
                t[v].fillna(t[v].mode(), inplace=True) #NaN e inlocuit cu valoarea cea mai fecventa


# citim datele din csv intr-un dataframe si le indexam dupa valorile primei coloane
miscare = pd.read_csv("MiscareaNatLoc.csv", index_col=0)
populatie = pd.read_csv("PopulatieLocalitati.csv", index_col=0)


# inlocuirea valorilor NaN din dataframe
nan_replace_t(miscare)
nan_replace_t(populatie)


# unim cele 2 dataframeuri, in primul adaugam din al 2lea coloanele care nu exista si le combina dupa codul siruta
miscare = miscare.merge(populatie[["Populatie", "Judet"]], left_index=True, right_index=True)


# CERINTA 1
# - localitatile cu (Decedati + DecedatiSub1An) > nascuti vii
# - codul Siruta, denumirea localității, total decedați și născuți vii

miscare["TotalDecedati"] = miscare["Decedati"] + miscare["DecedatiSub1An"]

cerinta1 = miscare[miscare["TotalDecedati"] > miscare["NascutiVii"]]

cerinta1 = (cerinta1[["Localitate","TotalDecedati","NascutiVii"]]
            .to_csv("Cerinta1.csv", index=True))





#CERINTA 2
# - rata mortalitatii infantile pe localitate in ordine descrescatoare(dupa rata mortalitatii infantile)
# - DecedatiSub1An*1000/ NascutiVii
# - codul Siruta, numele localității și rata mortalității infantile

miscare["RataMortalitatiiInfantile"] = miscare["DecedatiSub1An"] * 1000 / miscare["NascutiVii"]

cerinta2 = (miscare[["Localitate", "RataMortalitatiiInfantile"]]
            .sort_values(by="RataMortalitatiiInfantile", ascending=False)
            .to_csv("Cerinta2.csv", index=True))


# CERINTA 3
# - rata sporului natural la nivel de județ
# - diferența dintre rata natalității (născuți vii la 1000 locuitori) și rata mortalității (decedați la 1000 locuitori)
# - indicativul de județ și rata sporului natural

miscare["RataNatalitatii"] = miscare["NascutiVii"] / miscare["Populatie"] * 1000

miscare["RataMortalitatii"] = miscare["TotalDecedati"] / miscare["Populatie"] * 1000

miscare["RataSporuluiNatural"] = miscare["RataNatalitatii"] - miscare["RataMortalitatii"]

cerinta3 = (miscare
            .groupby("Judet")["RataSporuluiNatural"]
            .mean()
            .reset_index()
            .to_csv("Cerinta3.csv", index=False))


# CERINTA 4
# - localitățile în care ratele (valorile indicatorilor la 1000 locuitori) sunt cele mai mari
# - Pentru fiecare județ se va afișa indicativul de județ și numele localităților cu valorile maxime

def maxim(gr, cols): #gr contine ce reiese din groupby
    res = {} #initiaza serie goala
    for c in cols:
        max_val = gr[c].max() #valoarea maxima din grup
        res[c] = ",".join(gr[gr[c]==max_val]["Localitate"]) #gasim randurile cu valoarea maxima din grup si extragem coloana Localitate
    return pd.Series(res) #transforma intr-o serie pentru apply

indicatori = ["Casatorii","Decedati","DecedatiSub1An","Divorturi","NascutiMorti","NascutiVii"] #lista de indicatori

cerinta4 = (miscare
            .groupby("Judet") #grupam dupa judet
            .apply(maxim, cols=indicatori)) #aplicam functia maxim, gr sunt de la groupby si in cols specificam lista

cerinta4.reset_index(inplace = True) #resetam indexul pentru a avea coloana Judet

cerinta4.to_csv("Cerinta4.csv", index=False)









