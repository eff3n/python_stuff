import random
list_man = [] #deklaracja listy, ktora bedzie uzupelniona manualnie
list_rand = [] #deklaracja listy, ktora bedzie uzupelniona losowo
list_alg = [] #deklaracja listy, ktora bedzie uzupelniona wedle algorytmu
i1=0
print("Wprowadz 10 liczb w zakresie od 1 do 10000: ")
while i1 in range(0,10):
    x = int(input("Liczba nr. " + str(i1+1) + ": ")) #wartosc wprowadzona przez uzytkownika z odpowiednim komunikatem
    if x >= 1 and x <= 10000:
        list_man.append(x) #wprowadzenie nowej wartosci do listy, jesli znajduje sie w zadanycm przedziale
        i1 += 1
    else:
        print("Liczba poza przedzialem!")
for i2 in range(0,10):
    list_rand.append(random.randint(1,10000)) #wypelnienie listy przez 10 losowych liczb w zakresie od 1 do 10000
for i3 in range(0,10):
    list_alg.append(i3+(i3*10)) #wypelnienie listy przez 10 losowych liczb wedle algorytmu list_alg[i] = 11*i3, gdzie i3 to iterator petli
print("Lista uzupelniona manualnie:")
print(list_man)
print("Lista uzupelniona losowo: ")
print(list_rand)
print("Lista uzupelniona algorytmem: ")
print(list_alg)
for i4 in range(0,10):
    print(list_alg[i4]) #Lista z algorytmu wyswietlona w pionie
for i5 in range(0,10):
    print('list_rand[' + str(i5) + ']= ' + str(list_rand[i5])) #Lista losowa wyswietlona w pionie wraz z indeksem i nazwa
list_alg.append(100) #wprowadzenie liczby 100 na koniec listy
print(list_alg)
list_alg.insert(0,11) #wprowadzenie liczby 11 na poczatek listy
print(list_alg)
list_alg.insert(5,5) #wprowadzenie liczby 5 jako 5 element listy
print(list_alg)
list_alg.reverse() #odwrocenie kolejnosci listy z algorytmu
list_rand.sort() #posortowanie rosnaco listy losowej
list_man = list(map(str,list_man)) #przekonwertowanie elementow listy na stringi
list_man.sort(key=len) #sortowanie listy losowej wedle ilosci znakow w elementach
algmax = max(list_alg) #znalezienie wartosci maksymalnej w liscie z algorytmu
maxcount = list_alg.count(algmax)
for i6 in range(maxcount):
    list_alg.remove(algmax) #policzenie wystapien wartosci maksymalnej i ich usuniecie
algmin = min(list_alg) #znalezienie wartosci minimalnej w liscie z algorytmu
mincount = list_alg.count(algmin)
for i7 in range(mincount):
    list_alg.remove(algmin) #policzenie wystapien wartosci minimalnej i ich usuniecie
print(list_alg)
print(list_rand)
list_man = list(map(int,list_man)) #przekonwertowanie elementow znowu na integer
print(list_man)