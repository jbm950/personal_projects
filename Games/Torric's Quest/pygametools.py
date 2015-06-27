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
# Version:     0.6
# Written for: Python 3.3
#-------------------------------------------------------------------------------
#!/usr/bin/env python

# Module Contents
#   Button
#   Tile (for board game like games)
#   Linesoftext
#   BaseScreen
#   Menu
#   Textscreens
#   Tilemap


import pygame, sys, classtools


################################################################################
################################################################################

class Button(classtools.AttrDisplay):
    def __init__(self, type_of_button, file_or_text, position, midpoint = False, surface = None, **kargs):
        """This class will help make quick buttons for use with pygame.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            type_of_button - This input will differentiate between a picture
                button and a text button.
                0 = text button
                1 = picture button

            file_or_text - This input is a string containing either the text for
                a text button or a file name for the picture button (include
                extension for picture files such as .png)

            position - This is the x, y position of the top left corner of the
                button. (defining point can be changed to midpoint)

            midpoint - If true is passed to midpoint the button will be blitted
                to a surface, either automatically if a surface is passed or
                manually, such that the position input is the center of the
                button rather than the top left corner.

            surface - If a pygame surface or display is passed the button will
                automatically blit itself to that surface.

            resize - If a height and width are passed to this input the button
                will be adjusted to that size. For text buttons the background
                box will be adjusted to the given size while not altering the
                font size of the text.

            fontsize - This controls the size of the font of the text buttons.
                The default font size is 36.

            func - If a function is passed to the button the function will be
                called when the button is called and the button will return
                whatever the function would have returned.

            background - This can either be a rgb tuple of numbers or a string
                for a file to be loaded as the background image. (used for text
                buttons.)

            sound - This can be a string of a sound file. If given the sound
                will play whenever the button is clicked.

        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Important Attributes:
            image - This will be the pygame surface that contains the image
                of the button to be blitted onto another surface.

            pos - This is a tuple of the x, y cordinates of the button for
                blitting purposes.

            rect - This is a pygame rectangle object associated with the
                size and position of the button. This is used for collision
                detection with the mouse.

            blitinfo - This is a tuple containing the image and the position
                of the button. This can be unpacked into the blit method for
                convenience.

        (doc string updated ver 0.5)
        """

        # Initialize pygame font and sprite class
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()

        # Unpack the **kargs dictionary into the possible inputs (resize,
        # fontsize and func). If there are still items in kargs return
        # an error.
        resize = kargs.pop('resize',False)
        fontsize = kargs.pop('fontsize',36)
        func = kargs.pop('func',None)
        background = kargs.pop('background',(67,110,238))
        sound = kargs.pop('sound',None)
        if kargs:
            raise KeyError('An invalid input was passed')


        # Create a text button
        if type_of_button == 0:

            # Create the font object
            basicfont = pygame.font.Font(None,fontsize)

            # Create the text surface and find the size and midpoint of that surface
            text = basicfont.render(file_or_text,0,(1,1,1))
            textsize = text.get_size()
            textmidp = (int(textsize[0] * 0.5),int(textsize[1] * 0.5))

            # Create the background box
            if resize:
                self.image = pygame.Surface(resize)
            else:
                self.image = pygame.Surface((int(textsize[0] * 1.25),int(textsize[1] * 1.429)))
            imagesize = self.image.get_size()
            imagemidp = (int(imagesize[0] * 0.5),int(imagesize[1] * 0.5))

            # Create the background for the screen
            # If the backround is a filename load the file and blit it to the image
            if type(background) == str:
                background = pygame.image.load(background).convert()
                background =  pygame.transform.scale(background,(self.image.get_width(),self.image.get_height()))
                self.image.blit(background,(0,0))
            # Otherwise the background should contain an rgb value
            else:
                self.image.fill(background)

            # Center the text at the center of the box
            self.image.blit(text,(imagemidp[0]-textmidp[0], imagemidp[1]-textmidp[1]))

        # Create a picture button
        elif type_of_button == 1:

            # Load the given file
            self.image = pygame.image.load(file_or_text).convert()

            # Change the size of the picture if necessary
            if resize:
                self.image = pygame.transform.scale(self.image,resize)
            imagemidp = (int(self.image.get_width() * 0.5), int(self.image.get_height() * 0.5))

        # Set the position of the button
        self.set_position(position,midpoint)

        # automatically blit the button onto an input surface
        if surface:
            surface.blit(*self.blitinfo)

        # Set the function for the button to pass into the call for the class
        if func is not None:
            self.func = func

        # If a sound is given load the sound file
        if sound is not None:
            self.sound = pygame.mixer.Sound(sound)
        else:
            self.sound = None

    def set_position(self,position,midpoint = False):
        """This method allows the button to be moved manually and keep the click
        on functionality.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            position - This is the x, y position of the top left corner of the
                            button. (defining point can be changed to midpoint)

            midpoint - If true is passed to midpoint the button will be blitted
                to a surface, either automatically if a surface is passed or
                manually, such that the position input is the center of the
                button rather than the top left corner.

        (doc string updated ver 0.5)"""

        # Find the image size and midpoint of the image
        imagesize = self.image.get_size()
        imagemidp = (int(imagesize[0] * 0.5),int(imagesize[1] * 0.5))

        # if a midpoint arguement is passed, set the pos to the top left pixel
        # such that the position passed in is in the middle of the button
        if midpoint:
            self.pos = (position[0] - imagemidp[0], position[1] - imagemidp[1])
        else:
            self.pos = position

        # set the rectangle to be used for collision detection
        self.rect = pygame.Rect(self.pos,self.image.get_size())

        # Set up the information that is needed to blit the image to the surface
        self.blitinfo = (self.image, self.pos)

    def __call__(self):
        """Calling the button will call what ever function was passed to it when
           it was initialized. The button object returns whatever was returned
           by the function assigned to it. If a sound was given this sound will
           be played before the given function is called.
           (doc string updated ver 0.5)
           """

        # If a sound is given play the sound before returning the given function
        if self.sound is not None:
            self.sound.play()

        return self.func()


