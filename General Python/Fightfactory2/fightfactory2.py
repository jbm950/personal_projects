#-------------------------------------------------------------------------------
# Name:        fightfactory2
# Purpose:
#
# Author:      James
#
# Created:     09/09/2014
# Copyright:   (c) James 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame,sys,random,csv
import pygametools as pt

class army(object):
    def __init__(self,monster_list):
        self.monster_list = monster_list
    def shade_monster(self,monster,color):
        self.monster_list[monster].tile.toggle_shade(color)
    def check_defeat(self):
        # 0 means still have a living monster
        for i in self.monster_list:
            if i.hp > 0:
                return 0
        return 1
    def __getitem__(self,index):
        return self.monster_list[index]
    def __add__(self,item):
        self.monster_list += item
        return self
    def __sub__(self,item):
        self.monster_list.remove(item)
        return self

class monster(object):
    def __init__(self,monsternum):
        # Open up the text file with the monster data and prepare a list of the
        # different lines of data
        self.rawdata = list(csv.reader(open('monsterdata.txt')))[monsternum]

        # Take the raw data and set the monsters attributes
        self.name = self.rawdata[0]
        self.tile = pt.Tile(self.rawdata[1],(150,150))
        self.tile.initialize_shade('black',(0,0,0),235)
        self.hp = int(self.rawdata[2])
        self.damage = int(self.rawdata[3])
        self.hpmax = int(self.rawdata[4])


def attack(attacker,target):
    target.hp -= attacker.damage

def close():
    pygame.quit()
    sys.exit()

class Titlescreen(pt.Menu):
    def __init__(self):
        header = ['Welcome to Fight Factory 2']
        buttons = [['Play',lambda:2],['Quit',close]]
        pt.Menu.__init__(self,(1000,800),(0,200,200),header,buttons)

