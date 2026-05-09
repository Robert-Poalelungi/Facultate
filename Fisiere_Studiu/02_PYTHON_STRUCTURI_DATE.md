# Python — Structuri de Date, Funcții, Comprehensions
## Ghid complet pentru examen (grile + output prediction)

---

## 1. TIPURI DE DATE FUNDAMENTALE

### 1.1 Numere
```python
x = 10        # int
y = 3.14      # float
z = 2 + 3j    # complex

# Operatori aritmetici
10 / 3   # → 3.3333...  (împărțire reală, returnează FLOAT întotdeauna)
10 // 3  # → 3          (împărțire întreagă, returnează INT)
10 % 3   # → 1          (rest/modulo)
2 ** 3   # → 8          (putere)

# CAPCANA: 10 / 2 → 5.0 (FLOAT, nu INT!)
```

### 1.2 String-uri
```python
s = "Hello"
s = 'World'
s = """multi
linie"""

# Indexare (0-based)
s = "Python"
s[0]   # → 'P'
s[-1]  # → 'n'   (ultimul element)
s[-2]  # → 'o'

# Slicing: [start:stop:step]  — stop este EXCLUSIV
s[0:3]   # → 'Pyt'
s[1:4]   # → 'yth'
s[:3]    # → 'Pyt'  (de la început)
s[3:]    # → 'hon'  (până la sfârșit)
s[::-1]  # → 'nohtyP'  (inversat)
s[::2]   # → 'Pto'

# Metode string esențiale
"hello".upper()          # → 'HELLO'
"HELLO".lower()          # → 'hello'
"hello world".title()    # → 'Hello World'
" hello ".strip()        # → 'hello'
" hello ".lstrip()       # → 'hello '
" hello ".rstrip()       # → ' hello'
"hello".replace("l","L") # → 'heLLo'  (înlocuiește TOATE)
"a,b,c".split(",")       # → ['a', 'b', 'c']
"-".join(["a","b","c"])  # → 'a-b-c'
"hello".find("l")        # → 2  (primul index, -1 dacă nu există)
"hello".count("l")       # → 2
"hello".startswith("he") # → True
"hello".endswith("lo")   # → True
len("hello")             # → 5

# f-strings
name = "Ana"
f"Buna {name}"           # → 'Buna Ana'
f"{3.14159:.2f}"         # → '3.14'
```

---

## 2. LISTE (list) — MUTABLE

Lista este **ordonată, modificabilă, permite duplicate**.

```python
lst = [1, 2, 3, 4, 5]
lst = [1, "text", 3.14, True]  # tipuri mixte OK

# Indexare și slicing — identic cu string
lst[0]    # → 1
lst[-1]   # → 5
lst[1:3]  # → [2, 3]

# Metode MUTABILE (modifică lista IN PLACE, returnează None!)
lst.append(6)        # adaugă la SFÂRȘIT, return None
lst.insert(1, 99)    # insert(poziție, valoare)
lst.extend([7, 8])   # adaugă mai multe elemente
lst.remove(3)        # șterge PRIMA apariție a valorii 3
lst.pop()            # șterge și returnează ultimul element
lst.pop(0)           # șterge și returnează elementul de la index 0
lst.sort()           # sortare ascendentă, IN PLACE, return None
lst.sort(reverse=True)  # sortare descendentă
lst.reverse()        # inversare IN PLACE, return None
lst.clear()          # golește lista
lst.index(2)         # returnează indexul primei apariții a lui 2
lst.count(2)         # numărul aparițiilor lui 2
lst.copy()           # copie superficială

# Funcții built-in
len(lst)             # lungime
sum(lst)             # sumă (doar numere)
min(lst)             # minim
max(lst)             # maxim
sorted(lst)          # returnează NOUĂ listă sortată (lista originală NESCHIMBATĂ)
reversed(lst)        # iterator (folosiți list(reversed(lst)))
```

