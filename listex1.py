question1="how many threw balls in one hour ?"
print(question1)
print("A.1 B.2 C.8 D.6")
answer1=int(input('your ans is : '))
match answer1:
    case 1:
        print("wrong answer")
    case 2:
        print("wrong answer")
    case 8:
        print("wromg answer")
    case 6:
        print("correct answer")
    case _:
        print("deafault")
bb=[question1,answer1]
print(bb)
