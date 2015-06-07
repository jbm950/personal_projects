#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      James
#
# Created:     10/08/2014
# Copyright:   (c) James 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame,sys
import pygametools as pt
import torrics_quest_combat as tqc
pygame.init()

# Create the title screen
class Titlescreen(pt.Menu):
    def __init__(self):
        header = ['Welcome to Play with Tiles 2']
        buttons = [['Play',lambda:2],['Quit',self.close]]
        pt.Menu.__init__(self,(800,600),(255,69,0),header,buttons)
    def close(self):
        pygame.quit()
        sys.exit()

# Tilemap
class Tilemap():
    def __init__(self,player_tile,tilelist):
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

        # Create the image showing the tile the player is located on
        playerpic = pygame.image.load('Player.png').convert()
        playerpic = pygame.transform.scale(playerpic,(200,150))
        playerpic.set_colorkey((255,255,255))
        playerpos_xy = [player_tile[0] * 200,player_tile[1] *150]
        self.image.blit(playerpic,playerpos_xy)
        self.playerpos_tile = player_tile

    def update(self,screen,clock):
            while True:
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONUP and self.tilelist[self.playerpos_tile[0]][self.playerpos_tile[1]].rect.collidepoint(pygame.mouse.get_pos()):
                        return 3
                screen.blit(self.image,(0,0))
                pygame.display.flip()

    def moveupdate(self,movelist,screen,clock):
            while True:
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    for i in movelist:
                        if event.type == pygame.MOUSEBUTTONUP and self.tilelist[i[0]][i[1]].rect.collidepoint(pygame.mouse.get_pos()):
                            return (2, i)
                screen.blit(self.image,(0,0))
                pygame.display.flip()

# Tilescreen
class Tilescreen(pt.Menu):
    def __init__(self):
        header = ['Choose your action']
        buttons = [['Fight',lambda:4],['Move',lambda:5]]
        pt.Menu.__init__(self,(300,300),(255,69,0),header,buttons)
        pt.Menu.set_offset(self,(275,100))
    def close(self):
        pygame.quit()
        sys.exit()

# Game object
class Game(object):
    def __init__(self):
        self.progress = 1
        self.clock = pygame.time.Clock()
        self.player_tile = [0,0]
        self.tilelist = [[pt.Tile('forrest.png',(200,150)) for i in range(0,4)],
                         [pt.Tile('forrest.png',(200,150)) for i in range(0,4)],
                         [pt.Tile('forrest.png',(200,150)) for i in range(0,4)],
                         [pt.Tile('forrest.png',(200,150)) for i in range(0,4)]]

        self.player = tqc.Player(13)

    def movetiles(self,unshade = None):
        if unshade == None:
            row = self.player_tile[0]
            col = self.player_tile[1]
            movelist = []
            switchshaderows = []
            switchshadecols = []

            if row - 1 >= 0:
                switchshaderows = [row - 1]
            if row + 1 <= 3:
                switchshaderows += [row + 1]
            if col - 1 >= 0:
                switchshadecols = [col - 1]
            if col + 1 <= 3:
                switchshadecols += [col + 1]
            for x in switchshaderows:
                if self.tilelist[x][col].shade_state != 1:
                    self.tilelist[x][col].toggle_shade('r')
                movelist += [(x,col)]
            for y in switchshadecols:
                if self.tilelist[row][y].shade_state != 1:
                    self.tilelist[row][y].toggle_shade('r')
                movelist += [(row,y)]
            return movelist
        else:
            for i in unshade:
                if self.tilelist[i[0]][i[1]].shade_state != 1:
                    self.tilelist[i[0]][i[1]].toggle_shade('r')


    def update(self,screen):
        while True:
            if self.progress == 1:
                self.progress = Titlescreen().update(screen,self.clock)
            elif self.progress == 2:
                self.progress = Tilemap(self.player_tile,self.tilelist).update(screen,self.clock)
            elif self.progress == 3:
                self.progress = Tilescreen().update(screen,self.clock)
            elif self.progress == 4:
                self.progress = tqc.Combatscreen(self.player,2,lambda:2).update(screen,self.clock)
                self.tilelist[self.player_tile[0]][self.player_tile[1]].toggle_shade('b')
            # move tiles
            elif self.progress == 5:
                self.movelist = self.movetiles()
                self.progress,self.player_tile = Tilemap(self.player_tile,self.tilelist).moveupdate(self.movelist,screen,self.clock)
                self.movetiles(self.movelist)


# Initialization of the game

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    Game().update(screen)


