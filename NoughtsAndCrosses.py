import random
import sys

board = ["1","2","3","4","5","6","7","8","9"]

v="|"
h="-"

        #STARTS THE GAME
def gamestart():
    username = input("What is your name?\n")
    print("Welcome to Noughts and Crosses!\n")
    print("Hello " + username +", We are going to play a game!\n")
    decidewhogoesfirst()

        #PRINTS THE BOARD
def printboard():
    print("")
    print(board[0] + v + board[1] + v + board[2])
    print(h + h + h + h + h)
    print(board[3] + v + board[4] + v + board[5])
    print(h + h + h + h + h)
    print(board[6] + v + board[7] + v + board[8])
    print("")

        #RANDOM DECIDE WHO GOES FIRST
def decidewhogoesfirst():
    randomnum = random.randrange(1,3)
    if(randomnum==1):
        print("You will go first!\n")
        useronego()
    elif(randomnum==2):
        print("The AI will go first!\n")
        usertwogo()

        #USER'S GO
def useronego():
    printboard()
    if((board[0] == board[3] == board[6] == "X") or (board[1] == board[4] == board[7] == "X") or (board[2] == board[5] == board[8] == "X") or (board[0] == board[1] == board[2] == "X") or (board[3] == board[4] == board[5] == "X") or (board[6] == board[7] == board[8] == "X") or (board[0] == board[4] == board[8] == "X") or (board[2] == board[4] == board[6] == "X")):
        print("You win!\n")
        exitornot()
    elif((board[0] == board[3] == board[6] == "O") or (board[1] == board[4] == board[7] == "O") or (board[2] == board[5] == board[8] == "O") or (board[0] == board[1] == board[2] == "O") or (board[3] == board[4] == board[5] == "O") or (board[6] == board[7] == board[8] == "O") or (board[0] == board[4] == board[8] == "O") or (board[2] == board[4] == board[6] == "O")):
        print("You lose!\n")
        exitornot()
    else:
        userinput = 0
        while True:
            try:
                userinput = int(input("Pick a space to go in:"))
            except ValueError:
                print("Pick a number between 1 and 9!")
            else:
                gohere = userinput-1
                if(board[gohere] != "O") and (board[gohere] != "X"):
                    board[gohere]="X"
                    usertwogo()
                elif(board[gohere] =="O") or (board[gohere] == "X"):
                    print("That space is taken!\n")
                    useronego()
    
        #AI'S TURN
def usertwogo():
    printboard()
    if((board[0] == board[3] == board[6]) or (board[1] == board[4] == board[7]) or (board[2] == board[5] == board[8]) or (board[0] == board[1] == board[2]) or (board[3] == board[4] == board[5]) or (board[6] == board[7] == board[8]) or (board[0] == board[4] == board[8]) or (board[2] == board[4] == board[6])):
        print("You win!\n")
        exitornot()
    else:
        randomnum = random.randrange(0,9)
        if(board[randomnum] != "O") and (board[randomnum] != "X"):
            board[randomnum] = "O"
            print("The AI went in in space " + str(randomnum+1))
            useronego()
        elif(board[randomnum] =="O") or (board[randomnum] == "X"):
            usertwogo()

        #ASKS THE USER IF THEY WISH TO PLAY AGAIN
def exitornot():
    play = input("Play again? Y/N")
    if((play == "Y") or (play == "y")):
        resetboard()
    elif((play == "N") or (play =="n")):
        end()
    elif((play != "Y") and (play != "y") and (play != "n") and (play !="N")):
        exitornot()

        #TESTS FOR 3 IN A ROW
def testforend():
    if((board[0] == board[3] == board[6]) or (board[1] == board[4] == board[7]) or (board[2] == board[5] == board[8]) or (board[0] == board[1] == board[2]) or (board[3] == board[4] == board[5]) or (board[6] == board[7] == board[8]) or (board[0] == board[4] == board[8]) or (board[2] == board[4] == board[6])):
        print("You win!\n")
        exitornot()

        #RESETS THE BOARD
def resetboard():
    board[0] = "1"
    board[1] = "2"
    board[2] = "3"
    board[3] = "4"
    board[4] = "5"
    board[5] = "6"
    board[6] = "7"
    board[7] = "8"
    board[8] = "9"
    decidewhogoesfirst()

def end():
    print("Thanks for playing!")
        
gamestart()
