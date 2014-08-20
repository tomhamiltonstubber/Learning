class Gameboard:
    
    boardlist = ["1","2","3","4","5","6","7","8","9"]
    _v = "|"
    _h = "-"
    def __init__(self):
        pass

    #Check if the space is free
    def check_for_space(self,position,_symbol):
        if (self.boardlist[int(position)-1] == "X" or 
           self.boardlist[int(position)-1] == "O"):
            return False
        else:
            self.add_turn(position,_symbol)
        
    #Add the turn to the boardlist list and then go to next turn
    def add_turn(self, position, _symbol):
        self.boardlist[int(position)-1] = _symbol
        
    #Printing the boardlist
    def print_board(self):
        print("\t" + self.boardlist[0] + self._v + self.boardlist[1] + 
            self._v + self.boardlist[2])
        print("\t" + self._h + self._h + self._h + self._h + self._h)
        print("\t" + self.boardlist[3] + self._v + self.boardlist[4] + 
            self._v + self.boardlist[5])
        print("\t" + self._h + self._h + self._h + self._h + self._h)
        print("\t" + self.boardlist[6] + self._v + self.boardlist[7] + 
            self._v + self.boardlist[8])
        print("")
        
    #Check to see if the game is finished, either the boardlist is full or 
    #3 in a row
    def check_board(self, _symbol):
        if ((self.boardlist[0] == self.boardlist[1] == self.boardlist[2]) or 
        (self.boardlist[3] == self.boardlist[4] == self.boardlist[5]) or 
        (self.boardlist[6] == self.boardlist[7] == self.boardlist[8]) or 
        (self.boardlist[0] == self.boardlist[3] == self.boardlist[6]) or 
        (self.boardlist[1] == self.boardlist[4] == self.boardlist[7]) or 
        (self.boardlist[2] == self.boardlist[5] == self.boardlist[8]) or 
        (self.boardlist[0] == self.boardlist[4] == self.boardlist[8]) or 
        (self.boardlist[2] == self.boardlist[4] == self.boardlist[6])):
            if _symbol == "X":
                self.print_board()
                print("You win! Well done!")
            else:
                self.print_board()
                print("You lose! Bad luck!")
            return True
        if ((self.boardlist[0] == "X" or self.boardlist[0] =="O") and 
            (self.boardlist[1] == "X" or self.boardlist[1] =="O") and 
            (self.boardlist[2] == "X" or self.boardlist[2] =="O") and 
            (self.boardlist[3] == "X" or self.boardlist[3] =="O") and 
            (self.boardlist[4] == "X" or self.boardlist[4] =="O") and 
            (self.boardlist[5] == "X" or self.boardlist[5] =="O") and 
            (self.boardlist[6] == "X" or self.boardlist[6] =="O") and 
            (self.boardlist[7] == "X" or self.boardlist[7] =="O") and 
            (self.boardlist[8] == "X" or self.boardlist[8] =="O")):
            print("It's a draw!")
            return True
    #Cleaning the board for a new game
    def wipe_board(self):
        self.boardlist = ["1","2","3","4","5","6","7","8","9"]
        self.print_board()