### CAPCANA CRITICĂ: sort() vs sorted()
```python
lst = [3, 1, 2]
lst.sort()           # modifică lst, returnează None
result = lst.sort()  # result = None !!! (nu lista sortată)

sorted_lst = sorted(lst)  # returnează lista sortată, lst nemodificată
```

### Liste imbricate (nested)
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[0][1]   # → 2  (rândul 0, coloana 1)
matrix[1][2]   # → 6
matrix[-1][-1] # → 9
```

### Operatori pe liste
```python
[1, 2] + [3, 4]    # → [1, 2, 3, 4]  (concatenare)
[1, 2] * 3         # → [1, 2, 1, 2, 1, 2]  (repetare)
3 in [1, 2, 3]     # → True
5 not in [1, 2, 3] # → True
```

---

## 3. TUPLE (tuple) — IMMUTABLE

Tuplu este **ordonat, NEMODIFICABIL, permite duplicate**.

```python
t = (1, 2, 3)
t = 1, 2, 3        # parantezele sunt opționale
t = (1,)           # tuplu cu UN element — virgula e OBLIGATORIE!
t = (1)            # ATENȚIE: acesta este INT, nu tuplu!

# Indexare și slicing — identic cu liste
t[0]    # → 1
t[-1]   # → 3
t[1:3]  # → (2, 3)

# Ce NU se poate face cu tuple:
t.append(4)   # → AttributeError: 'tuple' object has no attribute 'append'
t[0] = 99     # → TypeError: 'tuple' object does not support item assignment
del t[0]      # → TypeError: 'tuple' object doesn't support item deletion

# Ce SE POATE face:
del t          # → șterge ÎNTREG tuplul din memorie (variabila nu mai există)
len(t)
t.count(1)
t.index(1)
t + (4, 5)    # → (1, 2, 3, 4, 5)  (creare tuplu nou)
```

### CAPCANA CRITICĂ: del tuple
```python
t = (1, 2, 3)
del t[0]   # → TypeError! nu poți șterge element individual
del t      # → OK! șterge ÎNTREAGA variabilă t
print(t)   # → NameError: name 't' is not defined
```

### Tuple unpacking
```python
a, b, c = (1, 2, 3)  # a=1, b=2, c=3
x, *rest = (1, 2, 3, 4)  # x=1, rest=[2, 3, 4]
first, *middle, last = (1, 2, 3, 4)  # first=1, middle=[2,3], last=4
```

---

## 4. DICȚIONARE (dict) — MUTABLE, NEORDONAT (Python 3.7+ menține ordinea inserției)

Dicționar = perechi cheie:valoare. **Cheile trebuie să fie hashable (imutabile)!**

```python
d = {"a": 1, "b": 2, "c": 3}
d = dict(a=1, b=2, c=3)

# Accesare
d["a"]           # → 1
d.get("a")       # → 1
d.get("z")       # → None  (nu ridică KeyError!)
d.get("z", 0)    # → 0  (valoare implicită)

# Modificare
d["a"] = 99      # modifică valoarea
d["d"] = 4       # adaugă cheie nouă
del d["a"]       # șterge perechea cu cheia "a"

# Metode
d.keys()         # → dict_keys(['a', 'b', 'c'])
d.values()       # → dict_values([1, 2, 3])
d.items()        # → dict_items([('a',1), ('b',2), ('c',3)])
d.pop("a")       # șterge și returnează valoarea pentru "a"
d.update({"e": 5})  # adaugă/actualizează chei
d.copy()         # copie superficială
len(d)

# Verificare existență cheie
"a" in d         # → True  (verifică CHEILE)
1 in d.values()  # → True  (verifică VALORILE)

# Iterare
for key in d:
    print(key)

for key, value in d.items():
    print(key, value)
```

### CAPCANA: Chei invalide
```python
# Cheile TREBUIE să fie hashable (imutabile)
d = {[1,2]: "valoare"}   # → TypeError: unhashable type: 'list'
d = {(1,2): "valoare"}   # → OK! tuplurile sunt hashable
d = {"cheie": "valoare"} # → OK!
d = {1: "valoare"}       # → OK!
```

---

## 5. SETURI (set) — MUTABLE, NEORDONAT, FĂRĂ DUPLICATE

```python
s = {1, 2, 3, 4}
s = set([1, 2, 2, 3])  # → {1, 2, 3}  (duplicatele se elimină automat!)
s = set()              # set gol (NU {}, acela e dict gol!)

