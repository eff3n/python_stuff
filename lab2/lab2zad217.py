n=int(input("wprowadz n:"))
m=int(input("wprowadz m:"))
i = 1
factn = 1
j = 1
factm = 1
while i<=n:
    factn = factn*i
    i = i+1
print("silnia n to: ", factn)
if n>m:
    while j <= m:
        factm = factm * j
        j = j + 1
    result = factn/factm
    print("wynik dzialania n!/m! to: ", result)
else:   print("n nie jest wieksze od m")