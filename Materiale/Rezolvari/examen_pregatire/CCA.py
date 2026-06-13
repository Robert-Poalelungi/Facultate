import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import chi2
from seaborn import heatmap
from sklearn.cross_decomposition import CCA

x = np.ndarray() # standardized
y = np.ndarray() # standardized

p = x.shape[1]
q = y.shape[1]
m = min(p, q)
cca = CCA(n_components=m)
z, u = cca.fit_transform(x, y)
rxz = np.corrcoef(x, z[:, :m], rowvar=False)[:p, p:]
ryu = np.corrcoef(y, u[:, :m], rowvar=False)[:q, q:]
r = []
for i in range(m):
    r.append(np.corrcoef(z[:, i], u[:, i], rowvar=False)[0, 1])


plt.figure(figsize=(10, 8))
heatmap(rxz, annot=True, cmap='coolwarm', xticklabels=range(1, m + 1), yticklabels=range(1, p + 1))
plt.title('Corelograma corelațiilor între x și variabilele canonice')
plt.show()

plt.figure(figsize=(8,8))
plt.title("Cercul de corelație", fontsize=14)
T=np.arange(0,np.pi*2,0.01)
X=np.cos(T)
Y=np.sin(T)
plt.plot(X,Y, color='black', linewidth=1)
plt.axhline(0,c='gray', linestyle='--')
plt.axvline(0,c='gray', linestyle='--')
plt.scatter(rxz[:,0],rxz[:,1], color='red', label='Variabile x')

plt.xlabel("Componenta Canonică 1", fontsize=12)
plt.ylabel("Componenta Canonică 2", fontsize=12)

for i in range(rxz.shape[0]):
    plt.annotate(f'x{i+1}', (rxz[i, 0], rxz[i, 1]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10)

plt.legend()
plt.show()

plt.figure(figsize=(7, 7))
plt.title('Biplot CCA')
plt.xlabel("x")
plt.ylabel("y")
plt.scatter(x[:, 0], x[:, 1], c='r', label='X')
plt.scatter(y[:, 0], y[:, 1], c='b', label='Y')
plt.legend()

# Varianța explicată de variabilele canonice pentru x
var_explicata_x = np.sum(rxz**2, axis=1)

# Varianța explicată de variabilele canonice pentru y
var_explicata_y = np.sum(ryu**2, axis=1)

# Redundanța informațională pentru x
redundanta_x = np.sum(rxz**2, axis=0)

# Redundanța informațională pentru y
redundanta_y = np.sum(ryu**2, axis=0)

# Testul Bartlett
n = x.shape[0]  # Numărul de observații

print("\nTestul Bartlett pentru relevanța rădăcinilor canonice:")
for i in range(m):
    lambda_wilk = np.prod(1 - np.array(r[i:])**2)  # Lambda Wilks pentru rădăcinile rămase
    chi_square = -(n - (p + q + 3) / 2) * np.log(lambda_wilk)  # Statistica testului
    df_bartlett = (p - i) * (q - i)  # Grade de libertate
    p_value = 1 - chi2.cdf(chi_square, df_bartlett)  # P-valoare

    print(f"Rădăcina {i+1}: p = {p_value:.4f} ({'Semnificativă' if p_value < 0.05 else 'Nu semnificativă'})")