#-------------------------------------------------------------------------------
# Name:        Fightfactory.py
# Purpose:     Use nested classes next time if multiple things are going to be
#              drawn on essentially the same screen
#
# Author:      James
#
# Created:     20/06/2014
# Copyright:   (c) James 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame, sys, random
import pygametools_0_0 as pt

class Monster(object):
    def __init__(self,monstertype):
        self.pic = monstertype + '.png'
        self.name = monstertype
        if self.name == 'hell_beast':
            self.name = 'hell beast'
        firetype = ['fire'] * 70 + ['water'] * 15 + ['earth'] * 15
        watertype = ['water'] * 70 + ['fire'] * 15 + ['earth'] * 15
        earthtype = ['earth'] * 70 + ['fire'] * 15 + ['water'] * 15
        if monstertype == 'hell_beast':
            self.type = firetype
        elif monstertype == 'goblin':
            self.type = earthtype
        elif monstertype == 'skeleton':
            self.type = watertype
        self.hp = 15

class Titlescreen(object):
    def __init__(self):
        self.image = pygame.Surface((800,600))
        self.image.fill((237, 145, 33))

        # Write the opening text at the top of the screen
        self.openingtext = pt.Linesoftext(['Welcome to Fight Factory',
                                           'A simple little fighting game'],(400,20),
                                           xmid = True,fontsize = 70,
                                           backgroundcolor = (237, 145, 33))
        self.image.blit(*self.openingtext.blitinfo)

        # Create the play and quit buttons
        self.play_button = pt.Button(0,'Play',(400,390),True,fontsize = 50)
        self.image.blit(*self.play_button.blitinfo)

        self.quit_button = pt.Button(0,'Quit',(400,460),True,fontsize = 50)
        self.image.blit(*self.quit_button.blitinfo)
    def update(self,screen,clock):
        while True:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and self.play_button.rect.collidepoint(pygame.mouse.get_pos()):
                    return 2
                if event.type == pygame.MOUSEBUTTONUP and self.quit_button.rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

            screen.blit(self.image,(0,0))
            pygame.display.flip()

