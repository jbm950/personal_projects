#-------------------------------------------------------------------------------
# Name:        combat_tester.py
# Purpose:     This program will create a test environment for the different
#              encounters in torrics quest.
#
# Author:      James
#
# Created:     24/06/2014
# Copyright:   (c) James 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame, sys, random, copy
import pygametools_0_0 as pt

class Monster(object):
    def __init__(self,monsternum):
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

class Titlescreen(object):
    def __init__(self):
        # Create the image that the screen will be drawn on
        self.image = pygame.Surface((800,600))
        self.image.fill((50, 205, 50))

        # Create the header text
        pt.Linesoftext(["Welcome to the combat tester for Torric's Quest"],
                                          (400,50),True,backgroundcolor = (50, 205, 50), surface = self.image)

        # Create the begin and quit buttons
        self.begin_button = pt.Button(0,'Begin',(400,350), True, surface = self.image)
        self.quit_button = pt.Button(0,'Quit',(400,400), True, surface = self.image)

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
                if event.type == pygame.MOUSEBUTTONUP and self.begin_button.rect.collidepoint(pygame.mouse.get_pos()):
                    return 2
            screen.blit(self.image,(0,0))
            pygame.display.flip()

class Encounterscreen(object):
    def __init__(self):
        # Create the image that the screen will be drawn on
        self.image = pygame.Surface((800,600))
        self.image.fill((50, 205, 50))

        # Create the header text
        self.header_text = pt.Linesoftext(['Choose the encounter'],(400,50),True,
                                          backgroundcolor = (50, 205, 50),surface = self.image)

        # Create the buttons for the different encounters in the game
        self.bridge = pt.Button(0,'Bridge',(150,150),surface = self.image)
        self.clearing1 = pt.Button(0,'Clearing 1',(150,200),surface = self.image)
        self.cave1 = pt.Button(0,'Cave 1',(150,250),surface = self.image)
        self.first_camp = pt.Button(0,'First Camp', (150,300),surface = self.image)
        self.cave2 = pt.Button(0,'Cave 2',(150,350),surface = self.image)
        self.clearing2 = pt.Button(0,'Clearing 2',(150,400),surface = self.image)
        self.second_camp = pt.Button(0,'Second Camp',(150,450),surface = self.image)
        self.cave3 = pt.Button(0,'Cave 3',(500,150),surface = self.image)
        self.clearing3 = pt.Button(0,'Clearing 3',(500,200),surface = self.image)
        self.cave4 = pt.Button(0,'Cave 4',(500,250),surface = self.image)
        self.cave5 = pt.Button(0,'Cave 5',(500,300),surface = self.image)
        self.third_camp = pt.Button(0,'Third Camp',(500,350),surface = self.image)
        self.final_battle = pt.Button(0,'Final Boss Fight',(500,400),surface = self.image)

    def update(self,screen,clock):
        while True:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # return Progress, monster number, encounter level
                if event.type == pygame.MOUSEBUTTONUP and self.bridge.rect.collidepoint(pygame.mouse.get_pos()):
                    return(3,1,1)
                if event.type == pygame.MOUSEBUTTONUP and self.clearing1.rect.collidepoint(pygame.mouse.get_pos()):
                    return(3,2,2)
                if event.type == pygame.MOUSEBUTTONUP and self.cave1.rect.collidepoint(pygame.mouse.get_pos()):
                    return(3,3,2)
                if event.type == pygame.MOUSEBUTTONUP and self.first_camp.rect.collidepoint(pygame.mouse.get_pos()):
                    return(3,4,2)
                if event.type == pygame.MOUSEBUTTONUP and self.cave2.rect.collidepoint(pygame.mouse.get_pos()):
                    return(3,5,3)
                if event.type == pygame.MOUSEBUTTONUP and self.clearing2.rect.collidepoint(pygame.mouse.get_pos()):
                    return(3,6,3)
                if event.type == pygame.MOUSEBUTTONUP and self.second_camp.rect.collidepoint(pygame.mouse.get_pos()):
                    return(3,7,4)
                if event.type == pygame.MOUSEBUTTONUP and self.cave3.rect.collidepoint(pygame.mouse.get_pos()):
                    return(3,8,4)
                if event.type == pygame.MOUSEBUTTONUP and self.clearing3.rect.collidepoint(pygame.mouse.get_pos()):
                    return(3,9,5)
                if event.type == pygame.MOUSEBUTTONUP and self.cave4.rect.collidepoint(pygame.mouse.get_pos()):
                    return(3,10,5)
                if event.type == pygame.MOUSEBUTTONUP and self.cave5.rect.collidepoint(pygame.mouse.get_pos()):
                    return(3,11,6)
                if event.type == pygame.MOUSEBUTTONUP and self.third_camp.rect.collidepoint(pygame.mouse.get_pos()):
                    return(3,12,6)
                if event.type == pygame.MOUSEBUTTONUP and self.final_battle.rect.collidepoint(pygame.mouse.get_pos()):
                    return(3,13,6)

            screen.blit(self.image,(0,0))
            pygame.display.flip()

