import matplotlib.pyplot as plt
import Functii as fun


a = 3
print(type(a)) # acesta un comentariu

a = 'acesta este un sir de caractere'; print(type(a))

# am aici un comentariu
# inca un comentariu

'''
acesta
este un
comentariu
care se intinde
pe mai multe
linii fizice
'''

x = 11
y = -3
print(x // y) # catul impartirii

a = 3 + \
    5 + \
    2
print(a)

# atribuire multipla
a = b = c = 7
print(a, b, c)

a, b, c = 1, 3.14, 'mama este cea mai buna'
print(a, b, c)

string_1 = 'acesta este un string'
print(id(string_1))
string_1 = 'un alt string'
print(id(string_1))

string_2 = """'mama mi-a spus: "fii atent la scoala!"'"""
print(string_2)

print(string_1*4) # concatenare multipla

list_1 = [1, 2, 3.14, 'mama este acasa', [4, 5, 6]]
print(list_1)

list_2 = [0, 1, 2, 3, 4, 5, 6,7, 8, 9, 10]
print(list_2[:]) # echivalent
print(list_2[::]) # echivalent
print(list_2[0::1]) # echivalent

# tiparire valori de la indecsi pari
print(list_2[::2])

# valorile de la indecsii impari
print(list_2[1::2])

print(list_2[len(list_2)-1])
print(list_2[-1])

list_3 = list_2[-1::-1] # crearea unei liste de valori in ordine inversa
print(list_3)

print(type(range(100)))
list_4 = [x for x in range(100)]
list_4 = [x for x in range(1, 101, 1)]
list_4 = [(x+1) for x in range(100)]
print(list_4)

# plt.plot(list_4); plt.show()

list_5 = [(x+1)**4 for x in range(100)]
print(list_5)

# plt.plot(list_5); plt.show()

list_6 = ['Obs'+str(x+1) for x in range(1000)]
print(list_6)

a = 11; b = 3
print(a, b)
fun.interschimb(a, b)
print(a, b)

list_ab = [11, 3]
print(list_ab)
fun.interschimb_list(list_ab)
print(list_ab)