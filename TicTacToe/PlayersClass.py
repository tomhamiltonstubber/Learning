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