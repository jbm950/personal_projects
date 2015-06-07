#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      James
#
# Created:     28/01/2015
# Copyright:   (c) James 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from riotwatcher import RiotWatcher
import pygametools as pt

w = RiotWatcher('e4a0c61e-4a2b-41b2-9b98-5f95f745b1b7')

# check if we have API calls remaining
#print(w.can_make_request())

me = w.get_summoner(name='salvsis')

print(me)

a = pt.Linesoftext([str(me['name'])],(300,50),True)
a.test((600,300))

#print(w.get_stat_summary(me['id']))