import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb

# concepte generale
# 1. figure = intreaga fereastra
# 2. axes/axis = o subsectiune din figure, o zona dedicata pentru desenare
# 3. plot = graficul propriu-zis

# exista 5 etape in constructia unui grafic:
# 1. achizitia de date
# 2. definirea zonelor de desenarea
# 3. graficul propriu-zis
# 4. stilizarea graficului
# 5. afisarea efectiva

# ------------------------------------------------------------------------------------------------------------
# Scatter plot - relatia dintre 2 variabile => dimensiunea setului de date X = dimensiunea setului de date Y
# ------------------------------------------------------------------------------------------------------------
# 1. achizitie de date
x = np.random.rand(50)
y = np.random.rand(50) * 0.2 + 3 * x

# 2. definirea zonelor de desenare
plt.figure(figsize=(8, 6))

# 3. graficul propriu-zis
plt.scatter(x=x, y=y, color='red', edgecolor='black', marker='o')
for i in range(50):
    plt.text(x[i], y[i], "V" + str(i), fontdict={'fontsize': 8, 'color':'blue'})

# 4. stilizarea graficului
plt.title("Relatia dintre X si Y", fontdict={'fontsize': 24, 'color':'orange'})
plt.xlabel("X",  fontdict={'fontsize': 12, 'color':'green'})
plt.ylabel("Y", fontdict={'fontsize': 12, 'color':'green'})
plt.grid(True)

# 5. afisarea efectiva
# plt.show()

# echivalent ca si functionalitate, dar alternativ
# 2. definirea zonelor de desenare
fig = plt.figure(figsize=(8, 6))
ax_1 = fig.add_subplot(2, 2, 1)
ax_4 = fig.add_subplot(2, 2, 4)

# 3. graficul propriu-zis
ax_4.scatter(x=x, y=y, color='red', edgecolor='black', marker='o')
for i in range(50):
    ax_4.text(x[i], y[i], "V" + str(i), fontdict={'fontsize': 8, 'color':'blue'})

# 4. stilizarea graficului
ax_4.set_title("Relatia dintre X si Y", fontdict={'fontsize': 24, 'color':'orange'})
ax_4.set_xlabel("X",  fontdict={'fontsize': 12, 'color':'green'})
ax_4.set_ylabel("Y",  fontdict={'fontsize': 12, 'color':'green'})
plt.grid(True)

# 5. afisarea efectiva
# plt.show()

# ------------------------------------------------------------------------------------------------------------
# Line chart - util in reprezentarea trendurilor in timp
# ------------------------------------------------------------------------------------------------------------
# 1. achizitia de date
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 2. definirea zonelor de desenarea
plt.figure(figsize=(8,6))

# 3. graficul propriu-zis
plt.plot(x, y1, color='blue', label='sin(x)')
plt.plot(x, y2, color='red', label='cos(x)')

# 4. stilizarea graficului
plt.title("Graficul functiilor sin si cos pe intervalul [0, 10)", fontdict={'fontsize': 24, 'color':'orange'})
plt.xlabel("X",  fontdict={'fontsize': 12, 'color':'green'})
plt.ylabel("Valorile fc. sin si cos", fontdict={'fontsize': 12, 'color':'green'})
plt.grid(True)
plt.legend()

# 5. afisarea efectiva
# plt.show()

# ------------------------------------------------------------------------------------------------------------
# Bar chart (histograma) - distributia unei variabile
# ------------------------------------------------------------------------------------------------------------
# 1. achizitia de date
x = np.random.normal(50, 10, 1000)

# 2. definirea zonelor de desenarea
plt.figure(figsize=(8,6))

# 3. graficul propriu-zis
plt.hist(x=x, bins=100, color='lightgreen', edgecolor='darkgreen', alpha=0.7)

# 4. stilizarea graficului
plt.title("Distributia valorilor", fontdict={'fontsize': 24, 'color':'darkorange'})
plt.xlabel("Interval de valori",  fontdict={'fontsize': 12, 'color':'green'})
plt.ylabel("Frecvente", fontdict={'fontsize': 12, 'color':'green'})
plt.grid(True)

# 5. afisarea efectiva
# plt.show()

# ------------------------------------------------------------------------------------------------------------
# Box plot (matplotlib si seaborn) - compara distributii sau pentru a identifica valori outlier
# ------------------------------------------------------------------------------------------------------------
# 1. achizitia de date
departamente = ["HR", "IT", "Finance"]
salarii = [
    np.random.normal(4000, 300, 50),
    np.random.normal(6500, 500, 50),
    np.random.normal(4800, 350, 50)
]

