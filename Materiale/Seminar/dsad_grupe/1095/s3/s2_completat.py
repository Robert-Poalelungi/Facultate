from functools import reduce
import numpy as np
import time

# comprehensions
numere = []
for each in range(20):
    if each % 2 == 0:
        numere.append(each ** 2)
# print(numere)

# echivalent cu blocul de mai sus:
# intr-un list comprehension sunt relevante 3 blocuri:
# - primul: instr. repetitiva: for x in range(20)
# - al doilea: transformari aplicate pe elemente citite (daca exista)
#               - in cazul nostru luam elementele ca atare: x ** 2
# - al treilea: filtre aplicate pe elementele citite din iterator
#               - in cazul nostru: if x % 2 == 0
numere = [x ** 2 for x in range(20) if x % 2 == 0]
# print(numere)

# dict comprehensions
nume = ["Ana", "Andrei", "Alina"]
note = [10, 9.5, 9.75]
catalog = {k: v for k, v in zip(nume, note)}
# print(catalog, type(catalog),
#       catalog.keys(), type(catalog.keys()),
#       catalog.values(), type(catalog.values()),
#       catalog.items(), type(catalog.items()))

celsius = [10, -3, 0, 20, 25]
fahrenheit = [ round(c * 9/5 + 32, 1) for c in celsius ]
# print(celsius, fahrenheit)

# lambda, map, filter, reduce
secventa = (1, 2, 3, 4)
result = map(lambda x: x ** 3, secventa)
# print(result, type(result), list(result), type(list(result)))

# de avut in vedere diferente subtile la nivel de definire a datelor
# adica: felul cum sunt construite obiectele folosind [], (), {}
# vs felul cum acestea sunt construite folosind constructori
l1 = [1, 2, 3, 4]
l2 = list((1,2,3,4))
l3 = list("ana")
s1 = set("analiza datelor")
s2 = {"analiza datelor"}
# print(l1, l2, l3, s1, s2)

# filter
result = filter(lambda x: x >= 0, celsius)
# echivalent cu list comprehensions
result_lc = [x for x in celsius if x >= 0]
print(type(result), result, list(result))

note = [3, 7, 4, 5, 9, 10, 5, 6]
promovat = [n for n in note if n >= 5]
status = ["promovat" if n >= 5 else "restant" for n in note]
print("Note: ", note)
print("Promovat: ", promovat)
print("Status: ", status)

emails = ["john.doe@gmail.com", "student@ase.ro", "support@google.com"]
valid = list(filter(lambda e: e.endswith("ase.ro"), emails))
print(valid)

# reduce
suma = reduce(lambda a,b: a+b, note)
print(suma, type(suma))
print("Media notelor:", suma / len(note))

# numpy
# numpy pune la dispozitie un obiect numit ndarray
# spre deosebire de o lista simpla in python care accepta elemente de tipuri diferite
# un ndarray forteaza un singur tip de date pt toate elem. din colectie
# in plus, acestea sunt repr. intr-o zona de memorie continua si suporta SIMD
l1 = [1, 2, 3.14, "ana", True, None, [5,6,7]]
print(l1)
a = np.array([1, 2, 3], dtype='int16')
b = np.array([[5.4, 3.2], [7.4, 1.6], [6.6, 2.2]])

print("Numpy arrays:")
print("a: \n", a)
print("b: \n", b)

# proprietati ale ndarray
print("Shape:", b.shape)
print("Dimensiuni:", b.ndim)
print("Tip de data:", b.dtype)
print("Dim. unui elem (bytes):", b.itemsize)
print("Dim. totala:", b.nbytes)

# indexing & slicing
print("Acces elemente")
# corectii pe S1
c = [1,2,3,4,5]
print(c[len(c)-1])
print(c[0 : len(c)])
print(c[0 : len(c)-1])
print(c[0 : len(c)+100])

# indexing
a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(a[1, 2], a[1][2])
a[1,2] = 20
print(a[1, 2], a[1][2])

# slicing [start idx : end idx : step]
print(a[0, 1:-1]) # 2, 3, 4
print(a[0, 1:-1:2]) # 2, 4
print(a[0, ::2]) # 1, 3, 5
print(a[0, :]) # 1,2,3,4,5
print(a[:, 3]) # 4, 9
print(a[:-1, 3]) # 4

# colectii predefinite
print("Zeros:", np.zeros(3)) # vector de 3 elemente
print("Zeros:", np.zeros((3, 2))) # metrice de 3 randuri si 2 coloane
print("Ones:", np.ones((2, 2), dtype='int32'))
print("Full:", np.full((2, 2), 100))
print("Random:", np.random.rand(2,2))
print("Random integers:", np.random.randint(-100, 100, size=(3, 3)))
print("Identity:", np.identity(4))

# repeat (extinzi fiecare elem) si tile (copy-paste al structurii)
a = np.array([1,2,3])
print("Tile:", np.tile(a, 2))
print("Repeat:", np.repeat(a, 2))

# shallow vs deep copy in ndarray
b = a
c = a.copy()

b[0] = 10
c[0] = 20
print("A:", a)
print("B:", b)
print("C:", c)

# performanta in numpy
start = time.time()
a = np.arange(1, 1_000_001)  # 1_000_001 <=> 1.000.001 (la nivel conceptual)
ap = a ** 2
durata = time.time() - start

start_lista = time.time()
lst = [i ** 2 for i in range(1, 1_000_001)]
# lstp = [i ** 2 for i in lst]
durata_lista = time.time() - start_lista

print("Comparatie in termeni de performanta")
print(f"Numpy: {durata:.5f}s | Python: {durata_lista:.5f}s")

# broadcasting si operatii pe ndarrays
# broadcasting - modalitatea prin care numpy rezolva operatii intre ndarrays de forme diferite prin extinderea automata a ndarray-ului de forma mai mica, a.i. acesta sa se potriveasca celui mare

c = np.array([
    [1,2,3],
    [4,5,6]
])

print("Broadcasting de elem - inmultire de matrice cu scalar:\n", c * 2)

x = np.array([
    [1, 2],
    [3, 4]
])
y = np.array([
    [5, 10],
    [20, 25]
])

print("Inmultire element cu element:\n", x * y)
print("Multiplicare de matrice ca la matematica: \n", x @ y)

a = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

d = np.array([1,2,3])

b = np.array([
    [1,2],
    [4,5],
    [7,8]
])

# d * b = (3,1) x (3,3) => in cazul acesta prin broadcasting, numpy extinde vectorul astfel incat inmultirea elem cu elem sa se efectueze
print(d * b)

# a * b = (3,2) x (3,3) => eroare, intrucat broadcasting nu reconciliaza elementele din ndarray a, pentru inmultire elem cu elem cu b
print(a*b)

# de revenit pt: ValueError: operands could not be broadcast together with shapes (3,) (3,2)