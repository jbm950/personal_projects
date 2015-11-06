#-------------------------------------------------------------------------------
# Name:        tq_graphics.py
# Purpose:     This module will be the different screens for the game Torric's
#              quest.
#
# Author:      James
#
# Created:     04/01/2015
# Copyright:   (c) James 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

################################################################################
################################################################################

# Program contents

# - Imports
# - Close function
# - Title screen
# - Story screen
# - Tutorial check
# - Combat screens
# - Level up screen
# - End game screen

################################################################################
################################################################################
# Imports

import pygame,sys
import pygametools as pt
import tq_story as tqs
import tq_combat as tqc

################################################################################
################################################################################
# Close function

def close():
    # close out pygame and the game window properly
    pygame.quit()
    sys.exit()

################################################################################
################################################################################
# Title screen

class Titlescreen(pt.Menu):
    def __init__(self):
        # set the arguments for the menu class and initialize it
        size = (800,600)
        header = ['Welcome to Torric\'s Quest!']
        background = 'fortress.png'
        pt.Menu.__init__(self,size,background,header,[])

        # Create the customized buttons and add them to the button list
        self.buttonlist += [pt.Button(0,'Close',(300,450),True,self.image,
                       resize = (80,37),func = close,sound = 'button_click.wav',
                       background = 'button_box.png')]
        self.buttonlist += [pt.Button(0,'Play',(500,450),True,self.image,
                       resize = (80,37),func = lambda:2,sound = 'button_click.wav',
                       background = 'button_box.png')]

################################################################################
################################################################################
# Story screen

class Storyscreens(pt.Textscreens):
    def __init__(self,text_num):
        text = tqs.get_text(text_num)
        lastbutton = ['Continue',lambda:4]
        background = 'background_01.png'
        self.nextbutton = pt.Button(0,'Next',(0,0),resize = (80,37),sound = 'button_click.wav',background = 'button_box.png')
        self.backbutton = pt.Button(0,'Back',(0,0),resize = (80,37),sound = 'button_click.wav',background = 'button_box.png')
        self.lastbutton = pt.Button(0,'Continue',(0,0),resize = (150,37),sound = 'button_click.wav',background = 'button_box.png')
        pt.Textscreens.__init__(self,(800,600),background,text,lastbutton,1)

################################################################################
################################################################################
# Tutorial check

class Tutorialcheck(pt.Menu):
    def __init__(self):
        # Initialize the menu attributes
        size = (400,300)
        header = ['  Would you like to view','the combat tutorial first?']
        background = (255,150,100)
        pt.Menu.__init__(self,size,background,header,[])

        # Create the customized buttons and add them to the buttonlist.
        self.buttonlist += [pt.Button(0,'Yes',(100,200),True,self.image,
                       resize = (80,37),func = lambda:3,sound = 'button_click.wav',
                       background = 'button_box.png')]
        self.buttonlist += [pt.Button(0,'No',(300,200),True,self.image,
                       resize = (80,37),func = lambda:4,sound = 'button_click.wav',
                       background = 'button_box.png')]

        # Set the menu in the middle of the screen
        pt.Menu.set_offset(self,(400,300),'c')

################################################################################
################################################################################
# Combat Screens

