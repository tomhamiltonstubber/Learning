from random import randrange
from board import Gameboard

class Players:
    myboard = Gameboard()
    def __init__(self):
        pass
        
    #Decide who goes first
    def decide_first_go(self):
        print("hello")
        if randrange(1,3) == 1:
            print("The AI will go first")
            self.player_2_turn()
        else:
            print("You will go first")
            self.myboard.print_board()
            self.player_1_turn()
        
    #Player 1's go
    def player_1_turn(self):
        pos = raw_input("Where would you like to go?")
        if pos in ["1","2","3","4","5","6","7","8","9"]:
            sym = "X"
            self.myboard.check_for_space(pos,sym)
        else:
            print("Please enter a number between 1 and 9")
            self.player_1_turn()
        
    #AI's go
    def player_2_turn(self):
        pos = randrange(1,10)
        sym = "O"
        self.myboard.check_for_space(pos,sym)
        
    #User decides whether to play again
    def end_game():
        goagain = raw_input("Would you like to try again? Y/N?")
        if (goagain == 'y') or (goagain == 'Y'):
            self.myboard.board = ["1","2","3","4","5","6","7","8","9"]
            self.decide_first_go()
        elif (goagain == 'n') or (goagain == 'N'):
            print("Thanks for playing!")
            sys.exit()
        else:
            self.end_game()