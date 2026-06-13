import numpy as np
import matplotlib.pyplot as plt



# concepts
# - figure = entire window
# - axes (axis) = drawing area relative to the figure
# - plot = actual chart composed of lines/points

# 1. Scatter plot - correlation between 2 variables
# in scatter plots len(x) = len(y)
# data acquisition
x = np.random.rand(50)
y = 3 * x + np.random.rand(50) * 0.2

# drawing windows definition
plt.figure(figsize=(8,6))

# actual plotting
plt.scatter(x=x, y=y, color='orange', edgecolor='black', marker='o')
for i in range(50):
    plt.text(x[i], y[i], "V" + str(i), fontdict={'fontsize': 8, 'color': 'black'})

# stylization area
plt.title("Scatter plot of x vs y", fontdict={'fontsize': 24, 'color': 'red'})
plt.xlabel("x values", fontdict={'fontsize': 12, 'color': 'green'})
plt.ylabel("y values", fontdict={'fontsize': 12, 'color': 'green'})
plt.grid(True)

# drawing display
plt.show()



