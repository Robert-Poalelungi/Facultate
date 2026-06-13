# liste
temperaturi = list(15, -3 , 22, 0, 7) #[15, -3 , 22, 0, 7]
print("lista:", temperaturi, type(temperaturi))
print("primul elem", temperaturi[0])
print("ultimele 2 elem", temperaturi[-2:])
print("lista mai putin ultimele 2 elem", temperaturi[:-2])

# tupluri
coordonate = (21, 45)
# coordonate[0] = 22
print("tupluri", coordonate, type(coordonate))

# dictionare
student = {"nume": "Ana", "nota": 10}
print(student["nume"], student.get("nota"))

#seturi
litere = set("analiza datelor")
print(litere)