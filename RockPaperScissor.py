print("""SELECT ONE:
1.   Stone
2.   Paper
3.   Scissor
""")
scoreA = 0;
scoreB = 0;

choiceA = str(input("Player A: "))
choiceB = str(input("Player B: "))
t = True

if(t==True):
    if(choiceA == 'Stone') & (choiceB == 'Paper'):
        scoreB = scoreB + 1
        print("B wins!")
    elif(choiceA == 'Stone') & (choiceB == 'Scissor'):
        scoreA = scoreA +1
        print("A wins")
    elif(choiceA == 'Stone') & (choiceB == 'Stone'):
        print("IT's a tie")
    elif(choiceA == 'Paper') & (choiceB == 'Paper'):
        print("IT's a tie")
    elif(choiceA == 'Paper') & (choiceB == 'Scissor'):
        scoreB = scoreB + 1
        print("B wins!")
    elif(choiceA == 'Paper') & (choiceB == 'Stone'):
        scoreA = scoreA +1
        print("A wins!")
    elif(choiceA == 'Scissor') & (choiceB == 'Stone'):
        scoreB = scoreB+1
        print("B wins!")
    elif(choiceA == 'Scissor') & (choiceB == 'Paper'):
        scoreA = scoreA +1
        print("A wins!")
    elif(choiceA == 'Scissor') & (choiceB == 'Scissor'):
        print("IT's a tie")
    else:
        print("Invalid Input! Try Again!")

cont = str(input("Do you want to continue? (Yes/No): "))
if(cont == 'Yes' or cont == 'yes'):
    t = True
else:
    t = False






