#-------------------------------------------------------------------------------
# Name:        rockpaperscissors.py
# Purpose:     This program will simulate the classic rock paper scissors game
#
# Author:      James
#
# Created:     19/06/2014
# Copyright:   (c) James 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame, sys, random
import pygametools_0_0 as pt

class Titlescreen(object):
    def __init__(self):

        # Set up the main image that the text will be put on top of
        self.image = pygame.Surface((640,480))
        self.image.fill((255,215,0))

        # Create the opening text
        self.main_text = pt.Linesoftext(['Welcome to rock paper scissors!'],(135,50),backgroundcolor = (255,215,0))
        self.image.blit(self.main_text.image,(135,50))

        # Create the play and quit buttons
        self.playbutton = pt.Button(0,'Play',(320,260),True,surface = self.image)


        self.quitbutton = pt.Button(0,'Quit',(320,316),True)
        self.image.blit(self.quitbutton.image,self.quitbutton.pos)

    def update(self,screen,clock):
        while True:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and self.playbutton.rect.collidepoint(pygame.mouse.get_pos()):
                    return 2
                if event.type == pygame.MOUSEBUTTONUP and self.quitbutton.rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
            screen.blit(self.image,(0,0))
            pygame.display.flip()

class Mainscreen(object):
    def __init__(self):

        # Create the surface that everything will be drawn on
        self.image = pygame.Surface((640,480))
        self.image.fill((255,215,0))

        # Create the text that will be displayed to the screen
        self.main_text = pt.Linesoftext(['Choose'],(250,50),fontsize = 50,backgroundcolor = (255,215,0))
        self.image.blit(self.main_text.image,(250,50))

        # Create the rock paper and scissors buttons
        self.rockbutton = pt.Button(0,'Rock',(200,200))
        self.image.blit(*self.rockbutton.blitinfo)

        self.paperbutton = pt.Button(0,'Paper',(200,250))
        self.image.blit(*self.paperbutton.blitinfo)

        self.scissorsbutton = pt.Button(0,'Scissors',(200,300))
        self.image.blit(*self.scissorsbutton.blitinfo)

    def update(self,screen,clock):
        while True:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Choice for Rock = 1, Paper = 2, Scissors = 3
                if event.type == pygame.MOUSEBUTTONUP and self.rockbutton.rect.collidepoint(pygame.mouse.get_pos()):
                    return(3,1)
                if event.type == pygame.MOUSEBUTTONUP and self.paperbutton.rect.collidepoint(pygame.mouse.get_pos()):
                    return(3,2)
                if event.type == pygame.MOUSEBUTTONUP and self.scissorsbutton.rect.collidepoint(pygame.mouse.get_pos()):
                    return(3,3)
            screen.blit(self.image,(0,0))
            pygame.display.flip()

class Endscreen(object):
    def __init__(self):
        # create the surface that everything will be posted on
        self.image = pygame.Surface((640,480))
        self.image.fill((255,215,0))

        #Pull in the pictures that will be used
        self.rockpic = pygame.image.load('rock.png')
        self.paperpic = pygame.image.load('paper.png')
        self.scissorspic = pygame.image.load('scissors.png')

        # Now create the new game button and the quit button
        self.newgamebutton = pt.Button(0,'New Game',(320,375),True)
        self.image.blit(self.newgamebutton.image,self.newgamebutton.pos)

        self.quitbutton = pt.Button(0,'Quit',(320,425),True)
        self.image.blit(self.quitbutton.image,self.quitbutton.pos)

        # Create the different outcome texts
        self.drawtext = pt.Linesoftext(['It was a Draw'],(248,300),backgroundcolor = (255,215,0))
        self.losttext = pt.Linesoftext(['You lost'],(274,300),backgroundcolor = (255,215,0))
        self.wontext = pt.Linesoftext(['Congratulations! You won!'],(164,300),backgroundcolor = (255,215,0))

        #self.image.blit(self.wontext.image,(164,300))
        #self.image.blit(self.paperpic,(370,20))

    def checkwin(self,choice):
        # create the choice for the opponent
        self.opponentchoice = random.randint(1,3)

        # based on the choices draw the pictures and the win/lose/draw text to
        # the screen
        if choice == 1:
            if self.opponentchoice == 1:
                self.image.blit(self.rockpic,(40,20))
                self.image.blit(self.rockpic,(370,20))
                self.image.blit(self.drawtext.image,(248,300))
            elif self.opponentchoice == 2:
                self.image.blit(self.rockpic,(40,20))
                self.image.blit(self.paperpic,(370,20))
                self.image.blit(self.losttext.image,(274,300))
            elif self.opponentchoice == 3:
                self.image.blit(self.rockpic,(40,20))
                self.image.blit(self.scissorspic,(370,20))
                self.image.blit(self.wontext.image,(164,300))
        elif choice == 2:
            if self.opponentchoice == 1:
                self.image.blit(self.paperpic,(40,20))
                self.image.blit(self.rockpic,(370,20))
                self.image.blit(self.wontext.image,(164,300))
            elif self.opponentchoice == 2:
                self.image.blit(self.paperpic,(40,20))
                self.image.blit(self.paperpic,(370,20))
                self.image.blit(self.drawtext.image,(248,300))
            elif self.opponentchoice == 3:
                self.image.blit(self.paperpic,(40,20))
                self.image.blit(self.scissorspic,(370,20))
                self.image.blit(self.losttext.image,(274,300))
        elif choice == 3:
            if self.opponentchoice == 1:
                self.image.blit(self.scissorspic,(40,20))
                self.image.blit(self.rockpic,(370,20))
                self.image.blit(self.losttext.image,(274,300))
            elif self.opponentchoice == 2:
                self.image.blit(self.scissorspic,(40,20))
                self.image.blit(self.paperpic,(370,20))
                self.image.blit(self.wontext.image,(164,300))
            elif self.opponentchoice == 3:
                self.image.blit(self.scissorspic,(40,20))
                self.image.blit(self.scissorspic,(370,20))
                self.image.blit(self.drawtext.image,(248,300))

    def update(self,screen,clock,choice):
        self.checkwin(choice)
        while True:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and self.newgamebutton.rect.collidepoint(pygame.mouse.get_pos()):
                    return 2
                if event.type == pygame.MOUSEBUTTONUP and self.quitbutton.rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
            screen.blit(self.image,(0,0))
            pygame.display.flip()


class Game(object):
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.progress = 1

    def update(self,screen):
        while True:
            if self.progress == 1:
                self.progress = Titlescreen().update(screen,self.clock)
            if self.progress == 2:
                (self.progress,self.choice) = Mainscreen().update(screen,self.clock)
            if self.progress == 3:
                self.progress = Endscreen().update(screen,self.clock,self.choice)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    Game().update(screen)
