from random import randrange

from board import Gameboard

class Players:
    myboard = Gameboard()
    def __init__(self):
        pass
    def player_turn(self, _player):
        #both ai and players go
        while True:
            if _player == "p1":
                _move = True
                _sym = "X"
                while _move == True: #Had to have this to make sure you cant go
                                     #in a filled space
                    self.myboard.print_board()
                    pos = raw_input("Where would you like to go?")
                    if pos in ["1","2","3","4","5","6","7","8","9"]:
                        if  self.myboard.check_for_space(pos,_sym) == False:
                            print("That space is taken!")
                            print("Please choose another:")
                        else:
                            _move = False
                    else:
                        print("Please enter a number between 1 and 9")

                if self.myboard.check_board(_sym):
                    break
                else:
                    _player = "p2"

            if _player == "p2":
                _move = True
                _sym = "O"
                while _move == True:
                    pos = randrange(1,10)
                    if self.myboard.check_for_space(pos,_sym) == False:
                        pass
                    else:
                        _move = False
                print("The AI went in space " + str(pos))
                if self.myboard.check_board(_sym):
                    break
                else:
                    _player = "p1"
        return True
    def clean_board(self):
        self.myboard.wipe_board()