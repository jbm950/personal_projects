#-------------------------------------------------------------------------------
# Name:        torrics_quest.py
# Purpose:     Welcome to Torric's quest, the first full video game that I have
#              written. This game will alternate through written story segments
#              and combat segments
#
# Author:      James
#
# Created:     07/07/2014
# Copyright:   (c) James 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

################################################################################
################################################################################

# Program contents

# - Imports
# - Player and monster classes
# - Combat engine
# - Title screen
# - Story screen
# - Story text
# - End game screen
# - Level up screen
# - Tutorial screen
# - Combat screens
# - Game class
# - Initialization of the game

################################################################################
################################################################################

# Imports

import pygame, sys, random, copy
import pygametools_0_2 as pt

################################################################################
################################################################################

# Player and monster classes

class Monster(object):
    def __init__(self,monsternum):
        # Open up the text file with the monster data and prepare a list of the
        # different lines of data
        self.rawdata = open('monsterdata.txt')
        self.rawdata = self.rawdata.readlines()[monsternum].split(',')

        # Take the raw data and set the monsters attributes
        self.name = self.rawdata[0]
        self.pic = self.rawdata[1]
        self.hp = int(self.rawdata[2])
        self.hpmax = self.hp
        self.damage = int(self.rawdata[3])
        self.evasion = int(self.rawdata[4])
        self.accuracy = int(self.rawdata[5])
        self.agress_bonus_damage = int(self.rawdata[6])
        self.def_damagereduc = int(self.rawdata[7])
        self.precision_bonus = int(self.rawdata[8])

        # Set the prefered attack type
        # 1 = standard
        # 2 = defensive
        # 3 = aggressive
        # 4 = precise
        if self.rawdata[9] == '1':
            self.attack_pref = ['standard'] * 70 + ['defensive'] * 10 + ['aggressive'] * 10 + ['precise'] * 10
        elif self.rawdata[9] == '2':
            self.attack_pref = ['standard'] * 10 + ['defensive'] * 70 + ['aggressive'] * 10 + ['precise'] * 10
        elif self.rawdata[9] == '3':
            self.attack_pref = ['standard'] * 10 + ['defensive'] * 10 + ['aggressive'] * 70 + ['precise'] * 10
        elif self.rawdata[9] == '4':
            self.attack_pref = ['standard'] * 10 + ['defensive'] * 10 + ['aggressive'] * 10 + ['precise'] * 70

class Player(Monster):
    # add level and level up functions to the monster class
    def __init__(self,monsternum):
        Monster.__init__(self,monsternum)
        self.level = 1

    # Create the different level up cases
    def str_up(self):
        self.damage += 2
        self.agress_bonus_damage += 1
        self.accuracy += 1
        self.hpmax += 3
        self.hp = self.hpmax
        self.level += 1

    def dur_up(self):
        self.hpmax += 5
        self.hp = self.hpmax
        self.accuracy += 3
        self.def_damagereduc += 1
        self.level += 1

    def dex_up(self):
        self.accuracy += 5
        self.damage += 1
        self.precision_bonus += 5
        self.hpmax += 1
        self.evasion += 5
        self.hp = self.hpmax
        self.level += 1

################################################################################
################################################################################

# Combat engine

