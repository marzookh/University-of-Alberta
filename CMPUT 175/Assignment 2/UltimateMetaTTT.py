    #----------------------------------------------------
# Assignment 2: Tic Tac Toe classes
# 
# Author: 
# Collaborators:
# References:
#----------------------------------------------------

class NumTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''      
        self.board = []
        self.size = 3
        
        for i in range(self.size):
            row = []
            for i in range(self.size):
                row.append(0)
            self.board.append(row)
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indices shown.
        Inputs: none
        Returns: None
        '''
        print("   0   1   2")
        index = 0
        for row in range(len(self.board)):
            rowList = []
            for col in range(len(self.board)):
                if self.board[row][col] == 0:
                    rowList.append('')
                else:
                     rowList.append(self.board[row][col])    
            print("{0}{1:>2} |{2:^3}|{3:^3}  ".format(index,rowList[0],rowList[1],rowList[2]))   
            if index != 2:   
                print("  -----------")     
            index = index + 1

    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is "empty", or if it already contains a number 
        greater than 0.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is "empty"; False otherwise
        '''
        if self.board[row][col] == 0:  
            return True 
        else:  
            return False 
    
    def update(self, row, col, mark):
        '''
        Assigns the integer, mark, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           mark (int) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
         
        if self.squareIsEmpty(row,col):# checking if space is empty   
            self.board[row][col] = mark
            return True  
        else:  
            return False   
    
    
    def boardFull(self):
        '''
        Checks if the board has any remaining "empty" squares.
        Inputs: none
        Returns: True if the board has no "empty" squares (full); False otherwise
        '''
        for row in range(len(self.board)):      
            for col in range(len(self.board)):  
                if self.squareIsEmpty(row,col):    
                    return False   
        return True  
        
           
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that 
        adds up to 15. That line can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        rowWin = False   
        for row in range(len(self.board)): 
            List = []   
            for col in range(len(self.board)):    
                List.append(self.board[row][col])  
            if sum(List) == 15:     
                rowWin = True   

        colWin = False   
        for col in range(len(self.board)):     
            column = []      
            for row in range(len(self.board)):     
                column.append(self.board[row][col])     
            if int(sum(column)) == 15:     
                colWin = True       

        diagWin = False   
        diagonal1 =[]  
        diagonal2 = [] 
        for index in range(len(self.board)):
            tile = self.board[index][index]
            diagonal1.append(tile)
            tile = self.board[index][len(self.board) - index - 1]
            diagonal2.append(tile)
        if sum(diagonal1) == 15 or sum(diagonal2) == 15:  
            diagWin = True 
            
        if diagWin == True or colWin == True or rowWin == True: 
            return True 
        else:   
            return False 
    def isNum(self):
        '''
        Checks whether this is a Numerical Tic Tac Toe board or not
        Inputs: none
        Returns: True
        '''
        return True    
    
    
class ClassicTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Classic Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        self.board = []
        self.size = 3 

        self.player_1 = 'X'
        self.player_2 ='O'
        self.turn = self.player_1
        
        for i in range(self.size):
            row = []
            for i in range(self.size):
                row.append('')
            self.board.append(row)

                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indices shown.
        Inputs: none
        Returns: None
        '''
        print("   0   1   2")
        index = 0
        for row in range(len(self.board)):
            rowList = []
            for col in range(len(self.board)):    
                if self.board[row][col] == 0:    
                    rowList.append('')
                else:     
                    rowList.append(self.board[row][col])    
            print("{0}{1:>2} |{2:^3}|{3:^3}  ".format(index,rowList[0],rowList[1],rowList[2]))   
            if index != 2:   
                print("  -----------")     
            index = index + 1
    
    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is "empty", or if it already contains an X or O.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is "empty"; False otherwise
        '''
        
        if self.board[row][col] == '':  
            
            return True 
        else:  
            return False
    
    
    def update(self, row, col, mark):
        '''
        Assigns the string, mark, to the board at the provided row and column, 
        but only if that square is "empty".
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           mark (str) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        
        if self.squareIsEmpty(row,col):# checking if space is empty   
            self.board[row][col] = mark   
            
            return True  
        else:  
            return False   
    
    
    def boardFull(self):
        '''
        Checks if the board has any remaining "empty" squares.
        Inputs: none
        Returns: True if the board has no "empty" squares (full); False otherwise
        '''
        for row in range(len(self.board)):      
            for col in range(len(self.board)):  
                if self.squareIsEmpty(row,col):    
                    return False   
        return True
   
    def isSame(self,alist):
      first = alist[0]
      index = 1
      same = True
      while index < len(alist) and same == True:
         #if alist[index] != first:
         #  same = False
         if alist[index] == '':
             return False
         same = alist[index] == (first)
         index = index + 1
         
      return same
        
           
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) with 
        matching marks (i.e. 3 Xs  or 3 Os). That line can be horizontal, vertical,
        or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        rowWin = False   
        for row in range(len(self.board)): 
            List = []   
            for col in range(len(self.board)):    
                List.append(self.board[row][col])  
            if self.isSame(List):     
                rowWin = True   

        colWin = False   
        for col in range(len(self.board)):     
            column = []      
            for row in range(len(self.board)):     
                column.append(self.board[row][col])     
            if self.isSame(column):     
                colWin = True       

        diagWin = False   
        diagonal1 =[]  
        diagonal2 = [] 
        for index in range(len(self.board)):
            tile = self.board[index][index]
            diagonal1.append(tile)
            tile = self.board[index][len(self.board) - index - 1]
            diagonal2.append(tile)
        if self.isSame(diagonal1) or self.isSame(diagonal2):  
            diagWin = True 
            
        if diagWin == True or colWin == True or rowWin == True: 
            return True 
        else:   
            return False  
    
    def isNum(self):
        '''
        Checks whether this is a Numerical Tic Tac Toe board or not
        Inputs: none
        Returns: False
        '''
        # TO DO: delete pass (and this comment) and complete method
        return False     


