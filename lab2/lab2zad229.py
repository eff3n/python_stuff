n = int(input("wprowadz stopien wielomianu: "))
x = int(input("podaj x:"))
suma = 0
for i in range(0,n+1):
    suma = suma + (i * pow(x,i-1))
print(end = '\n')
print("suma wielomianu to:",suma)