# Operații pe seturi
s.add(5)               # adaugă element
s.remove(3)            # șterge, ridică KeyError dacă nu există
s.discard(3)           # șterge, NU ridică eroare dacă nu există
s.pop()                # șterge și returnează element ARBITRAR (seturi neordonate!)

# Operații matematice pe seturi
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A | B    # → {1,2,3,4,5,6}  REUNIUNE (union)
A & B    # → {3, 4}          INTERSECȚIE (intersection)
A - B    # → {1, 2}          DIFERENȚĂ (A minus B)
A ^ B    # → {1,2,5,6}       DIFERENȚĂ SIMETRICĂ (în A sau B, nu în ambele)

A.union(B)
A.intersection(B)
A.difference(B)
A.symmetric_difference(B)

# Subset/superset
{1,2}.issubset({1,2,3})    # → True
{1,2,3}.issuperset({1,2})  # → True
```

---

## 6. COMPREHENSIONS

### List comprehension
```python
# Sintaxă: [expresie for variabilă in iterabil if condiție]

# Bazic
squares = [x**2 for x in range(5)]  # → [0, 1, 4, 9, 16]

# Cu condiție (filtru)
evens = [x for x in range(10) if x % 2 == 0]  # → [0, 2, 4, 6, 8]

# Cu transformare
words = ["hello", "world"]
upper = [w.upper() for w in words]  # → ['HELLO', 'WORLD']

# Imbricat
matrix = [[i*j for j in range(3)] for i in range(3)]
# → [[0,0,0], [0,1,2], [0,2,4]]

# ECHIVALENT cu:
result = []
for x in range(5):
    if x % 2 == 0:
        result.append(x**2)
```

### Dict comprehension
```python
squares_dict = {x: x**2 for x in range(5)}
# → {0:0, 1:1, 2:4, 3:9, 4:16}

inverted = {v: k for k, v in {"a":1, "b":2}.items()}
# → {1:'a', 2:'b'}
```

### Set comprehension
```python
unique_squares = {x**2 for x in [-2, -1, 0, 1, 2]}
# → {0, 1, 4}  (fără duplicate)
```

### Generator expression
```python
gen = (x**2 for x in range(5))  # generator, nu calculează imediat
list(gen)  # → [0, 1, 4, 9, 16]
```

---

## 7. FUNCȚII

### Definire și apelare
```python
def greet(name):
    return f"Buna, {name}!"

greet("Ana")   # → 'Buna, Ana!'
```

### Parametri impliciți (default)
```python
def power(base, exp=2):
    return base ** exp

power(3)     # → 9  (exp=2 implicit)
power(3, 3)  # → 27
power(2, 10) # → 1024
```

### *args și **kwargs
```python
def sum_all(*args):      # preia orice număr de argumente poziționale ca TUPLU
    return sum(args)

sum_all(1, 2, 3)    # → 6
sum_all(1, 2, 3, 4) # → 10

def describe(**kwargs):  # preia argumente cu cheie ca DICȚIONAR
    for key, val in kwargs.items():
        print(f"{key}: {val}")

describe(name="Ana", age=25)
# name: Ana
# age: 25
```

### Return multiplu
```python
def minmax(lst):
    return min(lst), max(lst)  # returnează TUPLU

a, b = minmax([3, 1, 4, 1, 5])  # a=1, b=5
result = minmax([3, 1, 4])      # result = (1, 4)
```

### Lambda (funcție anonimă)
```python
# Sintaxă: lambda parametri: expresie

double = lambda x: x * 2
double(5)   # → 10

add = lambda x, y: x + y
add(3, 4)   # → 7

