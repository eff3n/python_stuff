import random

lista = []
for i in range(10):
    lista.append(random.randint(0,100))
for i in range(len(lista)):
    print(str(i+1) + ": " + str(lista[i]))