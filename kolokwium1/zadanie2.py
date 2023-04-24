import random
list1=[]
for i in range(0,12):
    list1.append(random.randint(-25,25))
print(list1)
for i in range(0,len(list1)):
    print(i+1,list1[i])
list1.insert(0,1)
list1.insert(1,0)
for i in range(0,13):
    if list1[i]==5:
        list1.remove(5)
print(list1)
j=0
list2=[]
while j<len(list1):
    list2.append(list1[j])
    j=j+2
print(list2)
min=list2[0]
max=list2[0]
for i in range(0,len(list1)):
    if list1[i]>max:
        max=list1[i]
    if list1[i]<min:
        min=list1[i]
print(max)
print(min)
for i in range(0,len(list2)):
    if list2[i]==max:
        print("Lista2 zawiera max listy1")
    if list2[i]==min:
        print("Lista2 zawiera min listy1")
def abc(arg):
    x=arg
    list3=[]
    for i in range(0,len(list1)):
        if list1[i]%2==0 and list1[i]>x:
            list3.append(list1[i])
    print(list3)
    if len(list3)>0:
        print("Średnia:",sum(list3)/len(list3))
    else:
        print("Pusty zbiór, nie można obliczyć średniej")
abc(int(input("Podaj x:")))
def cdf(arg):
    x=arg
    min=list1[0]
    for i in range(0,len(list1)):
        if list1[i]%2==1:
            if list1[i]<min:
                min=list1[i]
    print("minimum nieparzyste:",min)
cdf(1)