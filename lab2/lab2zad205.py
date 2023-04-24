x=input("wprowadź coś: ")
if x.isnumeric()==True:
    print("jest to liczba")
elif x.islower()==True:
    print("to mała litera")
elif x.isupper()==True:
    print("to wielka litera")
else:
    print("to inny znak")
