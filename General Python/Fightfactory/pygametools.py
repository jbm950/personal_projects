#-------------------------------------------------------------------------------
# Name:        pygametools.py
# Purpose:     This module will hold different tools that I have made to improve
#              the rate of development of pygame programs
#
# Author:      James
#
# Created:     18/06/2014
# Copyright:   (c) James 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame, sys

class Button(pygame.sprite.Sprite):
    def __init__(self, type_of_button, fileortext, position, midpoint = False, resize = False,fontsize = 36,surface = None):
        """This class will help make quick buttons for use with pygame.
        If 0 is passed into type of button a text button will be made and if a
        1 is passed a picture button will be made. The fileortext variable will
        hold the file name for a picture button or the text to be displayed for
        a text button. The position variable is the (x,y) location of the button.
        If midpoint = True the (x,y) position is the midpoint position rather than
        the top left pixel"""
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()
        basicfont = pygame.font.Font(None,fontsize)

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
        elif type_of_button == 1:
            self.image = pygame.image.load(fileortext)
            # Change the size of the picture if necessary
            if resize:
                self.image = pygame.transform.scale(self.image,resize)
            self.imagemidp = (int(self.image.get_width() * 0.5), int(self.image.get_height() * 0.5))

        # if a midpoint arguement is passed set the pos to the top left pixel
        # such that the position passed in is in the middle of the button
        if midpoint:
            self.pos = (position[0] - self.imagemidp[0], position[1] - self.imagemidp[1])
        else:
            self.pos = position

        # set the rectangle to be used for collision detection
        self.rect = pygame.Rect(self.pos,self.image.get_size())

        # Set up the information that is needed to blit the image to the surface
        self.blitinfo = (self.image, self.pos)

        # automatically blit the button onto an input surface
        if surface:
            surface.blit(*self.blitinfo)


class Linesoftext(object):
    def __init__(self,text,position,xmid = False,fontsize = 36,backgroundcolor = (200,200,200),surface = None):
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
        self.image.fill(backgroundcolor)

        # Draw the text to the image
        n = 0
        for x in text:
            self.texttemp = basicfont.render(x,0,(1,1,1))
            self.image.blit(self.texttemp,(0,n * fontsize + n * 10))
            n +=1

        # Set the position of the text. If xmid is passed in as true set the
        # pos to the top middle pixel of the text
        if xmid:
            self.pos = (position[0] - int(self.image.get_width() / 2),position[1])
        else:
            self.pos = position

        # Set up the information that will be needed to blit the image to a
        # surface
        self.blitinfo = (self.image, self.pos)

        # automatically blit the text onto an input surface
        if surface:
            surface.blit(*self.blitinfo)

    def test(self,windowsize = False):
        """This can be used to quickly test the spacing of the words. If you want
        to test how the text looks with a specific window you can pass in a
        (width,height) into windowsize"""

        # set up a specific window to test the text in
        if windowsize:
            self.screen = pygame.display.set_mode(windowsize)
            self.screen.fill((200,200,200))
            self.screen.blit(*self.blitinfo)

        # if no specific window is specified create a small one around the
        # outside of the text
        else:
            self.screen = pygame.display.set_mode((self.imagewidth + 20,self.imageheight + 20))
            self.screen.fill((200,200,200))
            self.screen.blit(self.image, (10,10))

        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
