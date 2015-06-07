#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      James
#
# Created:     26/01/2015
# Copyright:   (c) James 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame,sys
import pygame_toolbox.graphics as ptg
import pygame_toolbox.tilegame_tools as pttt

pygame.init()
screen = pygame.display.set_mode((800,600))

class monster(object):
    def __init__(self,monsternum):
        # Open up the text file with the monster data and prepare a list of the
        # different lines of data
        self.rawdata = open('monsterdata.txt')
        self.rawdata = self.rawdata.readlines()[monsternum].split(',')

        # Take the raw data and set the monsters attributes
        self.name = self.rawdata[0]
        self.tile = pttt.Tile(self.rawdata[1],(150,150))
        self.tile.initialize_shade('black',(0,0,0),235)
        self.hp = int(self.rawdata[2])
        self.damage = int(self.rawdata[3])
        self.hpmax = int(self.rawdata[4])

class army(list):
    def shade_monster(self,monster,color):
        self[monster].tile.toggle_shade(color)
    def check_defeat(self):
        # 0 means still have a living monster
        for i in self:
            if i.hp > 0:
                return 0
        return 1

class Tile(pttt.Tile):
    def __init__(self):
        pttt.Tile.__init__(self,"forrest.png",(200,150))
        self.army = None
        self.armyflag = ptg.Button(1,'flag.png',(0,0),resize = (200,150))
        self.armyflag.image.set_colorkey((255,255,255))

    def initialize_army(self,army):
        self.army = army
        self.image.blit(*self.armyflag.blitinfo)

    def remove_army(self):
        self.army = None
        self.image.blit(self.pic,(0,0))

    def toggle_shade(self,shade):
        pttt.Tile.toggle_shade(self,shade)
        if self.army:
            self.initialize_army(self.army)


class Tilemap(pttt.Tilemap):
    def __init__(self,tilelist):
        pttt.Tilemap.__init__(self,(800,600),tilelist,1)

    def move_update(self,tileclicked,screen,clock):
        adj_tiles = self.tilelist.adjacent_tiles(tileclicked,'p')
        army_present = []
        for i in adj_tiles:
            if i.army is None:
                i.toggle_shade('red')
            else:
                army_present += [i]
                i.toggle_shade('blue')
        for i in army_present:
            adj_tiles.remove(i)
        self.__init__(self.tilelist)
        waiting = 1
        while waiting:
            tileclicked2move = self.update(screen,clock)
            if tileclicked2move in adj_tiles:
                waiting = 0
                tileclicked2move.initialize_army(tileclicked.army)
            elif tileclicked2move in army_present:
                waiting = Combinearmymenu(tileclicked,tileclicked2move).update(screen,clock)
                if not waiting:
                    tileclicked2move.army += tileclicked.army
        for i in adj_tiles:
            i.toggle_shade('red')
        for i in army_present:
            i.toggle_shade('blue')
        tileclicked.remove_army()

class Tilemenu(ptg.Menu):
    def __init__(self,tileclicked):
        if tileclicked.army:
            header = ['Choose an Action']
            buttons = [['View',lambda:4],['Move',lambda:5],['Return',lambda:1]]
        else:
            header = ['No Army Present']
            buttons = [['Return',lambda:1]]
        ptg.Menu.__init__(self,(500,400),(255,69,0),header,buttons)
        ptg.Menu.set_offset(self,(400,300),mid = 'c')

class Armyview(ptg.Menu):
    def __init__(self,army):
        header = ['Army View']
        buttons = []
        ptg.Menu.__init__(self,(500,400),(255,69,0),header,buttons)
        self.buttonlist += [ptg.Button(0,'Return',(250,350),True,self.image,func = lambda:2)]
        self.buttonlist += [ptg.Button(0,'Split',(250,300),True,self.image,func = lambda:6)]

        for i in army:
            self.image.blit(i.tile.image,((army.index(i)+1)*12+army.index(i)*150,100))

        ptg.Menu.set_offset(self,(400,300),mid = 'c')

class Combinearmymenu(ptg.Menu):
    def __init__(self,original_tile,final_tile):
        if len(original_tile.army) + len(final_tile.army) > 3:
            header = ['Too many monsters', 'present to combine armies']
            buttons = [['Return',lambda:1]]
        else:
            header = ['Would you like to combine armies?']
            buttons = [['yes',lambda:0],['no',lambda:1]]
        ptg.Menu.__init__(self,(500,400),(255,69,0),header,buttons)
        ptg.Menu.set_offset(self,(400,300),mid = 'c')

class Splitarmymenu(ptg.Menu):
    def __init__(self,army):
        header = ['Choose the units for the new army']
        buttons = []
        ptg.Menu.__init__(self,(500,400),(255,69,0),header,buttons)
        self.buttonlist += [ptg.Button(0,'Return',(250,350),True,self.image,func = lambda:4)]
        self.buttonlist += [ptg.Button(0,'Split',(250,300),True,self.image,func = lambda:1)]

        for i in army:
            self.image.blit(i.tile.image,((army.index(i)+1)*12+army.index(i)*150,100))

        ptg.Menu.set_offset(self,(400,300),mid = 'c')

class Main(object):
    def __init__(self):
        self.progress = 1
        self.clock = pygame.time.Clock()
        self.tilelist = pttt.Tilelist([[Tile() for i in range(0,4)],
                                       [Tile() for i in range(0,4)],
                                       [Tile() for i in range(0,4)],
                                       [Tile() for i in range(0,4)]])


        self.tilelist[0][1].initialize_army(army([monster(0),monster(1)]))
        self.tilelist[2][2].initialize_army(army([monster(3),monster(4),monster(5)]))
        self.tilelist[0][2].initialize_army(army([monster(2)]))

    def update(self,screen):
        while True:
            if self.progress == 1:
                tileclicked = Tilemap(self.tilelist).update(screen,self.clock)
                self.progress = 2
            elif self.progress == 2:
                self.progress = Tilemenu(tileclicked).update(screen,self.clock)
            elif self.progress == 4:
                self.progress = Armyview(tileclicked.army).update(screen,self.clock)
            elif self.progress == 5:
                Tilemap(self.tilelist).move_update(tileclicked,screen,self.clock)
                self.progress = 1
            elif self.progress == 6:
                self.progress = Splitarmymenu(tileclicked.army).update(screen,self.clock)

if __name__ == '__main__':
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    Main().update(screen)








