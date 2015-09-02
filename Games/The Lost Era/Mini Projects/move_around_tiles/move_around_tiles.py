# ------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      James
#
# Created:     26/01/2015
# Copyright:   (c) James 2015
# Licence:     <your licence>
# ------------------------------------------------------------------------------
# !/usr/bin/env python

import pygame
import pygame_toolbox.graphics as ptg
import pygame_toolbox.graphics.widgets as ptgw
import pygame_toolbox.tilegame_tools as pttt


class monster(object):
    def __init__(self, monsternum):
        # Open up the text file with the monster data and prepare a list of the
        # different lines of data
        self.rawdata = open('monsterdata.txt')
        self.rawdata = self.rawdata.readlines()[monsternum].split(',')

        # Take the raw data and set the monsters attributes
        self.name = self.rawdata[0]
        self.tile = ptgw.wTile(self.name, self.rawdata[1], (150, 150))
        self.tile.initialize_shade('black', (0, 0, 0), 235)
        self.hp = int(self.rawdata[2])
        self.damage = int(self.rawdata[3])
        self.hpmax = int(self.rawdata[4])


class army(list):
    def shade_monster(self, monster, color):
        self[monster].tile.toggle_shade(color)

    def check_defeat(self):
        # 0 means still have a living monster
        for i in self:
            if i.hp > 0:
                return 0
        return 1


class Tile(pttt.Tile):
    def __init__(self):
        pttt.Tile.__init__(self, "Forrest.png", (200, 150))
        self.army = None
        self.armyflag = ptg.Button(1, 'flag.png', (0, 0), resize=(200, 150))
        self.armyflag.image.set_colorkey((255, 255, 255))

    def initialize_army(self, army):
        self.army = army
        self.image.blit(*self.armyflag.blitinfo)

    def remove_army(self):
        """This method will clear the army attribute and take the flag off of
        the image
        """
        self.army = None
        self.image.blit(self.pic, (0, 0))

    def toggle_shade(self, shade):
        pttt.Tile.toggle_shade(self, shade)
        if self.army:
            self.initialize_army(self.army)


class Tilemap(pttt.Tilemap):
    def __init__(self, tilelist):
        pttt.Tilemap.__init__(self, (800, 600), tilelist, 1)

    def move_update(self, tileclicked, screen, clock):
        adj_tiles = self.tilelist.adjacent_tiles(tileclicked, 'p')
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
            tileclicked2move = self.update(screen, clock)
            if tileclicked2move in adj_tiles:
                waiting = 0
                tileclicked2move.initialize_army(tileclicked.army)
            elif tileclicked2move in army_present:
                tempmenu = Combinearmymenu(tileclicked, tileclicked2move)
                waiting = tempmenu.update(screen, clock)
                if not waiting:
                    tileclicked2move.army += tileclicked.army
        for i in adj_tiles:
            i.toggle_shade('red')
        for i in army_present:
            i.toggle_shade('blue')
        tileclicked.remove_army()


class Tilemenu(ptg.Menu):
    def __init__(self, tileclicked):
        if tileclicked.army:
            header = ['Choose an Action']
            buttons = [['View', lambda:4], ['Move', lambda:5],
                       ['Return', lambda:1]]
        else:
            header = ['No Army Present']
            buttons = [['Return', lambda:1]]
        ptg.Menu.__init__(self, (500, 400), (255, 69, 0), header, buttons)
        ptg.Menu.set_offset(self, (400, 300), mid='c')


class Armyview(ptg.Menu):
    def __init__(self, army):
        header = ['Army View']
        buttons = []
        ptg.Menu.__init__(self, (500, 400), (255, 69, 0), header, buttons)
        self.buttonlist += [ptg.Button(0, 'Return', (250, 350), True,
                                       self.image, func=lambda:2)]
        self.buttonlist += [ptg.Button(0, 'Split', (250, 300), True,
                                       self.image, func=lambda:6)]

        for i in army:
            self.image.blit(i.tile.image,
                            ((army.index(i)+1)*12+army.index(i)*150, 100))

        ptg.Menu.set_offset(self, (400, 300), mid='c')


class Combinearmymenu(ptg.Menu):
    def __init__(self, original_tile, final_tile):
        if len(original_tile.army) + len(final_tile.army) > 3:
            header = ['Too many monsters', 'present to combine armies']
            buttons = [['Return', lambda:1]]
        else:
            header = ['Would you like to combine armies?']
            buttons = [['yes', lambda:0], ['no', lambda:1]]
        ptg.Menu.__init__(self, (500, 400), (255, 69, 0), header, buttons)
        ptg.Menu.set_offset(self, (400, 300), mid='c')


class Splitarmymenu(ptg.Menu):
    def __init__(self, army):
        header = ['Choose the units for the new army']
        buttons = []
        ptg.Menu.__init__(self, (500, 400), (255, 69, 0), header, buttons)
        self.buttonlist += [ptg.Button(0, 'Return', (250, 350), True,
                                       self.image, func=lambda:4)]
        self.buttonlist += [ptg.Button(0, 'Split', (250, 300), True,
                                       self.image, func=lambda:7)]

        self.army = army

        for i in army:
            i.tile.set_position(((army.index(i)+1)*12+army.index(i)*150, 100),
                                surface=self.image)
            i.tile.func = toggle_unit
            self.widgetlist.append(i.tile)

        ptg.Menu.set_offset(self, (400, 300), mid='c')


def toggle_unit(unit, menu):
    unit.toggle_shade('blue')
    if unit.status:
        unit.status = 0
    else:
        unit.status = 1
    menu.__init__(menu.army)


