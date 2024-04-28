import pygame 
from constants import *
from Button import *

from GameLoop import GameLoop


pygame.init() 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TIC TAC TOE")
screen.fill(BG_COLOR)


#Loading Images for buttons and the title
hvh_img = pygame.image.load('assets/btn_hvh.png').convert_alpha()
hva_img = pygame.image.load('assets/btn_hva.png').convert_alpha()
ava_img = pygame.image.load('assets/btn_ava.png').convert_alpha()
title_img = pygame.image.load("assets/title.png").convert_alpha()


def starting_screen():
    running  = True

    # drawing the buttons and title on the screen 
    hvh_button = Button(100, 200, hvh_img, screen)
    hva_button = Button(100, 320, hva_img, screen)
    ava_button = Button(100, 440, ava_img, screen)
    hvh_button.draw()
    hva_button.draw()
    ava_button.draw()
    screen.blit(title_img, (110, 30))



    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN: 
                pos = pygame.mouse.get_pos() 
                if hvh_button.isClicked(pos):
                    screen.fill(BG_COLOR)
                    pygame.display.update()
                    GameLoop().start('pvp', screen)
                if hva_button.isClicked(pos):
                    screen.fill(BG_COLOR)
                    pygame.display.update()
                    GameLoop().start('pva', screen)
                if ava_button.isClicked(pos):
                    screen.fill(BG_COLOR)
                    pygame.display.update()
                    GameLoop().start('ava', screen)

        pygame.display.update()

starting_screen()

