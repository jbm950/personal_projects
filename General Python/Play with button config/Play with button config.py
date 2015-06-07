#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      James
#
# Created:     17/08/2014
# Copyright:   (c) James 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame,sys
import pygametools as pt

class Titlescreen(object):
    def __init__(self):
        self.image = pygame.Surface((800,600))
        self.image.fill((255,215,0))

        pt.Linesoftext(['Trying different button configurations'],(400,50),True,self.image,align = 'c')

        self.button1 = pt.Button(0,'First Button',(400,350),True,self.image,background = 'back.png')

    def update(self,screen,clock):
        screen.blit(self.image,(0,0))
        while True:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

class Game(object):
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.progress = 1

    def update(self,screen):
        while True:
            if self.progress == 1:
                self.progress = Titlescreen().update(screen,self.clock)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    Game().update(screen)