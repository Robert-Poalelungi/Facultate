import numpy as np
import matplotlib.pyplot as plt

# concepte
# figure - pagina intreaga, un fel canvas din HTML
# axes - (axis) o zona de desenare relativa la figure
# plot - graficul propriu-zis compuns din linii, puncte

# 1. Scatter plot - nor de puncte - relatia dintre 2 variabile
x = np.random.rand(50)
y = 3 * x + np.random.rand(50) * 0.2

plt.figure(figsize=(8, 6))

plt.scatter(x, y, color='royalblue', marker='x', edgecolor='red')
for i in range(50):
    plt.text(x[i], y[i], "v" + str(i))

plt.title("Scatter plot of x vs y", fontdict={'fontsize': 24, 'color':'orange'})
plt.xlabel("x values")
plt.ylabel("y values")
plt.grid(True)

plt.show()

# alternativ, dar echivalent ca functionalitate
fig = plt.figure(figsize=(8,6))
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,4)

ax2.scatter(x, y, color='royalblue', marker='x', edgecolor='red')
for i in range(50):
    ax2.text(x[i], y[i], "v" + str(i))

ax2.set_title("Scatter plot of x vs y", fontdict={'fontsize': 24, 'color':'orange'})
ax2.set_xlabel("x values", fontdict={'fontsize': 12, 'color':'green'})
ax2.set_ylabel("y values", fontdict={'fontsize': 12, 'color':'blue'})

plt.show()