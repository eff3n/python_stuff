ascii_dict = {i: chr(i) for i in range(32, 128)}
print(ascii_dict)
x = int(input("Wybierz opcje: 1- dodanie elementu, 2- usuniecie elementu, 3- wyswietlenie calego slownika, 4- wyswietlenie tylko kluczy, 5- wyswietlenie tylko wartosci, 6- wyswietlenie ilosci kluczy, 7- modyfikacja wartosci, 8- suma wartosci\n"))
match x:
    case 1:
        y = int(input("Wprowadz element: "))
        ascii_dict[y] = chr(y)
    case 2:
        y = int(input("Wybierz element do usuniecia: "))
        if y in ascii_dict:
            ascii_dict.pop(y)
            print("Usunieto element")
        else:
            print("Element nie wystepuje w slowniku")
    case 3:
        print(ascii_dict)
    case 4:
        print(ascii_dict.keys())
    case 5:
        print(ascii_dict.values())
    case 6:
        print(len(ascii_dict))
    case 7:
        y = int(input("Wybierz klucz do modyfikacji: "))
        z = input("Nadaj nowa wartosc: ")
        ascii_dict[y] = z
    case 8:
        vals = list(ascii_dict.keys())
        print(sum(vals))
    case _:
        print("Bledna opcja")