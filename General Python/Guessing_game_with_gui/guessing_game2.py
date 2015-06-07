#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      James
#
# Created:     17/06/2014
# Copyright:   (c) James 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame, sys, random

class Button(pygame.sprite.Sprite):
    def __init__(self,type_of_button,fileortext,position):
        """This class will help make quick buttons for use with pygame
        if 0 is passed into type of button a text button will be made and if a
        1 is passed a picture button will be made"""
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()
        basicfont = pygame.font.Font(None,36)
        self.pos = position
        #Create a text button

        if type_of_button == 0:

            # Create the text surface and find the size and midpoint of that surface

            self.text = basicfont.render(fileortext,0,(1,1,1))
            self.textsize = self.text.get_size()
            self.textmidp = (int(self.textsize[0] * 0.5),int(self.textsize[1] * 0.5))

            # Create the background box

            self.image = pygame.Surface((int(self.textsize[0] * 1.25),int(self.textsize[1] * 1.429)))
            self.imagesize = self.image.get_size()
            self.imagemidp = (int(self.imagesize[0] * 0.5),int(self.imagesize[1] * 0.5))
            self.image.fill((67,110,238))

            # Center the text at the center of the box

            self.image.blit(self.text,(self.imagemidp[0]-self.textmidp[0],self.imagemidp[1]-self.textmidp[1]))

        # Create a picture button

        elif type_of_button ==1:
            self.image = pygame.image.load(fileortext)
        self.rect = pygame.Rect(position,self.image.get_size())

class Linesoftext(object):
    def __init__(self,text,fontsize = 36):
        """This object will create an image of text that is passed in as a list
        of strings. It will put a new line for each element in the list. Use its
        image attribute to put this text on your screen"""
        pygame.font.init()
        basicfont = pygame.font.Font(None,fontsize)

        # Figure out the size of the image that will be drawn on and create that
        # image
        self.linewidths = []
        for x in text:
            self.texttemp = basicfont.render(x,0,(1,1,1))
            self.linewidths.append(self.texttemp.get_width())
        self.imagewidth = basicfont.render(text[self.linewidths.index(max(self.linewidths))],0,(1,1,1)).get_width()
        self.imageheight = len(text) * fontsize + (len(text)-1) * 10
        self.image = pygame.Surface((self.imagewidth,self.imageheight))
        self.image.fill((200,200,200))

        # Draw the text to the image
        n = 0
        for x in text:
            self.texttemp = basicfont.render(x,0,(1,1,1))
            self.image.blit(self.texttemp,(0,n * fontsize + n * 10))
            n +=1



class Openingscreen(object):
    def __init__(self):

        # Create the opening remarks about how the game works
        self.openingtext = ['Hello Contestant!','   In this game I will attempt to guess a number','between 1 and 500 that you choose at random.'
                            ,'Wish me Luck!','(Click ready when you have chosen your number)']
        self.openingtextimage = Linesoftext(self.openingtext)

        # Create the ready button

        self.ready_button = Button(0,'Ready?',(275,300))

        # prepare the image for the screen
        self.image = pygame.Surface((640,480))
        self.image.fill((200,200,200))
        self.image.blit(self.ready_button.image,self.ready_button.pos)
        self.image.blit(self.openingtextimage.image,(20,20))
    def update(self,screen,clock):
        while True:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and self.ready_button.rect.collidepoint(pygame.mouse.get_pos()):
                    return 2
            screen.blit(self.image,(0,0))
            pygame.display.flip()

class Mainscreen(object):
    def __init__(self):
        self.low = 0
        self.high = 501
        self.image = pygame.Surface((640,480))
        self.n = 0

    def makeguess(self):

        self.n +=1

        # Clear the screen from the previous guess
        self.image.fill((200,200,200))

        # Make a guess at the players number
        try:
            self.guess = random.randint(self.low + 1,self.high - 1)
            self.maintext = Linesoftext(['I guess that your number is','',
                                     '                      %d' % self.guess],50)
        except:
            self.maintext = Linesoftext(['You Fail!'],50)

        self.image.blit(self.maintext.image,(90,40))

        # Make the Low, Correct and High buttons
        self.lowbutton = Button(0,'Low',(100,300))
        self.image.blit(self.lowbutton.image,self.lowbutton.pos)

        self.correctbutton = Button(0,'Correct',(275,300))
        self.image.blit(self.correctbutton.image,self.correctbutton.pos)

        self.highbutton = Button(0,'High',(500,300))
        self.image.blit(self.highbutton.image,self.highbutton.pos)

    def update(self,screen,clock):
        self.makeguess()
        while True:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and self.lowbutton.rect.collidepoint(pygame.mouse.get_pos()):
                    self.low = self.guess
                    self.makeguess()
                if event.type == pygame.MOUSEBUTTONUP and self.highbutton.rect.collidepoint(pygame.mouse.get_pos()):
                    self.high = self.guess
                    self.makeguess()
                if event.type == pygame.MOUSEBUTTONUP and self.correctbutton.rect.collidepoint(pygame.mouse.get_pos()):
                    return (3,self.n)
            screen.blit(self.image,(0,0))
            pygame.display.flip()

class Endscreen(object):
    def __init__(self,n):
        self.image = pygame.Surface((640,480))
        self.image.fill((200,200,200))

        # Create the main text for the end game screen

        self.maintext = Linesoftext(['Yay I guessed your number and it only took %d tries!' % n])
        self.image.blit(self.maintext.image,(20,50))

        # Create the play again and quit buttons

        self.playagainbutton = Button(0,'Play Again?',(240,230))
        self.image.blit(self.playagainbutton.image,self.playagainbutton.pos)

        self.quitbutton = Button(0,'Quit',(290,300))
        self.image.blit(self.quitbutton.image,self.quitbutton.pos)

    def update(self,screen,clock):
        while True:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and self.playagainbutton.rect.collidepoint(pygame.mouse.get_pos()):
                    return 1
                if event.type == pygame.MOUSEBUTTONUP and self.quitbutton.rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
            screen.blit(self.image,(0,0))
            pygame.display.flip()


class Game(object):
    def main(self,screen):
        self.clock = pygame.time.Clock()
        self.progress = 1

        while True:
            if self.progress == 1:
                self.progress = Openingscreen().update(screen,self.clock)
            if self.progress == 2:
                (self.progress,self.n) = Mainscreen().update(screen,self.clock)
            if self.progress == 3:
                self.progress = Endscreen(self.n).update(screen,self.clock)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    Game().main(screen)

