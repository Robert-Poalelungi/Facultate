import numpy as np
import time

# built-in collections
# lists
temperatures = [10, -3, 20, 17, 0]
# type - built-in method that tells you what data type the parameter has at runtime
# len - built-in method that tells you the size/length of the collection
print(temperatures, type(temperatures))

# indexing - accessing elements in the list using an index
print(temperatures[0], temperatures[len(temperatures)-1])
temperatures[0] = 15
print(temperatures[0])

# slicing [start index : end index : step] - extracting a subset of the initial collection
print(temperatures[0:len(temperatures)])
# line 14 is equivalent to this
print(temperatures, temperatures[:])

print(temperatures[1:4])

# discussion about index out of bound and collection limits
#   |___|___|___|___|___|___|___|____|___|____|____________|
# c: 1   2    3  b:   a   n   a
# c[4]
# print(temperatures[1:14], temperatures[14])

print(temperatures[:-1], temperatures[1:-3])
print(temperatures[-4:])

print(temperatures[1:-1:2])
print(temperatures[::2])
print(temperatures[::-1])  # reading the list backwards

# tuple
t1 = (1,2,3)
print(t1, type(t1))
# t1[0] = 20
t2 = tuple((1,3,4))

# sets
s1 = {1,2,3, 1}
print(s1, type(s1))
s2 = set([1,2,3,1])
print(s2, type(s2))

s3 = {"analiza datelor", 1, True, None}
s4 = set("analiza datelor")
print(s3, type(s3), s4, type(s4))

# dictionaries
d = {
    "name": "Ana",
    "grade": 10
}
d["name"] = "Andreea"
d["faculty"] = "CSIE"
print(d, type(d),
      d["name"], d["grade"], d.get("name"),
      d.keys(), type(d.keys()), d.values(), d.items())

# comprehensions
numbers = []
for each in range(20):  # range is a built-in function that would return a list of integer numbers starting from 0 up to the limit - 1
    if each % 2 == 0:
        numbers.append(each ** 2)
print(numbers)

# equivalent to this syntax using list comprehension
numbers = [x ** 2 for x in range(20) if x % 2 == 0]
# [x ** 2 for x in range(20) if x % 2 == 0] => might be split in 3 sections:
# 1st: for x in range(20) - iteration part
# 2nd: the right-side part - filter
# 3rd: the left-side part - data transformation

celsius = [10, -5, 20, 3, 17, 0]
# f = c * 9/5 + 32
fahrenheit = [round(c * 9/5 + 32, 1) for c in celsius]
print(celsius, fahrenheit)

# dict comprehension
names = ["Ana", "Andreea", "Alin"]
grades = [10, 9.5, 9]
gradebook = {my_key: my_value for my_key, my_value in zip(names, grades)}
print(gradebook)

grades = [3, 6, 4, 7, 8, 10, 9]
status = ["passed" if g >=5 else "failed" for g in grades]
print(grades, status)

# functional features: lambda, map, filter, reduce
seq = (1,2,3,4,5)
# map(func, iterable)

# equivalents:
def raise_to_3(x):
    return x**3
result = map(raise_to_3, seq)

result = map(lambda x: x**3, seq)
print(result, type(result), list(result))

# filter(func, iterable)
positive_temp = filter(lambda x: x >= 0, celsius)
print(positive_temp, type(positive_temp), list(positive_temp))

# reduce
from functools import reduce
sum_of_grades = reduce(lambda a,b: a+b, grades)
print("Mean of grades:", sum_of_grades/len(grades), sum(grades)/len(grades))

# numpy
# in built-in lists in python data is stored in memory in discontinuous manner
# numpy forces that all the elements in the ndarray have the same data type, and they are stored in continuous regions in memory
# the ndarray object is written in C and allows execution of SIMD operations (Single Instruction Multiple Data)

a = np.array([1,2,3], dtype='int8')

b = np.array([
        [3.2, 6.7],
        [1.2, 7.8],
        [9.3, 4.4]
])

print(a)
print(b)

# properties
print("Shape:", a.shape, b.shape)
print("No of dimensions:", a.ndim, b.ndim)
print("Item size:", a.itemsize, b.itemsize)
print("No of elements:", a.size, b.size)
print("Data type:", a.dtype, b.dtype)
print("Total size in memory in bytes:", a.nbytes, b.nbytes)

# indexing and slicing
l1 = [1,2,3,4,5]
a = np.array([1,2,3,4,5])
b = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])

# indexing - reading or accessing values using the index. operator for indexing is []
print(l1[0], l1[4], l1[len(l1)-1])
l1[0] = 10
print(l1)

print(a[0], a[2], a[a.size - 1], a[len(a) - 1])
print(b[0][0], b[1][3], b[0, 0], b[1, 3])
a[0] = 100
b[1,3] = 200
print(a, b)
l1[0] = 1
a[0] = 1
b[1,3] = 9

# slicing - taking a subset of the entire collection - operator for slicing is again []
# [ start index : end index : size/step ]
print(l1[0 : 3])  # 1,2,3
print(l1[3 : len(l1)])  # 4,5
print(l1[3 : len(l1)-1])  # 4
print(l1[:5]) # 1,2,3,4,5
print(l1[0:]) # 1,2,3,4,5
print(l1[:])  # 1,2,3,4,5
print(l1[::2])  # 1, 3, 5
print(l1[0:5:2]) # 1,3,5
print(l1[2:5:2]) # 3, 5
print(l1[2:4:2]) # 3
print(l1[::-1])  # 5,4,3,2,1
print(l1[-3:]) # equivalent to l1[len(l1)-3]  # 3,4,5
print(l1[-3:-1]) # 3,4

print(b[0, 1:-1])  # 2,3,4
print(b[0, 1:-1:2]) # 2,4
print(b[0, ::2])  # 1,3,5
print(b[0, :]) # 1,2,3,4,5
print(b[:, 3]) # 4, 9
print(b[:-1, 3]) # 4

# predefined ndarrays
print("Zeros: \n", np.zeros(3), np.zeros((3,2)))
print("Ones:\n", np.ones((2,3), dtype='int8'))
print("Full:\n", np.full((3,4), 100))
print("Random:\n", np.random.rand(2,2))
print("Random integers:\n", np.random.randint(-50,50,(3,4)))
# also valid: print("Random integers:\n", np.random.randint(size=(3,4), high=50, low=-50))
print("Identity:\n", np.identity(5))

# tile (copy-paste behavior) vs repeat (repeating each element for n times)
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

# performance
start = time.time()
a = np.arange(1, 1_000_001) # 1_000_001 <=> at least conceptually with 1.000.001 <=> 1000001
a ** 2
end = time.time()
duration = end - start

start_lst = time.time()
lst = [i for i in range(1_000_001)]
lst_s = [i ** 2 for i in lst]
end_lst = time.time()
duration_lst = end_lst - start_lst

print(f"Performance results:\nNumpy: {duration:.5f} \nPython: {duration_lst:.5f} \n{duration_lst/duration}")




