import random
l = ["Rock", "Paper", "Scissor"]

'''
Rock vs Paper > Paper wins
Rock vs Scissor > Rock wins
Paper vs Scissor > Scissor wins
'''

while True:
    ccount=0
    ucount=0


    uc = int(input('''
    Game Start.....
    1 YES
    2 NO | EXIT
    
    '''))
    if uc==1:
        for i in range(1,6):
            userinput = int(input('''
            1 Rock
            2 Paper
            3 Scissor
            '''))

            if userinput==1:
                uchoice ="Rock"
            elif userinput==2:
                uchoice = "Paper"
            elif userinput==3:
                uchoice = "Scissor"
            Cchoice=random.choice(l)
            if Cchoice==uchoice:
                print("Computer Value",Cchoice)
                print("User Value",uchoice)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1

            elif(uchoice=="Rock" and Cchoice=="Scissor") or (uchoice=="Paper" and Cchoice=="Rock") or (uchoice=="Scissor" and Cchoice=="Paper"):
                print("Computer Value", Cchoice)
                print("User Value",uchoice)
                print("You Win")
                ucount=ucount+1
            else:
                print("Computer Value",Cchoice)
                print("User Value",uchoice)
                print("Computer Wins")
                ccount=ccount+1
        if ucount==ccount:
            print("Draw..")
            print("User Score",ucount)
            print(":Computer Score",ccount)
        elif ucount>ccount:
            print("You Wins!!")
            print("User Score", ucount)
            print("Computer Score", ccount)
        else:
            print("Computer WIns the GAme")
            print("User Score", ucount)
            print(":Computer Score", ccount)

    else:
        break

