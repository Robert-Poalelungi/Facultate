import numpy as np
import Utile as utl
import matplotlib.pyplot as plt


# problema 1 - sa creeze o lista de 100 numere aleatoare,
# utilizand list comprehension
print(type(np.random.rand(100)), np.random.rand(100))
list_1 = list(np.random.rand(100))
print(type(list_1), list_1) # terminatorul de linie <CR><NL>

print(type(range(100)), range(100))
# list_2 = [x for x in list_1] # creez de fapt o copie a listei list_1
# print(list_2)
list_2 = [x for x in np.random.rand(100)]
print(list_2)

# crearea unei liste de 100 de valori aleatoare in intervalul [-5, 5]
print(type(utl.random(-5, 5, 7)))
list_3 = [x for x in utl.random(2, 3, 100)]
print(list_3)

# dictionare
dict_1 = {'luni': 1,  # nu este necesar \ pentru a continua o linie logica pe mai multe linii fizice
          'marti': 3.14,
          'miercuri': 'un sir de caractere',
          'joi': [1, 2, 3]}

print(dict_1)
print(dict_1['joi'])

print(type(dict_1.keys()), dict_1.keys())
print(type(list(dict_1.keys())), list(dict_1.keys()))

print(type(dict_1.values()), dict_1.values())
print(type(list(dict_1.values())), list(dict_1.values()))

lista_de_perechi = list(dict_1.items())
print(type(lista_de_perechi), lista_de_perechi)

for (k, v) in dict_1.items():
    print(k, ': ', v)

fisierIntrare = open('Seminar_2.py', 'r')

# timparire la consola a continutului unui fisier text
with fisierIntrare as f:
    string_mare = ''
    for rand in f:
        # consider fisierul text ca o lista string-uri
        # print(type(rand), rand)
        # print(rand, end='')
        # print(rand[:-1]) # vad randul ca o lista de caractere
        string_mare += rand # vad fisierul text ca o concatenare de randuri (strings)
    print(string_mare)

# popularea cu date in maniera programatica a unui dictionar
# f(x) = x = y , functia identitate
dict_2 = {x: x for x in range(100)}
print(dict_2)

dict_3 = {k: v for (k, v) in dict_2.items()} # este in fapt realizarea unei copii a dict_2
# dict_3 = {k: v**2 for (k, v) in dict_2.items()}
print(dict_3)

# f(x) = log(x) = y
# dict_4 = {x+1: np.log(x+1) for x in range(100)}
dict_4 = {k+1: np.log(v+1) for (k, v) in dict_2.items()}
print(dict_4)

# plt.plot(dict_4.values())
# plt.plot(dict_4.values(), dict_4.keys())
plt.plot(dict_4.keys(), dict_4.values())
# plt.show()

# problema 3 - creati un dictionar care sa aiba cheile de forma col1, col2, col3 ...
# iar valorile sa fie liste de cate 5 numere aleatoare in intervalul [1, 2]
# dict_5 = {'col'+str(j): [x for x in utl.random(1, 2, 5)] for j in range(1, 4)}
dict_5 = {'col'+str(j): list(utl.random(1, 2, 5)) for j in range(1, 4)}
print(dict_5)

lista_de_liste = list(dict_5.values())
print(lista_de_liste)

matrice = lista_de_liste
for linie in matrice:
    print(linie)