# 2. definirea zonelor de desenarea
plt.figure(figsize=(8,6 ))

# 3. graficul propriu-zis
plt.boxplot(x=salarii, labels=departamente, patch_artist=True)

# 4. stilizarea graficului
plt.title("Boxplot - Salarii in functie de departament")
plt.ylabel("Salarii")
plt.xlabel("Departemente")

# 5. afisarea efectiva
#plt.show()

# Seaborn example

# 2. definirea zonelor de desenarea
plt.figure(figsize=(8,6))

# 3. graficul propriu-zis
salarii_sb = np.concatenate(salarii)
departamente_sb = np.repeat(departamente, 50)
sb.boxplot(x=departamente_sb, y=salarii_sb, palette='Set2')

# 4. stilizarea graficului
plt.title("Boxplot - Salarii in functie de departament")
plt.ylabel("Salarii")
plt.xlabel("Departemente")

# 5. afisarea efectiva
# plt.show()

# ------------------------------------------------------------------------------------------------------------
# Radar chart (spider chart)
# ------------------------------------------------------------------------------------------------------------
# 1. achizitia de date
labels = ["Speed", "Accuracy", "Stamina", "Skill", "Teamwork"]
data = np.array([
    [7,8,6,9,7],
    [6,7,8,8,8],
    [8,6,7,9,9]
])
players = ["Player 1", "Player 2", "Player 3"]

unghiuri = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
unghiuri += unghiuri[:1]

# 2. definirea zonelor de desenarea
plt.subplots(subplot_kw=dict(polar=True), figsize=(8,6))

# 3. graficul propriu-zis
for i in range(len(players)):
    valori = data[i].tolist() + [data[i][0]]
    plt.plot(unghiuri, valori, label=players[i])
    plt.fill(unghiuri, valori, alpha=0.25)

# 4. stilizarea graficului
plt.xticks(unghiuri[:-1], labels)
plt.title("Spider chart")
plt.legend()

# 5. afisarea efectiva
# plt.show()

# ------------------------------------------------------------------------------------------------------------
# Area chart
# ------------------------------------------------------------------------------------------------------------
# 1. achizitia de date
quarters = np.arange(1,5)
hr_revenues = [10, 12, 6, 3]
it_revenues = [18, 20, 25, 27]
fin_revenues = [12,14,6,17]

# 2. definirea zonelor de desenarea
plt.figure(figsize=(8,6))

# 3. graficul propriu-zis
plt.stackplot(quarters,
              hr_revenues, it_revenues, fin_revenues,
              labels=["HR", "IT", "FIN"],
              colors=["red", "green", "blue"],
              alpha=0.5)

# 4. stilizarea graficului
plt.title("Revenue growth by department")
plt.xlabel("Quarter")
plt.ylabel("Revenue")
plt.legend(loc='upper left')

# 5. afisarea efectiva
#plt.show()

# ------------------------------------------------------------------------------------------------------------
# Pie chart
# ------------------------------------------------------------------------------------------------------------
# 1. achizitia de date
departamente = ["HR", "IT", "Finance", "Marketing"]
bugete = [150_000, 500_000, 300_000, 200_000]

# 2. definirea zonelor de desenarea
plt.figure(figsize=(8,6))

# 3. graficul propriu-zis
plt.pie(bugete, labels=departamente,
        # shadow=True, # efect 3d
        autopct='%1.1f%%', # afiseaza procentele cu 1 zecimala
        #explode=(0, 0.1, 0, 0), # trage usor in afara 'felia' cea mai mare
        #colors=["red", "green", "lightblue", "yellow"]
        )


# 4. stilizarea graficului
plt.title("Distributia bugetelor departamentelor")

# 5. afisarea efectiva
# plt.show()

# ------------------------------------------------------------------------------------------------------------
# Combined chart
# ------------------------------------------------------------------------------------------------------------
# 1. achizitia de date
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
noise = np.random.randn(100) * 0.2
y_noise = y + noise

# 2. definirea zonelor de desenarea
plt.figure(figsize=(8,6))

# 3. graficul propriu-zis
plt.plot(x, y, label='sin(x)', color='green')
plt.scatter(x, y_noise, label='noise', color='red')

# 4. stilizarea graficului
plt.title("Grafic combinat")
plt.legend()

# 5. afisarea efectiva
plt.show()
