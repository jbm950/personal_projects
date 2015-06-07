#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      James
#
# Created:     27/05/2015
# Copyright:   (c) James 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame_toolbox.tilegame_tools as pttt

import pygame,sys

pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill((200,200,200))

tilelist = pttt.Tilelist([[pttt.Tile('forrest.png',(150,150)) for i in range(0,4)],
                          [pttt.Tile('forrest.png',(150,150)) for i in range(0,4)],
                          [pttt.Tile('forrest.png',(150,150)) for i in range(0,4)],
                          [pttt.Tile('forrest.png',(150,150)) for i in range(0,4)]])

class Tilemap(pttt.Tilemap):
    def __init__(self,tilelist):
        pttt.Tilemap.__init__(self,(600,600),tilelist,1)

clock = pygame.time.Clock()

while True:
    x = Tilemap(tilelist).update(screen,clock)
    color_tiles = tilelist.adjacent_tiles(x,'p')
    for i in color_tiles:
        i.toggle_shade('red')