class Levelupscreen(object):
    def __init__(self,player,encounterlvl):
        # set the indicator to display the first part of the screen
        self.page = 1
        self.player = player
        self.encounterlvl = encounterlvl

    class Nextlevel(object):
        def __init__(self,player,encounterlvl):
            self.player = player
            self.encounterlvl = encounterlvl

            # create the image that the screen will be drawn on
            self.image = pygame.Surface((800,600))
            self.image.fill((50, 205, 50))

            # Draw the header text to the image
            self.header_text = pt.Linesoftext(['           Level up!','Choose your bonuses'],(400,50),
                                              True,backgroundcolor = (50, 205, 50),surface = self.image)

            # Draw the buttons
            self.strength_button = pt.Button(0,'Strength',(330,250),surface = self.image)
            self.durability_button = pt.Button(0,'Durability',(330,300),surface = self.image)
            self.dexterity_button = pt.Button(0,'Dexterity',(330,350),surface = self.image)
            self.back_button = pt.Button(0,'Back',(200,500),True,surface = self.image)

        def update(self,screen,clock):
            while True:
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONUP and self.back_button.rect.collidepoint(pygame.mouse.get_pos()):
                        return 3
                    if event.type == pygame.MOUSEBUTTONUP and self.strength_button.rect.collidepoint(pygame.mouse.get_pos()):
                        self.player.str_up()
                        if self.player.level == self.encounterlvl:
                            return 2
                    if event.type == pygame.MOUSEBUTTONUP and self.durability_button.rect.collidepoint(pygame.mouse.get_pos()):
                        self.player.dur_up()
                        if self.player.level == self.encounterlvl:
                            return 2
                    if event.type == pygame.MOUSEBUTTONUP and self.dexterity_button.rect.collidepoint(pygame.mouse.get_pos()):
                        self.player.dex_up()
                        if self.player.level == self.encounterlvl:
                            return 2
                screen.blit(self.image,(0,0))
                pygame.display.flip()

    class Finishleveling(object):
        def __init__(self):
            # Create the background image to be drawn upon
            self.image = pygame.Surface((800,600))
            self.image.fill((50, 205, 50))

            # Draw the header text
            self.header_text = pt.Linesoftext(['You are at the correct level for the encounter'],(400,200),
                                              True,backgroundcolor = (50, 205, 50),surface = self.image)

            # Draw the back and continue buttons
            self.back_button = pt.Button(0,'Back',(200,500),True,surface = self.image)
            self.continue_button = pt.Button(0,'Continue',(600,500),True,surface = self.image)

        def update(self,screen,clock):
            while True:
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONUP and self.back_button.rect.collidepoint(pygame.mouse.get_pos()):
                        return 3
                    if event.type == pygame.MOUSEBUTTONUP and self.continue_button.rect.collidepoint(pygame.mouse.get_pos()):
                        return 4
                screen.blit(self.image,(0,0))
                pygame.display.flip()

    def update(self,screen,clock):
        if self.player.level == self.encounterlvl:
            self.page = 2
        while True:
            if self.page == 1:
                self.page = self.Nextlevel(self.player,self.encounterlvl).update(screen,clock)
            if self.page == 2:
                self.page = self.Finishleveling().update(screen,clock)
            if self.page == 3:
                return 2
            if self.page == 4:
                return 4

