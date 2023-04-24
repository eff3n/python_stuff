import random
lk1=[]
for x in range(11):
    lk1.append(random.randrange(0,200))
print(lk1)
for x in range(len(lk1)):
    print(x,lk1[x])
lk2=[]
for x in range(len(lk1)):
    if lk1[x]>20 and lk1[x]<100:
        lk2.append(lk1[x])
print(lk2)
lk3=[]
for x in range(len(lk1)):
    if lk1[x]%2==1:
        lk3.append(lk1[x])
print(sum(lk1)/len(lk1))
def fc1():
    max=lk1[0]
    for x in range(len(lk1)):
        if lk1[x]%2==1 and lk1[x]>max:
            max=lk1[x]
            k=x+1
    return(k,max)
print(fc1())
a=int(input('wprowadz liczbe'))
y=int(input('wprowadz liczbe'))
lk4=[]
def fp2(x,y):
    for x in range(len(lk1)):
        if lk1[x]>a and lk1[x]%y==0:
            lk4.append(lk1[x])
    return(lk4)
print(fp2(x,y))