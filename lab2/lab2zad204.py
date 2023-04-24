x=int(input("wprowadz liczbe: "))
if x<0:
    x=x+1
    print(x)
elif x>=0 and x<=1:
    print(x)
else:
    print(pow(x,2)-1)
