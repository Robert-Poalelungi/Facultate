import numpy as np
import matplotlib.pyplot as plt

# concepte
# - figure = intreaga fereastra disponibila
# - axes(axis) = zona de desenare relativa la figure
# - plot = graficul propriu-zis compus din linii/puncte

# 1. Scatter plot - nor de puncte - corelatia dintre 2 variabile

# achizitia de date
x = np.random.rand(50)
y = x * 3 + 0.2 * np.random.rand(50)
# pt grafice de tip scatter nr de elem din x = nr de elem din y

# definirea zonei de desenare
plt.figure(figsize=(8,6))

# graficul propriu-zis
plt.scatter(x=x, y=y, color='orange', edgecolor='black', marker='o')
for i in range(50):
    plt.text(x[i], y[i], "V" + str(i), fontdict={'fontsize': 6, 'color': 'darkgreen'})

# zona de stilizare
plt.title("Scatter plot of x vs y", fontdict={'fontsize': 24, 'color': 'green'})
plt.xlabel("x values")
plt.ylabel("y values")
plt.grid(True)

# afisarea graficului
# plt.show()

# alternativ, dar echivalent ca si functionalitate
fig = plt.figure(figsize=(8,6))
ax1 = fig.add_subplot(2,2,1)
ax4 = fig.add_subplot(2,2,4)

ax4.scatter(x=x, y=y, color='orange', edgecolor='black', marker='o')
for i in range(50):
    ax4.text(x[i], y[i], "V" + str(i))

ax4.set_title("Scatter plot of x vs y", fontdict={'fontsize': 24, 'color': 'green'})
ax4.set_xlabel("x values", fontdict={'fontsize': 12, 'color': 'purple'})
ax4.set_ylabel("y values", fontdict={'fontsize': 12, 'color': 'purple'})

# plt.show()

# 2. Line chart - tendinta sau trendul unei variabile in timp
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(8,6))

plt.plot(x, y1, color='red', label='sin(x)')
plt.plot(x, y2, color='green', label='cos(x)')

plt.title("Valorile functiilor sin si cos pe intervalul [0:10)", fontdict={'fontsize': 24, 'color': 'green'})
plt.xlabel("x")
plt.ylabel("valorile functiilor")
plt.legend()

# plt.show()

# 3. Histograma - distributia valorilor unei variabile sau cum sunt distribuite acestea
date = np.random.normal(50, 10, 1000)

plt.figure(figsize=(8,6))

plt.hist(x=date, bins=30, color='cyan', edgecolor='black', alpha=0.7)

plt.title("Histograma", fontdict={'fontsize': 24, 'color': 'green'})
plt.xlabel("x")
plt.ylabel("frecventa")

plt.show()
