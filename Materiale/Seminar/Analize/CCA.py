import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from seaborn import heatmap
from sklearn.cross_decomposition import CCA
from scipy.stats import chi2
from sklearn.preprocessing import StandardScaler

rawVoturi = pd.read_csv('./dateIN/Vot.csv', index_col=0)
rawCoduri = pd.read_csv('./dateIN/CoduriLocalitati2.csv', index_col=0)

labels = list(rawVoturi.columns.values[1:])
merged = rawVoturi.merge(rawCoduri, left_index=True, right_index=True).drop('Localitate_x', axis=1).rename(columns={'Localitate_y': 'Localitate'})[['County', 'Localitate'] + labels]
merged.fillna(np.mean(merged[labels], axis=0), inplace=True)

# Separarea seturilor de date pe barbati si femei
x_labels = [col for col in labels if 'Barbati' in col]  # Variabile pentru barbați
y_labels = [col for col in labels if 'Femei' in col]    # Variabile pentru femei

x = merged[x_labels].values  # Selectam doar coloanele cu "Barbati"
y = merged[y_labels].values  # Selectam doar coloanele cu "Femei"

# Standardizare
scaler_x = StandardScaler()
scaler_y = StandardScaler()
x = scaler_x.fit_transform(x)
y = scaler_y.fit_transform(y)

# Aplicare Analiza Canonică (CCA)
p = x.shape[1]
q = y.shape[1]
m = min(p, q)  # Numărul maxim de rădăcini canonice

cca = CCA(n_components=m)
z, u = cca.fit_transform(x, y)

# Calcul corelații canonice
r = []
for i in range(m):
    r.append(np.corrcoef(z[:, i], u[:, i], rowvar=False)[0, 1])

# Determinare relevanță rădăcini canonice (Test Bartlett)
n = x.shape[0]  # Numărul de observații

print("\nTestul Bartlett pentru relevanța rădăcinilor canonice:")
for i in range(m):
    lambda_wilk = np.flip(np.cumprod(np.flip(1 - np.array(r) ** 2)))[i]  # Lambda Wilks
    chi_square = -(n - (p + q + 3) / 2) * np.log(lambda_wilk)  # Statistica testului
    df_bartlett = (p - i) * (q - i)  # Grade de libertate
    p_value = 1 - chi2.cdf(chi_square, df_bartlett)  # P-valoare

    print(f"Rădăcina {i+1}: p = {p_value:.4f} ({'Semnificativă' if p_value < 0.05 else 'Nu semnificativă'})")

# Calcul corelații variabile observate - variabile canonice
rxz = np.corrcoef(x, z[:, :m], rowvar=False)[:p, p:]
ryu = np.corrcoef(y, u[:, :m], rowvar=False)[:q, q:]

# Trasare plot corelații variabile observate - variabile canonice (Cercul corelațiilor)
plt.figure(figsize=(8,8))
plt.title("Cercul de corelație", fontsize=14)
T = np.arange(0, np.pi * 2, 0.01)
X = np.cos(T)
Y = np.sin(T)
plt.plot(X, Y, color='black', linewidth=1)
plt.axhline(0, c='gray', linestyle='--')
plt.axvline(0, c='gray', linestyle='--')
plt.scatter(rxz[:, 0], rxz[:, 1], color='red', label='Variabile X')
plt.scatter(ryu[:, 0], ryu[:, 1], color='blue', label='Variabile Y')

plt.xlabel("Componenta Canonică 1", fontsize=12)
plt.ylabel("Componenta Canonică 2", fontsize=12)

for i in range(rxz.shape[0]):
    plt.annotate(f'X{i+1}', (rxz[i, 0], rxz[i, 1]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10)
for i in range(ryu.shape[0]):
    plt.annotate(f'Y{i+1}', (ryu[i, 0], ryu[i, 1]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10)

plt.legend()
plt.show()

# Trasare corelograma corelații variabile observate - variabile canonice
plt.figure(figsize=(10, 8))
heatmap(rxz, annot=True, cmap='coolwarm', xticklabels=[f'Comp {i+1}' for i in range(m)], yticklabels=[f'X{i+1}' for i in range(p)])
plt.title('Corelograma corelațiilor între X și variabilele canonice')
plt.show()

plt.figure(figsize=(10, 8))
heatmap(ryu, annot=True, cmap='coolwarm', xticklabels=[f'Comp {i+1}' for i in range(m)], yticklabels=[f'Y{i+1}' for i in range(q)])
plt.title('Corelograma corelațiilor între Y și variabilele canonice')
plt.show()

# Trasare plot instanțe în spațiile celor două variabile (Biplot) (primele 2 componente canonice)
plt.figure(figsize=(7, 7))
plt.title('Biplot CCA')
plt.xlabel("Componenta Canonică 1")
plt.ylabel("Componenta Canonică 2")
plt.scatter(z[:, 0], z[:, 1], c='r', label='Scoruri Canonice X (bărbați)')
plt.scatter(u[:, 0], u[:, 1], c='b', label='Scoruri Canonice Y (femei)')
plt.legend()
plt.show()

# Calcul varianță explicată și redundanță informațională
var_explicata_x = np.sum(rxz**2, axis=1)  # Varianța explicată de variabilele canonice pentru X
var_explicata_y = np.sum(ryu**2, axis=1)  # Varianța explicată de variabilele canonice pentru Y

redundanta_x = np.sum(rxz**2, axis=0)  # Redundanța informațională pentru X
redundanta_y = np.sum(ryu**2, axis=0)  # Redundanța informațională pentru Y

# Salvare rezultate
df_varianta = pd.DataFrame({"Varianta Explicată X": var_explicata_x, "Varianta Explicată Y": var_explicata_y,
                            "Redundanța X": redundanta_x, "Redundanța Y": redundanta_y})
df_varianta.to_csv("./dateOUT/CCA_Varianta.csv", index=False)

