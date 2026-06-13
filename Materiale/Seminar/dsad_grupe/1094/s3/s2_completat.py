from functools import reduce
import numpy as np
import time

# comprehensions list si dict
numere = []
for each in range(20):  # metoda built-in care intoarce un set de numere intregi cuprins intre [0:19]
    if each % 2 == 0:
        numere.append(each ** 3)
print(numere)

# blocul de mai sus este echivalent cu randul urmator:
numere = [x ** 3 for x in range(20) if x % 2 == 0]
# un comprehension se compune din 3 blocuri:
# - primul: for x in range(20) - blocul iterativ - mereu prezent
# - al doilea bloc (in dreapta for): if x % 2 == 0 - blocul de filtrare
# - al treilea bloc (in stanga for): x ** 3 - blocul de transformare - mereu prezent

celsius = [10, -5, 3, 17, 0, 20, 19]
# f = c * 9/5 + 32
# in exemplul de mai jos avem de a face cu o mapare a datelor din celsius in fahrenheit folosind list comprehension
fahrenheit = [round(c * 9 / 5 + 32, 1) for c in celsius]
print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)

# in exemplul de mai jos avem de a face cu o filtrare a datelor folosind list comprehension
temp_pozitive = [c for c in celsius if c >= 0]
print(temp_pozitive)

note = [3, 6, 7, 5, 4, 10, 9]
status = ["promovat" if n >= 5 else "restant" for n in note]  # diferit de ["promovat" for n in note if n >= 5]

# dict comprehension
nume = ["Ana", "Andreea", "Alin"]
note_dict = [10, 9.2, 9.6]
catalog = {my_key: my_value for my_key, my_value in zip(nume, note_dict) if my_value > 9.5}
print(catalog, type(catalog),
      catalog.keys(), type(catalog.keys()),
      catalog.values(), type(catalog.values()),
      catalog.items(), type(catalog.items()))

# lambda, map, filter, reduce

# s1 = {1, 2, 3, 4}
# s2 = set((1, 2, 3, 4))
#
# s3 = {"analiza datelor"}
# s4 = set("analiza datelor")
# print(s1, s2, s3, s4)

secventa = (1, 2, 3, 4)
# map(func, iterable)
result = map(lambda x: x ** 3, secventa)
print(result, type(result), list(result))


# blocul de mai sus este echivalent ca functionalitate cu urmatoarele randuri:
def ridica_la_cub(x):
    return x ** 3


result = map(ridica_la_cub, secventa)
print(result, type(result), list(result))

a = [1, 2, 3]
b = [10, 20, 30]
c = [5, 15, 25]
result = map(lambda x, y, z: x * y * z, a, b, c)
print(list(result))

# filter(func, iterable)
result = filter(lambda c: c >= 0, celsius)
print(result, type(result), list(result))

emails = ["user@gmail.com", "user@yahoo.com", "user@stud.ase.ro"]
valid = list(filter(lambda e: e.endswith('ase.ro'), emails))
print(valid)

# reduce(func, iterable)
suma = reduce(lambda a, b: a + b, note)
print("Media notelor:", suma / len(note), sum(note) / len(note))

# numpy
# numpy ofera un obiect de tip ndarray (N-dimensional array)
# 1D: [1, 2, 3] => reprezentarea in memorie nu e de forma 1 rand si 3 coloane, ci 3 randuri si 1 coloana
#  --         --
# |     1      |
# |     2      |
# |     2      |
# --         --

# 2D: matrice ca la matematica
# (3, 2)
#  --         --
# |   2   5    |
# |   3   6    |
# |   4   7    |
# --         --

# in memorie listele built-in nu sunt reprezentate in forma continua
# |__1_|__3_|___|___|__ana_|___|___|___|__True_|___|___|___|___|
# un ndarray forteaza acelasi tip de data pentru toate elementele din colectie, deci pot avea aritmetica de pointeri
# si nu mai trebuie sa verific la runtime tipul fiecarui element
# in plus, implementarea de ndarray este scrisa in C
# si permite operatii de timp SIMD (Single Instruction Multiple Data)
# |__1_|__3_|__4_|__6_|__2_|__9_|__11_|

