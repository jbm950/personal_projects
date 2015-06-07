#-------------------------------------------------------------------------------
# Name:        tq_combat.py
# Purpose:     This module will contain the necessary classes to perform the
#              combat functions of the game Torric's Quest.
#
# Author:      James
#
# Created:     03/02/2015
# Copyright:   (c) James 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

################################################################################
################################################################################

# Program contents

# - Imports
# - Player and monster classes
# - Combat engine

################################################################################
################################################################################
#Imports

import copy, random

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