print("*********************** ROCK , PAPER , SCISSOR GAME ******************")
print("********** r STANDS FOR ROCK , p STANDS FOR PAPER , s STANDS FOR SCISSOR ***************")
# THis is the code writte n by aadi
i=1
while(i):
    a=input("Enter your choice PLAYER 1 ==")
    b=input("Enter your choice PLAYER 2 ==")
    if a=='r' and b=='s': print("Congratulations Player 1 you Wins")
    elif a=='s' and b=='r': print("Congratulations Player 2 you Wins")
    elif a=='p' and b=='s': print("Congratulations Player 2 you Wins")
    elif a=='s' and b=='p': print("Congratulations Player 1 you Wins")
    elif a=='r' and b=='p': print("Congratulations Player 2 you Wins")
    elif a=='p' and b=='r': print("Congratulations Player 1 you Wins")
    elif a=='' and b=='': print("Pls Enter Something")
    elif a=='': print("Why Are You Not Entering Your Choice Player 1")
    elif b=='': print("Why Are You Not Entering Your Choice Player 2")
    elif(a==b) : print("Match Draw")
    else:print("Pls Enter Valid Input")
    i+=1
