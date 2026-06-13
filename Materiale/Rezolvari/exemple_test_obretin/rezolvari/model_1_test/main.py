# importuri
import pandas as pd
from pandas.api.types import is_numeric_dtype

# functie completare date
def nan_replace(t):
    assert isinstance(t, pd.DataFrame)
    for v in t.columns:
        if any(t[v].isna()):
            if is_numeric_dtype(t[v]):
                t[v].fillna(t[v].mean(), inplace = True)
            else:
                t[v].fillna(t[v].mode()[0], inplace = True)

# citire date
miscare = pd.read_csv('./res/MiscareaNatLoc.csv', index_col = 0)
populatie = pd.read_csv('./res/PopulatieLocalitati.csv', index_col = 0)

# inlocuire valori nan
nan_replace(miscare)
nan_replace(populatie)

print(miscare)
print(populatie)

# merge intre tabele

merge = miscare.merge(populatie[['Judet', 'Populatie']],
                      left_index= True,
                      right_index= True)
print(merge)

# 1. Să se salveze în fișierul Cerinta1.csv localitățile în care numărul total de decedați (Decedați + DecedatiSub1An) este mai mare decât numărul de născuți vii. Se va salva pentru fiecare localitate, codul Siruta, denumirea localității, total decedați și născuți vii.

merge['Total_Decedati'] = merge['Decedati'] + merge['DecedatiSub1An']
cerinta1 = merge[merge['Total_Decedati'] > merge['NascutiVii']]
cerinta1 = cerinta1[[ 'Localitate', 'Total_Decedati', 'NascutiVii']]
cerinta1.to_csv('./output/Cerinta1.csv', index = True)

#2. Să se salveze în fișierul Cerinta2.csv rata mortalității infantile la nivel de localitate, în ordine
# descrescătoare. Rata mortalității infantile se calculează ca număr de decedați sub un an la 1000 de
# născuți vii: DecedatiSub1An*1000/ NascutiVii. Pentru fiecare localitate se va salva codul Siruta,
# numele localității și rata mortalității infantile, în ordine descrescătoare după rata mortalității
# infantile.

merge['RMI'] = merge['DecedatiSub1An'] * 1000 / merge['NascutiVii']
cerinta2 = merge[[ 'Localitate', 'RMI']].sort_values(by='RMI', ascending=False)
cerinta2.to_csv('./output/Cerinta2.csv', index=True)

# 3. Să se salveze în fișierul Cerinta3.csv rata sporului natural la nivel de județ. Rata sporului natural
# este diferența dintre rata natalității (născuți vii la 1000 locuitori) și rata mortalității (decedați la
# 1000 locuitori). Pentru fiecare județ se va salva indicativul de județ și rata sporului natural.

merge['RN'] = merge['NascutiVii'] / merge['Populatie'] * 1000
merge['RM'] = merge['Total_Decedati'] / merge['Populatie'] * 1000
merge['SN'] = merge['RN'] - merge['RM']
cerinta3 = merge.groupby('Judet')['SN'].mean()
cerinta3.to_csv('./output/Cerinta3.csv', index=True)


# 4. Să se calculeze și să se salveze în fișierul Cerinta4.csv pentru fiecare județ, localitățile în care
# ratele (valorile indicatorilor la 1000 locuitori) sunt cele mai mari. Pentru fiecare județ se va afișa
# indicativul de județ și numele localităților cu valorile maxime.

def max(grupe, coloane):
    rezultat = {}
    for c in coloane:
        maxim = grupe[c].max()
        rezultat[c] = ','.join(grupe[grupe[c]==maxim]['Localitate'])
    return pd.Series(rezultat)

indicatori = ["Casatorii","Decedati","DecedatiSub1An","Divorturi","NascutiMorti","NascutiVii"]
cerinta4 = merge.groupby("Judet").apply(max, coloane=indicatori)
cerinta4.reset_index(inplace=True)
cerinta4.to_csv('./output/Cerinta4.csv', index=False)







