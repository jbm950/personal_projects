# ------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      James
#
# Created:     27/05/2015
# Copyright:   (c) James 2015
# Licence:     <your licence>
# ------------------------------------------------------------------------------
# !/usr/bin/env python

import pygame_toolbox.graphics as ptg
import pygame
import sys


def close():
    pygame.quit()
    sys.exit()


class Titlescreen(ptg.Menu):
    def __init__(self):
        header = ['Welcome to Fight Factory 2']
        buttons = [['Play', lambda:2], ['Quit', close]]
        ptg.Menu.__init__(self, (800, 600), (0, 200, 200), header,
                          buttons, "sports_card.wav")
        self.buttonlist += [ptg.Button(0, 'go to second screen', (300, 450),
                                       True, self.image, func=lambda:2,
                                       sound='button_click.wav')]


class Screen_two(ptg.Menu):
    def __init__(self):
        header = ['Screen two']
        buttons = [['Play', lambda:1], ['Quit', close]]
        ptg.Menu.__init__(self, (800, 600), (0, 200, 200), header, buttons)
        self.buttonlist += [ptg.Button(0, 'go to first screen', (300, 450),
                                       True, self.image, func=lambda:1,
                                       sound='button_click.wav')]


class Eventhandler:
    def __init__(self, events):
        self.events = events
        self.progress = 1
        self.clock = pygame.time.Clock()

    def update(self):
        while True:
            for i in self.events:
                if i[0] == self.progress:
                    self.progress = i[1].update(self.screen, self.clock)


class Main(Eventhandler):
    def __init__(self, screen):
        self.screen = screen
        events = [[1, Titlescreen()], [2, Screen_two()]]
        Eventhandler.__init__(self, events)


if __name__ == '__main__':
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    Main(screen).update()
