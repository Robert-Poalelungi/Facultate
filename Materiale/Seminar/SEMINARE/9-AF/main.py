from funtii import *
from grafice import *

np.set_printoptions(5, 10000, suppress=True)

set_date = pd.read_csv("mortalitate_ro.csv", index_col=1)
variabile_observate = list(set_date)[1:]

nan_replace(set_date)

model_acp = acp(set_date, variabile_observate)
model_acp.fit()
# print("Varinta componentelor principale:")
# print(model_acp.alpha)

# Analiza variantei
varianta = model_acp.tabelare_varianta()
varianta.to_csv("Varianta.csv")
print(varianta)
print("Criterii de selectie:")
print(model_acp.criterii)
alpha = model_acp.alpha
plot_varianta(alpha, model_acp.criterii)

# Analiza corelatiilor factoriale
r = model_acp.r
etichete_componente = varianta.index
t_r = pd.DataFrame(r, variabile_observate, etichete_componente)
t_r.to_csv("R.csv")
corelograma(t_r)
scatter(t_r, titlu="Plot corelatii", corelatii=True)

# Analiza scorurilor
c = model_acp.c
s = c / np.sqrt(alpha)
t_s = pd.DataFrame(s, set_date.index, etichete_componente)
t_s.to_csv("Scoruri.csv")
scatter(t_s)

# Calcul metrici
# Calcul cosinusuri
c2 = c * c
cosin = (c2.T / np.sum(c2, axis=1)).T
t_cosin = pd.DataFrame(cosin, set_date.index, etichete_componente)
t_cosin.to_csv("cosin.csv")
cosin_max = t_cosin.apply(func=lambda x: x.index[x.argmax()], axis=1)
cosin_max.name = "Componenta dominanta"
cosin_max.to_csv("cosin_max.csv")

# Contributiile
contrib = c2 * 100 / np.sum(c2, axis=0)
t_contrib = pd.DataFrame(contrib, set_date.index, etichete_componente)
t_contrib.to_csv("contrib.csv")
contrib_max = t_contrib.apply(func=lambda x: x.index[x.argmax()], axis=0)
contrib_max.name = "Instanta dominanta"
contrib_max.to_csv("contrib_max.csv")

# Comunalitati
r2 = r * r
comm = np.cumsum(r2, axis=1)
t_comm = pd.DataFrame(comm, variabile_observate, etichete_componente)
t_comm.to_csv("comm.csv")
corelograma(t_comm,0,"Reds",titlu="Comunalitati")

show()
