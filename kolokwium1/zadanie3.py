#zad 1 1h
ta1=[]
for i in range(0,10):
    ta1.append(int(input('podaj liczbe:')))
#zad 2
for i in range(0,10):
    print(i+1,ta1[i])
#zad 3
ta2=[]
for i in range(0,len(ta1)):
    if ta1[i]>0 and ta1[i]%2==0:
        ta2.append(ta1[i])
print(ta2)
#zad 4
licz=0
for i in range(0,len(ta1)):
    if ta1[i]>=-9 and ta1[i]<=9:
        licz=licz+1
print(licz)
#zad 5
def abc():
    ta3=[]
    x1=int(input("Podaj dolny zakres:"))
    x2=int(input("Podaj górny zakres:"))
    for i in range(x1,x2-1):
        ta3.append(i)
    ta4=[]
    y=int(input("Podaj dzielnik:"))
    for i in range(x1,x2-1):
        if ta3[i]%y==0:
            ta4.append(i)
    print(sum(ta4)/len(ta4))
abc()
#zad 6
def xyz():
    ta5=[]
    for i in range(1,10):
        if ta1[i]<0 and ta1[i]%2==0:
            ta5.append(ta1[i])
    if len(ta5)>1:
        ta5.sort(reverse=True)
        print(ta5)
        print(ta5[1])
    else:
        print("za mało liczb ujemnych parzystych")
xyz()