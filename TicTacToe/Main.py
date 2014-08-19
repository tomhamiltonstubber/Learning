import sys
import random

    #Class for the board
class gameboard(object):
    board = ["1","2","3","4","5","6","7","8","9"]
    v = "|"
    h = "-"

    def __init__(self,name):
        self.name = name
        
        #Check to see if the space is free
    def check_for_space(self,position,symbol):
        if self.board[int(position)-1] == "X" or self.board[int(position)-1] == "O":
            if symbol == "O":
                playersturn.player_2_turn()
            else:
                print("That space is taken")
                print("Please choose another")
                playersturn.player_1_turn()
        else:
            self.add_turn(position,symbol)
            
        #Change the board space to the appropriate symbol
    def add_turn(self, position, symbol):
        self.board[int(position)-1] = symbol
        self.print_board()
        addtoboard.check_board(symbol)
        if symbol == "X":
            playersturn.player_2_turn()
        if symbol == "O":
            print("The AI went in space " + str(position))
            playersturn.player_1_turn()
        
        #Print the board
    def print_board(self):
        print(self.board[0] + self.v + self.board[1] + self.v + self.board[2])
        print(self.h + self.h + self.h + self.h + self.h)
        print(self.board[3] + self.v + self.board[4] + self.v + self.board[5])
        print(self.h + self.h + self.h + self.h + self.h)
        print(self.board[6] + self.v + self.board[7] + self.v + self.board[8])
        print("")
    
        #Check to see if game is over
    def check_board(self, symbol):
        if (self.board[0] == self.board[1] == self.board[2]) or (self.board[3] == self.board[4] == self.board[5]) or (self.board[6] == self.board[7] == self.board[8]) or (self.board[0] == self.board[3] == self.board[6]) or (self.board[1] == self.board[4] == self.board[7]) or (self.board[2] == self.board[5] == self.board[8]) or (self.board[0] == self.board[4] == self.board[8]) or (self.board[2] == self.board[4] == self.board[6]):
            if symbol == "X":
                print("You win! Well done!")
                end_game()
            else:
                print("You lose! Bad luck!")
                end_game()
        if (self.board[0] == "X" or self.board[0] =="O") and (self.board[1] == "X" or self.board[1] =="O") and (self.board[2] == "X" or self.board[2] =="O") and (self.board[3] == "X" or self.board[3] =="O") and (self.board[4] == "X" or self.board[4] =="O") and (self.board[5] == "X" or self.board[5] =="O") and (self.board[6] == "X" or self.board[6] =="O") and (self.board[7] == "X" or self.board[7] =="O") and (self.board[8] == "X" or self.board[8] =="O"):
            print("It's a draw!")
            end_game()

    
    #Class for players         
class players(object):
    def __init__(self,name):
        self.name = name
    
        #Decide who goes first
    def decide_first_go(self):
        if random.randrange(1,3) == 1:
            print("The AI will go first")
            self.player_2_turn()
        else:
            print("You will go first")
            addtoboard.print_board()
            self.player_1_turn()
            
        #Player 1'S go
    def player_1_turn(self):
        pos = raw_input("Where would you like to go?")
        if pos in ["1","2","3","4","5","6","7","8","9"]:
            sym = "X"
            addtoboard.check_for_space(pos,sym)
        else:
            print("Please enter a number between 1 and 9")
            self.player_1_turn()
    
        #AI's go
    def player_2_turn(self):
        pos = random.randrange(1,10)
        sym = "O"
        addtoboard.check_for_space(pos,sym)
        
        #Player decide whether or not to play again
def end_game():
    goagain = raw_input("Would you like to try again? Y/N?")
    if (goagain == 'y') or (goagain == 'Y'):
        addtoboard.board = ["1","2","3","4","5","6","7","8","9"]
        playersturn.decide_first_go()
    elif (goagain == 'n') or (goagain == 'N'):
        print("Thanks for playing!")
        sys.exit()
    else:
        end_game()


addtoboard = gameboard("board")    
playersturn = players("player")

playersturn.decide_first_go()