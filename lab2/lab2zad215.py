tekst=input("napisz coś: ")
print("wybierz 1 jeśli chcesz wypisać wszystko wedle kodu ASCII")
print("wybierz 2 jeśli chcesz wypisać tylko duże litery")
print("wybierz 3 jeśli chcesz wypisać tylko małe litery")
x=int(input("opcja: "))
match x:
    case 1:
        for i in tekst:
            print(ord(i)) 
    case 2:
        for i in tekst:
            if i.isupper():
                print(i) 
    case 3:
        for i in tekst:
            if i.islower():
                print(i) 
    case _:
        print("zły wybór")
