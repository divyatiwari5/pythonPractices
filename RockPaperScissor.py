print("Stone/Paper/Scissor: ")

scoreA = 0
scoreB = 0

t = True

while t:
    choiceA = str(input("Player A: ")).capitalize()
    choiceB = str(input("Player B: ")).capitalize()

    if choiceA == 'Stone' and choiceB == 'Paper':
        scoreB += 1
        print("B wins!")

    elif choiceA == 'Stone' and (choiceB == 'Scissor'):
        scoreA = scoreA +1
        print("A wins")

    elif(choiceA == 'Stone') and (choiceB == 'Stone'):
        print("IT's a tie")
    elif(choiceA == 'Paper') and (choiceB == 'Paper'):
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
    if cont.upper() == 'YES':
        t = True
    else:
        t = False

print(scoreA)
print(scoreB)