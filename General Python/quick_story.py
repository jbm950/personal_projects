#-------------------------------------------------------------------------------
# Name:        quick_story.py
# Purpose:     This program will tell a short story to test nested classes and
#              the amount of lines possible for  narritive in a set window size
#
# Author:      James
#
# Created:     22/06/2014
# Copyright:   (c) James 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame, sys
import pygametools as pt

class Titlescreen(object):
    def __init__(self):

        # Create the image that the title screen is to be written on
        self.image = pygame.Surface((800,600))
        self.image.fill((200,200,200))

        # Create the top text
        self.maintext = pt.Linesoftext(['Title Screen'],(400,20),xmid = True)
        self.image.blit(*self.maintext.blitinfo)

        # Create the Read and quit buttons
        self.readbutton = pt.Button(0,'Read',(400,400),midpoint = True)
        self.image.blit(*self.readbutton.blitinfo)

        self.quitbutton = pt.Button(0,'Quit',(400,450),midpoint = True)
        self.image.blit(*self.quitbutton.blitinfo)

    def update(self,screen,clock):
        while True:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and self.readbutton.rect.collidepoint(pygame.mouse.get_pos()):
                    return 2
                if event.type == pygame.MOUSEBUTTONUP and self.quitbutton.rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
            screen.blit(self.image,(0,0))
            pygame.display.flip()

class Storyscreen(object):
    def __init__(self):
        self.page = 1

    class Page1(object):
        def __init__(self):

            # Create the image that is going to contain the main text
            self.image = pygame.Surface((800,600))
            self.image.fill((200,200,200))

            # Start writing the story
            self.storyseg1 = pt.Linesoftext(['    Mike Dismang thinks abount the Iraqi children who shook his',
                       'hand and smiled when he told them that all would be OK in the',
                       'end.','    Zach Clark thinks about his fellow Marines killed. What he',
                       'sees on the news "has got my blood boiling" said Clark, who',
                       'came home in 2008 with head trauma and eye injuries.',
                       '    Micheal Miller, who returned scarred and hurting after an',
                       'attack on his base south of Baghdad, thinks about an Iraq that',
                       'was hopelessly cleaved by sectarian strife back when he served.',
                       'Sizing up the current insurgency that has driven the country to',
                       'the brink of collapse, Miller said, "Iraq should have been divided...'],
                       (400,20),xmid = True,fontsize = 30)
            self.image.blit(*self.storyseg1.blitinfo)

            # Create the next and quit buttons
            self.next_button = pt.Button(0,'Next',(600,550),True)
            self.image.blit(*self.next_button.blitinfo)

            self.quit_button = pt.Button(0,'Quit',(200,550),True)
            self.image.blit(*self.quit_button.blitinfo)

        def update(self,screen,clock):
            while True:
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONUP and self.quit_button.rect.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONUP and self.next_button.rect.collidepoint(pygame.mouse.get_pos()):
                        return 2
                screen.blit(self.image,(0,0))
                pygame.display.flip()

    class Page2(object):
        def __init__(self):

            # Create the image that the screen will be drawn on
            self.image = pygame.Surface((800,600))
            self.image.fill((200,200,200))

            # Create the storysegment
            self.storyseg2 = pt.Linesoftext(['up in the first place."', '    They are Kansas City area veterans of Operation Iraqi',
                       'Freedom now wondering if all was for naught.','    Some did multiple tours and thought progress was made.',
                       'Many think the progress was doomed by U.S. troops leaving too',
                       'soon',"    Others say their country should never have invaded, and",
                       " they're not suprised that Iraq's"],(400,20),True)
            self.image.blit(*self.storyseg2.blitinfo)

            # Create the Next, Back and quit buttons
            self.next_button = pt.Button(0,'Next',(600,550),True)
            self.image.blit(*self.next_button.blitinfo)

            self.back_button = pt.Button(0,'Back',(400,550),True)
            self.image.blit(*self.back_button.blitinfo)

            self.quit_button = pt.Button(0,'Quit',(200,550),True)
            self.image.blit(*self.quit_button.blitinfo)

        def update(self,screen,clock):
            while True:
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONUP and self.quit_button.rect.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONUP and self.back_button.rect.collidepoint(pygame.mouse.get_pos()):
                        return 1
                    if event.type == pygame.MOUSEBUTTONUP and self.next_button.rect.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()
                screen.blit(self.image,(0,0))
                pygame.display.flip()

    def update(self,screen,clock):
        while True:
            if self.page == 1:
                self.page = self.Page1().update(screen,clock)
            if self.page == 2:
                self.page = self.Page2().update(screen,clock)

class Game(object):
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.progress = 1

    def update(self,screen):
        while True:
            if self.progress == 1:
                self.progress = Titlescreen().update(screen,self.clock)
            if self.progress == 2:
               self.progress = Storyscreen().update(screen,self.clock)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    Game().update(screen)
