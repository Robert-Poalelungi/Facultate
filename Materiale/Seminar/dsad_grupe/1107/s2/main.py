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



