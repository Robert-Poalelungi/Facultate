import numpy as np
import matplotlib.pyplot as plt

# concepte
# figure - canvas in HTML sau fereastra/plansa unde desenez
# axes - zona de desenare relativa la figure (1 figure poate avea 1 sau mai multe axes)
# plot - desenul propriu-zis compus din puncte, linii

# 1. Scatter plot - nor de puncte - corelatii intre variabile
x = np.random.rand(50)
y = 3 * x + np.random.rand(50) * 0.2

plt.figure(figsize=(8,6))
plt.scatter(x, y, color='royalblue', edgecolor='red', marker='o')
for i in range(50):
    plt.text(x[i], y[i], "V" + str(i))
plt.title("Scatter plot of x vs y", fontdict={'fontsize': 24, 'color': 'red'})
plt.xlabel("X values")
plt.ylabel("Y values")
# plt.grid(True)
#plt.show()

# alternativ, dar echivalent ca si functionalitate
fig = plt.figure(figsize=(8, 6))
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 4)

ax2.scatter(x, y, color='royalblue', edgecolor='red', marker='o')
ax2.set_title("Scatter plot of x vs y", fontdict={'fontsize': 24, 'color': 'red'})
ax2.set_xlabel("X values", fontdict={'fontsize': 12, 'color': 'blue'})
ax2.set_ylabel("Y values", fontdict={'fontsize': 12, 'color': 'green'})

for i in range(50):
    ax2.text(x[i], y[i], "V" + str(i))

#plt.show()

# 2. Line plot - grafic linie - trenduri sau tendinte in timp
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(8,6))
plt.plot(x, y1, label='sin(x)', color='red')
plt.plot(x, y2, label='cos(x)', color='blue')
plt.title("Line chart of x vs y")
plt.xlabel("x values")
plt.ylabel("function values")
#plt.legend()
#plt.show()

# 3. Histograma - bar chart - distributia unei variabile sau cum sunt valorile dispersate
data = np.random.normal(50, 10, 1000)
plt.figure(figsize=(8,6))
plt.hist(data, bins=20, color='skyblue', edgecolor='gray', alpha=0.7)
plt.title("Distributie normala")
plt.xlabel("value range")
plt.ylabel("frecventa")
plt.show()









