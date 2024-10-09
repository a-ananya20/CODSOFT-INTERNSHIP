import random
def game():
    print("Enter r for Rock")
    print("Enter p for Paper")
    print("Enter s for Scissors")
    c=["r","p","s"]
    userresult=0
    compresult=0
    while(True):  
        userChoice=input("Enter your choice to play: ")
        if(userChoice=='0'):
            break
        compChoice=random.choice(c)
        if(userChoice == 'r' or userChoice ==  'p' or userChoice ==  's' ):
            print("computer choice is: ",compChoice)
            if(userChoice==compChoice):
                print("That was a tie...") 
            else:
                if(compChoice=="r"):
                    if(userChoice=="s"):
                        print("computer won the game")
                        compresult+=1
                    else:
                        print("You won the game")
                        userresult+=1
                elif(compChoice=="p"):
                    if(userChoice=="r"):
                        print("computer won the game")
                        compresult+=1
                    else:
                        print("You won the game")
                        userresult+=1
                elif(compChoice=="s"):
                    if(userChoice=="p"):
                        print("computer won the game")
                    compresult+=1
                else:
                    print("You won the game")
                    userresult+=1
                print("Your Score :",userresult)
                print("Computer Score :",compresult)
        else:
            print("Invalid option please enter r or p or s")     
game()
    