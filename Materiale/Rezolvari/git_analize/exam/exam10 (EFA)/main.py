import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from factor_analyzer import FactorAnalyzer,calculate_kmo,calculate_bartlett_sphericity

div_df = pd.read_csv('Diversitate.csv')
cod_df = pd.read_csv('Coduri_Localitati.csv')

# Cerinta A1
ani_list = list(div_df.columns[2:])
cerinta1 = div_df[div_df[ani_list].min(axis=1) == 0]
cerinta1 = cerinta1[["Siruta", "Localitate"] + ani_list]
cerinta1.to_csv("Cerinta1.csv", index=False)



# Cerinta A2
t = div_df.merge(cod_df[["Siruta", "Judet"]], on="Siruta")
t["Diversitate Medie"] = t[ani_list].mean(axis=1)

max_judet = (
    t.groupby("Judet")["Diversitate Medie"]
     .agg("max")
     .reset_index()
)

cerinta2 = t.merge(max_judet, on=["Judet", "Diversitate Medie"])
cerinta2 = cerinta2[["Judet", "Localitate", "Diversitate Medie"]]
cerinta2.rename(
    columns={"Diversitate Medie" : "Diversitate Maxima"},
    inplace=True
)
cerinta2.to_csv("Cerinta2.csv", index=False)












# Cerinta B1
x = div_df[ani_list].astype(float).values
fa_n = FactorAnalyzer(rotation=None)
fa_n.fit(x)
valori_proprii, _ = fa_n.get_eigenvalues()

n_factori = max(2, sum(valori_proprii > 1))

efa = FactorAnalyzer(n_factors= x.shape[1] - 1, rotation='varimax')
scores=efa.fit_transform(x)

varianta_fact,proc_var_extrasa,proc_var_cum=efa.get_factor_variance() # tuplu cu cele 3 valori cerute
print(varianta_fact,proc_var_extrasa,proc_var_cum)
df_varianta=pd.DataFrame(data={
    'Varianta factorilor': varianta_fact,
    'Procentul de varianta extrasa': proc_var_extrasa * 100,
    'Procentul de varianta cumulat': proc_var_cum *100
}).to_csv('./dateOUT/Varianta.csv',index=False)

















# Cerinta B2
factor_labels = [f"F{i + 1}" for i in range(n_factori)]

r = pd.DataFrame(
    data=efa.loadings_,
    index=ani_list,
    columns=factor_labels
)

r.to_csv("r.csv")

# Cerinta B3
x = efa.loadings_[:, 0]
y = efa.loadings_[:, 1]

t = np.arange(0, 2 * np.pi, 0.01)
xc = np.cos(t)
yc = np.sin(t)

plt.figure(figsize=(8,8))

plt.plot(xc, yc)

plt.scatter(x=x, y=y, color='orange', edgecolor='black', marker='o')

for i in range(len(ani_list)):
    plt.text(x[i], y[i], ani_list[i], fontdict={'fontsize': 6, 'color':'black'})

plt.title("Cercul corelatiilor (F1 vs F2)", fontdict={'fontsize': 20, 'color':'green'})
plt.xlabel("F1", fontdict={'fontsize': 20, 'color':'red'})
plt.ylabel("F2", fontdict={'fontsize': 20, 'color':'red'})
plt.grid(True)

plt.show()