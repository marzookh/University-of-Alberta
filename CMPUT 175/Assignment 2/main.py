# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 22:52:46 2020

@author: marza
"""

from UltimateMetaTTT import NumTicTacToe, ClassicTicTacToe, MetaTicTacToe

def main():
    '''
    object1 = MetaTicTacToe("MetaTTTconfig.txt")
    #object1.update(0,0,'X')
    #object1.drawBoard()
    #object1.update(1,1,'X')
    #object1.update(2,2,'X')
    object1.drawBoard()
    print(object1.getLocalBoard(1,1))
    #print(object1.isWinner())
    '''
    #Class = ClassicTicTacToe()
    continueGame = True
    while continueGame:
        playerTurn = 1
        
        LBoardExit= False
        #setX = False
        metaWin = ''
        
        meta = MetaTicTacToe('MetaTTTconfig.txt')

        print(meta.isWinner())
        while not LBoardExit:
            sPlayerTurn = playerTurn
            print("Meta Tic Tac Toe")
            draw = 0
            #print(setX)
            meta.drawBoard()
            #continue = False
            #while continue == False:
            
            row = int(input('Player {} please enter a row:'.format(sPlayerTurn)))
            col = int(input('Player {} please enter a col:'.format(sPlayerTurn)))
            object = meta.getLocalBoard(row,col)
            while object == None:
                print('Error Board has already been played')
                if opa:
                    row = int(input('Player {} please enter a row:'.format(sPlayerTurn)))
                col = int(input('Player {} please enter a col:'.format(sPlayerTurn)))
                object = meta.getLocalBoard(row,col)
            SBoardexit = False
            #####
            if object.isNum():
                print('This is a Numerical Tic Tac Toe.')
            else:
                print('This is a Classical Tic Tac Toe.')
            entry = 'X'    
            
            
            
            while not SBoardexit:
                object.drawBoard()
                
                if object.isNum():
                    
                    if sPlayerTurn % 2 == 0:
                        numDescription = 'even'
                        lowerRange = 2
                        upperRange = 8        
                    else:
                        numDescription = 'odd'
                        lowerRange = 1
                        upperRange = 9  
                    correct = False
                    while not correct:
                        prompt = 'Player {}, please enter an {} number ({}-{}): '
                        prompt = prompt.format(sPlayerTurn, numDescription, lowerRange, upperRange)
                        
                        same = False
                        while not same:
                            try:
                                var=False
                                entry = int(input(prompt))
                                var=True
                            except:
                                print("Error")
                            if var==True:
                                valid = False
                                while valid == False:
                                    if entry in range(1,10):
                                        valid = True
                                    else:
                                        print('Error, number is out of range')
                                        entry = int(input(prompt))
                                for i in object.board:
                                    if entry in i:
                                        print("Error: that number has already been entered")
                                        entry = int(input(prompt))
                                    if entry not in i:
                                        same = True
                                
                            
                        
                        if numDescription == 'even':
                            if entry % 2 != 0:
                                print("not even")
                            else:
                                correct = True
                        if numDescription == 'odd':
                            if entry %2 == 0:
                                print('not odd')
                            else:
                                correct = True
                            
                            
            
                #else:  #classicalTicTacToe
                    
                    
                    #if setX:
                    #    entry = 'X'
                   
                print(entry)
                rows = 9
                cols = 9
                
                
                while rows not in range(0,3):
                    try:
                        rows = int(input('Player {} please enter a row:'.format(sPlayerTurn)))
                    except:
                        print('error')
                while cols not in range(0,3):
                    try:
                        cols = int(input('Player {} please enter a col:'.format(sPlayerTurn)))
                    except:
                        print('error')
                if object.update(rows, cols, entry):
                    
                    if object.isWinner():
                        #setX = True
                        object.drawBoard()
                        print ('Player', sPlayerTurn ,"wins. Congrats!")           
                        SBoardexit = True
                    elif object.boardFull():
                        object.drawBoard()
                        print ("It's a tie.")  
                        draw = True
                        if sPlayerTurn == 1:
                            sPlayerTurn = 2
                        else:
                            sPlayerTurn = 1
                        SBoardexit = True 
                    
                    if sPlayerTurn == 1:
                        sPlayerTurn = 2
                    else:
                        sPlayerTurn = 1
                    if entry == 'X':
                        entry = 'O'
                    else:
                        entry = 'X'
                else:
                    print('Could not make move')
                    
           
            if sPlayerTurn == 1:
                metaWin = 'O'
            
            else:
                metaWin = 'X'
            if draw == True:
                metaWin = 'D'
            
            if meta.update(row, col, metaWin):
                    
                if meta.isWinner():
                    meta.drawBoard()
                    print ('Player', sPlayerTurn ,"wins. Congrats!")           
                    LBoardExit = True
                elif meta.boardFull():
                    meta.drawBoard()
                    print ("It's a tie.")   
                    LBoardExit = True        
            else:
                print('could not make move')
            if playerTurn == 1:
                playerTurn = 2
            else:
                playerTurn = 1
        a = input("do you want to play again? Y/N")
        if a.upper() == 'Y':
            continueGame = True
        elif a.upper() == 'N':
            continueGame = False
        else:
            print('Enter Y or N')
            a = input("do you want to play again? Y/N")
    
        
    
main()
