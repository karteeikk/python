question=[
    ["what is your name?","a.kartik","b.meet","c.raj","d.mohit",1],
    ["what is your father name?","a.kiribhai","b.jagdishbhai","c.arvindbhai","d.vikasbhai",1],
    ["what is your surname?","a.patel","b.malani","c.mangukiya","d.limbani",3],
    ["what is your age?","a.16","b.17","c.19","d.13",3],
    ["which course you learn?","a.BCA","b.BBA","c.BSC IT","d.BA",1]
    ]

price=[1000,2000,3000,5000,10000]

money=0
for i in range(0,len(question)):
    questions=question[i]

    print(f"\nthe question price is rs. {price[i]}")
    print(f"{questions[0]}")
    print(f"{questions[1]}  {questions[2]}  {questions[3]}  {questions[4]}")
    
    reply=int(input("enter your answer : "))

    if(reply==0):
        break
    elif(reply==questions[-1]):
        money=money+price[i]
        print(f"correct answer,you won rs. {price[i]}")
    else:
        if(i<=2):
            money=0
        elif(i==3 or i==4):
            money=6000
        print("wrong answer")
        break
print(f"you'r home taken won rs. {money}")