# Uzual cu sorted(), filter(), map()
lst = [("b", 2), ("a", 1), ("c", 3)]
sorted(lst, key=lambda x: x[1])   # sortează după al doilea element
# → [('a', 1), ('b', 2), ('c', 3)]

nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))  # → [2, 4]
doubled = list(map(lambda x: x * 2, nums))         # → [2, 4, 6, 8, 10]
```

---

## 8. STRUCTURI DE CONTROL

### if/elif/else
```python
x = 10
if x > 10:
    print("mare")
elif x == 10:
    print("egal")
else:
    print("mic")
# Output: egal

# One-liner (ternary)
result = "par" if x % 2 == 0 else "impar"
```

### for loop
```python
# Range
for i in range(5):       # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 7):    # 2, 3, 4, 5, 6
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8
    print(i)

for i in range(5, 0, -1): # 5, 4, 3, 2, 1
    print(i)

# enumerate — index + valoare simultan
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, fruit)
# 0 apple
# 1 banana
# 2 cherry

for i, fruit in enumerate(fruits, start=1):  # start de la 1
    print(i, fruit)
# 1 apple
# 2 banana
# 3 cherry

# zip — iterare paralelă
names = ["Ana", "Bob"]
ages = [25, 30]
for name, age in zip(names, ages):
    print(name, age)
# Ana 25
# Bob 30
```

### while loop
```python
n = 0
while n < 5:
    print(n)
    n += 1
# Output: 0 1 2 3 4

# break / continue
for i in range(10):
    if i == 5:
        break      # iese din loop
    if i % 2 == 0:
        continue   # sare la iterația următoare
    print(i)
# Output: 1 3
```

---

## 9. FUNCȚII BUILT-IN ESENȚIALE

```python
# Tip și conversie
type(x)        # tipul variabilei
int("3")       # → 3
float("3.14")  # → 3.14
str(3)         # → '3'
bool(0)        # → False  (0, None, [], {}, "" sunt False)
list((1,2,3))  # → [1, 2, 3]
tuple([1,2,3]) # → (1, 2, 3)
set([1,2,2])   # → {1, 2}

# Intrare/ieșire
input("Mesaj: ")  # returnează ÎNTOTDEAUNA string!

# Matematice
abs(-5)         # → 5
round(3.567, 2) # → 3.57
round(3.5)      # → 4  (rotunjire bancherului: 2.5→2, 3.5→4)
pow(2, 10)      # → 1024  (echivalent cu 2**10)

# Verificări
all([True, True, True])   # → True  (toți trebuie să fie truthy)
all([True, False, True])  # → False
any([False, True, False]) # → True   (cel puțin unul truthy)
any([False, False])       # → False

# Iterabile
range(5)          # 0..4
enumerate(lst)    # perechi (index, valoare)
zip(lst1, lst2)   # perechi paralele
map(func, lst)    # aplică func pe fiecare element
filter(func, lst) # păstrează elementele pentru care func=True
```

---

## 10. MODULE ȘI IMPORT

```python
import math
math.sqrt(16)    # → 4.0
math.pi          # → 3.14159...
math.ceil(3.2)   # → 4
math.floor(3.8)  # → 3

from math import sqrt, pi
sqrt(25)         # → 5.0

import os
os.getcwd()              # directorul curent
os.listdir(".")          # fișierele din director
os.path.exists("file.txt")

import random
random.random()          # float în [0, 1)
random.randint(1, 10)    # int între 1 și 10 inclusiv
random.choice([1,2,3])   # element aleatoriu
random.shuffle(lst)      # amestecă IN PLACE, return None

import datetime
datetime.date.today()
datetime.datetime.now()
```

---

## 11. GRILE TIPICE — PREDICȚIE OUTPUT

### Grila tip 1: Ce returnează metoda?
```python
lst = [3, 1, 4, 1, 5]
result = lst.sort()
print(result)   # → None  (sort returnează None!)

