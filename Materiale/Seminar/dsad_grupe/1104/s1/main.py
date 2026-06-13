# lists

temperatures = [15, 22, -3, 0, 7]
x = [0, True, [3, 4,], {"ana"}, 5]
print("list", temperatures, type(temperatures), x)
# temperatures = True
# print(temperatures, type(temperatures))
print("first element:", temperatures[0], temperatures[2],
      temperatures[len(temperatures) - 1])
print("last 2 elements:", temperatures[-2:])
print("test", temperatures[1: 5])

# tuples
values = (20, 30, 40)
# values[0] = 50

# dictionaries
student = {
    "name": "Ana",
    "grade": 10
}
print(student["name"], student.get("grade"))

# sets
letters = {"analiza datelor"}
letters_2 = set("analiza datelor")
list()
tuple()
dict()
print(letters, type(letters))
print(letters_2, type(letters_2))