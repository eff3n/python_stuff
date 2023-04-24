n = 0
j = 1
m = int(input("wprowadz koniec zakresu: "))
szereg = 0
print (u"\u221Ae = ")
for i in range(n,m+1):
    fact = 1
    while j <= i:
        fact = fact * j
        j = j + 1
    print("1/2^",i,"*",i,"! + ")
    szereg = szereg + (1/(pow(2,i)*fact))
print (u"\u221Ae = ",szereg)