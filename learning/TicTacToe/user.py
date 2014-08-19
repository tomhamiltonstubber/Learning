from random import randrange
from board import Gameboard

class Players:
    myboard = Gameboard()
    def __init__(self):
        pass
    #Player 1's go
    def player_turn(self, player):
        #User
        if player == "p1":
            self.myboard.print_board()
            pos = raw_input("Where would you like to go?")
            if pos in ["1","2","3","4","5","6","7","8","9"]:
                sym = "X"
                if self.myboard.check_for_space(pos,sym) == False:
                    print("That space is taken!")
                    print("Please choose another:")
                    self.player_turn("p1")
            else:
                print("Please enter a number between 1 and 9")
                self.player_turn("p1")
            if self.myboard.check_board(sym) == True:
                return True
            self.player_turn("p2")
        #AI    
        elif player == "p2":
            pos = randrange(1,10)
            sym = "O"
            if self.myboard.check_for_space(pos,sym) == False:
                self.player_turn("p2")
            self.myboard.print_board()
            print("The AI went in space " + str(pos))
            if self.myboard.check_board(sym) == True:
                return True
            self.player_turn("p1")