################################################################################
################################################################################

class Tile(Button):
    def __init__(self,file,size):
        """This will load an image and resize it as specified. The class comes
        with shading features and can be used as a parent class for board game
        like tiles that need additional attributes.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            file - This is a string of the picture file name including extension

            size - This is a tuple containing the length and height of the tile

        (doc string updated ver 0.5)
        """

        # Initialize button class and set the picture attribute of the instance
        Button.__init__(self,1,file,(0,0),resize = size)
        self.pic = pygame.Surface(self.image.get_size())
        self.pic.blit(self.image,(0,0))

        # Set up the shades dictionary. The first item determines if the shade
        # is on and the second item is the surface containing the shade.
        self.shades = {}

        # Create blue and red shades for the tile
        self.initialize_shade('blue',(0,0,255),150)
        self.initialize_shade('red',(255,0,0),150)



    def initialize_shade(self,shade_name,shade_color,alpha):
        """This method will create semi-transparent surfaces with a specified
        color. The surface can be toggled on and off.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            Shade_name - String of the name that you want to associate with the
                surface

            Shade_color - An rgb tuple of the color of the shade

            Alpha - Level of transparency of the shade (0-255 with 150 being a
                good middle value)

        (doc string updated ver 0.6)
        """

        self.shades[shade_name] = [0, pygame.Surface(self.image.get_size())]
        self.shades[shade_name][1].fill(shade_color)
        self.shades[shade_name][1].set_alpha(alpha)

    def toggle_shade(self,shade):
        """This method will overlay a semi-transparent shade on top of the
        tile's image.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            shade - This will designate which shade you wish to turn on or off.
                Blue and red shades are available by default.

        (doc string updated ver 0.6)
        """

        # First toggle the user specified shade
        if self.shades[shade][0]:
            self.shades[shade][0] = 0
        else:
            self.shades[shade][0] = 1

        # Now draw the image with the active shades
        self.image.blit(self.pic,(0,0))
        for key in self.shades:
            if self.shades[key][0]:
                self.image.blit(self.shades[key][1],(0,0))


