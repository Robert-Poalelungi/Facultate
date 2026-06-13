from functools import reduce
import time
import numpy as np


# list comprehensions
numbers = []
for each in range(20):  # built-in method that returns a sequence of integers [0 : 19]
    if each % 2 == 0:
        numbers.append(each ** 3)
print(numbers)

# code block above is equivalent to:
numbers = [x ** 3 for x in range(20) if x % 2 == 0]
print(numbers)

# comprehensions in general are composed of 3 parts:
# 1st is the iteration: for x in range(20) - it is mandatory
# 2nd is the filtration: if x % 2 == 0 => on the right hand side of the iteration
# 3rd is the transformation/mapping: x ** 3 - it is mandatory => on the left hand side of the iteration

celsius = [10, -5, 3, -7, 19, 18, 22, 21]
# f = c * 9/5 + 32
fahrenheit = [round(c * 9 / 5 + 32, ndigits=2) for c in celsius]
print(celsius, fahrenheit)

# dict comprehensions
names = ["Ana", "Andreea", "Alin"]
grades = [10, 9.6, 9.2]
gradebook = {my_key + "_graded": my_value + 1 for my_key, my_value in zip(names, grades) if my_value > 9.5}
print(gradebook)

# list()
# set()
# dict()
# tuple()
#
# l1 = [1,2,3]
# l2 = list((1,2,3))
# l3 = list("ana")
# print(l1,l2,l3, type((1,2,3)))
#
# s1 = {"analiza datelor", 1, 2}
# s2 = set(("analiza datelor", 1, 2))
# print(s1, s2)


# lambda, map, filter, reduce
sequence = (1,2,3,4)

# map(func, iterable)
result = map(lambda x: x**3, sequence)
print(result, type(result), list(result))


# equivalent to:
def raise_to_power3(x):
    return x ** 3


result = map(raise_to_power3, sequence)
print(result, type(result), list(result))

a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
c = [2, 4, 6, 8]
result = map(lambda x, y, z: (x + z) * y, a, b, c)
print(result, list(result))

# filter(func, iterable)
result = filter(lambda c: c >= 0, celsius)
print(result, type(result), list(result))

# [x for x in celsius if x >= 0]

grades = [2, 5, 8, 10, 3, 8]
status = ["passed" if g >= 5 else "failed" for g in grades]
# different from: status = ["passed" for g in grades if g >= 5]
print(status)

emails = ["user@gmail.com", "user@yahoo.com", "user@stud.ase.ro"]
valid = filter(lambda e: e.endswith("ase.ro"), emails)
print(list(valid))

# reduce(func, iterable)
sum_of_grades = reduce(lambda a, b: a+b, grades)
print("Average grade:", sum_of_grades/len(grades), sum(grades)/len(grades))

# numpy
# numpy provides an object of type ndarray - n dimensional array, which is written in C
# 1D: [1, 2, 3]
# 2D: --            --
#     |   5    6     |
#     |   7    8     |
#     --           --

# built-in python lists are not represented in memory in continuous areas
# |_1_|_2_|__|__|_True_|__|__|__|__|_ana_|__|
l1 = [1, 2, True, None, "ana", 3.14, [5,6]]
print(l1)

# ndarray object enforces the same data type for all the elements in the collection
# ndarray content is represented in memory in continuous areas
# |_1_|_2_|_3_|_4_|_5_|_6_|_7_|_8_|_9_|
# ndarray allows SIMD (Single Instruction Multiple Data)

a = np.array([1,2,3], dtype='int8')
b = np.array([
    [1.2, 5.6],
    [3.4, 7.8],
    [7.7, 5.1]
])

print("a: \n", a)
print("b: \n", b)

# properties
print("Shape", a.shape, b.shape)  # (3,) <=> (3,1)
print("No. of dimensions", a.ndim, b.ndim)
print("Data type", a.dtype, b.dtype)
print("Item size (bytes)", a.itemsize, b.itemsize)
print("Size", a.size, b.size)
print("Total size (bytes)", a.nbytes, b.nbytes)

# predefined ndarrays
print("Zeros:\n", np.zeros(3), np.zeros((2,3)))
print("Ones:\n", np.ones((3,3)))
print("Full:\n", np.full((2,2), 100))
print("Random:\n", np.random.rand(2,2))
print("Random integers:\n", np.random.randint(-50, 50, (3,5)))
print("Identity:\n", np.identity(3))

# indexing and slicing
a = np.array([1,2,3])
# indexing = accessing values using an index. the indexing operator is []
print(a[0], a[2], a[a.size - 1], a[len(a)-1])
a[0] = 10

# slicing - take a subset of the entire collection
print(a, a[::2], a[::-1], a[::-2], a[1:-1])

b = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])
# indexing
print(b[0][0], b[0 , 0], b[1,4])
b[0,0]=100
print(b)
b[0,0] = 1

b = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])
# slicing
print(b[0, 1:-1]) # 2,3,4
print(b[0, 1:-1:2]) # 2,4
print(b[0, ::2]) # 1,3,5
print(b[0, :]) # 1,2,3,4,5
print(b[:, 3]) # 4,9
print(b[:-1, 3]) # 4

# tile (repeat the entire structure n time - copy/paste) vs repeat (repeat each element in the ndarray for n times)
a = np.array([1,2,3])
print("Tile: ", np.tile(a, 3))
print("Repeat: ", np.repeat(a, 3))

# shallow vs deep copy
b = a
c = a.copy()
b[0] = 10
c[0] = 100
print("A: ", a)
print("B: ", b)
print("C: ", c)

# performance
# numpy
start = time.time()
a = np.arange(1, 1_000_001) # 1_000_001 <=> 1000001 <=> (conceptually equivalent to) 1.000.001
a ** 2
end = time.time()
duration = end - start

# python
start_lst = time.time()
lst = [i**2 for i in range(1, 1_000_001)]
# lstp = [i ** 2 for i in lst]
end_lst = time.time()
duration_lst = end_lst - start_lst

print(f"Performance res: \nNumpy: {duration}\nPython: {duration_lst}\nResult: {duration_lst/duration}")

# broadcasting
# simple broadcast: multiplying an array with a scalar value
# complex broadcast: multiplying arrays element-wise

a = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])
print("Broadcast: \n", a * 2)

b = np.array([
    [1,2],
    [3,4]
])
c = np.array([
    [10,20],
    [30,40]
])
print("Broadcast - element wise:\n", b * c)
print("Mathematical matrix multiplication: \n", b @ c)

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
z = np.array([1,2,3])
v = np.array([1,2])
# print(x * y)
print(z * y)
# print(v * y)







