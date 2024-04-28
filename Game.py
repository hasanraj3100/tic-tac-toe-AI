import pygame
from Board import Board
from AI import AI
from constants import *

class Game: 
    def __init__(self, mode, screen):
        self.board = Board()
        self.player = 1 # 1-X 2-O
        self.gamemode = mode # pvp, pva, ava 
        self.ai = AI()
        self.ai2 = AI(player=1)
        self.running = True
        self.screen = screen
        self.show_lines()
      
    

    def show_lines(self):
        #Vertical
        pygame.draw.line(self.screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (WIDTH - SQSIZE, 0), (WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)
       
        #Horizontal
        pygame.draw.line(self.screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (0, HEIGHT - SQSIZE), (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)

    def next_turn(self):
        self.player = self.player % 2 + 1
    

    def make_move(self, row, col):
        self.board.mark_sqr(row, col, self.player)
        self.draw_fig(row, col)
        self.next_turn()  

    def draw_fig(self, row, col): 
        if self.player == 1: # Draw Cross 
            #Descending Line
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(self.screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)

            #Ascending Line
            start_asc = (col * SQSIZE + OFFSET,  row * SQSIZE + SQSIZE - OFFSET)
            end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
            pygame.draw.line(self.screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)

        elif self.player == 2: # Draw Circle
            center = (col*SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE //2)
            pygame.draw.circle(self.screen, CIRC_COLOR, center, RADIUS, CIRC_WIDTH)
