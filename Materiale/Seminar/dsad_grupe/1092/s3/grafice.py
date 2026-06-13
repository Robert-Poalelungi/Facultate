import numpy as np
import matplotlib.pyplot as plt

# concepte
# - figure = fereastra completa/ecran
# - axes (axis) = zona efectiva de desenare relativa la figure (1 figure poate avea 1 sau mai multe axes/axis)
# - plot = graficul propriu-zis compus din linii/puncte/figuri geometrice

# 1. Scatter plot - nor de puncte - corelatia dintre 2 variabile
# achizitia de date
# intr-un scatter plot len(x) = len(y)
x = np.random.rand(50)
y = x * 3 + 0.2 * np.random.rand(50)

# definirea zonei de desenare
plt.figure(figsize=(8,6))

# graficul propriu-zis
plt.scatter(x=x, y=y, color='orange', edgecolor='black', marker='o')
for i in range(50):
    plt.text(x[i], y[i], "V" + str(i), fontdict={'fontsize': 6, 'color':'black'})

# zona de stilizare
plt.title("Scatter plot of x vs y", fontdict={'fontsize': 24, 'color':'green'})
plt.xlabel("x values")
plt.ylabel("y values")
plt.grid(True)

# afisarea graficului
plt.show()

# alternativ, dar echivalent ca si functionalitate
fig = plt.figure(figsize=(8,6))
ax1 = fig.add_subplot(2,2,1)
ax4 = fig.add_subplot(2,2,4)

ax4.scatter(x=x, y=y, color='orange', edgecolor='black', marker='o')
for i in range(50):
    ax4.text(x[i], y[i], "V" + str(i), fontdict={'fontsize': 6, 'color':'black'})

ax4.set_title("Scatter plot of x vs y", fontdict={'fontsize': 24, 'color':'green'})
ax4.set_xlabel("x values", fontdict={'fontsize': 12, 'color':'purple'})
ax4.set_ylabel("y values", fontdict={'fontsize': 12, 'color':'purple'})

plt.show()

# 2. Line chart - plot - evolutia in timp a unui fenomen
