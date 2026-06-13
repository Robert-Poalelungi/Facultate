# grafice
import numpy as np
import matplotlib.pyplot as plt

# explicatie a conceptelor de baza in matplotlib
# - figure - intreaga pagina/ecran ori echivalentul unui canvas din HTML
# - axes - o zona de desenare in interiorul figurii
# - plot - desenul propriu zis compus din linii, puncte, histograme

# 1. Scatter plot - relatia intre 2 variabile
# date
x = np.random.rand(50)
y = 3 * x + np.random.rand(50) * 0.2

plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='royalblue', marker='o', edgecolor='black')
plt.title("Scatter plot of x vs. y", fontdict={'fontsize': 12, 'color': 'green'})
plt.xlabel("x values")
plt.ylabel("y values")
plt.grid(True)
# plt.show()

# alternativ pentru un scatter plot
fig = plt.figure(figsize=(8, 6))
# -------------------
# |   ax1  |   ax2  |
# -------------------
ax1 = fig.add_subplot(1,1,1)
# ax2 = fig.add_subplot(1,2,2)

ax1.set_title("Scatter plot of x vs. y", fontdict={'fontsize': 12, 'color': 'green'})
ax1.set_xlabel("x values")
ax1.set_ylabel("y values")

ax1.scatter(x, y, color='royalblue', marker='o', edgecolor='black')
for i in range(50):
    ax1.text(x[i], y[i], "V" + str(i))
# plt.show()

# 2. Line plot - util pentru evolutia trendurilor in timp
t = np.arange(0, 10, 0.1)
y1 = np.sin(t)
y2 = np.cos(t)

plt.figure(figsize=(8,6))
plt.plot(t, y1, color='royalblue', label='sin(t)')
plt.plot(t, y2, color='red', label='cost(t)')
plt.title("Line chart - sin & cos")
plt.xlabel("t values")
plt.ylabel('fc value')
plt.legend()
plt.show()

# 3. Histograma / BarChart - distributia unei variabile / cum sunt valorile distribuite
data = np.random.normal(50, 10, 1000)

plt.figure(figsize=(8,6))
plt.hist(data, bins=20, color='skyblue', edgecolor='gray', alpha=0.7)
plt.title("Histogram of data")
plt.xlabel("value range")
plt.ylabel("freq")
plt.show()