class Splitarmyerror(ptg.Menu):
    def __init__(self, error_flag):
        """error_flag = 1 - too few units to split
        error_flag = 2 - can't split all units
        """
        if error_flag == 1:
            header = ["Can't split an army of one"]
            buttons = [['Return', lambda: 4]]
        elif error_flag == 2:
            header = ["Need at least one unit to remain"]
            buttons = [['Return', lambda: 6]]

        ptg.Menu.__init__(self, (400, 300), (60, 69, 255), header, buttons)
        ptg.Menu.set_offset(self, (400, 300), mid='c')


class Mainhandle(ptg.Eventhandler):
    def __init__(self, screen):
        self.tilelist = pttt.Tilelist([[Tile() for i in range(0, 4)],
                                       [Tile() for i in range(0, 4)],
                                       [Tile() for i in range(0, 4)],
                                       [Tile() for i in range(0, 4)]])
        events = [[1, self.Tilemaphandle],
                  [2, self.Tilemenuhandle],
                  [4, self.Armyviewhandle],
                  [5, self.Movehandle],
                  [6, self.Splitarmymenuhandle],
                  [7, self.Armyprocess]]
        ptg.Eventhandler.__init__(self, events, screen)
        self.tilelist[0][1].initialize_army(army([monster(0), monster(1)]))
        self.tilelist[2][2].initialize_army(army([monster(3), monster(4),
                                                  monster(5)]))
        self.tilelist[0][2].initialize_army(army([monster(2)]))

    def Tilemaphandle(self, screen, clock):
        self.tileclicked = Tilemap(self.tilelist).update(screen, self.clock)
        return 2

    def Tilemenuhandle(self, screen, clock):
        return Tilemenu(self.tileclicked).update(screen, clock)

    def Armyviewhandle(self, screen, clock):
        temp = Armyview(self.tileclicked.army).update(screen, clock)

        if temp == 6:
            if len(self.tileclicked.army) == 1:
                return Splitarmyerror(1).update(screen, clock)
            else:
                return temp
        return temp

    def Movehandle(self, screen, clock):
        Tilemap(self.tilelist).move_update(self.tileclicked, screen, self.clock)
        return 1

    def Splitarmymenuhandle(self, screen, clock):
        tempmenu = Splitarmymenu(self.tileclicked.army)
        [progress, self.split_status] = tempmenu.update(screen, self.clock)

        if progress == 4:
            for i in self.tileclicked.army:
                if i.tile.shades['blue'][0]:
                    i.tile(Splitarmymenu(self.tileclicked.army))

        return progress

    def Armyprocess(self, screen, clock):
        temp_army = army([])
        for i in self.split_status:
            if i[1] == 0:
                current_index = self.split_status.index(i)
                temp_army.append(self.tileclicked.army[current_index])
        if len(temp_army) == 0:
            return Splitarmyerror(2).update(screen, self.clock)
        else:
            for i in temp_army:
                self.tileclicked.army.remove(i)
            for i in self.tileclicked.army:
                i.tile(Splitarmymenu(self.tileclicked.army))
            Tilemap(self.tilelist).move_update(self.tileclicked, screen,
                                               self.clock)
            self.tileclicked.initialize_army(temp_army)
            return 1


class Main(object):
    def __init__(self):
        self.progress = 1
        self.clock = pygame.time.Clock()
        self.tilelist = pttt.Tilelist([[Tile() for i in range(0, 4)],
                                       [Tile() for i in range(0, 4)],
                                       [Tile() for i in range(0, 4)],
                                       [Tile() for i in range(0, 4)]])

        self.tilelist[0][1].initialize_army(army([monster(0), monster(1)]))
        self.tilelist[2][2].initialize_army(army([monster(3), monster(4),
                                                  monster(5)]))
        self.tilelist[0][2].initialize_army(army([monster(2)]))

    def update(self, screen):
        while True:
            if self.progress == 1:
                tileclicked = Tilemap(self.tilelist).update(screen, self.clock)
                self.progress = 2
            elif self.progress == 2:
                self.progress = Tilemenu(tileclicked).update(screen, self.clock)
            elif self.progress == 4:
                self.progress = Armyview(tileclicked.army).update(screen,
                                                                  self.clock)
                if self.progress == 6:
                    if len(tileclicked.army) == 1:
                        self.progress = Splitarmyerror(1).update(screen,
                                                                 self.clock)
            elif self.progress == 5:
                Tilemap(self.tilelist).move_update(tileclicked,
                                                   screen, self.clock)
                self.progress = 1
            elif self.progress == 6:
                tempmenu = Splitarmymenu(tileclicked.army)
                [self.progress, self.split_status] = tempmenu.update(screen,
                                                                     self.clock)
                if self.progress == 4:
                    for i in tileclicked.army:
                        if i.tile.shades['blue'][0]:
                            i.tile(Splitarmymenu(tileclicked.army))
            elif self.progress == 7:
                temp_army = army([])
                for i in self.split_status:
                    if i[1] == 0:
                        current_index = self.split_status.index(i)
                        temp_army.append(tileclicked.army[current_index])
                if len(temp_army) == 0:
                    self.progress = Splitarmyerror(2).update(screen, self.clock)
                else:
                    for i in temp_army:
                        tileclicked.army.remove(i)
                    for i in tileclicked.army:
                        i.tile(Splitarmymenu(tileclicked.army))
                    Tilemap(self.tilelist).move_update(tileclicked, screen,
                                                       self.clock)
                    tileclicked.initialize_army(temp_army)
                    self.progress = 1


if __name__ == '__main__':
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    Mainhandle(screen).update()
