import numpy as np

def indiceDisimilaritate(X_df, col):
    #extragere matrice de date numerica ca numpy.ndarray
    X = X_df[col].values

    #calcul sume pe linii
    sumePeLinii = np.sum(a=X, axis=1) #suma pe linii
    sumePeColoane = np.sum(a=X, axis=0)  # sume pe coloane(etnii)


    #calcul matrice de resturi
    matriceResturi = np.transpose(sumePeLinii - X.T) #.T e pentru transpunerea unui dataframe
    resturiColoane = np.sum(a=matriceResturi, axis=0) #resturi pe coloane

    # inlocuire valori nule cu element neutru la impartire(adica 1)
    sumePeColoane[sumePeColoane==0] = 1 #oriunde avem valoarea 0 in vector, inlocuim cu valoarea 1
    resturiColoane[resturiColoane==0] = 1


    pXTx = X / sumePeColoane

    pRTr = matriceResturi / resturiColoane

    #componenta e echivalentul chestiei care se afla in modul(dupa suma) in formula indicelui de disimilaritate

    componente = 0.5*np.abs(pXTx - pRTr)

    return np.sum(componente, axis=1) #suma pe linii, pentru fiecare uitate administrativ teritoriala
