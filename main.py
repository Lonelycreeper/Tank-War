import pygame
import sys
import time
import os
py=pygame
py.init
scr=py.display.set_mode((600,450),pygame.RESIZABLE)
py.display.set_caption("Tank War")
WIDTH=60
HEIGHT=60
clock = pygame.time.Clock()
pygame.display.flip()
V=1
size=[40,55]
size2=[55,43]
xy=[0,0]
ST=2
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image =py.image.load("./img/Tank.png").convert()#load image
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, size)
    def update(self):
        posi=self.rect
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
                xy[0] -=V
                self.image =py.image.load("./img/Tank-l.png").convert()
                self.image = pygame.transform.scale(self.image, size2)
                pygame.time.wait(ST)
        if keys[pygame.K_RIGHT]:
                xy[0] += V
                self.image =py.image.load("./img/Tank-r.png").convert()
                self.image = pygame.transform.scale(self.image, size2)
                pygame.time.wait(ST)
        if keys[pygame.K_UP]:
                xy[1] -= V
                self.image =py.image.load("./img/Tank.png").convert()
                self.image = pygame.transform.scale(self.image, size)
                pygame.time.wait(ST)
        if keys[pygame.K_DOWN]:
                xy[1] +=V
                self.image =py.image.load("./img/Tank-d.png").convert()
                self.image = pygame.transform.scale(self.image, size)
                pygame.time.wait(ST)
        posi=posi.move(xy)
        scr.blit(self.image,posi)
        pygame.display.flip()

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

#////////////////////sprite//////////////////////////////#

all_sprites = pygame.sprite.Group()
player=Player()
all_sprites.add(player)
run = True
all_sprites.draw(scr)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    scr.fill((255,255,255))
    player.update()
        

