import main as fun
import numpy as py

#Prima varianta de interschimbare
a = 7
b = 11

a, b = fun.interschimb(a, b)

print(a, b)

#Exista si optiunea mai usoara in Python
a, b = b, a

print(a, b)

#in Python, parametrii la functii/metode sunt pasati ca referinte la obiect
lista = [5, 9]
fun.interschimbCuLista(lista);

print(lista)

#List comprehension
#populare programatica cu valori a unei liste
lista2 = [element + 1 for element in range(-10, 10)]
print(lista2)

#Problema: extrageti din lista2 valori pozitive si impare
lista3 = [element for element in lista2 if (element > 0 and element % 2 == 1)]
print(lista3)

#Problema: sa se creeze o lista cu valori din lista3 si lista4
#astfel incat f(x, y) = (x + y)** 2 pentru (x + y) valoare para
lista4 = [1, 2, 3]
lista5 = [(x + y)**2 for x in lista3 \
          for y in lista4 if (x+y) % 2 == 0]

print(lista5)

#Lucru cu fisiere text
fisier_text = open('Seminar.py', 'rt')

#mergem de la ultimul, pana la penultimul element din lista, ultimul fiind /n care ne creea o linie goala in plus la afisare
# with fisier_text as f:
#     for linie in f:
#         print(linie[:-1])
#
# fisier_text.close();

#Disctionare
dictionar = {'luni': 'mama',
             'marti': 12.34,
             'miercuri': [1, 2, 3, 'tata', [4, 5]]}

print(dictionar)

#extragerea cheilor
print(dictionar.keys())
print(list(dictionar.keys()))

#extragerea valorilor
print(dictionar.values())
print(list(dictionar.values()))

#lista de perechi (cheie, valoare)
print(dictionar.items())

for key, value in dictionar.items():
    print('cheie: ', key, ' valoare:', value)

#Dictionary comprehension
dictionar2 = {element: element + 1 for element in range(10)}
print(dictionar2)

#Problema: Sa se creeze un dictionar ce are cheile de forma
#S1, S2, ..., S10 si valorile numere intregi aleatoare intre
#1 si 10
vectorAleator = py.random.random(10)
print(vectorAleator)
dictionar3 = {}