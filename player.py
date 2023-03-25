import pygame
import sys
import time
import os
import enemy
import random

py=pygame
x=0
y=0
clock = pygame.time.Clock()
size=[40,55]
size2=[55,43]
xy=[0,0]
ST=2
ST2=2    
class Player(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image =py.image.load("./img/Tank.png").convert_alpha()#load image
                self.rect = self.image.get_rect()
                self.image = pygame.transform.scale(self.image, size)
                self.v=1
                self.angle=0
                self.posi=self.rect 
                
        def update(self):
                posi=self.rect
                keys = pygame.key.get_pressed()
                if not keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                        if keys[pygame.K_LEFT]:
                                xy[0] -= self.v
                                self.image =py.image.load("./img/Tank.png").convert_alpha()
                                self.image = pygame.transform.scale(self.image, size)
                                self.image=py.transform.rotate(self.image,90)
                                pygame.time.wait(ST)
                        if keys[pygame.K_RIGHT]:
                                xy[0] +=self.v
                                self.image =py.image.load("./img/Tank.png").convert_alpha()
                                self.image = pygame.transform.scale(self.image, size)
                                self.image=py.transform.rotate(self.image,270)
                                pygame.time.wait(ST)
                if not keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
                
                        if keys[pygame.K_UP]:
                                xy[1] -=self.v
                                self.image =py.image.load("./img/Tank.png").convert_alpha()
                                self.image = pygame.transform.scale(self.image, size)
                                pygame.time.wait(ST)                                
                        if keys[pygame.K_DOWN]:
                                xy[1] += self.v
                                self.image =py.image.load("./img/Tank.png").convert_alpha()
                                self.image = pygame.transform.scale(self.image, size)
                                self.image=py.transform.rotate(self.image,180)
                                pygame.time.wait(ST)
                self.posi=posi.move(xy)

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
           
        
        


#////////////////////sprite//////////////////////////////#

        

