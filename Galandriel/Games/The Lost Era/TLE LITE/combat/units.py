# ------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      James
#
# Created:     01/09/2015
# Copyright:   (c) James 2015
# Licence:     <your licence>
# ------------------------------------------------------------------------------
# !/usr/bin/env python


class monster_base(object):
    def __init__(self, monsternum):
        # Open up the text file with the monster data and prepare a list of the
        # different lines of data
        self.rawdata = open('monsterdata.txt')
        self.rawdata = self.rawdata.readlines()[monsternum].split(',')

        # Take the raw data and set the monsters attributes
        self.name = self.rawdata[0]
        self.tile = ptgw.wTile(self.name, self.rawdata[1], (150, 150))
        self.tile.initialize_shade('black', (0, 0, 0), 235)
        self.hp = int(self.rawdata[2])
        self.damage = int(self.rawdata[3])
        self.hpmax = int(self.rawdata[4])
