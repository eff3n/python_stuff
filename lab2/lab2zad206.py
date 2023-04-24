x=int(input("wprowadz ocenę:"))
match x:
    case 2:
        print("dwa")
    case 2,5:
        print("dwa i pół")
    case 3:
        print("trzy")
    case 3,5:
        print("trzy i pół")
    case 4:
        print("cztery")
    case 4,5:
        print("cztery i pół")
    case 5:
        print("pięć")
    case _:
        print("błędna ocena")
        