def combat(player,monster,action):
    """The player and monster are the player and monster objects of the game.
    Standard attack > action = 1
    Defensive attack > action = 2
    Aggressive attack > action = 3
    Precise attack > action = 4
    Returns a list of strings containing the results of the round."""

    # Create the responses for the different attack type match ups
    def standard(playertemp,monstertemp,monsteraction):
        if monsteraction == 'defensive':
            pass
        elif monsteraction == 'aggressive':
            monstertemp.damage += int(monstertemp.agress_bonus_damage * 0.7)
            monstertemp.accuracy -= int(monstertemp.accuracy * 0.7)
        elif monsteraction == 'precise':
            monstertemp.accuracy += monstertemp.precision_bonus
            monstertemp.damage += int(monstertemp.damage * 0.3)

    def defensive(playertemp,monstertemp,monsteraction):
        if monsteraction == 'standard':
            pass
        elif monsteraction == 'aggressive':
            playertemp.damage += int(monstertemp.agress_bonus_damage * 0.5)
            monstertemp.damage -= playertemp.def_damagereduc
        elif monsteraction == 'precise':
            playertemp.accuracy = int(playertemp.accuracy * 0.7)
            monstertemp.damage -= int(playertemp.def_damagereduc * 0.7)
            monstertemp.accuracy += monstertemp.precision_bonus

    def aggressive(playertemp,monstertemp,monsteraction):
        if monsteraction == 'standard':
            playertemp.damage += int(playertemp.agress_bonus_damage * 0.7)
            playertemp.accuracy -= int(playertemp.accuracy * 0.7)
        elif monsteraction == 'defensive':
            monstertemp.damage += int(playertemp.agress_bonus_damage * 0.5)
            playertemp.damage -= monstertemp.def_damagereduc
        elif monsteraction == 'precise':
            playertemp.accuracy += int(playertemp.accuracy * 0.4)
            playertemp.damage += playertemp.agress_bonus_damage
            monstertemp.damage = int(monstertemp.damage * 0.7)

    def precise(playertemp,monstertemp,monsteraction):
        if monsteraction == 'standard':
            playertemp.accuracy += playertemp.precision_bonus
            playertemp.damage += int(playertemp.damage * 0.3)
        elif monsteraction == 'defensive':
            playertemp.accuracy += playertemp.precision_bonus
            playertemp.damage -= int(monstertemp.def_damagereduc * 0.7)
            monstertemp.accuracy = int(monstertemp.accuracy * 0.7)
        elif monsteraction == 'aggresive':
            playertemp.damage = int(playertemp.damage * 0.7)
            monstertemp.accuracy += int(monstertemp.accuracy * 0.4)
            monstertemp.damage += playertemp.agress_bonus_damage

    # Create a string declaring the player's attack type
    if action == 1:
        attacktype = 'standard'
    elif action == 2:
        attacktype = 'defensive'
    elif action == 3:
        attacktype = 'aggressive'
    elif action == 4:
        attacktype = 'precise'

    # Create temporary versions of the player and monster
    playertemp = copy.copy(player)
    monstertemp = copy.copy(monster)

    # Decide an action for the monster
    monsteraction = random.choice(monster.attack_pref)

    # Create an empty string to store the results of the round of combat in
    results = []

    # Change attributes of the temporary monster and player based on attack type
    # match ups
    if action == 1:
        standard(playertemp,monstertemp,monsteraction)
    elif action == 2:
        defensive(playertemp,monstertemp,monsteraction)
    elif action == 3:
        aggressive(playertemp,monstertemp,monsteraction)
    elif action == 4:
        precise(playertemp,monstertemp,monsteraction)

    # Attempt to hit and do damage
    if random.randint(1,100) <= (100 - monstertemp.evasion + playertemp.accuracy):
        monster.hp -= playertemp.damage
        results.append('You used a/an %s attack doing %d damage' % (attacktype,playertemp.damage))
    else:
        results.append('Your %s attack missed' % (attacktype))

    if random.randint(1,100) <= (100 - playertemp.evasion + monstertemp.accuracy):
        player.hp -= monstertemp.damage
        results.append('%s used a/an %s attack doing %d damage' % (monster.name,monsteraction,monstertemp.damage))
    else:
        results.append('%s used a/an %s attack and missed' % (monster.name,monsteraction))

    # Return the results list
    return results

################################################################################
################################################################################

# Title screen

class Titlescreen(object):
    def __init__(self):
        # Create the image that the title screen is to be written on
        self.image = pygame.Surface((800,600))
        self.image.fill((255,193,37))

        # Create the header text
        pt.Linesoftext(['Welcome to Torrics Quest!'],(400,40),xmid = True,surface = self.image)

        # Create the play and quit buttons
        self.play_button = pt.Button(0,'Play',(400,350), True, surface = self.image,func = lambda: 2)
        self.quit_button = pt.Button(0,'Quit',(400,400), True, surface = self.image)

    def update(self,screen,clock):
        # handle the events of the title screen
        while True:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP and self.quit_button.rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP and self.play_button.rect.collidepoint(pygame.mouse.get_pos()):
                    return self.play_button()
            screen.blit(self.image,(0,0))
            pygame.display.flip()

