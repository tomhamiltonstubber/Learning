import sys
import random

    #CLASS FOR THE BOARD
class gameboard(object):
    board = ["1","2","3","4","5","6","7","8","9"]
    v = "|"
    h = "-"

    def __init__(self,name):
        self.name = name
        
        #CHECK IF THE SPACE IS FREE OTHERWISE RETURN TO PLAYER
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
            
        #ADD THE TURN TO THE BOARD LIST, THEN GO TO NEXT PLAYER
    def add_turn(self, position, symbol):
        self.board[int(position)-1] = symbol
        self.print_board()
        addtoboard.check_board(symbol)
        if symbol == "X":
            playersturn.player_2_turn()
        if symbol == "O":
            print("The AI went in space " + str(position))
            playersturn.player_1_turn()
        
        #PRINT THE BOARD
    def print_board(self):
        print(self.board[0] + self.v + self.board[1] + self.v + self.board[2])
        print(self.h + self.h + self.h + self.h + self.h)
        print(self.board[3] + self.v + self.board[4] + self.v + self.board[5])
        print(self.h + self.h + self.h + self.h + self.h)
        print(self.board[6] + self.v + self.board[7] + self.v + self.board[8])
        print("")
    
        #CHECK TO SEE IF THE BOARD IS FULL OR 3-IN-A-ROW
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

    
    #CLASS FOR THE PLAYER'S            
class players(object):
    def __init__(self,name):
        self.name = name
    
        #DECIDE WHO GOES FIRST
    def decide_first_go(self):
        if random.randrange(1,3) == 1:
            print("The AI will go first")
            self.player_2_turn()
        else:
            print("You will go first")
            addtoboard.print_board()
            self.player_1_turn()
            
        #PLAYER 1'S GO
    def player_1_turn(self):
        pos = raw_input("Where would you like to go?")
        if pos in ["1","2","3","4","5","6","7","8","9"]:
            sym = "X"
            addtoboard.check_for_space(pos,sym)
        else:
            print("Please enter a number between 1 and 9")
            self.player_1_turn()
    
        #AI's GO
    def player_2_turn(self):
        pos = random.randrange(1,10)
        sym = "O"
        addtoboard.check_for_space(pos,sym)
        
        #DECIDE WHETHER TO PLAY AGAIN, ELSE END
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