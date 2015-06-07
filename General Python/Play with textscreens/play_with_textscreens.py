#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      James
#
# Created:     28/08/2014
# Copyright:   (c) James 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame,sys
import pygametools as pt

pygame.init()

text = [['        You start to wake up. First thing you notice is a dizzing headache. As',
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
                  ['OH my god!','SOOO many pages'], ['Like seriously!','Lots of pages!'],
                  ['        "Boulden how bad is it? How many are left?", you ask. "Very bad sir. Not',
                    " many survived as far as we can tell and those that did aren't in good shape.",
                    " You look like the most whole person I've" ' seen this morning", he stammered.',
                    '"Come ' "I'll show you to the others. We've set up a medical area on the lawn",
                    ' out front"']]

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

class Textscreens(pt.Textscreens):
    def __init__(self,text):
        pt.Textscreens.__init__(self,(800,600),(200,200,200),text,['Continue',lambda:15])

x = Textscreens(text).update(screen,clock)
print(x)


pygame.quit()
sys.exit()





