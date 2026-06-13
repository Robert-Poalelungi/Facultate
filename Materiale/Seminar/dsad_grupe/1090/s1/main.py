# liste
temperaturi = [20, -3, 0, 7, 22]
print("lista", temperaturi, type(temperaturi))
# temperaturi = True
# print(type(temperaturi), temperaturi)
print("primul elem:", temperaturi[0])
print("ultimele 2 elem", temperaturi[-2:])

# tupluri
coordonate = (21, 45)
print("tuplu", coordonate, type(coordonate))
# coordonate[0] = 30

# dictionar
student = {
    "nume": "Ana",
    "nota": 10
}
print(student["nume"], student.get("nota"))

# seturi
litere = {"analiza datelor"}
litere_2 = set("analiza datelor")
# x = tuple()
# y = dict({"nume": "Ana", "nota": 10})
# z = list()
print(litere, type(litere))
print(litere_2, type(litere_2))