# Corect ar fi:
lst.sort()
print(lst)  # → [1, 1, 3, 4, 5]
```

### Grila tip 2: Tuplu — operații invalide
```python
t = (1, 2, 3)
t.append(4)  # → AttributeError
t[0] = 99    # → TypeError
del t[0]     # → TypeError
del t        # → OK (șterge variabila)
```

### Grila tip 3: Indexare negativă
```python
lst = [10, 20, 30, 40, 50]
print(lst[-1])   # → 50
print(lst[-2])   # → 40
print(lst[1:-1]) # → [20, 30, 40]
```

### Grila tip 4: Comprehension output
```python
result = [x*2 for x in range(4) if x % 2 != 0]
# x iterează: 0, 1, 2, 3
# condiție x%2 != 0: x=1 (True), x=3 (True)
# expresie x*2: 2, 6
# → [2, 6]
```

### Grila tip 5: Dict — chei invalide
```python
d = {[1,2]: "test"}  # → TypeError: unhashable type: 'list'
d = {(1,2): "test"}  # → OK
```

### Grila tip 6: Slice cu step
```python
s = "abcdefg"
print(s[1:6:2])  # → 'bdf'  (pozițiile 1,3,5)
print(s[::-1])   # → 'gfedcba'
```

### Grila tip 7: Mutable default argument (capcana clasică)
```python
def add_item(item, lst=[]):
    lst.append(item)
    return lst

add_item(1)   # → [1]
add_item(2)   # → [1, 2]  (NU [2]! lista default e partajată!)
add_item(3)   # → [1, 2, 3]
```

### Grila tip 8: is vs ==
```python
a = [1, 2, 3]
b = [1, 2, 3]
a == b   # → True  (valori egale)
a is b   # → False  (obiecte diferite în memorie)

a = b    # acum a și b referă același obiect
a is b   # → True
```

### Grila tip 9: Funcție fără return
```python
def func(x):
    x * 2  # calculează dar nu returnează!

result = func(5)
print(result)  # → None
```

### Grila tip 10: range și list
```python
r = range(3, 10, 2)
list(r)  # → [3, 5, 7, 9]

# range(stop): 0..stop-1
# range(start, stop): start..stop-1
# range(start, stop, step)
```

---

## 12. TABEL COMPARATIV — STRUCTURI DE DATE

| Caracteristică | list | tuple | dict | set |
|---|---|---|---|---|
| Sintaxă | `[]` | `()` | `{}` | `set()` sau `{1,2}` |
| Ordonat | Da | Da | Da* | Nu |
| Modificabil | Da | **Nu** | Da | Da |
| Duplicate | Da | Da | Chei: Nu | **Nu** |
| Indexare | Da | Da | Prin cheie | Nu |
| Hashable | **Nu** | Da (dacă elementele sunt) | Nu | Nu |
| Utilizare tipică | Colecție generală | Date fixe | Mapare cheie-valoare | Unicitate/Operații matematice |

*Dict menține ordinea inserției în Python 3.7+

---

## 13. CAPCANE FRECVENTE LA GRILE

1. **`sort()` vs `sorted()`** — sort() returnează None, sorted() returnează lista nouă
2. **`del tuple[i]`** — TypeError! Doar `del t` funcționează (șterge variabila)
3. **Tuple cu un element** — `(1,)` nu `(1)` (al doilea e int!)
4. **Dict cu list ca cheie** — TypeError: unhashable type: 'list'
5. **`/` vs `//`** — 10/2 = 5.0 (float!), 10//2 = 5 (int)
6. **input()** — returnează întotdeauna string, trebuie convertit cu int()/float()
7. **Metode care returnează None** — append(), extend(), sort(), reverse(), shuffle()
8. **`is` vs `==`** — is verifică identitate (același obiect), == verifică egalitate de valoare
9. **Variabile globale în funcții** — citire OK, scriere necesită `global var`
10. **set()** pentru set gol, nu `{}` (acela e dict gol)
11. **Slicing nu ridică IndexError** — `lst[100:]` returnează `[]`, nu eroare
12. **String-urile sunt imutabile** — `s[0] = 'X'` → TypeError
