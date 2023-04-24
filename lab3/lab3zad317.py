import random
sum = 0
diag = 0
n = int(input("Podaj wymiar macierzy: "))
list = []
M = [[random.randint(0, 99) for a in range(n)] for b in range(n)] #utworzenie macierzy NxN wypelnionej losowymi liczbami
print(M)
for k in range(n): #wyswietlanie w formie macierzy
    print(M[k])
print(M[0]) #wyswietlenie pierwszego wiersza macierzy
for m in range(n): #wyswietlanie ostatniej kolumny
    print(M[m][-1])
for g in range(n): #liczenie sumy elementow macierzy
    for h in range(n):
        sum += M[g][h]
print(sum)
sum = 0
for z in range (n): #petla liczaca srednia wartosci elementow po glownej przekatnej macierzy
    sum += M[z][z] #sumowanie elementow
diag = sum/n
print(diag)
total_sum = 0
for i in range(n): #liczenie sumy na obwodzie macierzy
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1: #sprawdzenie czy element powinien byc sumowany
            total_sum += M[i][j]
print(total_sum)
max_values = [0] * len(M[0])
for column in range(len(M[0])): #liczenie maksymalnej wartosci w kazdej kolumnie
    max_values[column] = max(row[column] for row in M)
print(max_values)
min_values = [min(row) for row in M] #liczenie minimum w kazdym wierszu
print(min_values)
sum_even = 0
for c in range(n): #petle liczace sume elementow na parzystych wspolrzednych macierzy
    for d in range(n):
        if c % 2 == 1 and d % 2 == 1 and M[c][d] % 2 == 0: #sprawdzenie koordynatow i parzystosci liczby
            sum_even += M[c][d]
print(sum_even)
M_transposed = []
for i in range(len(M)): #transponowanie macierzy
    row = []
    for j in range(len(M)):
        row.append(M[j][i]) #zapisanie wartosci do nowej listy (wiersza)
    M_transposed.append(row)
print(M_transposed)