################################################################################
################################################################################

# Story screens

class Storyscreen(object):
    def __init__(self,progress):
        self.page = 1
        self.progress = progress
        self.text = get_text(progress)
        self.text_pos = 0
    class Page1(object):
        def __init__(self,text):
            # Create the image that the title screen is to be written on
            self.image = pygame.Surface((800,600))
            self.image.fill((255,193,37))

            # Create the story text
            pt.Linesoftext(text,(400,30),True,30,self.image)

            # Create the next button
            self.next_button = pt.Button(0,'Next',(600,550),True,surface = self.image)

        def update(self,screen,clock):
            while True:
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONUP and self.next_button.rect.collidepoint(pygame.mouse.get_pos()):
                        return 2
                screen.blit(self.image,(0,0))
                pygame.display.flip()

    class Page2(object):
        def __init__(self,text,progress):
            # Create the image that the title screen is to be written on
            self.image = pygame.Surface((800,600))
            self.image.fill((255,193,37))

            # Create the story text
            pt.Linesoftext(text,(400,30),True,30,self.image)

            # Create the next button
            self.fight_button = pt.Button(0,'Fight',(600,550),True,surface = self.image)

            # If this is the first screen put the tutorial button in
            self.progress = progress
            if progress == 1:
                self.tutorial_button = pt.Button(0,'Tutorial',(300,550),True,surface = self.image)

        def update(self,screen,clock):
            while True:
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONUP and self.fight_button.rect.collidepoint(pygame.mouse.get_pos()):
                        return 4
                    elif self.progress == 1:
                        if event.type == pygame.MOUSEBUTTONUP and self.tutorial_button.rect.collidepoint(pygame.mouse.get_pos()):
                            return 5

                screen.blit(self.image,(0,0))
                pygame.display.flip()

    def update(self,screen,clock):
        while True:
            # Page
            # 1 = Story text
            # 2 = Pull up the next text and return to page 1
            # 3 = Last page of text
            # 4 = Initiate combat
            # 5 = Initiate tutorial
            if self.page == 1:
                self.page = self.Page1(self.text[self.text_pos]).update(screen,clock)
            elif self.page == 2:
                self.text_pos += 1
                if self.text_pos < (len(self.text) - 1):
                    self.page = 1
                elif self.text_pos == (len(self.text) - 1):
                    self.page = 3
            elif self.page == 3:
                self.page = self.Page2(self.text[self.text_pos],self.progress).update(screen,clock)
            elif self.page == 4:
                return (3,self.progress)
            elif self.page == 5:
                return (4,1)

################################################################################
################################################################################

# Story text

def get_text(text_num):
    if text_num == 1:
        return [['        You start to wake up. First thing you notice is a dizzing headache. As',
                  " your eyes start to inch open you see debris scattered around you. You're",
                  " definitely still in the monastary but can't quite figure out how you ended up",
                  " on the floor.",
                  '        As you try to get up you feel a dull ache in your side and glancing down',
                  ' you see some dried blood. Its starts to come back. GOBLINS... GOBLINS AND',
                  ' ORCS IN THE MONASTARY! We were under attack! You start to notice the',
                  ' other bodies lying on the floor, decorn and goblinkind. They had attacked in',
                  ' the middle of the night and looking around they had killed many.',
                  "        You notice movement in the doorway and before you can hide they walk",
                  ' straight into the room. "Torric!' " You're still alive!"' Thank the gods!", they',
                  ' shouted. It was Boulden the gardener.'],
                  ['        "Boulden how bad is it? How many are left?", you ask. "Very bad sir. Not',
                    " many survived as far as we can tell and those that did aren't in good shape.",
                    " You look like the most whole person I've" ' seen this morning", he stammered.',
                    '"Come ' "I'll show you to the others. We've set up a medical area on the lawn",
                    ' out front"']]
    elif text_num == 2:
        return [['You killed the goblin congrats!'],['There\'s currently one more fight available in the beta']]
    elif text_num == 3:
        return [['You killed the skeleton too?'],['Congrats you finished the beta!']]
    elif text_num == 13:
        return [['                                           Welcome to the Tutorial!',
                    '        In Torric\'s quest the combat is based off of four different attack types:',
                    'standard, defensive, aggressive and precise. Each attack type has a different',
                    'direct combat bonus and an effect based on the attack type chosen by the',
                    'opponent.',
                    '        There is no direct combat bonus for a standard attack',
                    '        If a defensive attack is used the opponents damage potential is reduced',
                    '        If a aggressive attack is used bonus damage will be done',
                    '        If a precise attack is used your chance to hit the opponent is increased'],
                    ['This is the end of the tutorial']]

