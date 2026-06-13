import numpy as np
import matplotlib.pyplot as plt
from sympy.abc import alpha

# concepte
# - figure - intreaga fereastra / echivalentul unui canvas in HTML
# - axes(axis) - zona de desenare relativa la figure
# - plot - graficul propriu-zis compus din linii/puncte

# 1. Scatter plot - nor de puncte - corelatia dintre 2 variabile
# zona de definire a datelor
x = np.random.rand(50)
y = 3 * x + 0.2 * np.random.rand(50)

# zona de definire a figure/axis
plt.figure(figsize=(8,6))

# graficul propriu-zis
plt.scatter(x=x, y=y, color='orange', marker='x', edgecolor='black')
for i in range(50):
    plt.text(x[i], y[i], "V" + str(i))

# stilizare
plt.title("Scatter plot of x vs y", fontdict={'fontsize': 24, 'color':'green'})
plt.xlabel("x values")
plt.ylabel("y values")
# plt.grid(True)

# zona de afisare propriu-zisa
#plt.show()

# alternativ dar echivalent ca si functionalitate
fig = plt.figure(figsize=(8,6))
ax1 = fig.add_subplot(2,2,1)
ax4 = fig.add_subplot(2,2,4)

ax4.scatter(x=x, y=y, color='orange', marker='x', edgecolor='black')
for i in range(50):
    ax4.text(x[i], y[i], "V" + str(i), fontdict={'fontsize': 6, 'color':'purple'})

ax4.set_title("Scatter plot of x vs y", fontdict={'fontsize': 24, 'color':'green'})
ax4.set_xlabel("x values", fontdict={'fontsize': 12, 'color':'purple'})
ax4.set_ylabel("y values", fontdict={'fontsize': 12, 'color':'purple'})

#plt.show()

# 2. Line chart - utilizat pentru a vizualiza trenduri/tendinte in timp
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(8,6))

plt.plot(x, y1, label="sin(x)", color='blue')
plt.plot(x, y2, label='cos(x)', color='red')

plt.title('Evolutia sin(x) si cos(x) pt x in [0:10)')
plt.xlabel("x")
plt.ylabel("valorile functiilor")
plt.legend()

# plt.show()

# 3. Histograma - bar chart - distributia unei variabile sau cum sunt valorile variabilei distribuite
date = np.random.normal(50, 10, 1000)

plt.figure(figsize=(8,6))

plt.hist(x=date, color='cyan', alpha=0.7, edgecolor='black')

plt.title("Histograma")
plt.xlabel("set de valori")
plt.ylabel("frecventa")

plt.show()