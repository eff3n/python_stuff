imiona1 = {'Agata','Andrzej','Michal','Stasiek','Dawid','Mateusz','Karolina','Ola','Marek','Marcin'}
imiona2 = {'Robert,','Stasiek','Ola','Mateusz','Jan','Grzegorz','Damian','Marek','Kamil','Wiktoria'}
sum_list = list(imiona1.union(imiona2)) #suma zbiorów imiona1 i imiona2 zapisana jako lista
sum_tuple = tuple(imiona1.union(imiona2)) #suma zbiorów imiona1 i imiona2 zapisana jako krotka
diff_list = list(imiona1.difference(imiona2)) #roznica zbiorów imiona1 i imiona2 zapisana jako lista
diff_tuple = tuple(imiona1.difference(imiona2)) #roznica zbiorów imiona1 i imiona2 zapisana jako krotka
sym_diff_list = list(imiona1.symmetric_difference(imiona2)) #roznica symetryczna zbiorów imiona1 i imiona2 zapisana jako lista
sym_diff_tuple = tuple(imiona1.symmetric_difference(imiona2)) #roznica symetryczna zbiorów imiona1 i imiona2 zapisana jako krotka
intersect_list = list(imiona1.intersection(imiona2)) #czesc wspolna zbiorow imiona1 i imiona2 zapisana jako lista
intersect_tuple = tuple(imiona1.intersection(imiona2)) #czesc wspolna zbiorow imiona1 i imiona2 zapisana jako krotka
samogloski = ['a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y'] #lista samoglosek
print("Imiona zaczynajace sie samogloska: ")
for imie in imiona1.union(imiona2):
    if imie[0].lower() in samogloski: #dokonujemy konwersje na male litery, aby nie musiec rozrozniac wielkosci liter przy sprawdzaniu elementow
        print(imie)
print("Imiona konczace sie litera 'a': ")
for imie in imiona1.union(imiona2):
    if imie[-1].lower() == 'a': #dokonujemy konwersje na male litery, aby nie musiec rozrozniac wielkosci liter przy sprawdzaniu elementow
        print(imie)
print("Imiona skladajace sie tylko z 3 liter: ")
for imie in imiona1.union(imiona2):
    if len(imie) == 3:
        print(imie)