################################################################################
################################################################################

# End game screen

class Endgamescreen(object):
    def __init__(self,progress):
        self.page = 1
        self.progress = progress
        self.text = get_text(progress)
        self.text_pos = 0
    class Page1(object):
        def __init__(self,text):
            # Create the image that the title screen is to be written on
            self.image = pygame.Surface((800,600))
            self.image.fill((255,193,37))

            # Create the story text
            pt.Linesoftext(text,(400,30),True,30,self.image)

            # Create the next button
            self.next_button = pt.Button(0,'Next',(600,550),True,surface = self.image)

        def update(self,screen,clock):
            while True:
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONUP and self.next_button.rect.collidepoint(pygame.mouse.get_pos()):
                        return 2
                screen.blit(self.image,(0,0))
                pygame.display.flip()

    class Page2(object):
        def __init__(self,text,progress):
            # Create the image that the title screen is to be written on
            self.image = pygame.Surface((800,600))
            self.image.fill((255,193,37))

            # Create the story text
            pt.Linesoftext(text,(400,30),True,30,self.image)

            # Create the next button
            self.finish_button = pt.Button(0,'Finish',(600,550),True,surface = self.image)

        def update(self,screen,clock):
            while True:
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONUP and self.finish_button.rect.collidepoint(pygame.mouse.get_pos()):
                        return 4

                screen.blit(self.image,(0,0))
                pygame.display.flip()

    def update(self,screen,clock):
        while True:
            # Page
            # 1 = Story text
            # 2 = Pull up the next text and return to page 1
            # 3 = Last page of text
            # 4 = Return to title page
            if self.page == 1:
                self.page = self.Page1(self.text[self.text_pos]).update(screen,clock)
            elif self.page == 2:
                self.text_pos += 1
                if self.text_pos < (len(self.text) - 1):
                    self.page = 1
                elif self.text_pos == (len(self.text) - 1):
                    self.page = 3
            elif self.page == 3:
                self.page = self.Page2(self.text[self.text_pos],self.progress).update(screen,clock)
            elif self.page == 4:
                break

################################################################################
################################################################################

# Tutorial screens

