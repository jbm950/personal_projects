#-------------------------------------------------------------------------------
# Name:        play_with_tiles.py
# Purpose:
#
# Author:      James
#
# Created:     28/07/2014
# Copyright:   (c) James 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

# Import the necessary modules and initialize pygame
import pygame,sys
import pygametools_0_3 as pt
pygame.init()

screen = pygame.display.set_mode((800,600))

class Tile(pygame.sprite.Sprite):

    pos = ()
    shade_state = 0

    def __init__(self,file,size):

        # Initialize pygame sprite class
        pygame.sprite.Sprite.__init__(self)

        # Create the image for the tile
        self.image = pygame.Surface(size)

        # Load the given file and adjust the size
        self.pic = pygame.image.load(file)
        self.pic = pygame.transform.scale(self.pic,size)
        self.image.blit(self.pic,(0,0))

        # Create some shades for the tile
        self.blue_shade = pygame.Surface(size)
        self.blue_shade.fill((0,0,255))
        self.blue_shade.set_alpha(150)

        self.red_shade = pygame.Surface(size)
        self.red_shade.fill((255,0,0))
        self.red_shade.set_alpha(150)

        # Set up the pygame rect object for collision detection
        self.rect = self.image.get_rect()

    def set_position(self,x,y):

        # Set the location of the rectangle
        self.rect[0] = x
        self.rect[1] = y

        # Set the position of the tile
        self.pos = (x,y)

    def toggle_shade(self,shade):

        # If the tile is unshaded turn on the shade requested
        if self.shade_state == 0:
            if shade == 'b':
                self.image.blit(self.pic,(0,0))
                self.image.blit(self.blue_shade,(0,0))
                self.shade_state = 1
            elif shade == 'r':
                self.image.blit(self.pic,(0,0))
                self.image.blit(self.red_shade,(0,0))
                self.shade_state = 2

        # If the tile is already shaded turn off the shade
        else:
            self.image.blit(self.pic,(0,0))
            self.shade_state = 0

tiledict = {'forrest tile ' + str(i):Tile('forrest.png',(200,150)) for i in range(1,17)}
tilelist = [[Tile('forrest.png',(200,150)) for i in range(0,4)],
            [Tile('forrest.png',(200,150)) for i in range(0,4)],
            [Tile('forrest.png',(200,150)) for i in range(0,4)],
            [Tile('forrest.png',(200,150)) for i in range(0,4)]]

print(tilelist)

i = 0
n = 0
for x in range(0,800,200):
    for y in range(0,600,150):
        screen.blit(tilelist[n][i].image,(x,y))
        tilelist[n][i].set_position(x,y)
        i += 1
        if i > 3:
            i = 0
            n += 1



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        for n in tilelist:
            for i in n:
                if event.type == pygame.MOUSEBUTTONUP and i.rect.collidepoint(pygame.mouse.get_pos()):
                    row = tilelist.index(n)
                    col = n.index(i)
                    """
                    tilelist[row][col].toggle_shade('b')
                    screen.blit(tilelist[row][col].image,tilelist[row][col].pos)
                    """
                    if row - 1 >= 0:
                        switchshaderows = [row - 1]
                    if row + 1 <= 3:
                        switchshaderows += [row + 1]
                    if col - 1 >= 0:
                        switchshadecols = [col - 1]
                    if col + 1 <= 3:
                        switchshadecols += [col + 1]
                    for x in switchshaderows:
                        tilelist[x][col].toggle_shade('r')
                        screen.blit(tilelist[x][col].image,tilelist[x][col].pos)
                    for y in switchshadecols:
                        tilelist[row][y].toggle_shade('r')
                        screen.blit(tilelist[row][y].image,tilelist[row][y].pos)

        switchshaderows = []
        switchshadecols = []

    pygame.display.flip()

