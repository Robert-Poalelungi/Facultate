# liste
temperaturi = [15, -3, 20, 0, 7]
print("lista: ", temperaturi, type(temperaturi))
# temperaturi = True
# print(type(temperaturi))
print("primul elem:", temperaturi[0])
print("ultimul elem:", temperaturi[len(temperaturi) -1])
print("ultimele 2 elem:", temperaturi[-2:])

# tupluri
coordonate = (21, 45)
# coordonate[0] = 230

# dictionare
student = {"nume": "Ana", "nota": 10}
print(student["nume"], student.get("nota"))

# seturi
lit = {"analiza datelor"}
litere = set("analiza datelor")
print(lit, type(lit), litere, type(litere))