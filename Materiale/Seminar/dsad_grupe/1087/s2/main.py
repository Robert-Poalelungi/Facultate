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