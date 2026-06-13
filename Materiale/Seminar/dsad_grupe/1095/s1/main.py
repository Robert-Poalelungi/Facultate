# liste
temperaturi = [15, -3, 22, 0 ,7]
print("lista: ", temperaturi, type(temperaturi))
print("primul elem: ", temperaturi[0])
print("ultimele 2 elem:", temperaturi[-2:])

# tupluri
coordonate = (21, 45)
# coordonate[0] = 6

# dictionare
student = { "nume": "Ana", "nota": 9.5 }
print(student["nume"], student.get("nota"))

# seturi
litere = set("analiza datelor")
print("seturi: ", litere)

# comprehensions
celsius = [10, -5, 0, 20, 25]
fahrenheit = [round(c * 9/5 + 32, 1) for c in celsius]
print("C: ", celsius)
print("F: ", fahrenheit)

# filtrare folosind comprehensions
pozitive = [ x for x in celsius if x >= 0]
print("temp poz:", pozitive)

from functools import reduce

fahrenheit2 = list(map(lambda c: c * 9/5 + 32, celsius))
print(fahrenheit2)

filterpoz = list(filter(lambda c: c >=0, celsius))
print(filterpoz)

suma = reduce(lambda a,b : a+b, filterpoz)
medie = suma / len(filterpoz)
print("media temp poz", medie)




