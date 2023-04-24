import random
n = int(input("Podaj wielkosc listy (nie przekrocz 100 elementow): "))
lista = []
lista_par = []
lista_niepar = []
if n <= 100: #sprawdzenie czy liczba miesci sie w zakresie
    for i in range(0,n+1): #losowanie wartosci
        x = random.randint(0,1000)
        if x%2==0: #wybranie do ktorej listy dolaczyc element, czy do zbioru liczb parzystych czy nieparzystych
            lista_par.append(x)
        else: lista_niepar.append(x)
else:
    print("Przekroczono limit")
lista_par.sort() #sortowanie listy parzystej rosnaco
lista_niepar.sort(reverse=True) #sortowanie listy nieparzystej malejaco
print(lista_par)
print(lista_niepar)
lista.extend(lista_par) #zlaczenie dwoch list w jedna liste posortowana
lista.extend(lista_niepar)
print(lista)

