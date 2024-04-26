option={"stone","paper","sizer"}
step=option.pop()
print("stone paper sizer game\n")
player=input("enter your choice is : ")
if step==player:
    print("computer choice is : ",step)
    print("you'r dismiss") 
elif step=="paper" and player=="sizer":
    print("computer choic is : ",step)
    print("you win")
elif step=="stone" and player=="sizer":
    print("computer choice is : ",step)
    print("you loss")
elif step=="stone" and player=="paper":
    print("computer choice is : ",step)
    print("your win")
elif step=="sizer" and player=="paper":
    print("computer choice is : ",step)
    print("you loss")
elif step=="paper" and player=="stone":
    print("computer choice is : ",step)
    print("you loss")
elif step=="sizer" and player=="stone":
    print("computer choice is : ",step)
    print("you win")

