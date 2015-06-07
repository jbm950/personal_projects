#-------------------------------------------------------------------------------
# Name:        tq_story.py
# Purpose:     this module will hold the story text for the game Torric's Quest
#
# Author:      James
#
# Created:     05/01/2015
# Copyright:   (c) James 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

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
                    ' out front"'],['Meet goblin guarding bridge']]
    elif text_num == 2:
        return [['Find a skeleton in a cave']]
    elif text_num == 3:
        return [['First goblin camp']]
    elif text_num == 4:
        return [['Second cave']]
    elif text_num == 5:
        return [['Open clearing']]
    elif text_num == 6:
        return [['Goblin camp cleared by hellbeast']]
    elif text_num == 7:
        return [['Third cave']]
    elif text_num == 8:
        return [['second clearing']]
    elif text_num == 9:
        return [['ghoul in cave']]
    elif text_num == 10:
        return [['find a shelum']]
    elif text_num == 11:
        return [['third goblin camp']]
    elif text_num == 12:
        return [['Final boss battle']]
    elif text_num == 13:
        return [['Epilogue']]
    elif text_num == 14:
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