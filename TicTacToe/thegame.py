from random import randrange
from sys import exit
from user import Players

class Game():
    _players = Players()
    def __init__(self):
        pass
    #Decide who goes first
    def decide_first_go(self):
        if randrange(1,3) == 1:
            print("The AI will go first")
            if self._players.player_turn("p2"):
                self.end_game()
        else:
            print("You will go first")
            if self._players.player_turn("p1"):
                self.end_game()

    #User decides whether to play again
    def end_game(self):
        goagain = raw_input("Would you like to try again? Y/N?")
        if (goagain == 'y') or (goagain == 'Y'):
            self._players.clean_board()
            self.decide_first_go()
        elif (goagain == 'n') or (goagain == 'N'):
            print("Thanks for playing!")
            exit()
        else:
            self.end_game()