class Combatscreen(object):
    def __init__(self,player,monster):
        # Bring in the player and monster data
        self.player = player
        self.monster = monster

        # Set the screen indicator
        self.page = 1

    class Chooseaction(object):
        def __init__(self,player,monster):
            # Bring in the player and monster data
            self.player = player
            self.monster = monster

            # Create the image that the screen will be drawn on
            self.image = pygame.Surface((800,600))
            self.image.fill((50, 205, 50))

            # Create the health and pictures of the combatants
            self.playerimage = pt.Button(1,self.player.pic,(200,200), midpoint = True,
                                         resize = (300,300),surface = self.image)
            self.monsterimage = pt.Button(1,self.monster.pic,(600,200), midpoint = True,
                                         resize = (300,300),surface = self.image)
            self.playerhptext = pt.Linesoftext(['Hp                               %d/%d' % (self.player.hp,self.player.hpmax)],
                                                (200,10), xmid = True, backgroundcolor = (50, 205, 50),surface = self.image)
            self.monsterhptext = pt.Linesoftext(['Hp                               %d/%d' % (self.monster.hp,self.monster.hpmax)],
                                                (600,10), xmid = True, backgroundcolor = (50, 205, 50),surface = self.image)

            self.playerhpbar = pygame.Rect((87,12),(int(200 * self.player.hp/self.player.hpmax),20))
            pygame.draw.rect(self.image,(255,0,0),self.playerhpbar)

            self.monsterhpbar = pygame.Rect((490,12),(int(200 * self.monster.hp/self.monster.hpmax),20))
            pygame.draw.rect(self.image,(255,0,0),self.monsterhpbar)

            # Draw the instructional text and the four attack type buttons
            self.header_text = pt.Linesoftext(['Choose a type of attack'],(400,370),True,
                                              backgroundcolor = (50, 205, 50),surface = self.image)
            self.standard_button = pt.Button(0,'Standard',(250,430),True,surface = self.image)
            self.defensive_button = pt.Button(0,'Defensive',(250,480),True,surface = self.image)
            self.aggressive_button = pt.Button(0,'Aggressive',(530,430),True,surface = self.image)
            self.precise_button = pt.Button(0,'Precise',(530,480),True,surface = self.image)

        def update(self,screen,clock):
            while True:
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONUP and self.standard_button.rect.collidepoint(pygame.mouse.get_pos()):
                        return (2,1)
                    if event.type == pygame.MOUSEBUTTONUP and self.defensive_button.rect.collidepoint(pygame.mouse.get_pos()):
                        return (2,2)
                    if event.type == pygame.MOUSEBUTTONUP and self.aggressive_button.rect.collidepoint(pygame.mouse.get_pos()):
                        return (2,3)
                    if event.type == pygame.MOUSEBUTTONUP and self.precise_button.rect.collidepoint(pygame.mouse.get_pos()):
                        return (2,4)
                screen.blit(self.image,(0,0))
                pygame.display.flip()

    class Fight(object):
        def __init__(self,player,monster,action):
            # Bring in the player and monster data and the attack type that the
            # player chose
            self.player = player
            self.monster = monster
            self.action = action

            if self.action == 1:
                self.attacktype = 'standard'
            elif self.action == 2:
                self.attacktype = 'defensive'
            elif self.action == 3:
                self.attacktype = 'aggressive'
            elif self.action == 4:
                self.attacktype = 'precise'


            # Create temporary versions of the player and monster
            self.playertemp = copy.copy(player)
            self.monstertemp = copy.copy(monster)

            # Chose an action for the monster
            self.monsteraction = random.choice(self.monster.attack_pref)

            # Initiate the results list of strings
            self.results = []

        def standard(self):
            if self.monsteraction == 'defensive':
                pass
            elif self.monsteraction == 'aggressive':
                self.monstertemp.damage += int(self.monstertemp.agress_bonus_damage * 0.7)
                self.monstertemp.accuracy -= int(self.monstertemp.accuracy * 0.7)
            elif self.monsteraction == 'precise':
                self.monstertemp.accuracy += self.monstertemp.precision_bonus
                self.monstertemp.damage += int(self.monstertemp.damage * 0.3)

        def defensive(self):
            if self.monsteraction == 'standard':
                pass
            elif self.monsteraction == 'aggressive':
                self.playertemp.damage += int(self.monstertemp.agress_bonus_damage * 0.5)
                self.monstertemp.damage -= self.playertemp.def_damagereduc
            elif self.monsteraction == 'precise':
                self.playertemp.accuracy = int(self.playertemp.accuracy * 0.7)
                self.monstertemp.damage -= int(self.playertemp.def_damagereduc * 0.7)
                self.monstertemp.accuracy += self.monstertemp.precision_bonus

        def aggressive(self):
            if self.monsteraction == 'standard':
                self.playertemp.damage += int(self.playertemp.agress_bonus_damage * 0.7)
                self.playertemp.accuracy -= int(self.playertemp.accuracy * 0.7)
            elif self.monsteraction == 'defensive':
                self.monstertemp.damage += int(self.playertemp.agress_bonus_damage * 0.5)
                self.playertemp.damage -= self.monstertemp.def_damagereduc
            elif self.monsteraction == 'precise':
                self.playertemp.accuracy += int(self.playertemp.accuracy * 0.4)
                self.playertemp.damage += self.playertemp.agress_bonus_damage
                self.monstertemp.damage = int(self.monstertemp.damage * 0.7)

        def precise(self):
            if self.monsteraction == 'standard':
                self.playertemp.accuracy += self.playertemp.precision_bonus
                self.playertemp.damage += int(self.playertemp.damage * 0.3)
            elif self.monsteraction == 'defensive':
                self.playertemp.accuracy += self.playertemp.precision_bonus
                self.playertemp.damage -= int(self.monstertemp.def_damagereduc * 0.7)
                self.monstertemp.accuracy = int(self.monstertemp.accuracy * 0.7)
            elif self.monsteraction == 'aggresive':
                self.playertemp.damage = int(self.playertemp.damage * 0.7)
                self.monstertemp.accuracy += int(self.monstertemp.accuracy * 0.4)
                self.monstertemp.damage += self.playertemp.agress_bonus_damage

        def combat(self):
            if self.action == 1:
                self.standard()
            elif self.action == 2:
                self.defensive()
            elif self.action == 3:
                self.aggressive()
            elif self.action == 4:
                self.precise()

            # Attempt to hit and do damage
            if random.randint(1,100) <= (100 - self.monstertemp.evasion + self.playertemp.accuracy):
                self.monster.hp -= self.playertemp.damage
                self.results.append('You used a/an %s attack doing %d damage' % (self.attacktype,self.playertemp.damage))
            else:
                self.results.append('Your %s attack missed' % (self.attacktype))

            if random.randint(1,100) <= (100 - self.playertemp.evasion + self.monstertemp.accuracy):
                self.player.hp -= self.monstertemp.damage
                self.results.append('%s used a/an %s attack doing %d damage' % (self.monster.name,self.monsteraction,self.monstertemp.damage))
            else:
                self.results.append('%s used a/an %s attack and missed' % (self.monster.name,self.monsteraction))

        def draw(self):
            # run the combat logic
            self.combat()

            # if either combatant died set the hp to zero
            if self.monster.hp <= 0:
                self.monster.hp = 0
            if self.player.hp <= 0:
                self.player.hp = 0

            # Create the image to be drawn upon
            self.image = pygame.Surface((800,600))
            self.image.fill((50, 205, 50))

            # Draw the player and monster images and health
            # Create the health and pictures of the combatants
            self.playerimage = pt.Button(1,self.player.pic,(200,200), midpoint = True,
                                         resize = (300,300),surface = self.image)
            self.monsterimage = pt.Button(1,self.monster.pic,(600,200), midpoint = True,
                                         resize = (300,300),surface = self.image)
            self.playerhptext = pt.Linesoftext(['Hp                               %d/%d' % (self.player.hp,self.player.hpmax)],
                                                (200,10), xmid = True, backgroundcolor = (50, 205, 50),surface = self.image)
            self.monsterhptext = pt.Linesoftext(['Hp                               %d/%d' % (self.monster.hp,self.monster.hpmax)],
                                                (600,10), xmid = True, backgroundcolor = (50, 205, 50),surface = self.image)

            self.playerhpbar = pygame.Rect((87,12),(int(200 * self.player.hp/self.player.hpmax),20))
            pygame.draw.rect(self.image,(255,0,0),self.playerhpbar)

            self.monsterhpbar = pygame.Rect((490,12),(int(200 * self.monster.hp/self.monster.hpmax),20))
            pygame.draw.rect(self.image,(255,0,0),self.monsterhpbar)

            # Put the results of the turn on the screen
            self.resultstext = pt.Linesoftext(self.results,(400,400),True,backgroundcolor = (50, 205, 50),
                                              surface = self.image)

            # Create continue button and back buttons
            self.continue_button = pt.Button(0,'Continue',(600,500),True,surface = self.image)
            self.back_button = pt.Button(0,'Back',(200,500),True,surface = self.image)

        def update(self,screen,clock):
            self.draw()
            while True:
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONUP and self.continue_button.rect.collidepoint(pygame.mouse.get_pos()):
                        if self.player.hp <= 0 or self.monster.hp <= 0:
                            return 4
                        else:
                            return 1
                    if event.type == pygame.MOUSEBUTTONUP and self.back_button.rect.collidepoint(pygame.mouse.get_pos()):
                        return 3
                screen.blit(self.image,(0,0))
                pygame.display.flip()

    class Endscreen(object):
        def __init__(self,player,monster):
            # Bring in the player and monster data
            self.player = player
            self.monster = monster

            # Create the surface that the screen will be drawn on
            self.image = pygame.Surface((800,600))
            self.image.fill((50, 205, 50))

            # Create the win loss text
            if self.player.hp == 0 and self.monster.hp == 0:
                self.header_text = pt.Linesoftext(['It was a draw!'],(400,400),True,backgroundcolor = (50, 205, 50),surface = self.image)
            elif self.player.hp == 0:
                self.header_text = pt.Linesoftext(['You lost'],(400,400),True,backgroundcolor = (50, 205, 50),surface = self.image)
            elif self.monster.hp == 0:
                self.header_text = pt.Linesoftext(['You won!'],(400,400),True,backgroundcolor = (50, 205, 50),surface = self.image)

            # Draw the player and monster images and health
            # Create the health and pictures of the combatants
            self.playerimage = pt.Button(1,self.player.pic,(200,200), midpoint = True,
                                         resize = (300,300),surface = self.image)
            self.monsterimage = pt.Button(1,self.monster.pic,(600,200), midpoint = True,
                                         resize = (300,300),surface = self.image)
            self.playerhptext = pt.Linesoftext(['Hp                               %d/%d' % (self.player.hp,self.player.hpmax)],
                                                (200,10), xmid = True, backgroundcolor = (50, 205, 50),surface = self.image)
            self.monsterhptext = pt.Linesoftext(['Hp                               %d/%d' % (self.monster.hp,self.monster.hpmax)],
                                                (600,10), xmid = True, backgroundcolor = (50, 205, 50),surface = self.image)

            self.playerhpbar = pygame.Rect((87,12),(int(200 * self.player.hp/self.player.hpmax),20))
            pygame.draw.rect(self.image,(255,0,0),self.playerhpbar)

            self.monsterhpbar = pygame.Rect((490,12),(int(200 * self.monster.hp/self.monster.hpmax),20))
            pygame.draw.rect(self.image,(255,0,0),self.monsterhpbar)

            # Create the back button
            self.back_button = pt.Button(0,'Back',(200,500),True,surface = self.image)

        def update(self,screen,clock):
            while True:
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONUP and self.back_button.rect.collidepoint(pygame.mouse.get_pos()):
                        return 3
                screen.blit(self.image,(0,0))
                pygame.display.flip()

    def update(self,screen,clock):
        while True:
            if self.page == 1:
                (self.page,self.action) = self.Chooseaction(self.player,self.monster).update(screen,clock)
            elif self.page == 2:
                self.page = self.Fight(self.player,self.monster,self.action).update(screen,clock)
            elif self.page == 3:
                return 2
            elif self.page == 4:
                self.page = self.Endscreen(self.player,self.monster).update(screen,clock)

class Game(object):
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.progress = 1

    def update(self,screen):
        while True:
            if self.progress == 1:
                self.progress = Titlescreen().update(screen,self.clock)
            if self.progress == 2:
                (self.progress,self.monsternum,self.encounterlvl) = Encounterscreen().update(screen,self.clock)
                self.monster = Monster(self.monsternum)
                print(type(self.monster.rawdata[9]))
                self.player = Player(14)
            if self.progress == 3:
                self.progress = Levelupscreen(self.player,self.encounterlvl).update(screen,self.clock)
            if self.progress == 4:
                self.progress = Combatscreen(self.player,self.monster).update(screen,self.clock)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    Game().update(screen)
