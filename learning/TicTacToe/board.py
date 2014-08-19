from user import Players

class Gameboard:
    myplayer = Players()

    board = ["1","2","3","4","5","6","7","8","9"]
    v = "|"
    h = "-"
    def __init__(self):
        pass

    #Check if the space is free
    def check_for_space(self,position,symbol):
        if self.board[int(position)-1] == "X" or self.board[int(position)-1] == "O":
            if symbol == "O":
                self.myplayer.player_2_turn()
            else:
                print("That space is taken")
                print("Please choose another")
                self.myplayer.player_1_turn()
        else:
            self.add_turn(position,symbol)
        
    #Add the turn to the board list and then go to next turn
    def add_turn(self, position, symbol):
        self.board[int(position)-1] = symbol
        self.print_board()
        self.check_board(symbol)
        if symbol == "X":
            self.myplayer.player_2_turn()
        if symbol == "O":
            print("The AI went in space " + str(position))
            self.myplayer.player_1_turn()
        
    #Printing the board
    def print_board(self):
        print(self.board[0] + self.v + self.board[1] + self.v + self.board[2])
        print(self.h + self.h + self.h + self.h + self.h)
        print(self.board[3] + self.v + self.board[4] + self.v + self.board[5])
        print(self.h + self.h + self.h + self.h + self.h)
        print(self.board[6] + self.v + self.board[7] + self.v + self.board[8])
        print("")
        
    #Check to see if the game is finished, either the board is full or 3 in a row
    def check_board(self, symbol):
        if (self.board[0] == self.board[1] == self.board[2]) or (self.board[3] == self.board[4] == self.board[5]) or (self.board[6] == self.board[7] == self.board[8]) or (self.board[0] == self.board[3] == self.board[6]) or (self.board[1] == self.board[4] == self.board[7]) or (self.board[2] == self.board[5] == self.board[8]) or (self.board[0] == self.board[4] == self.board[8]) or (self.board[2] == self.board[4] == self.board[6]):
            if symbol == "X":
                print("You win! Well done!")
                self.myplayer.end_game()
            else:
                print("You lose! Bad luck!")
                self.myplayer.end_game()
        if (self.board[0] == "X" or self.board[0] =="O") and (self.board[1] == "X" or self.board[1] =="O") and (self.board[2] == "X" or self.board[2] =="O") and (self.board[3] == "X" or self.board[3] =="O") and (self.board[4] == "X" or self.board[4] =="O") and (self.board[5] == "X" or self.board[5] =="O") and (self.board[6] == "X" or self.board[6] =="O") and (self.board[7] == "X" or self.board[7] =="O") and (self.board[8] == "X" or self.board[8] =="O"):
            print("It's a draw!")
            self.myplayer.end_game()