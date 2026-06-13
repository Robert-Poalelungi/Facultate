# liste
temperaturi = [20, 10, -3, 0, 12]
print("lista", temperaturi, type(temperaturi))
# temperaturi = True
# print(temperaturi, type(temperaturi))
print("primul elem:", temperaturi[0], temperaturi[2],
      temperaturi[len(temperaturi) - 1])
print("ultimele 2 elem", temperaturi[-2:])

# tuplu
valori = (10, 20 ,30 ,40)
# valori[0] = 100

# dictionar
student = {
    "nume": "Ana",
    "nota": 10
}
print(student["nume"], student.get("nota"))

# set
litere = {"analiza datelor"}
litere_2 = set("analiza datelor")
# dict()
# list()
# tuple()
print(litere, type(litere))
print(litere_2, type(litere_2))