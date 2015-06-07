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

import pygame, sys
import pytmx as tmx

class Player(pygame.sprite.Sprite):
    def __init__(self,location,*groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load('player.png')
        self.rect = pygame.rect.Rect(location, self.image.get_size())


    def update(self,dt,game):
        last = self.rect.copy()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 200 * dt
        if key[pygame.K_RIGHT]:
            self.rect.x += 200 * dt
        if key[pygame.K_UP]:
            self.rect.y -= 200 * dt
        if key[pygame.K_DOWN]:
            self.rect.y += 200 * dt

        new = self.rect
        for cell in game.tilemap.layers['triggers'].collide(new,'blockers'):
            blockers = cell['blockers']
            if 'l' in blockers and last.right <= cell.left and new.right > cell.left:
                new.right = cell.left
            if 'r' in blockers and last.left >= cell.right and new.left < cell.right:
                new.left = cell.right
            if 't' in blockers and last.bottom <= cell.top and new.bottom > cell.top:
                new.bottom = cell.top
            if 'b' in blockers and last.top >= cell.bottom and new.top < cell.bottom:
                new.top = cell.bottom

        for cell in game.tilemap.layers['triggers'].collide(new,'win'):
            game.win = 0

        game.tilemap.set_focus(new.x, new.y)

class Picture_Button(pygame.sprite.Sprite):
    #This class is used for creating picture buttons
    def __init__(self,picture_name,x = 0, y = 0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(picture_name)
        self.rect = pygame.rect.Rect((x,y),self.image.get_size())

    def set_size(self,w,h):
        """This will resize the image to the given width and height inputs"""
        self.image = pygame.transform.scale(self.image,(w,h))


class Game(object):
    def main(self,screen):
        clock = pygame.time.Clock()

        self.tilemap = tmx.load('map.tmx',screen.get_size())
        self.sprites = tmx.SpriteLayer()
        start_cell = self.tilemap.layers['triggers'].find('player')[0]
        self.player = Player((start_cell.px, start_cell.py), self.sprites)
        self.tilemap.layers.append(self.sprites)

        self.win = True
        winbox_pos = self.tilemap.layers['triggers'].find('win')[0]
        self.winbox = Picture_Button('win box.png',winbox_pos.px - 64,
                                     winbox_pos.py- 64)

        while True:
            dt = clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if self.win == 0:
                self.sprites.add(self.winbox)
                self.win = 1

            self.tilemap.update(dt / 1000.,self)
            self.tilemap.draw(screen)

            pygame.display.flip()



if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1200, 700))
    Game().main(screen)


