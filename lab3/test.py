N = 5  # rozmiar macierzy kwadratowej
matrix = [[0 for j in range(N)] for i in range(N)]

# wypełnij macierz danymi losowymi z zakresu 0 do 99
import random
for i in range(N):
    for j in range(N):
        matrix[i][j] = random.randint(0, 99)

# wyświetl ostatni element z każdej zagnieżdżonej listy
for row in matrix:
    print(row[-1])