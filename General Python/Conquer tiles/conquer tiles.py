#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     This is a game where a map of 3x3 tiles is to be conquered by a
#              player using the combat engine from torric's quest
#
# Author:      James
#
# Created:     18/08/2014
# Copyright:   (c) James 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame,sys,random
import pygametools_0_4 as pt
import torrics_quest_combat as tqc

def close():
    pygame.quit()
    sys.exit()

class Tile(pt.Tile):
    def __init__(self,pic):
        pt.Tile.__init__(self,pic,(267,200))

        if pic == 'Forrest.png':
            self.monnum = 2
        if pic == 'Grassland.png':
            self.monnum = 1
        if pic == 'Mountains.png':
            self.monnum = 3

        self.conquered = 0

class Titlescreen(pt.Menu):
    def __init__(self):
        header = ['Welcome to Conquer the Tiles']
        buttons = [['Play',lambda:2],['Quit',close]]
        pt.Menu.__init__(self,(800,600),'background.png',header,buttons)

# Tilemap
class Tilemap():
    def __init__(self,player_tile,tilelist):
        # Create the image that the map will be drawn on
        self.image = pygame.Surface((800,600))

        # Create the list of tile objects and draw them on the screen
        self.tilelist = tilelist
        for x in range(0,800,267):
            for y in range(0,600,200):
                self.image.blit(self.tilelist[x // 267][y // 200].image,(x,y))
                self.tilelist[x // 267][y // 200].set_position(x,y)

        # Create the image showing the tile the player is located on
        playerpos_xy = [player_tile[0] * 267,player_tile[1] * 200]
        self.playerpic = pt.Button(1,'Player.png',playerpos_xy,resize = (267,200))
        self.playerpic.image.set_colorkey((255,255,255))
        self.image.blit(*self.playerpic.blitinfo)

        self.playerpos_tile = player_tile

    def movetiles(self,tilelist,player_tile,unshade = None):
        if unshade == None:
            row = player_tile[0]
            col = player_tile[1]
            movelist = []
            switchshaderows = []
            switchshadecols = []

            if row - 1 >= 0:
                switchshaderows = [row - 1]
            if row + 1 <= 2:
                switchshaderows += [row + 1]
            if col - 1 >= 0:
                switchshadecols = [col - 1]
            if col + 1 <= 2:
                switchshadecols += [col + 1]
            for x in switchshaderows:
                if tilelist[x][col].shade_state != 1:
                    tilelist[x][col].toggle_shade('r')
                movelist += [(x,col)]
            for y in switchshadecols:
                if tilelist[row][y].shade_state != 1:
                    tilelist[row][y].toggle_shade('r')
                movelist += [(row,y)]
            return movelist
        else:
            for i in unshade:
                if tilelist[i[0]][i[1]].shade_state != 1:
                    tilelist[i[0]][i[1]].toggle_shade('r')

    def update(self,screen,clock):
            while True:
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONUP and self.playerpic.rect.collidepoint(pygame.mouse.get_pos()):
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

class Tilescreen(pt.Menu):
    def __init__(self):
        header = ['Choose your action']
        buttons = [['Fight',lambda:4],['Move',lambda:5]]
        pt.Menu.__init__(self,(300,300),(255,69,0),header,buttons)
        pt.Menu.set_offset(self,(250,150))

class Winscreen(pt.Menu):
    def __init__(self):
        header = ['Congratulations!','    You\'ve won!']
        buttons = [['Play again?',lambda:1],['Quit',close]]
        pt.Menu.__init__(self,(800,600),'background.png',header,buttons)

# Class that holds all of the game's data and mechanics
class Game(object):
    def __init__(self):
        self.player = tqc.Player(4)
        self.player_tile = [0,0]

        self.tilechance = ['Forrest.png'] * 3 + ['Grassland.png'] * 5 + ['Mountains.png'] * 2
        self.tilelist = []
        for i in range(0,3):
            self.tilelist.append([])
            for x in range(0,3):
                self.tilelist[i].append(Tile(random.choice(self.tilechance)))

        self.movelist = []

    def check_win(self):
        win = 1
        for i in range (0,3):
            for x in range(0,3):
                if self.tilelist[i][x].conquered == 0:
                    win = 0
        return win


class Main(object):
    def __init__(self):
        self.progress = 1
        self.clock = pygame.time.Clock()

    def update(self,screen):
        while True:
            if self.progress == 1:
                self.progress = Titlescreen().update(screen,self.clock)
                self.data = Game()
            elif self.progress == 2:
                self.progress = Tilemap(self.data.player_tile,self.data.tilelist).update(screen,self.clock)
            elif self.progress == 3:
                self.progress = Tilescreen().update(screen,self.clock)
            elif self.progress == 4:
                self.progress = tqc.Combatscreen(self.data.player,
                                                 self.data.tilelist[self.data.player_tile[0]][self.data.player_tile[1]].monnum,
                                                 lambda:2).update(screen,self.clock)
                self.data.tilelist[self.data.player_tile[0]][self.data.player_tile[1]].conquered = 1
                self.data.tilelist[self.data.player_tile[0]][self.data.player_tile[1]].toggle_shade('b')
                if self.data.check_win():
                    self.progress = 6

            elif self.progress == 5:
                self.data.movelist = Tilemap.movetiles(self,self.data.tilelist,self.data.player_tile)
                self.progress,self.data.player_tile = Tilemap(self.data.player_tile,self.data.tilelist).moveupdate(self.data.movelist,screen,self.clock)
                Tilemap.movetiles(self,self.data.tilelist,self.data.player_tile,self.data.movelist)
            elif self.progress == 6:
                self.progress = Winscreen().update(screen,self.clock)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    Main().update(screen)
