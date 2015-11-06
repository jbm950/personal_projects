#-------------------------------------------------------------------------------
# Name:        tq_main.py
# Purpose:     This will be the main script file for the game Torric's Quest
#
# Author:      James
#
# Created:     04/01/2015
# Copyright:   (c) James 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame
import tq_graphics as tqg
import tq_combat as tqc

class Main(object):
    def __init__(self):
        self.progress = 1
        self.page = 1
        self.clock = pygame.time.Clock()
        self.player = tqc.Player(13)

    def update(self,screen):
        # Screen Order
        # 1 - Title screen
        # 2 - Story screen
        #   - Tutorial check (with story screen)
        # 3 - Tutorial screen
        # 4 - Combat screens
        # 5 - Level up screen
        # 6 - End game screen

        while True:
            if self.page == 1:
                self.page = tqg.Titlescreen().update(screen,self.clock)
            elif self.page == 2:
                self.page = tqg.Storyscreens(self.progress).update(screen,self.clock)
                if self.progress == 1:
                    self.page = tqg.Tutorialcheck().update(screen,self.clock)
                elif self.progress == 13:
                    self.page = 6
            elif self.page == 3:
                self.page = tqg.Storyscreens(14).update(screen,self.clock)
            elif self.page == 4:
                self.page = tqg.Combatscreens(self.player,self.progress).update(screen,self.clock)
                self.progress +=1
                if self.progress % 2 == 0:
                    self.page = 5
            elif self.page == 5:
                tqg.Levelupscreen(self.player).update(screen,self.clock)
                self.page = 2
            elif self.page == 6:
                tqg.Endgamescreen().update(screen,self.clock)
                self.__init__()
                self.page = 2


if __name__ == '__main__':
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    Main().update(screen)