class Tutorialscreen(object):
    def __init__(self,progress):
        self.page = 1
        self.progress = progress
        self.text = get_text(progress)
        self.text_pos = 0
    class Page1(object):
        def __init__(self,text):
            # Create the image that the title screen is to be written on
            self.image = pygame.Surface((800,600))
            self.image.fill((255,193,37))

            # Create the story text
            pt.Linesoftext(text,(400,30),True,30,self.image)

            # Create the next button
            self.next_button = pt.Button(0,'Next',(600,550),True,surface = self.image)

        def update(self,screen,clock):
            while True:
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONUP and self.next_button.rect.collidepoint(pygame.mouse.get_pos()):
                        return 2
                screen.blit(self.image,(0,0))
                pygame.display.flip()

    class Page2(object):
        def __init__(self,text,progress):
            # Create the image that the title screen is to be written on
            self.image = pygame.Surface((800,600))
            self.image.fill((255,193,37))

            # Create the story text
            pt.Linesoftext(text,(400,30),True,30,self.image)

            # Create the next button
            self.fight_button = pt.Button(0,'Fight',(600,550),True,surface = self.image)

        def update(self,screen,clock):
            while True:
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONUP and self.fight_button.rect.collidepoint(pygame.mouse.get_pos()):
                        return 4
                screen.blit(self.image,(0,0))
                pygame.display.flip()

    def update(self,screen,clock):
        while True:
            # Page
            # 1 = Story text
            # 2 = Pull up the next text and return to page 1
            # 3 = Last page of text
            # 4 = Initiate combat
            if self.page == 1:
                self.page = self.Page1(self.text[self.text_pos]).update(screen,clock)
            elif self.page == 2:
                self.text_pos += 1
                if self.text_pos < (len(self.text) - 1):
                    self.page = 1
                elif self.text_pos == (len(self.text) - 1):
                    self.page = 3
            elif self.page == 3:
                self.page = self.Page2(self.text[self.text_pos],self.progress).update(screen,clock)
            elif self.page == 4:
                return (3,1)

################################################################################
################################################################################

# Level up screens

class Levelupscreen(object):
    def __init__(self,player):
        # set the indicator to display the first part of the screen
        self.page = 1
        self.player = player

    class Nextlevel(object):
        def __init__(self,player):
            self.player = player

            # create the image that the screen will be drawn on
            self.image = pygame.Surface((800,600))
            self.image.fill((50, 205, 50))

            # Draw the header text to the image
            pt.Linesoftext(['           Level up!','Choose your bonuses'],(400,50),True,surface = self.image)

            # Draw the buttons
            self.strength_button = pt.Button(0,'Strength',(330,250),surface = self.image)
            self.durability_button = pt.Button(0,'Durability',(330,300),surface = self.image)
            self.dexterity_button = pt.Button(0,'Dexterity',(330,350),surface = self.image)

        def update(self,screen,clock):
            while True:
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONUP and self.strength_button.rect.collidepoint(pygame.mouse.get_pos()):
                        self.player.str_up()
                        return 2
                    elif event.type == pygame.MOUSEBUTTONUP and self.durability_button.rect.collidepoint(pygame.mouse.get_pos()):
                        self.player.dur_up()
                        return 2
                    elif event.type == pygame.MOUSEBUTTONUP and self.dexterity_button.rect.collidepoint(pygame.mouse.get_pos()):
                        self.player.dex_up()
                        return 2
                screen.blit(self.image,(0,0))
                pygame.display.flip()

    class Finishleveling(object):
        def __init__(self):
            # Create the background image to be drawn upon
            self.image = pygame.Surface((800,600))
            self.image.fill((50, 205, 50))

            # Draw the header text
            pt.Linesoftext(['            Please continue.'],(400,200),True,surface = self.image)

            # Draw the continue button
            self.continue_button = pt.Button(0,'Continue',(600,500),True,surface = self.image)

        def update(self,screen,clock):
            while True:
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONUP and self.continue_button.rect.collidepoint(pygame.mouse.get_pos()):
                        return 3
                screen.blit(self.image,(0,0))
                pygame.display.flip()

    def update(self,screen,clock):
        while True:
            if self.page == 1:
                self.page = self.Nextlevel(self.player).update(screen,clock)
            elif self.page == 2:
                self.page = self.Finishleveling().update(screen,clock)
            elif self.page == 3:
                return 2

################################################################################
################################################################################

# Combat screens

