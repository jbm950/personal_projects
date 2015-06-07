#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      James
#
# Created:     16/06/2014
# Copyright:   (c) James 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame,sys

class Game(object):
    def main(self,screen):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    Game().main(screen)


