# list comprehensions
from functools import reduce
import time
import numpy as np

numere = []
for each in range(20):  # metoda built-in care intoarce o secventa de numere intregi in intervalul inchis [0:19]
    if each % 2 == 0:
        numere.append(each ** 3)
print(numere)

numere = [each ** 3 for each in range(20) if each % 2 == 0]
# orice comprehension se compune din 3 parti
# prima parte - iteratia: for each in range(20) - obligatorie
# a doua parte - filtrarea: if each % 2 == 0 - sta mereu in dreapta zonei de iteratie, optionala
# a treia parte - translatare/mapare: each ** 3 - sta mereu in stanga zonei de iteratie, obligatorie

celsius = [10, -5, -3, 7, 9, 11, 26, 29]
# f = c * 9/5 + 32
fahrenheit = [round(c * 9 / 5 + 32, 1) for c in celsius]
print(celsius, fahrenheit)

temp_pozitive = [t for t in celsius if t >= 0]
print(temp_pozitive)

# dict comprehensions
nume = ["Ana", "Andreea", "Alin"]
note = [10, 9.6, 9.2]
catalog = {my_key + "_corectat": my_value + 1 for (my_key, my_value) in zip(nume, note) if my_value >= 9.5}

print(catalog, type(catalog),
      catalog.keys(), type(catalog.keys()),
      catalog.values(), type(catalog.values()),
      catalog.items(), type(catalog.items()))


# l1 = [1,2,3]
# l2 = list((1,2,3))
# l3 = list("ana")
# print(l1, l2, l3, type((1,2,3)))
#
# s1 = {"analiza datelor", 1, 2}
# s2 = set(["analiza datelor", 1, 2])
# print(s1,s2)
#
# list()
# set()


# lambda, map, filter, reduce
# map(func, iterable)
secventa = (1,2,3,4)
result = map(lambda x: x ** 3, secventa)
print(result, type(result), list(result))

# blocul de cod de mai sus este echivalent cu urmatorele randuri:


def ridicare_la_cub(x):
    return x**3


result = map(ridicare_la_cub, secventa)
print(result, type(result), list(result))

a = [1,2,3,4]
b = [10,20,30,40]
c = [5,15,25,35]
result = map(lambda x,y,z: (x+z) * y, a, b, c)
print(list(result))

note = [3, 5, 6, 2, 10, 8]
status = ["promovat" if n >=5 else "restant" for n in note]
print(status)

# diferita de ["promovat" for n in note if n >=5]

# filter(func, iterable)
celsius = [10, -5, -3, 7, 9, 11, 26, 29]
result = filter(lambda c: c >= 0, celsius)
print(result, type(result), list(result))

emails = ["user@gmail.com", "user@yahoo.com", "user@stud.ase.ro"]
valid = filter(lambda e: e.endswith("ase.ro"), emails)
print(list(valid))

# reduce(func, iterable)
suma = reduce(lambda a, b: a+b, note)
print("Media notelor:", suma/len(note), sum(note)/len(note))

# numpy
# numpy ofera un obiect numit ndarray (N dimensional array) care este scris in C si care spre deosebire de listele built-in ofera cateva avantaje
# 1D: [1, 2, 3]
# 2D
# 3D
l1 = [1, 2, True, "ana", None, [3.14, 6.78]]
# |_1_|_2_|__|__|_True_|__|__|__|_ana_|__|__|
# |_1_|_2_|_3_|_4_|_5_|   * 2
# listele built-in din python nu sunt reprezentate in memorie in zone continue si ca atare nu poti aplica aritmetica de pointeri
# ndarray forteaza acelasi tip de data pentru toate elementele din colectie, acestea sunt stocate in memorie in zone continue
# obiectele de tip ndarray permit SIMD (Single Instruction Multiple Data)

a = np.array([1,2,3], dtype='int8')
b = np.array([
    [3.1, 4.5],
    [3.7, 7.8],
    [4.3, 5.6]
])

print("a: \n", a)
print("b: \n", b)

# proprietati
print("Shape (forma):", a.shape, b.shape)  # (3,) <=> (3,1)
print("No. of dimensions (numar dimensiuni)", a.ndim, b.ndim)
print("Data type (tip de data):", a.dtype, b.dtype)
print("Item size (dimensiune elem in memorie in bytes):", a.itemsize, b.itemsize)
print("Size (numar elem):", a.size, b.size)
print("No. of bytes (dimensiune totala in memorie in bytes):", a.nbytes, b.nbytes)

# indexing si slicing
# indexing - accesare de elemente folosind un index
c = [1,2,3,4,5]
c[1] = 7
print(c[0], c[2], len(c), c[len(c)-1], c[1])

# slicing [start idx : end idx : step]
print(c[0:4], c[0: len(c)-1], c[0:len(c)], c[1:len(c) + 100])

# indexing:
a = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])

print(a[0,3], a[0][3])  # 4
a[0,3] = 20
print(a[0,3], a[0][3])  # 20

# slicing:
a = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])
print(a[0, 1:-1])  # 2,3,4
print(a[0, 1:-1:2])  # 2, 4
print(a[0, ::2])  # 1, 3, 5
print(a[0, :])  # 1,2,3,4,5
print(a[:, 3])  # 4, 9
print(a[:-1, 3])  # 4