import random
lista = []
for i in range(10):
    lista.append(random.randint(-10,10))
print(lista)
#podpunkt a) wyznaczyc sume wszystkich liczb
suma = 0
for i in range(len(lista)):
    suma += lista[i]
print("Suma wartosci z listy to: " + str(suma))
#podpunkt b) srednia arytmetyczna
print("Srednia wartosci z listy to: " + str(suma/len(lista)))
#podpunkt c) wyznacz liczbe elementow parzystych i nieparzystych
n_par = 0
n_niepar = 0
for i in range(len(lista)):
    if lista[i]%2==0 and i%2==0: n_par += 1
    else: n_niepar += 1
print("Liczb nieparzystych jest: " + str(n_par) + " a nieparzystych: " + str(n_niepar))
#podpunkt d) wyznacz liczbe elementow z przedzialu <5,10>
n = 0
for i in range(len(lista)):
    if lista[i]>=5 and lista[i]<=10: n+=1
print("Liczba elementow w przedziale <5,10> to: " + str(n))
#podpunkt e) wyznacz średnią elementów ujemnych
uj = 0
suma = 0
for i in range(len(lista)):
    if lista[i]<0:
        uj += 1
        suma += lista[i]
print("Srednia elementow ujemnych to: " + str(suma/uj))
#podpunkt f) wyznacz srednia elementow w przedziale <0,10>
suma = 0
n = 0
for i in range(len(lista)):
    if lista[i] in range(0,11):
        suma+=lista[i]
        n += 1
print("Suma elementow w przedziale <0,10> to:"+str(suma/n))