################################################################################
################################################################################

class Linesoftext(classtools.AttrDisplay):
    def __init__(self,text,position,xmid = False,surface = None,**kargs):
        """This object will create an image of text with multiple lines.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            text - This is a list of strings. Each item in the list will be
                drawn on a separate line.

            position - This is the x, y postion of the top left pixel of the
                text image.

            xmid - If passed True the position argument will be treated as the
                middle of the top of the text image.

            surface - If a pygame surface or screen is passed in the Linesoftext
                object will automatically blit itself to that surface/screen.

            fontsize - This is the size of the font of the rendered text. The
                default fontsize is 36.

            align - This will determine if the text is aligned to the left,
                right or center. The default is left aligned.
                'l' = left align
                'c' = center align
                'r' = right align

        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Important Attributes:
            image - This will be the pygame surface that contains the image
                of the text to be blitted onto another surface.

            pos - This is a tuple of the x, y cordinates of the text for
                blitting purposes.

            blitinfo - This is a tuple containing the image and the position
                of the text. This can be unpacked into the blit method for
                convenience.

        (doc string updated ver 0.4)
        """

        # Initialize the pygame font class.
        pygame.font.init()

        # Unpack the **kargs dictionary
        fontsize = kargs.pop('fontsize',36)
        align = kargs.pop('align','l')

        # Create the font object
        basicfont = pygame.font.Font(None,fontsize)

        # Figure out the size of the image that will be drawn on and create that
        # image
        linewidths = []
        for x in text:
            texttemp = basicfont.render(x,0,(1,1,1))
            linewidths.append(texttemp.get_width())
        # The width of the image is the width of the text that corresponds to
        # the index of linewidths that contains the largest number in linewidths
        self.imagewidth = basicfont.render(text[linewidths.index(max(linewidths))],0,(1,1,1)).get_width()
        self.imageheight = len(text) * fontsize + (len(text)-1) * 10
        self.image = pygame.Surface((self.imagewidth,self.imageheight))
        self.image.fill((200,200,200))

        # make the background transparent
        self.image.set_colorkey((200,200,200))

        # Draw the text to the image using the user chosen alignment
        n = 0
        if align == 'l':
            for x in text:
                texttemp = basicfont.render(x,0,(1,1,1))
                self.image.blit(texttemp,(0,n * fontsize + n * 10))
                n +=1
        elif align == 'c':
            for x in text:
                texttemp = basicfont.render(x,0,(1,1,1))
                self.image.blit(texttemp,(self.imagewidth // 2 - texttemp.get_width() // 2,n * fontsize + n * 10))
                n +=1
        elif align == 'r':
            for x in text:
                texttemp = basicfont.render(x,0,(1,1,1))
                self.image.blit(texttemp,(self.imagewidth - texttemp.get_width(),n * fontsize + n * 10))
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
        """This can be used to quickly test the spacing of the words.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            windowsize - A (width,height) tuple can be passed to create a window
                with a specific size otherwise a window will be sized to the
                given text.

        (doc string updated ver 0.6)
        """

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


################################################################################
################################################################################

class BaseScreen(classtools.AttrDisplay):
    def __init__(self,size,background = None):
        """This is a base class for the other screens offered in the pygametools
        module.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            size - an (x,y) tuple defining the width and height of the screen to
                be made (in pixels).

            background - The background can either be a rgb tuple or a sting for
                 a file name.
        (doc string updated ver 0.6)
        """

        # Create the image that the screen will be drawn on
        self.image = pygame.Surface((size[0],size[1]))

        # Create the background for the screen
        # If the backround is a filename load the file and blit it to the image
        if type(background) == str:
            background = pygame.image.load(background).convert()
            background =  pygame.transform.scale(background,size)
            self.image.blit(background,(0,0))
        # Otherwise the background should contain an rgb value
        elif type(background) == tuple:
            self.image.fill(background)

        # Set the default position of the screen to (0,0)
        self.pos = (0,0)

    def set_offset(self,offset,mid = None):
        """This method will allow the menu to be placed anywhere in the open
           window instead of just the upper left corner.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            offset - This is the x,y tuple of the position that you want to
                move the screen to.

            mid - The offset will be treated as the value passed in instead of
                the top left pixel.

                'x' (the x point in offset will be treated as the middle of the
                      menu image)

                'y' (the y point in offset will be treated as the middle of the
                      menu image)

                'c' (the offset will be treated as the center of the menu image)

        (doc string updated ver 0.6)
        """

        if mid:
            imagesize = self.image.get_size()
            imagemidp = (int(imagesize[0] * 0.5),int(imagesize[1] * 0.5))
            if mid == 'x':
                offset = (offset[0] - imagemidp[0], offset[1])
            if mid == 'y':
                offset = (offset[0], offset[1] - imagemidp[1])
            if mid == 'c':
                offset = (offset[0] - imagemidp[0], offset[1] - imagemidp[1])

        self.pos = offset

        for i in self.buttonlist:
                i.rect[0] += offset[0]
                i.rect[1] += offset[1]


################################################################################
################################################################################

class Menu(BaseScreen):
    def __init__(self,size,background,header,buttons):
        """This will create a screen with header text and buttons that call the
        user specified functions when clicked.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            size - This will specify the size of the menu in pixels. An x and a
                y value are to be given.

            background - This can either be a rgb tuple of numbers or a string
                for a file to be loaded as the background image.

            header - This is the text that will be displayed at the top of the
                menu screen. The text needs to be entered as a string in a list

            buttons - This is a list containing text function pairs for each
                desired button. Example [['Play',lambda:2],['quit',lambda:3]]
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Important Attributes:
            buttonlist - If you add button objects to this list the menu will
                automatically check if they're clicked in its update function
                (you need to blit the added button to self.image manually)

        (doc string updated ver 0.5)
        """

        # Initialize the screen class
        BaseScreen.__init__(self,size,background)

        # Determine the mid position of the given screen size and the
        # y button height
        xmid = size[0]//2
        ybuth = int(size[1]*0.583333)

        # Create the header text
        Linesoftext(header,(xmid,40),xmid = True,surface = self.image)

        # Create the buttons
        self.buttonlist = []
        for i in buttons:
            self.buttonlist += [Button(0,i[0],(xmid,ybuth + buttons.index(i) * 50), True, surface = self.image,func = i[1])]

    def update(self,screen,clock):
        # handle the events of the title screen
        while True:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                for i in self.buttonlist:
                    if event.type == pygame.MOUSEBUTTONUP and i.rect.collidepoint(pygame.mouse.get_pos()):
                        return i()
            screen.blit(self.image,self.pos)
            pygame.display.flip()


################################################################################
################################################################################

class Textscreens(BaseScreen):
    def __init__(self,size,background,text,lastbutton,manual_buttons = None):
        """This is a class that will make multiple screens for displaying text,
        like a book using  pages that can be flipped back and forth between.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            size - This is the (x,y) size of the screen in pixels.

            background - This can either be a rgb tuple of numbers or a string
                for a file to be loaded as the background image.

            text - This is a list containing a separate list of text for each
                page. Each page's text will have the lines of the text separated
                by commas.

            lastbutton - This is a list containing a string of what the last
                button should display and a function that should be run if the
                last button is clicked. If manual buttons are used a function
                still has to be provided as the second item in a list here.

            manual_buttons - If a 1 is passed then the nextbutton, backbutton
                and lastbutton need to be initialized separately before this
                class's __init__ function is run.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Important Attributes:
            nextbutton - This is the button that progresses through the pages

            backbutton - This is the button that will return to previous pages

            lastbutton - This is the button that replaces the nextbutton on the
                last page of the text to allow the program to move on.

        (doc string updated ver 0.6)
        """


        # Make the inputs into attributes to pass to the individual screens
        self.size = size
        self.background = background
        self.text = text
        self.lastbutton_func = lastbutton[1]

        # Set the progress counter for the text and page indicator for the
        # individual screens
        self.progress = 0
        self.page = 1

        # Set up the buttons for the screens
        xthird = size[0]//3
        ybut = int(size[1] * 0.9)

        # If the buttons are created manually set the func and pos attributes
        # for the text screens
        if manual_buttons:
            self.nextbutton.func = lambda: 2
            self.nextbutton.set_position((size[0] - xthird,ybut),True)

            self.backbutton.func = lambda: 3
            self.backbutton.set_position((xthird,ybut),True)

            self.lastbutton.func = lambda: 4
            self.lastbutton.set_position((size[0] - xthird,ybut),True)

        # If the defaullt buttons are being used create them
        else:
            self.nextbutton = Button(0,'Next',(size[0] - xthird, ybut),True,
                                     func = lambda: 2)
            self.backbutton = Button(0,'Back',(xthird, ybut),True,
                                     func = lambda: 3)
            self.lastbutton = Button(0,lastbutton[0],(size[0] - xthird, ybut),
                                     True, func = lambda: 4)

    def Screens(self,text,prog,screen,clock):
        """Prog = 0 for first page, 1 for middle pages, 2 for last page"""
        # Initialize the screen class
        BaseScreen.__init__(self,self.size,self.background)

        # Determine the mid position of the given screen size and the
        # y button height
        xmid = self.size[0]//2

        # Create the header text
        Linesoftext(text,(xmid,40),xmid = True,surface = self.image,fontsize = 30)

        # Create the buttons
        self.buttonlist = []
        if prog == 0:
            self.buttonlist += [self.nextbutton]

        elif prog == 1:
            self.buttonlist += [self.nextbutton]
            self.buttonlist += [self.backbutton]

        elif prog == 2:
            self.buttonlist += [self.lastbutton]
            self.buttonlist += [self.backbutton]

        # Draw the buttons to the screen
        for i in self.buttonlist:
            self.image.blit(*i.blitinfo)

        # Use the menu update method to run the screen and process button clicks
        return Menu.update(self,screen,clock)

    def update(self,screen,clock):
        while True:
            # Navigation through the screens
            # page = 1 - pages of text
            # page = 2 - Advance to next page of text
            # page = 3 - return a page of text
            # page = 4 - exit the set of pages

            if self.page == 1:
                # check for last page then first page then make the middle pages
                if self.progress == (len(self.text) - 1):
                    self.page = self.Screens(self.text[self.progress],2,screen,clock)
                elif self.progress == 0:
                    self.page = self.Screens(self.text[self.progress],0,screen,clock)
                else:
                    self.page = self.Screens(self.text[self.progress],1,screen,clock)
            elif self.page == 2:
                self.progress += 1
                self.page = 1
            elif self.page == 3:
                self.progress -= 1
                self.page = 1
            elif self.page == 4:
                return self.lastbutton_func()


################################################################################
################################################################################

class Tilemap(BaseScreen):
    def __init__(self,size,tilelist,buttonflag):
        """This class will draw an array of tile objects to a screen and return
        a clicked tile or use a given button. It also currently contains basic
        tilelist processing methods.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            size - This is the (x,y) size of the screen. (you need to make the
                tiles the correct size for this screen when the tiles are
                initialized.

            tilelist - This is a list of tile objects to be drawn to the screen.

            buttonflag - If a 1 is passed the update function will return a tile
                that was clicked. If a 0 is passed the update function will
                check the buttons in the button list and call the function of
                a button that was clicked.

        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Important Attributes:
            buttonlist - If you add button objects to this list the tilemap will
                automatically check if they're clicked in its update function if
                0 is passed for buttonflag.
                (you need to blit the added button to self.image manually)

        (doc string updated ver 0.6)
        """

        # Initialize the screen class
        BaseScreen.__init__(self,size)

        # Create the list of tile objects and draw them on the screen
        self.tilelist = tilelist
        xlen = self.tilelist[0][0].image.get_width()
        ylen = self.tilelist[0][0].image.get_height()
        for x in range(0,size[0],xlen):
            for y in range(0,size[1],ylen):
                try:
                    self.image.blit(self.tilelist[x // xlen][y // ylen].image,(x,y))
                    self.tilelist[x // xlen][y // ylen].set_position((x,y))
                except:
                    pass

        # Set up an empty button list and the buttonflag
        self.buttonlist = []
        self.buttonflag = buttonflag

    def set_offset(self,offset,mid = None):
        """This method will allow the menu to be placed anywhere in the open
           window instead of just the upper left corner.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            offset - This is the x,y tuple of the position that you want to
                move the screen to.

            mid - The offset will be treated as the value passed in instead of
                the top left pixel.

                'x' (the x point in offset will be treated as the middle of the
                      menu image)

                'y' (the y point in offset will be treated as the middle of the
                      menu image)

                'c' (the offset will be treated as the center of the menu image)

        (doc string updated ver 0.6)
        """

        BaseScreen.set_offset(self,offset,mid)
        for i in self.tilelist:
            for j in i:
                j.rect[0] += offset[0]
                j.rect[1] += offset[1]

    def adjacent_tiles(self,tile,pattern):
        """This will return a list of the tiles adjacent to a given tile.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Inputs:
            tile - This is the tile object for which the method will find
                adjacent tiles.

            pattern - This will designate the pattern type that you want the
                method to return

                'p' = plus sign
                'x' = diagonal
                'b' = box

        (doc string updated ver 0.6)
        """

        # Initialize the list of tiles to return
        adj_tiles = []

        # Find the row and column of the input tile
        for i in self.tilelist:
            for j in i:
                if j == tile:
                    row = self.tilelist.index(i)
                    column = self.tilelist[row].index(j)

        # Define functions for the 2 distinct patterns
        def plus_sign(self,row,column):
            nonlocal adj_tiles
            if row - 1 >= 0:
                adj_tiles += [self.tilelist[row - 1][column]]
            if row + 1 != len(self.tilelist):
                adj_tiles += [self.tilelist[row + 1][column]]
            if column - 1 >= 0 :
                adj_tiles += [self.tilelist[row][column - 1]]
            if column + 1 != len(self.tilelist[row]):
                adj_tiles += [self.tilelist[row][column + 1]]

        def diagonal(self,row,column):
            nonlocal adj_tiles
            if column - 1 >= 0:
                if row - 1 >= 0:
                    adj_tiles += [self.tilelist[row - 1][column - 1]]
                if row + 1 != len(self.tilelist):
                    adj_tiles += [self.tilelist[row + 1][column - 1]]
            if column + 1 != len(self.tilelist[row]):
                if row - 1 >= 0:
                    adj_tiles += [self.tilelist[row - 1][column + 1]]
                if row + 1 != len(self.tilelist):
                    adj_tiles += [self.tilelist[row + 1][column + 1]]

        # Return the tiles that form a plus sign with the given input tile
        if pattern == 'p':
            plus_sign(self,row,column)

        # Return the tiles touching the four corners of the input tile
        elif pattern == 'x':
            diagonal(self,row,column)

        # Return all of the tiles surrounding the input tile
        elif pattern == 'b':
            plus_sign(self,row,column)
            diagonal(self,row,column)

        return adj_tiles

    def update(self,screen,clock):
            while True:
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    # If the button flag is set to 1 return any tile clicked
                    if self.buttonflag:
                        for i in self.tilelist:
                            for x in i:
                                if event.type == pygame.MOUSEBUTTONUP and x.rect.collidepoint(pygame.mouse.get_pos()):
                                    return x
                    # If the button flag is not set to one use a list of buttons
                    # and call the function of any button that is called.
                    else:
                        for i in self.buttonlist:
                            if event.type == pygame.MOUSEBUTTONUP and i.rect.collidepoint(pygame.mouse.get_pos()):
                                return i()

                screen.blit(self.image,self.pos)
                pygame.display.flip()



