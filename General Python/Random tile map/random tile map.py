#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      James
#
# Created:     13/08/2014
# Copyright:   (c) James 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame,sys,random,time
import pygametools as pt
pygame.init()

# Create the title screen
class Titlescreen(pt.Menu):
    def __init__(self):
        header = ['Welcome to Random Map generator']
        buttons = [['Draw',lambda:2],['Quit',self.close]]
        pt.Menu.__init__(self,(800,600),(255,69,0),header,buttons)
    def close(self):
        pygame.quit()
        sys.exit()


# Tilemap
class Tilemap():
    def __init__(self,tilelist):
        # Create the image that the map will be drawn on
        self.image = pygame.Surface((800,600))

        # Create the list of tile objects and draw them on the screen
        self.tilelist = tilelist
        i = 0
        n = 0
        for x in range(0,800,200):
            for y in range(0,600,150):
                self.image.blit(self.tilelist[n][i].image,(x,y))
                self.tilelist[n][i].set_position(x,y)
                i += 1
                if i > 3:
                    i = 0
                    n += 1

    def update(self,screen,clock):
            while True:
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                screen.blit(self.image,(0,0))
                pygame.display.flip()

# Game object
class Game(object):
    def __init__(self):
        self.progress = 1
        self.clock = pygame.time.Clock()
        self.tilechance = ['Forrest.png'] * 3 + ['Grassland.png'] * 5 + ['Mountains.png'] * 2
        self.tilelist = []
        for i in range(0,4):
            self.tilelist.append([])
            for x in range(0,4):
                self.tilelist[i].append(pt.Tile(random.choice(self.tilechance),(200,150)))

    def update(self,screen):
        while True:
            if self.progress == 1:
                self.progress = Titlescreen().update(screen,self.clock)
            elif self.progress == 2:
                self.progress = Tilemap(self.tilelist).update(screen,self.clock)

# Initialization of the game

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    Game().update(screen)