class MetaTicTacToe:
    def __init__(self, configFile):
        '''
        Initializes an empty Meta Tic Tac Toe board, based on the contents of a 
        configuration file.
        Inputs: 
           configFile (str) - name of a text file containing configuration information
        Returns: None
        '''       
        # TO DO: delete pass (and this comment) and complete method
        file1 = open(configFile,'r')
        self.board = file1.readlines()
        self.size = 3
        file1.close()
        for i in range(self.size):
            self.board[i] = self.board[i].strip()
            self.board[i] = self.board[i].split()
        
                
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indices shown.
        Inputs: none
        Returns: None
        '''
        print("   0   1   2")
        index = 0
        for row in range(len(self.board)):
            rowList = []
            for col in range(len(self.board)):    
                if self.board[row][col] == 0:    
                    rowList.append('')
                else:     
                    rowList.append(self.board[row][col])    
            print("{0}{1:>2} |{2:^3}|{3:^3}  ".format(index,rowList[0],rowList[1],rowList[2]))   
            if index != 2:   
                print("  -----------")     
            index = index + 1
        


    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square contains a non-played local game board ("empty"),
        or the result of a played local game board (not "empty").
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is "empty"; False otherwise
        '''
        if self.board[row][col] == 'c' or self.board[row][col] == 'n':  
            
            return True 
        else:  
            return False
    
    
    def update(self, row, col, result):
        '''
        Assigns the string, result, to the board at the provided row and column, 
        but only if that square is "empty".
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           result (str) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        if self.squareIsEmpty(row,col):# checking if space is empty   
            self.board[row][col] = result
            return True  
        else:  
            return False
    
    
    def boardFull(self):
        '''
        Checks if the board has any remaining "empty" squares (i.e. any un-played
        local boards).
        Inputs: none
        Returns: True if the board has no "empty" squares (full); False otherwise
        '''
        for row in range(len(self.board)):      
            for col in range(len(self.board)):  
                if self.squareIsEmpty(row,col):    
                    return False   
        return True
    
    def isSame(self,alist):
      first = alist[0]
      index = 1
      same = True
      while index < len(alist) and same == True:
         #if alist[index] != first:
         #  same = False
         if alist[index] == 'n' or alist[index] == 'c':
             return False
         
         if alist[index] == '':
             return False
         same = alist[index] == (first)
         index = index + 1
         
      return same
        
           
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) of their
        mark (three Xs for Player 1, three Os for Player 2), or 3 draws. That line
        can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        rowWin = False   
        for row in range(len(self.board)): 
            List = []   
            for col in range(len(self.board)):    
                List.append(self.board[row][col])  
            if self.isSame(List):     
                rowWin = True   

        colWin = False   
        for col in range(len(self.board)):     
            column = []      
            for row in range(len(self.board)):     
                column.append(self.board[row][col])     
            if self.isSame(column):     
                colWin = True       

        diagWin = False   
        diagonal1 =[]  
        diagonal2 = [] 
        for index in range(len(self.board)):
            tile = self.board[index][index]
            diagonal1.append(tile)
            tile = self.board[index][len(self.board) - index - 1]
            diagonal2.append(tile)
        if self.isSame(diagonal1) or self.isSame(diagonal2):  
            diagWin = True 
            
        if diagWin == True or colWin == True or rowWin == True: 
            return True 
        else:   
            return False  
      
    
    def isNum(self):
        '''
        Checks whether this is a Numerical Tic Tac Toe board or not
        Inputs: none
        Returns: False
        '''
        # TO DO: delete pass (and this comment) and complete method
        return False  
    
    def getLocalBoard(self, row, col):
        '''
        Returns the instance of the empty local board at the specified row, col 
        location (i.e. either ClassicTicTacToe or NumTicTacToe).
        Inputs:
           row (int) - row index of square
           col (int) - column index of square
        Returns: instance of appropriate empty local board if un-played; 
                 None if local board has already been played
        '''
        print(self.squareIsEmpty(row, col))
        if self.squareIsEmpty(row, col):
            if self.board[row][col] == 'c':
                return (ClassicTicTacToe())
            elif self.board[row][col] == 'n':
                return (NumTicTacToe())
            else:
            
                return None
            
            
            
     

    
if __name__ == "__main__":
    # TEST EACH CLASS THOROUGHLY HERE
    num = NumTicTacToe()
    classic = ClassicTicTacToe()
    meta = MetaTicTacToe('MetaTTTconfig.txt')
    
    num.drawBoard()
    classic.drawBoard()
    meta.drawBoard()

    print('Tests for NumTicTacToe')
    num.drawBoard()
    print(num.update(0,0,5))
    print(num.squareIsEmpty(0,0))
    num.drawBoard()

    print(num.isWinner())
    print(num.boardFull())
    print(num.isNum())


    print('Test for ClassicTicTacToe')
    classic.drawBoard()
    print(classic.update(0,0,1))
    
    print(classic.squareIsEmpty(0,0))
    classic.drawBoard()

    print(classic.isWinner())
    print(classic.boardFull())
    print(classic.isNum())

    print('Test for MetaTicTacToe')
    meta.drawBoard()
    print(meta.update(0,0,1))
    print(meta.squareIsEmpty(0,0))
    print(meta.isWinner())
    print(meta.boardFull())
    print(meta.getLocalBoard(0,0))
    print(meta.getLocalBoard(0,2))
    print(meta.getLocalBoard(0,1))
    

    

    
    
    
    
    
    
    
