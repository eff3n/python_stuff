import itertools #importowanie biblioteki, ktora umozliwi zapisanie kodu w krotszej i prostszej postaci
import random #importowanie biblioteki generujacej liczby losowe
def generate():
    list = []
    for i in range(0,11):
       list.append(random.randint(0,99))
    return list
set = set(generate()) # tworzenie zbioru 10-elementowego
print("Set:", set)
for k in range(2, 10): # iteracja po mozliwych wartosciach k od 2 do 9
    x = list(itertools.combinations(set, k))  # generowanie kombinacji k-elementowych
    print("kombinacje ", k, "-elementowe:", len(x))  # wyświetlenie liczby kombinacji
    print(x[:10]) # wyswietlenie pierwszych 10 kombinacji