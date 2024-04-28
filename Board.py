import numpy as np 
from constants import *
class Board: 

    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))
        self.empty_sqrs = self.squares
        self.marked_sqrs  = 0 
    
    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1
    
    def is_sq_empty(self, row, col):
        return self.squares[row][col] == 0
    
    def is_full(self):
        return self.marked_sqrs == 9
    
    def is_initialPos(self):
        return self.marked_sqrs == 0
    
    def get_empty_sqrs(self):
        empty_sqrs = [] 
        for row in range(ROWS):
            for col in range(COLS):
                if self.is_sq_empty(row, col):
                    empty_sqrs.append((row,col))
        
        return empty_sqrs
    
    def final_state(self):
        '''
            return 0 if there is no win yet 
            return 1 if player1 wins 
            return 2 if player2 wins 
        '''
        #vertical wins 
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0: 
                return self.squares[0][col]
        
        #Horizontal wins 
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0: 
                return self.squares[row][0]
        
        #top-left to bottom right wins 
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            return self.squares[0][0]
        
        #top right to bottom left wins 
        if self.squares[0][2] == self.squares[1][1] == self.squares[2][0] != 0: 
            return self.squares[0][2] 
        
        return 0