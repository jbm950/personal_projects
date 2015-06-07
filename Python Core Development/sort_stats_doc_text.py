#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      James
#
# Created:     04/06/2015
# Copyright:   (c) James 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import cProfile
import re
cProfile.run('re.compile("foo|bar")', 'restats')

import pstats
p = pstats.Stats('restats')
#p.strip_dirs().sort_stats(-1).print_stats()
p.sort_stats('time', 'cumtime').print_stats(.5, 'init')