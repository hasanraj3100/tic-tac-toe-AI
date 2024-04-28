import pygame
import sys, time
from Game import Game 
from constants import * 


class GameLoop: 

    def __init__(self):
        self.game = None 
        self.board = None 
    
    def start(self, mode, screen):

        self.game = Game(mode, screen) 
        self.board = self.game.board

        
        while True: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if not self.game.gamemode == 'ava' and not self.board.final_state() and event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos 
                    row = pos[1] // SQSIZE
                    col = pos[0] // SQSIZE
                    if self.board.is_sq_empty(row, col):
                        self.game.make_move(row, col)

                
            
            pygame.display.update()
            
            if self.game.gamemode == 'ava' and not self.board.final_state() and not self.board.is_full(): 
                time.sleep(1)
                row, col = self.game.ai2.eval(self.board)
                self.game.make_move(row,col)
            
            

            if not self.game.gamemode == 'pvp' and self.game.player == self.game.ai.player and not self.board.is_full() and not self.board.final_state(): 
                pygame.display.update() 
                time.sleep(1)
                row, col = self.game.ai.eval(self.board)
                self.game.make_move(row, col)

            pygame.display.update()