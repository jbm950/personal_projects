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
                    ' out front"', "        Arriving at the medical area you see many decorn in bad"
                   " condition.", "There are some tending to the wounded but the vast majority are "
                   "the ones","being tended to, many looking like this might be their last day.",
                   '        "Torric!" you hear from one of the tents. Looking over you see Segal,',
                   " the second in charge at the monastary, though given the recent events it's",
                   "likely that his status has changed."],['        "Torric we need your help. The sacred sigil'
                    ' was taken in the raid last', 'night. With it the goblins and orcs could create '
                    "unprecedented chaos.", "As you can see you're the only one fit here to go retrieve it."
                    ' Torric,', 'the stability of the region is now in your hands you must head out at','once.'
                    ' The goblins have taken to the old trail heading along the edge of','the mountains."',
                    "        The news hits hard. The anchient sigil?! It's known to","contain powerful magic"
                    " but nothing has known how to use such magic", "in centuries. You quickly grab the nearest"
                    " armor and sword from among", "the fallen and head towards the old trail. At least your "
                    "headache has", "subsided"],
                   ["        You've just started down the old trail, pine trees your only current",
                    "company. Despite being an nice day in early spring the forest remains",
                    "quiet as if in reverence to those who fell during the night. You can hear",
                    "Low River in the distance and can already picture the old bridge that",
                    "you've crossed so many times over the years.",
                    "        As you approach the bridge you see an unwelcome visitor blocking",
                    "your path. One of the goblins from the raid remains standing directly in",
                    'the middle of your path. "They says one of yous might be comin after us.',
                    'I\'m here to ensure your road ends at this nasty place" it yells at you.',
                    'With that the goblin lunges foward sword drawn']]
    elif text_num == 2:
        return [['        With the goblin slain your journey continues. You keep following the',
                 'trail though the goblins still have quite a lead on you. The time and effort',
                 'to kill the goblin on the bridge set you back even more. With the sun',
                 'setting and still being a bit sore from the previous night you seek shelter.',
                 'By this time you\'ve left Low River far behind you and you begin to near',
                 'the mountains. As such you notice a cave not far off of the trail that would',
                 'make decent shelter for the fast approaching night. After making a mental',
                 'note of where to pick up the goblins trail in the morning you head off to',
                 'the cave to sleep.',
                 '        You wake up in the middle of the night, not really sure how many hours',
                 'have past. It\'s raining outside now and there\'s the occasional flash of',
                 'lightning. Perhaps that is what woke you up from your slumber.'],
                ['        As your head starts to clear from sleepy foggyness you notice another',
                 'noise in addition to the rain and lightning. Its a sort of rattling sound coming',
                 'from one of the side holes in the cave. While trying to make sense of the new',
                 'noise a figure stumbles out of the hole.',
                 '        It\'s a skeleton! But what unholyness could reanimate such a corpse?',
                 'Like the sigil\'s magic such a thing had been unheard of for centuries. Many',
                 'had even believed such stories to simply be fanciful tales rather than',
                 'historical fact. Such musings were irrelevant in the moment, however, as',
                 'the skeleton seems to have noticed your presence and with a seeming',
                 'hatred starts towards you. That\'s when you notice its axe.']]
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