class Combatscreen(object):
    def __init__(self,player,encounter):
        self.page = 1

        # bring in the player as an attribute of the combat screen
        self.player = player

        # Create the monster for the encounter
        self.encounter = encounter
        self.monster = Monster(encounter)

    class Chooseaction(object):
        def __init__(self,player,monster):

            # Create the image that the screen will be drawn on
            self.image = pygame.Surface((800,600))
            self.image.fill((50, 205, 50))

            # Create the health and pictures of the combatants
            pt.Button(1,player.pic,(200,200), midpoint = True,resize = (300,300),surface = self.image)
            pt.Button(1,monster.pic,(600,200), midpoint = True,resize = (300,300),surface = self.image)

            pt.Linesoftext(['Hp                               %d/%d' % (player.hp,player.hpmax)],(200,10),True,surface = self.image)
            pt.Linesoftext(['Hp                               %d/%d' % (monster.hp,monster.hpmax)],(600,10),True,surface = self.image)

            playerhpbar = pygame.Rect((87,12),(int(200 * player.hp/player.hpmax),20))
            pygame.draw.rect(self.image,(255,0,0),playerhpbar)

            monsterhpbar = pygame.Rect((490,12),(int(200 * monster.hp/monster.hpmax),20))
            pygame.draw.rect(self.image,(255,0,0),monsterhpbar)

            # Draw the instructional text and the four attack type buttons
            pt.Linesoftext(['Choose a type of attack'],(400,370),True,surface = self.image)

            self.standard_button = pt.Button(0,'Standard',(250,480),True,surface = self.image)
            self.defensive_button = pt.Button(0,'Defensive',(250,430),True,surface = self.image)
            self.aggressive_button = pt.Button(0,'Aggressive',(530,430),True,surface = self.image)
            self.precise_button = pt.Button(0,'Precise',(530,480),True,surface = self.image)

        def update(self,screen,clock):
            while True:
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONUP and self.standard_button.rect.collidepoint(pygame.mouse.get_pos()):
                        return (2,1)
                    elif event.type == pygame.MOUSEBUTTONUP and self.defensive_button.rect.collidepoint(pygame.mouse.get_pos()):
                        return (2,2)
                    elif event.type == pygame.MOUSEBUTTONUP and self.aggressive_button.rect.collidepoint(pygame.mouse.get_pos()):
                        return (2,3)
                    elif event.type == pygame.MOUSEBUTTONUP and self.precise_button.rect.collidepoint(pygame.mouse.get_pos()):
                        return (2,4)
                screen.blit(self.image,(0,0))
                pygame.display.flip()

    class Fight(object):
        def __init__(self,player,monster,action):
            # Bring in the player and monster data
            self.player = player
            self.monster = monster

            # run the combat logic
            results = combat(player,monster,action)

            # if either combatant died set the hp to zero
            if monster.hp <= 0:
                monster.hp = 0
            if player.hp <= 0:
                player.hp = 0

            # Create the image to be drawn upon
            self.image = pygame.Surface((800,600))
            self.image.fill((50, 205, 50))

            # Create the health and pictures of the combatants
            pt.Button(1,player.pic,(200,200), midpoint = True,resize = (300,300),surface = self.image)
            pt.Button(1,monster.pic,(600,200), midpoint = True,resize = (300,300),surface = self.image)

            pt.Linesoftext(['Hp                               %d/%d' % (player.hp,player.hpmax)],(200,10),True,surface = self.image)
            pt.Linesoftext(['Hp                               %d/%d' % (monster.hp,monster.hpmax)],(600,10),True,surface = self.image)

            playerhpbar = pygame.Rect((87,12),(int(200 * player.hp/player.hpmax),20))
            pygame.draw.rect(self.image,(255,0,0),playerhpbar)

            monsterhpbar = pygame.Rect((490,12),(int(200 * monster.hp/monster.hpmax),20))
            pygame.draw.rect(self.image,(255,0,0),monsterhpbar)

            # Put the results of the turn on the screen
            pt.Linesoftext(results,(400,400),True,surface = self.image)

            # Create continue button and back buttons
            self.continue_button = pt.Button(0,'Continue',(600,500),True,surface = self.image)

        def update(self,screen,clock):
            while True:
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONUP and self.continue_button.rect.collidepoint(pygame.mouse.get_pos()):
                        if self.player.hp <= 0 or self.monster.hp <= 0:
                            return 3
                        else:
                            return 1
                screen.blit(self.image,(0,0))
                pygame.display.flip()

    class Endscreen(object):
        def __init__(self,player,monster):

            # Create the surface that the screen will be drawn on
            self.image = pygame.Surface((800,600))
            self.image.fill((50, 205, 50))

            # Create the win loss text
            if player.hp == 0 and monster.hp == 0:
                pt.Linesoftext(['It was a draw!'],(400,400),True,surface = self.image)
                self.condition = 0
            elif player.hp == 0:
                pt.Linesoftext(['You lost'],(400,400),True,surface = self.image)
                self.condition = 0
            elif monster.hp == 0:
                pt.Linesoftext(['You won!'],(400,400),True,surface = self.image)
                self.condition = 1

            # Create the retry or continue buttons
            if self.condition == 0:
                self.retry_button = pt.Button(0,'Retry?',(600,500),True,surface = self.image)
            elif self.condition == 1:
                self.continue_button = pt.Button(0,'Continue',(600,500),True,surface = self.image)

            # Create the health and pictures of the combatants
            pt.Button(1,player.pic,(200,200), midpoint = True,resize = (300,300),surface = self.image)
            pt.Button(1,monster.pic,(600,200), midpoint = True,resize = (300,300),surface = self.image)

            pt.Linesoftext(['Hp                               %d/%d' % (player.hp,player.hpmax)],(200,10),True,surface = self.image)
            pt.Linesoftext(['Hp                               %d/%d' % (monster.hp,monster.hpmax)],(600,10),True,surface = self.image)

            playerhpbar = pygame.Rect((87,12),(int(200 * player.hp/player.hpmax),20))
            pygame.draw.rect(self.image,(255,0,0),playerhpbar)

            monsterhpbar = pygame.Rect((490,12),(int(200 * monster.hp/monster.hpmax),20))
            pygame.draw.rect(self.image,(255,0,0),monsterhpbar)

        def update(self,screen,clock):
            while True:
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if self.condition:
                        if event.type == pygame.MOUSEBUTTONUP and self.continue_button.rect.collidepoint(pygame.mouse.get_pos()):
                            return 4
                    elif event.type == pygame.MOUSEBUTTONUP and self.retry_button.rect.collidepoint(pygame.mouse.get_pos()) and not self.condition:
                        return 5
                screen.blit(self.image,(0,0))
                pygame.display.flip()

    def update(self,screen,clock):
        """Handle the different pages of the combat screens"""
        while True:
            if self.page == 1:
                (self.page,self.action) = self.Chooseaction(self.player,self.monster).update(screen,clock)
            elif self.page == 2:
                self.page = self.Fight(self.player,self.monster,self.action).update(screen,clock)
            elif self.page == 3:
                self.page = self.Endscreen(self.player,self.monster).update(screen,clock)
            elif self.page == 4:
                # Player won and is continuing
                self.player.hp = self.player.hpmax
                return 2
            elif self.page == 5:
                # Player lost and is going to retry the combat
                self.player.hp = self.player.hpmax
                self.monster = Monster(self.encounter)
                self.page = 1


################################################################################
################################################################################

# Game class

class Game(object):
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.progress = 1
        self.pages = 1
        self.player = Player(13)

    def update(self,screen):
        while True:
            # Progress:
            # 1 = Title screen
            # 2 = Story screen
            # 3 = Combat screens
            # 4 = Tutorial screen
            # 5 = Level up screen
            # 6 = End game screen

            if self.pages == 1:
                self.pages = Titlescreen().update(screen,self.clock)
            elif self.pages == 2:
                self.pages,self.encounter = Storyscreen(self.progress).update(screen,self.clock)
            elif self.pages == 3:
                self.pages = Combatscreen(self.player,self.encounter).update(screen,self.clock)
                self.progress += 1
                if not self.progress % 2:
                    self.pages = 5
                elif self.progress == 3:
                    self.pages = 6
            elif self.pages == 4:
                self.pages,self.encounter = Tutorialscreen(13).update(screen,self.clock)
            elif self.pages == 5:
                self.pages = Levelupscreen(self.player).update(screen,self.clock)
            elif self.pages == 6:
                Endgamescreen(self.progress).update(screen,self.clock)
                self.__init__()

################################################################################
################################################################################

# Initialization of the game

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    Game().update(screen)

