import numpy as np
import matplotlib.pyplot as plt
from sympy.abc import alpha

# concepte
# figure - canvas de desenat, "foaia de desen"
# axes - zona dedicata de desenare relativa la o figure
# plot - desenul propriu-zis compus din linii, puncte

# 1. Scatter plot - nor de puncte - relatia intre 2 variabile
x = np.random.rand(50)
y = 3 * x + np.random.rand(50) * 0.2

plt.figure(figsize=(8,6))
plt.scatter(x, y, color='royalblue', marker='o', edgecolor='black')
plt.title("Scatter plot of x vs y", fontdict={'fontsize': 24, 'color':'orange'})
plt.xlabel("x values")
plt.ylabel("y values")
for i in range(50):
    plt.text(x[i], y[i], "V" + str(i))
plt.grid(True)
# plt.show()

# alternativ, dar echivalent ca si functionalitate
fig = plt.figure(figsize=(8,6))
# ax1 = fig.add_subplot(2,2,1)
# ax2 = fig.add_subplot(2,2,4)
ax2 = fig.add_subplot(1,1,1)
ax2.set_title("Scatter plot of x vs y", fontdict={'fontsize': 24, 'color':'orange'})
ax2.set_xlabel("x values", fontdict={'fontsize': 12, 'color':'blue'})
ax2.set_ylabel("y values", fontdict={'fontsize': 12, 'color':'green'})
ax2.scatter(x, y, color='royalblue', marker='o', edgecolor='black')
for i in range(50):
    ax2.text(x[i], y[i], "V" + str(i))
# plt.show()


# 2. Line chart - tendinte sau trenduri in timp
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(8,6))
plt.plot(x, y1, label='sin(x)', color='red')
plt.plot(x, y2, label='cos(x)', color='green')
plt.title("Line chart of x vs y")
plt.xlabel("x")
plt.ylabel("function value")
# plt.legend()
plt.show()

# 3. Histograma (Bar Chart) - distributia unei variabile sau cum sunt dispersate valorile unei variabile
data = np.random.normal(50, 10, 1000)

plt.figure(figsize=(8,6))
plt.hist(data, bins=20, color='skyblue', edgecolor='gray', alpha=0.7)
plt.title("Bar chart - normal distribution")
plt.xlabel("value range")
plt.ylabel("frecventa")
plt.show()