l1 = [1, 3, "ana", True, None, 3.14, [4, 5]]
print(l1, l1[3])

a = np.array([1, 2, 3], dtype='int8')
b = np.array([
    [3.2, 6.7],
    [1.8, 9.4],
    [3.3, 7.8]
])
print("a: \n", a)
print("b: \n", b)

# proprietati
print("Shape (forma):", a.shape, b.shape)  # (3,) <=> (3,1)
print("No of Dimensions (numar dimensiuni):", a.ndim, b.ndim)
print("Data type (tip de data):", a.dtype, b.dtype)
print("Item size (dimensiunea unui elem in bytes):", a.itemsize, b.itemsize)
print("Size (numar elemente):", a.size, b.size)
print("No of bytes (dimensiune totala in memorie):", a.nbytes, b.nbytes)

# indexing si slicing
# indexing [idx]
c = [1, 2, 3, 4, 5]
print(c[0], c[len(c) - 1], c[3])  # , c[len(c)])

# slicing [ start idx : end idx : step ]
print(c[0: len(c) - 1])  # 1,2,3,4
print(c[0: len(c)])  # 1,2,3,4,5
print(c[0: len(c) + 100])  # 1,2,3,4,5
print(c[::2])  # 1, 3, 5
print(c[::-1])  # 5, 4, 3, 2, 1

# indexing in numpy
a = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])

print(a[1, 2], a[1][2])  # 8
a[0, 0] = 20
print(a[0, 0])

# slicing in numpy
a = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])
print(a[0, 1:-1])  # 2,3,4
print(a[0, 1:-1:2])  # 2,4
print(a[0, ::2])  # 1,3,5
print(a[0, :])  # 1,2,3,4,5
print(a[:, 3])  # 4, 9
print(a[:-1, 3])  # 4

# matrice predefinite in numpy
print("Zeros: \n", np.zeros(3), np.zeros((2, 2)))
print("Ones: \n", np.ones((2, 2), dtype='int32'))
print("Full: \n", np.full((3, 2), 100))
print("Random: \n", np.random.rand(3, 4))
print("Random integer: \n", np.random.randint(-100, 100, size=(3, 3)))
print("Identity: \n", np.identity(4))

# repeat (repeta fiecare elem din ndarray de n ori) vs tile (comportament de tip copy-paste)
a = np.array([1,2,3])
print("Tile: ", np.tile(a, 3))
print("Repeat: ", np.repeat(a, 3))

# shallow vs deep copy
b = a
c = a.copy()
b[0] = 10
c[0] = 20
print("A:", a)
print("B:", b)
print("C:", c)

# performanta
start = time.time()
a = np.arange(1, 1_000_001)  # 1_000_001 <=> (la nivel conceptual) 1.000.001 <=> 1000001
a ** 2
end = time.time()
duration = end - start

start_lst = time.time()
lst = [i**2 for i in range(1_000_001)]
# lst_p = [i ** 2 for i in lst]
end_lst = time.time()
duration_lst = end_lst - start_lst

print(f"Rezultate performanta:\nNumpy: {duration:.5f}  \nPython: {duration_lst:.5f}   \n{duration_lst/duration}")

# broadcasting
# broadcast simplu: inmultirea unui nrarray cu un scalar
# broadcast complex: inmultirea elem cu elem a valorilor din ndarrays (element-wise)

a = np.array([
    [1,2,3],
    [4,5,6]
])
print("Broadcast: \n", a * 2)

b = np.array([
    [1,2],
    [3,4]
])
c = np.array([
    [10, 20],
    [30, 40]
])

print("Broadcast elem-wise:\n", b * c)
print("Inmultirea matematica a matricelor:\n", b @ c)

x = np.array([
    [1,2],
    [3,4],
    [5,6]
])
y = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
z = np.array([1,2,3]) # (3,)
v = np.array([1,2]) # (2,)
# (3,2) * (3,3)
# print(x * y)
print(v * y)