a=int(input("wprowadź długość boku a:"))
b=int(input("wprowadź długość boku b:"))
c=int(input("wprowadź długość boku c:"))
if a>0 and b>0 and c>0:
    if a+b>c and a+b<2*c:
        print("Jest to trójkąt")
    elif a+c>b and a+c<2*b:
        print("Jest to trójkąt")
    elif c+b>a and c+b<2*a:
        print("Jest to trójkąt")
    else:
        print("z tych boków nie można zbudować trójkąta")
else:
    print("wszystkie wartości muszą być dodatnie!")
