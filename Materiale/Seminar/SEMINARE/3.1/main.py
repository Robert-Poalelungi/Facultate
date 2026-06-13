from functii import *
from sklearn.preprocessing import StandardScaler

np.set_printoptions(threshold=np.inf) #seteaza optiunile de afisare: threshold=np.inf se afiseaza tot indiferent de dimensiune

tabel = pd.read_csv("Teritorial_2022.csv", index_col=0) #se citeste csv intr-un tabel, cu coloana 0 index
# print(tabel,type(tabel))
variabile = list(tabel) #se retin numele variabilelor intr o lista de tabel
variabile_numerice = variabile[3:] #se retin numele variabilelor numerice intr o lista de variabile
print(variabile, variabile_numerice, sep="\n") #putem sa afisam tabelul, sau listele de variabile

x = tabel[variabile_numerice].values #se retin intr un array valorile numerice ale variabilelor numerice
# print(x, type(x))

# Cerinta 1
nan_replace(x)
# print(x)

# Cerinta 2
x_c = standardize(x, std=False)
x_std = standardize(x)
salvare(x_c, tabel.index, variabile_numerice, "x_c.csv")
salvare(x_std, tabel.index, variabile_numerice, "x_std.csv")
# print(np.std(x_std,axis=0),np.mean(x_std,axis=0))
# scalare = StandardScaler()
# x_std_ = scalare.fit_transform(x)
# print(np.std(x_std_,axis=0))

# Cerinta 3
v = np.cov(x, rowvar=False)
r = np.corrcoef(x, rowvar=False)
salvare(v, variabile_numerice, variabile_numerice, "V.csv")
salvare(r, variabile_numerice, variabile_numerice, "R.csv")

# Cerinta 4
rez_teste = teste_c(x)
salvare(rez_teste[0],variabile_numerice,["Shapiro","KS","Chi2"],"tc_pvalues.csv")
salvare(rez_teste[1],variabile_numerice,["Shapiro","KS","Chi2"],"tc.csv")
