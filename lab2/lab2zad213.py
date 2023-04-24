x=1
suma=0
i=1
while x in range(1,7):
    x=int(input("wprowadź ocenę: "))
    if x in range (1,7):
        suma=suma+x
        srednia=suma/i
        print("Srednia przy ", i, "iteracji to: ", srednia)
        i=i+1
    else:
        break
