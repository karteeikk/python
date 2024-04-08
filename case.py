n=int(input())
match n:
    case 0:
        print("n is zero")
    case 1:
        print("n is one")
    case 2:
        print("n is two")
    case _ if n>100:
        print(" n is more than 100")
    case _ if n<0:
        print("n is negative")
    case _:
        print("n is deafault")