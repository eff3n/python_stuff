a=int(input("wprowadź początek zakresu: "))
b=int(input("wprowadź koniec zakresu: "))
for i in range(a,b+1):
    if i%2==0:
        print(i)
