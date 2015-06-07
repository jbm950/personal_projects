#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      James
#
# Created:     01/06/2015
# Copyright:   (c) James 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame_toolbox.graphics as ptg
import pygame_toolbox.graphics.widgets as ptgw
import pygame, sys, random

def close():
    pygame.quit()
    sys.exit()

class Screen_1(ptg.Menu):
    def __init__(self):
        self.header = ['Screen 1']
        self.buttons = [['Screen 2',lambda:2],['Quit',close]]
        ptg.Menu.__init__(self,(800,600),(150,69,69),self.header,self.buttons)

        self.widgetlist += [ptgw.Checkbox("option a",(200,200),(17,17),True,self.image,'c')]

class Screen_2(ptg.Menu):
    def __init__(self,widget_info):
        header = ['Screen 2','%s was %s' % (widget_info[0][0],bool(widget_info[0][1]))]
        buttons = [['Screen 1',lambda:1],['Quit',close]]
        ptg.Menu.__init__(self,(800,600),(150,69,150),header,buttons)

class Main(object):
    def __init__(self):
        self.progress = 1
        self.clock = pygame.time.Clock()

    def update(self,screen):
        while True:
            if self.progress == 1:
                self.progress = Screen_1().update(screen,self.clock)
                self.widget_info = self.progress[1]
                self.progress = self.progress[0]
            elif self.progress == 2:
                self.progress = Screen_2(self.widget_info).update(screen,self.clock)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    Main().update(screen)