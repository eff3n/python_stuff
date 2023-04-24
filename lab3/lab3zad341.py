languages = {
    "Python" : 14.51,
    "C" : 14.41,
    "Java" : 13.23,
    "C++" : 12.96,
    "C#" : 8.21,
    "Visual Basic" : 4.40,
    "JavaScript" : 2.10,
    "SQL" : 1.68,
    "PHP" : 1.36,
    "Go" : 1.28,
    "Delphi/Object Pascal" : 1.23,
    "Assembly Language" : 1.03,
    "Classic Visual Basic" : 0.92,
    "MATLAB" : 0.86,
    "Scratch" : 0.79,
    "R" : 0.76,
    "Swift" : 0.72,
    "Ruby" : 0.66,
    "Rust" : 0.63,
    "Fortran" : 0.59,
}
languages["NieistniejacyJezyk"] = 99.99 #dodanie elementu do slownika
print(languages)
languages.pop("NieistniejacyJezyk") #usuniecie elementu ze slownika
print(languages)
print(languages.keys()) #wyswietlenie kluczy slownika
print(languages.values()) #wyswietlenie wartosci slownika
print(len(languages)) #wyswietlenie ilosci kluczy slownika
popularity = list(languages.values()) #zapisanie wartosci ze slownika do listy
print(sum(popularity)) #zsumowanie wartosci
languages["SAS"] = 0.56
languages["Ada"] = 0.55
print(languages)
popularity = list(languages.values())
del_key = None
min_key = min(popularity) #znalezienie wartosci najmniejszej
max_key = max(popularity) #znalezienie wartosci najwiekszej
for key, value in languages.items(): #ta petla szuka klucza ktoremu odpowiada wartosc najmniejsza i go usuwa
    if value == min_key:
        del_key = key
        del languages[del_key]
        break
for key, value in languages.items(): #ta petla szuka klucza ktoremu odpowiada wartosc najwieksza i go usuwa
    if value == max_key:
        del_key = key
        del languages[del_key]
        break
print(languages)
biggerthanfive = 0
for i in range(0, len(popularity)): #ta petla liczy ilosc jezykow o popularnosci wiekszej niz 5 procent
    if float(popularity[i]) > 5:
        biggerthanfive += 1
print(biggerthanfive)
between = 0
for i in range(0, len(popularity)): #ta petla liczy ilosc jezykow o popularnosci miedzy 2 a 4 procent
    if float(popularity[i]) > 2 and float(popularity[i]) < 4:
        between += 1
print(between)
keys = languages.keys()
for j in keys: #ta petla szuka jezykow zaczynajacych sie na literę C korzystajac w listy jezykow utworzonej w linijce powyzej
    if j[0].lower() == 'c': #dokonujemy konwersje na male litery, aby nie musiec rozrozniac wielkosci liter przy sprawdzaniu elementow
        print(j)
threechars = 0
for key in languages: #petla wyszukuje klucze o dlugosci wiekszej niz 3
    if len(key) > 3:
        threechars += languages[key]
print(threechars)
sorted_languages = sorted(languages, key=languages.get, reverse=True) #posortowanie jezykow w kolejnosc odwrotnej
for language in sorted_languages:
    print(language)