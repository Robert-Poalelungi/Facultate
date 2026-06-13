from functools import reduce
import time
import numpy as np

# structuri de date built-in in python
# liste
temperaturi = [10, 10, 5, 20, -3, True, None, 3.14, "ana", [5, 6, 7]]
print("lista", temperaturi, temperaturi[0], temperaturi[len(temperaturi) - 1], type(temperaturi))
temperaturi[0] = 20
print(temperaturi[0])
l1 = list((10, 15, 5, 20, -3))
l2 = list("analiza datelor")

# seturi - colectii ce nu contin duplicate si care nu pastreaza ordinea insertiei
s1 = {"analiza datelor", 10, 5, -3, True}
s2 = set("analiza datelor")
print(s1, s2)

# tupluri - similar cu o lista doar ca este immutable (nu mai poti modifica elem odata declarate)
t = (10, 20, 30, "ana", True)
print(t, t[3], type(t))
# t[0] = 20
# tuple()

# dictionare - perechi cheie valoare, efectiv corespondentul in python pt un JSON
# dict()
d = {
    "nume": "Ana",
    "nota": 10
}
print(d, type(d),
      d.keys(), type(d.keys()),
      d.values(), type(d.values()),
      d.items(), type(d.items()))

# list comprehensions & dict comprehensions
numere_pp = []
for each in range(20):
    if each % 2 == 0:
        numere_pp.append(each ** 2)
print(numere_pp)

numere_pp = [ x**2 for x in range(20) if x % 2 == 0 ]
print(numere_pp, type(numere_pp))

# dict comprehension
nume = ["Ana", "Andreea", "Alin"]
note = [10, 9.5, 9]
catalog = { k:v for k,v in zip(nume, note) }
print(catalog, type(catalog))

celsius = [10, -3, 5, 0, 12, 27]
# f = c * 9/5 + 32
fahrenheit = [round(c * 9/5 + 32, 1) for c in celsius]
print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)

# lambda, map, filter, reduce
# map(func, iterable)
secventa = (1,2,3,4)
result = map(lambda x: x**3, secventa)
print(result, type(result), list(result))

a = [1,2,3,4]
b = [10,20,30,40]
print(list(map(lambda x,y: x*y, a, b)))

# echivalent urmatoarele:
def ridicare_cub(x):
    return x**3

# private int ridicare_cub(int x) {
#     return x**3
# }

result = map(ridicare_cub, secventa)
print(result, type(result), list(result))

# filter(func, iterable)
result = filter(lambda c: c>=0, celsius)
print(result, type(result), list(result))

note = [3, 6, 7, 8, 2, 10]
promovat = [n for n in note if n >= 5]
status = ["promovat" if n >=5 else "restant" for n in note]
print(note, promovat, status)

emails = ["user@gmail.com", "user@yahoo.com", "user@stud.ase.ro"]
valid = list(filter(lambda e: e.endswith("ase.ro"), emails))
print("valid emails:", valid)

# reduce(func, iterable)
suma = reduce(lambda a,b : a+b, note)
print("Media notelor:", suma/len(note), sum(note)/len(note))

# numpy
# numpy ofera un obiect numit ndarray, care spre deosebire de listele built-in garanteaza un tip de data unic la nivel
# array, stocheaza datele in zone de memorie continue si permite operatii de tip SIMD

a = np.array([1,2,3], dtype='int16')
b = np.array([
    [3.2, 5.6],
    [3.2, 1.2],
    [7.8, 9.2]
])
print("a: \n", a)
print("b: \n", b)

# proprietati
print("Forma (shape): ", a.shape, b.shape)
print("Numar dimensiuni (no of dimensions):", a.ndim, b.ndim)
print("Tip de data (data type):", a.dtype, b.dtype)
print("Dim unui elem (item size) in bytes: ", a.itemsize, b.itemsize)
print("Numar elemente (size):", a.size, b.size)
print("Dimensiune totala in memorie in bytes:", a.nbytes, b.nbytes)

# indexing si slicing
l1 = [1,2,3,4,5]
a = np.array([1,2,3,4,5])
b = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])

# indexing - accesarea de elemente pe baza de index, folosind operatorul []
print("citire elem din list:", l1[0], l1[len(l1) - 1]) # index out of range: l1[len(l1) + 100])
l1[0] = 10
print("accesare urmata de citire elem din list:", l1[0], l1)
l1[0] = 1

a[0] = 11
b[0][0] = 111
b[1,1] = 888
print("citire folosind operatorul de indexare dintr-un ndarray", a[0], a[3], b[1][1], b[0, 4])

# slicing - [ start index : end index : step (size) ]
print(l1[0:len(l1)])  # <=> l1[0:5]  1,2,3,4,5
print(l1[0:5])   # 1,2,3,4,5
print(l1[0:len(l1)-1])  # 1,2,3,4
print(l1[0:100]) # 1,2,3,4,5
print(l1[0:]) # 1,2,3,4,5
print(l1[:len(l1)])  # 1,2,3,4,5
print(l1[1:len(l1)-1]) # 2,3,4
print(l1[2:3]) # 3
print(l1[::2]) # 1,3,5
print(l1[1:-1:2]) # 2,4
print(l1[::-1]) # 5,4,3,2,1


b = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])

print(b[0, 1:-1])  # 2,3,4
print(b[0, 1:-1:2])  # 2,4
print(b[0, ::2])  # 1, 3, 5
print(b[0, :])  # 1,2,3,4,5
print(b[:, 3])  # 4, 9
print(b[:-1, 3])  # 4

# matrice predefinite
print("Zeros:\n", np.zeros(3), "\n", np.zeros((3,3)))
print("Ones:\n", np.ones(3), "\n", np.ones((2,2), dtype='int8'))
print("Full:\n", np.full((2,2), 100))
print("Random values:\n", np.random.rand(3,2))
print("Random integer values:\n", np.random.randint(-50, 50, size=(4,4)))
print("Identity:\n", np.identity(4))

# repeat (repeta elementul de n ori) vs tile (copy paste asa cum il stim)
a = np.array([1,2,3])
print("Tile:", np.tile(a, 3))
print("Repeat:", np.repeat(a, 3))

# shallow vs deep copy
b = a
c = a.copy()

b[0] = 10
c[0] = 100
print("A:", a)
print("B:", b)
print("C:", c)

# performanta
start = time.time()
a = np.arange(1, 1_000_001)  # 1_000_001 <=> 1000001 <=> la nivel conceptual 1.000.001
ap = a ** 2
durata = time.time() - start

start_lst = time.time()
b = [i ** 2 for i in range(1_000_001)]
# bp = [i ** 2 for i in b]
durata_lst = time.time() - start_lst

print(f"Performanta: Numpy - {durata:.5f} | Python - {durata_lst:.5f}")

# broadcasting
# broadcast simplu - inmultire a unui array cu un scalar
# broadcast complex - inmultirea elem cu elem a arrays

a = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])
print("Broadcast simplu:\n", a * 2)

b = np.array([
    [1,2],
    [3,4]
])
c = np.array([
    [10,20],
    [30,40]
])

print("Broadcast complex - inmultire elem cu elem:\n", b * c)
print("Inmultirea matematica a matricelor:\n", b @ c)

