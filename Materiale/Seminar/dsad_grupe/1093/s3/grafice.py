import numpy as np
import matplotlib.pyplot as plt

# concepte
# - figure = intreaga fereastra
# - axes (axis) = zona de desenare relativa la figure
# - plot = graficul propriu-zis compus din linii/puncte

# 1. Scatter plot - nor de puncte - corelatia dintre 2 variabile
# intr-un scatter plot len(x) = len(y)

# achizitie de date
x = np.random.rand(50)
y = 3 * x + 0.2 * np.random.rand(50)

# constructia zonelor de desenare
plt.figure(figsize=(8,6))

# graficul propriu-zis
plt.scatter(x=x, y=y, color='orange', edgecolor='black', marker='o')
for i in range(50):
    plt.text(x[i], y[i], "V" + str(i), fontdict={'fontsize': 6, 'color':'black'})

# zona de stilizare
plt.title("Scatter plot of x vs y", fontdict={'fontsize': 20, 'color':'green'})
plt.xlabel("x values", fontdict={'fontsize': 20, 'color':'red'})
plt.ylabel("y values", fontdict={'fontsize': 20, 'color':'red'})
plt.grid(True)

# afisarea graficelor
plt.show()