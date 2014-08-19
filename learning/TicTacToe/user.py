from random import randrange
from board import Gameboard

class Players:
    myboard = Gameboard()
    def __init__(self):
        pass
    def player_turn(self, player):
        #both ai and players go
        while True:
            if player == "p1":
                move = True
                sym = "X"
                while move == True: #Had to have this to make sure you cant go 
                                    #in a filled space
                    self.myboard.print_board()
                    pos = raw_input("Where would you like to go?")
                    if pos in ["1","2","3","4","5","6","7","8","9"]:
                        if  self.myboard.check_for_space(pos,sym) == False:
                            print("That space is taken!")
                            print("Please choose another:")
                        else:
                            move = False
                    else:
                        print("Please enter a number between 1 and 9")

                if self.myboard.check_board(sym) == True:
                    break
                else:
                    player = "p2"

            if player == "p2":
                move = True
                sym = "O"
                while move == True:
                    pos = randrange(1,10)
                    if self.myboard.check_for_space(pos,sym) == False:
                        print("AI same space")
                    else:
                        move = False
                print("The AI went in space " + str(pos))
                if self.myboard.check_board(sym) == True:
                    break
                else:
                    player = "p1"
        return True
    def clean_board(self):
        self.myboard.wipe_board()