class Combatscreens(pt.Menu):
    def __init__(self,player,encounter_number):
        self.page = 1
        self.player = player
        self.encounter_number = encounter_number
        self.monster = tqc.Monster(encounter_number)

    def draw_main(self):
        size = (800,600)
        background = 'background_03.png'
        header = ['']
        pt.Menu.__init__(self,size,background,header,[])

        # Create the health and pictures of the combatants
        pt.Button(1,self.player.pic,(200,200),True,self.image,resize = (300,300))
        pt.Button(1,self.monster.pic,(600,200),True,self.image,resize = (300,300))

        pt.Linesoftext(['Hp                               %d/%d' % (self.player.hp,self.player.hpmax)],(200,10),True,self.image)
        pt.Linesoftext(['Hp                               %d/%d' % (self.monster.hp,self.monster.hpmax)],(600,10),True,self.image)

        playerhpbar = pygame.Rect((87,12),(int(200 * self.player.hp/self.player.hpmax),20))
        pygame.draw.rect(self.image,(255,0,0),playerhpbar)

        monsterhpbar = pygame.Rect((490,12),(int(200 * self.monster.hp/self.monster.hpmax),20))
        pygame.draw.rect(self.image,(255,0,0),monsterhpbar)

    def choose_action(self,screen,clock):
        self.draw_main()
        pt.Linesoftext(['Choose a type of attack'],(400,370),True,self.image)

        # Create the buttons for the specific screen
        self.buttonlist += [pt.Button(0,'Standard',(250,480),True,self.image,
                            resize = (145,37),func = lambda:(2,1),sound = 'button_click.wav',
                            background = 'button_box.png')]
        self.buttonlist += [pt.Button(0,'Defensive',(250,430),True,self.image,
                            resize = (145,37),func = lambda:(2,2),sound = 'button_click.wav',
                            background = 'button_box.png')]
        self.buttonlist += [pt.Button(0,'Aggressive',(530,430),True,self.image,
                            resize = (145,37),func = lambda:(2,3),sound = 'button_click.wav',
                            background = 'button_box.png')]
        self.buttonlist += [pt.Button(0,'Precise',(530,480),True,self.image,
                            resize = (145,37),func = lambda:(2,4),sound = 'button_click.wav',
                            background = 'button_box.png')]

        return pt.Menu.update(self,screen,clock)

    def fight(self,screen,clock):
        results = tqc.combat(self.player,self.monster,self.action)

        end_result = (1,0)

        # Set up the win loss results
        if self.player.hp <= 0:
            self.player.hp = 0
            end_result = (3,['You lost'])
        elif self.monster.hp <= 0:
            self.monster.hp = 0
            end_result = (3,['You won!'])
        if self.player.hp <= 0 and self.monster.hp <= 0:
            self.player.hp = 0
            self.monster.hp = 0
            end_result = (3,['It was a draw!'])

        self.draw_main()

        # Put the results on the screen and add the continue button
        pt.Linesoftext(results,(400,400),True,self.image)
        self.buttonlist += [pt.Button(0,'Continue',(600,500),True,self.image,
                            resize = (145,37),func = lambda: end_result,sound = 'button_click.wav',
                            background = 'button_box.png')]

        return pt.Menu.update(self,screen,clock)

    def end_screen(self,screen,clock):
        self.draw_main()

        pt.Linesoftext(self.end_result,(400,400),True,self.image)

        # Create the retry or continue buttons
        if self.end_result == ['You lost'] or self.end_result == ['It was a draw!']:
            self.buttonlist += [pt.Button(0,'Retry?',(600,500),True,self.image,
                                  resize = (145,37),func = lambda: 1,sound = 'button_click.wav',
                                  background = 'button_box.png')]
        elif self.end_result == ['You won!']:
            self.buttonlist += [pt.Button(0,'Continue',(600,500),True,surface = self.image,
                                     resize = (145,37),func = lambda: 4,sound = 'button_click.wav',
                                     background = 'button_box.png')]

        return pt.Menu.update(self,screen,clock)

    def update(self,screen,clock):
        while True:
            if self.page == 1:
                (self.page,self.action) = self.choose_action(screen,clock)
            elif self.page == 2:
                (self.page,self.end_result) = self.fight(screen,clock)
            elif self.page == 3:
                self.page = self.end_screen(screen,clock)
                if self.page == 1:
                    self.player.hp = self.player.hpmax
                    self.monster = tqc.Monster(self.encounter_number)
            elif self.page == 4:
                self.player.hp = self.player.hpmax
                return 2

################################################################################
################################################################################
# Level up screen

class Levelupscreen(pt.Menu):
    def __init__(self,player):
        # set the arguments for the menu class and initialize it
        size = (800,600)
        header = ['','                      You have leveled up!','',
                  'Choose where you wish to use your ability point.']
        background = 'background_04.png'
        pt.Menu.__init__(self,size,background,header,[])

        # Create the customized buttons and add them to the button list
        self.buttonlist += [pt.Button(0,'Strength',(400,300),True,self.image,
                       resize = (130,37),func = player.str_up,sound = 'button_click.wav',
                       background = 'button_box.png')]
        self.buttonlist += [pt.Button(0,'Durability',(400,400),True,self.image,
                       resize = (130,37),func = player.dur_up,sound = 'button_click.wav',
                       background = 'button_box.png')]
        self.buttonlist += [pt.Button(0,'Dexterity',(400,500),True,self.image,
                       resize = (130,37),func = player.dex_up,sound = 'button_click.wav',
                       background = 'button_box.png')]

################################################################################
################################################################################
# End game screen

class Endgamescreen(pt.Menu):
    def __init__(self):
        # set the arguments for the menu class and initialize it
        size = (800,600)
        header = ['You have completed Torric\'s Quest!']
        background = 'fortress.png'
        pt.Menu.__init__(self,size,background,header,[])

        # Create the customized buttons and add them to the button list
        self.buttonlist += [pt.Button(0,'Close',(300,450),True,self.image,
                       resize = (80,37),func = close,sound = 'button_click.wav',
                       background = 'button_box.png')]
        self.buttonlist += [pt.Button(0,'Play Again?',(500,450),True,self.image,
                       resize = (165,37),func = lambda:0,sound = 'button_click.wav',
                       background = 'button_box.png')]
