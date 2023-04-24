def pierwiastek(a):
    x = a
    k = 1
    y = 1
    e = 5 * pow(10,-12)
    while (abs((pow(x,2)-a)/a) > e):
        x = (x + y) / 2
        y = a / x
        print("Wykonano", k, "iteracje")
        k = k+1
    return x
a = int(input("Wprowadz liczbe: "))
print("Pierwiastek liczby ", a, "to ", pierwiastek(a))