class Mainscreen(object):
    def __init__(self):

        # Create the backgound image for the mainscreen
        self.image = pygame.Surface((800,600))
        self.image.fill((237, 145, 33))

        # Create the player and monster objects
        self.player = Monster('decorn')
        monsterchoices = ['skeleton','hell_beast','goblin']
        self.monster = Monster(random.choice(monsterchoices))

        # Create the player and monster items that will be drawn to the screen
        self.playerimage = pt.Button(1,self.player.pic,(200,200), midpoint = True,
                                     resize = (300,300))

        self.monsterimage = pt.Button(1,self.monster.pic,(600,200), midpoint = True,
                                     resize = (300,300))

    def choose_action(self):

        # Clear the image
        self.image.fill((237,145,33))

        # Put the main images on the screen

        self.image.blit(*self.playerimage.blitinfo)
        self.image.blit(*self.monsterimage.blitinfo)

        self.playerhptext = pt.Linesoftext(['Hp                               %d/15' % self.player.hp],
                                            (200,10), xmid = True, backgroundcolor = (237, 145, 33))
        self.image.blit(*self.playerhptext.blitinfo)

        self.playerhpbar = pygame.Rect((87,12),(int(200 * self.player.hp/15),20))
        pygame.draw.rect(self.image,(255,0,0),self.playerhpbar)

        self.monsterhptext = pt.Linesoftext(['Hp                               %d/15' % self.monster.hp],
                                            (600,10), xmid = True, backgroundcolor = (237, 145, 33))
        self.image.blit(*self.monsterhptext.blitinfo)

        self.monsterhpbar = pygame.Rect((487,12),(int(200 * self.monster.hp/15),20))
        pygame.draw.rect(self.image,(255,0,0),self.monsterhpbar)

        # Create the instructional text
        self.choose_action_text = pt.Linesoftext(['Choose an attack type'],(400,400),xmid = True,backgroundcolor = (237, 145, 33))
        self.image.blit(*self.choose_action_text.blitinfo)

        # Create the fire, water , and earth buttons
        self.firebutton = pt.Button(0,'Fire',(200,475),midpoint = True)
        self.image.blit(*self.firebutton.blitinfo)

        self.waterbutton = pt.Button(0,'Water',(400,475),midpoint = True)
        self.image.blit(*self.waterbutton.blitinfo)

        self.earthbutton = pt.Button(0,'Earth',(600,475),midpoint = True)
        self.image.blit(*self.earthbutton.blitinfo)

    def combat(self,action):

        # Clean the image
        self.image.fill((237, 145, 33))

        # decide an action for the monster
        monsteraction = random.choice(self.monster.type)
        actions = ['fire','water','earth']
        monsteraction = actions.index(monsteraction)

        # Logic for how much damage is done to both sides
        # pdd = player damage dealt
        # mdd = monster damge dealt
        if action == 0:
            if monsteraction == 0:
                self.player.hp -= 2
                mdd = 2
                self.monster.hp -= 2
                pdd = 2
            elif monsteraction == 1:
                self.player.hp -= 3
                mdd = 3
                self.monster.hp -= 1
                pdd = 1
            elif monsteraction == 2:
                self.player.hp -=1
                mdd = 1
                self.monster.hp -=3
                pdd = 3
        elif action == 1:
            if monsteraction == 0:
                self.player.hp -= 1
                mdd = 1
                self.monster.hp -= 3
                pdd = 3
            elif monsteraction == 1:
                self.player.hp -= 2
                mdd = 2
                self.monster.hp -= 2
                pdd = 2
            elif monsteraction == 2:
                self.player.hp -= 3
                mdd = 3
                self.monster.hp -= 1
                pdd = 1
        elif action == 2:
            if monsteraction == 0:
                self.player.hp -= 3
                mdd = 3
                self.monster.hp -= 1
                pdd = 1
            elif monsteraction == 1:
                self.player.hp -= 1
                mdd = 1
                self.monster.hp -= 3
                pdd = 3
            elif monsteraction == 2:
                self.player.hp -= 2
                mdd = 2
                self.monster.hp -= 2
                pdd = 2

        # if one of the monsters die run win_lose
        if self.player.hp <= 0 or self.monster.hp <= 0:
            self.win_lose()

        # Display the results
        else:
            self.resultstext = pt.Linesoftext([('You used a %s type attack doing %d damage' % (actions[action], pdd)),
                                               ('The %s used a %s type attack doing %d damage' % (self.monster.name, actions[monsteraction], mdd))],
                                               (400,400),xmid = True,backgroundcolor = (237, 145, 33))
            self.image.blit(*self.resultstext.blitinfo)

            self.image.blit(*self.playerimage.blitinfo)
            self.image.blit(*self.monsterimage.blitinfo)

            self.playerhptext = pt.Linesoftext(['Hp                               %d/15' % self.player.hp],
                                                (200,10), xmid = True, backgroundcolor = (237, 145, 33))
            self.image.blit(*self.playerhptext.blitinfo)

            self.playerhpbar = pygame.Rect((87,12),(int(200 * self.player.hp/15),20))
            pygame.draw.rect(self.image,(255,0,0),self.playerhpbar)

            self.monsterhptext = pt.Linesoftext(['Hp                               %d/15' % self.monster.hp],
                                                (600,10), xmid = True, backgroundcolor = (237, 145, 33))
            self.image.blit(*self.monsterhptext.blitinfo)

            self.monsterhpbar = pygame.Rect((487,12),(int(200 * self.monster.hp/15),20))
            pygame.draw.rect(self.image,(255,0,0),self.monsterhpbar)

            self.continuebutton = pt.Button(0,'Continue',(400,525),midpoint = True)
            self.image.blit(*self.continuebutton.blitinfo)

    def win_lose(self):

        # Clear the image
        self.image.fill((237,145,33))

        if self.player.hp <= 0 and self.monster.hp <= 0:
            self.player.hp = 0
            self.monster.hp = 0
            self.draw_text = pt.Linesoftext(['The match ended in a draw'],(400,400),xmid = True,backgroundcolor = (237,145,33))
            self.image.blit(*self.draw_text.blitinfo)
        elif self.player.hp <= 0:
            self.player.hp = 0
            self.lose_text = pt.Linesoftext(['You lost the match'],(400,400),xmid = True,backgroundcolor = (237,145,33))
            self.image.blit(*self.lose_text.blitinfo)
        elif self.monster.hp <= 0:
            self.monster.hp = 0
            self.win_text = pt.Linesoftext(['You won the match'],(400,400),xmid = True,backgroundcolor = (237,145,33))
            self.image.blit(*self.win_text.blitinfo)

        # Draw the main information to the screen
        self.image.blit(*self.playerimage.blitinfo)
        self.image.blit(*self.monsterimage.blitinfo)

        self.playerhptext = pt.Linesoftext(['Hp                               %d/15' % self.player.hp],
                                            (200,10), xmid = True, backgroundcolor = (237, 145, 33))
        self.image.blit(*self.playerhptext.blitinfo)

        self.playerhpbar = pygame.Rect((87,12),(int(200 * self.player.hp/15),20))
        pygame.draw.rect(self.image,(255,0,0),self.playerhpbar)

        self.monsterhptext = pt.Linesoftext(['Hp                               %d/15' % self.monster.hp],
                                            (600,10), xmid = True, backgroundcolor = (237, 145, 33))
        self.image.blit(*self.monsterhptext.blitinfo)

        self.monsterhpbar = pygame.Rect((487,12),(int(200 * self.monster.hp/15),20))
        pygame.draw.rect(self.image,(255,0,0),self.monsterhpbar)

        # Create the play again and quit buttons
        self.play_againbutton = pt.Button(0,'Play Again?',(275,525))
        self.image.blit(*self.play_againbutton.blitinfo)

        self.quitbutton = pt.Button(0,'Quit',(475,525))
        self.image.blit(*self.quitbutton.blitinfo)

    def update(self,screen,clock):
        # action 0 = fire, 1 = water, 2 = earth
        self.choose_action()
        # step 1 = choose action, 2 = combat, 3 = win_lose page
        self.step = 1
        while True:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and self.step == 1:
                    if self.firebutton.rect.collidepoint(pygame.mouse.get_pos()):
                        self.combat(0)
                        if self.player.hp <= 0 or self.monster.hp <= 0:
                            self.win_lose()
                            self.step = 3
                        else: self.step = 2
                    if self.waterbutton.rect.collidepoint(pygame.mouse.get_pos()):
                        self.combat(1)
                        if self.player.hp <= 0 or self.monster.hp <= 0:
                            self.win_lose()
                            self.step = 3
                        else: self.step = 2
                    if self.earthbutton.rect.collidepoint(pygame.mouse.get_pos()):
                        self.combat(2)
                        if self.player.hp <= 0 or self.monster.hp <= 0:
                            self.win_lose()
                            self.step = 3
                        else: self.step = 2
                if event.type == pygame.MOUSEBUTTONUP and self.step == 2:
                    if self.continuebutton.rect.collidepoint(pygame.mouse.get_pos()):
                        self.choose_action()
                        self.step = 1
                if event.type == pygame.MOUSEBUTTONUP and self.step == 3:
                    if self.play_againbutton.rect.collidepoint(pygame.mouse.get_pos()):
                        self.step = 1
                        self.__init__()
                        self.choose_action()
                    if self.quitbutton.rect.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()
            if self.player.hp <= 0 or self.monster.hp <= 0:
                self.win_lose()

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
            elif self.progress == 2:
                self.progress = Mainscreen().update(screen,self.clock)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    Game().update(screen)