class Combatscreens:
    def __init__(self):
        # create the player and monster's armies
        self.playerarmy = army([monster(0),monster(1)])
        self.playerarmy += [monster(2)]
        extramonster = monster(2)
        self.monsterarmy = army([monster(3),monster(4),monster(5),extramonster])
        self.monsterarmy -= extramonster
        self.page = 1
        self.image = pygame.Surface((1000,800))
        self.actionlist = []
        self.mon_choosing = 0
        self.pos = (0,0)
        print()

    def combat(self):
        for i in range(0,3):
            if self.actionlist[i] == 'Pass':
                pass
            else:
                self.actionlist[i][0](*self.actionlist[i][1:3])
                if self.actionlist[i][2].hp <= 0:
                    self.actionlist[i][2].hp = 0
                    self.actionlist[i][2].tile.toggle_shade('black')
            if self.monsterarmy[i].hp > 0:
                choice = monster(2)
                choice.hp = 0
                while choice.hp == 0:
                    choice = random.choice(self.playerarmy.monster_list)
                choice.hp -= self.monsterarmy[i].damage
                if choice.hp <= 0:
                    choice.hp = 0
                    choice.tile.toggle_shade('black')


    def draw_main(self):
        self.image.fill((0,200,200))
        def drawside(self,army,side):
            if side == 1:
                x = (150,115)
            elif side == 2:
                x = (700,665)
            for i in army:
                y = 85 + army.monster_list.index(i) * 200
                self.image.blit(i.tile.image,(x[0],y))
                i.tile.set_position((x[0],y))

                y2 = y - 30
                hpbar = pygame.Rect((x[0],y2),(int(150 * i.hp/i.hpmax),20))
                pygame.draw.rect(self.image,(255,0,0),hpbar)

                hptext = pt.Linesoftext(['Hp                                 %d/%d' % (i.hp,i.hpmax)],
                                        (x[1],y2),surface = self.image,fontsize = 28)

        drawside(self,self.playerarmy,1)
        drawside(self,self.monsterarmy,2)

    def choose_action(self,screen,clock):
        self.playerarmy.shade_monster(self.mon_choosing,'blue')

        self.draw_main()

        self.buttonlist = [pt.Button(0,'Fight',(350,700),True,self.image,func = lambda:1,sound = 'button_click.wav')]
        self.buttonlist += [pt.Button(0,'Pass',(550,700),True,self.image,func = lambda:2,sound = 'button_click.wav')]

        return pt.Menu.update(self,screen,clock)

    def choose_target(self,screen,clock):
        self.buttonlist = []
        for i in self.monsterarmy.monster_list:
            if i.hp > 0:
                i.tile.toggle_shade('red')
                self.buttonlist += [i.tile]

        self.draw_main()

        pt.Linesoftext(['Choose your target!'],(500,700),True,self.image)

        def ct_update(self,screen,clock):
            # handle the events of the title screen
            while True:
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        close()
                    for i in self.buttonlist:
                        if event.type == pygame.MOUSEBUTTONUP and i.rect.collidepoint(pygame.mouse.get_pos()):
                            for j in self.monsterarmy:
                                if j.tile.shades['red'][0]:
                                    j.tile.toggle_shade('red')
                                if j.tile == i:
                                    target = j
                            return target

                screen.blit(self.image,(0,0))
                pygame.display.flip()

        return ct_update(self,screen,clock)

    def display_results(self,screen,clock):
        self.draw_main()
        self.buttonlist = [pt.Button(0,'Continue',(500,700),True,self.image,func = lambda:1,sound = 'button_click.wav')]

        return pt.Menu.update(self,screen,clock)

    def final_page(self,screen,clock,result):
        self.draw_main()
        self.buttonlist = [pt.Button(0,'End',(550,750),True,self.image,func = close,sound = 'button_click.wav')]
        self.buttonlist += [pt.Button(0,'Play again?',(420,750),True,self.image,func = lambda:5,sound = 'button_click.wav')]
        if result == 0:
            pt.Linesoftext(['You lost!'],(500,700),True,self.image)
        elif result == 1:
            pt.Linesoftext(['You won!'],(500,700),True,self.image)

        return pt.Menu.update(self,screen,clock)

    def update(self,screen,clock):
        while True:
            if self.page == 1:
                choice = self.choose_action(screen,clock)
                if choice == 1:
                    self.page = 2
                elif choice == 2:
                    self.actionlist += ['Pass']
                    self.playerarmy.shade_monster(self.mon_choosing,'blue')
                    if self.mon_choosing != 2:
                        self.mon_choosing += 1
                        if self.playerarmy.monster_list[self.mon_choosing].hp == 0:
                            self.actionlist += ['Pass']
                            if self.mon_choosing != 2:
                                self.mon_choosing += 1
                            else:
                                self.page = 3
                            if self.playerarmy.monster_list[self.mon_choosing].hp == 0:
                                self.actionlist += ['Pass']
                                self.page = 3
                    else: self.page = 3

            elif self.page == 2:
                self.page = 1
                self.actionlist += [[attack,self.playerarmy[self.mon_choosing],self.choose_target(screen,clock)]]
                self.playerarmy.shade_monster(self.mon_choosing,'blue')
                if self.mon_choosing != 2:
                    self.mon_choosing += 1
                    if self.playerarmy.monster_list[self.mon_choosing].hp == 0:
                        self.actionlist += ['Pass']
                        if self.mon_choosing != 2:
                            self.mon_choosing += 1
                            if self.playerarmy.monster_list[self.mon_choosing].hp == 0:
                                self.actionlist += ['Pass']
                                self.page = 3
                        else:
                            self.page = 3

                else: self.page = 3

            elif self.page == 3:
                self.combat()
                if self.playerarmy.check_defeat():
                    self.result = 0
                    self.page = 4
                elif self.monsterarmy.check_defeat():
                    self.result = 1
                    self.page = 4
                if self.playerarmy.monster_list[0].hp > 0:
                    self.actionlist = []
                    self.mon_choosing = 0
                elif self.playerarmy.monster_list[1].hp > 0:
                    self.actionlist = ['Pass']
                    self.mon_choosing = 1
                else:
                    self.actionlist = ['Pass','Pass']
                    self.mon_choosing = 2
                if self.page == 3:
                    self.page = self.display_results(screen,clock)

            elif self.page == 4:
                self.page = self.final_page(screen,clock,self.result)

            elif self.page == 5:
                self.__init__()

class Main(object):
    def __init__(self):
        self.progress = 1
        self.clock = pygame.time.Clock()

    def update(self,screen):
        while True:
            if self.progress == 1:
                self.progress = Titlescreen().update(screen,self.clock)
            elif self.progress == 2:
                self.progress = Combatscreens().update(screen,self.clock)


if __name__ == '__main__':
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    screen = pygame.display.set_mode((1000,800))
    Main().update(screen)

