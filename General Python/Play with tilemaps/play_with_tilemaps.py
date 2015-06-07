#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      James
#
# Created:     21/08/2014
# Copyright:   (c) James 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame,sys
import pygametools as pt

pygame.init()
screen = pygame.display.set_mode((800,600))
screen.fill((200,200,200))

tilelist = [[pt.Tile('forrest.png',(150,150)) for i in range(0,4)],
            [pt.Tile('forrest.png',(150,150)) for i in range(0,4)],
            [pt.Tile('forrest.png',(150,150)) for i in range(0,4)],
            [pt.Tile('forrest.png',(150,150)) for i in range(0,4)]]

class Tilemap(pt.Tilemap):
    def __init__(self,tilelist):
        pt.Tilemap.__init__(self,(600,600),tilelist,1)
        pt.Tilemap.set_offset(self,(100,0))

clock = pygame.time.Clock()

x = Tilemap(tilelist).update(screen,clock)
color_tiles = Tilemap(tilelist).adjacent_tiles(x,'b')
for i in color_tiles:
    i.toggle_shade('red')
x = Tilemap(tilelist).update(screen,clock)
print(x)


pygame.quit()
sys.exit()
