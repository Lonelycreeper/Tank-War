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
sizet=[20,25]
ST=2
xy=[0,0]
ST2=2    
class Player(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image =py.image.load("./img/tankt.png").convert_alpha()#load image
                self.ttimage=py.image.load("./img/PT.png").convert_alpha()#load image
                self.rect = self.image.get_rect()
                self.image = pygame.transform.scale(self.image, size)
                self.ttimage=py.transform.scale(self.ttimage, sizet)
                self.v=4
                self.angle=0
                self.posi=self.rect
                self.xy=xy 
                
        def update(self):#main function of player
                posi=self.rect
                keys = pygame.key.get_pressed()
                if not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
                        if keys[pygame.K_LEFT]:
                                xy[0] -= self.v
                                self.image =py.image.load("./img/tankt.png").convert_alpha()
                                self.image = pygame.transform.scale(self.image, size)
                                self.image=py.transform.rotate(self.image,90)
                                pygame.time.wait(ST)
                        if keys[pygame.K_RIGHT]:
                                xy[0] +=self.v
                                self.image =py.image.load("./img/tankt.png").convert_alpha()
                                self.image = pygame.transform.scale(self.image, size)
                                self.image=py.transform.rotate(self.image,-90)
                                pygame.time.wait(ST)
                if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
                        if keys[pygame.K_UP]:
                                xy[1] -=self.v
                                self.image =py.image.load("./img/tankt.png").convert_alpha()
                                self.image = pygame.transform.scale(self.image, size)
                                pygame.time.wait(ST)
                        if keys[pygame.K_DOWN]:
                                xy[1] += self.v
                                self.image =py.image.load("./img/tankt.png").convert_alpha()
                                self.image = pygame.transform.scale(self.image, size)
                                self.image=py.transform.rotate(self.image,180)
                                pygame.time.wait(ST)
                self.posi=posi.move(self.xy)

class Bullet(pygame.sprite.Sprite):#the bullet part
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image=py.image.load("./img/bullet.png").convert_alpha()
                self.image = pygame.transform.scale(self.image, size)
                self.rect=self.image.get_rect()
                self.v=5
                self.xy=[0,0]
                self.move=0
                self.toward=1
                self.posi=self.rect
        def update(self):
                posi=self.rect
                self.image =py.image.load("./img/bullet.png").convert_alpha()
                self.image = pygame.transform.scale(self.image, size)
                keys=pygame.key.get_pressed()
                if self.move==0:
                        if keys[pygame.K_UP]:
                                self.toward=1
                        if keys[pygame.K_DOWN]:
                                self.toward=2
                                self.image=py.transform.rotate(self.image,180)
                        if keys[pygame.K_LEFT]:
                                self.toward=3
                                self.image=py.transform.rotate(self.image,90)
                        if keys[pygame.K_RIGHT]:
                                self.toward=4
                                self.image=py.transform.rotate(self.image,-90)
                        if keys[pygame.K_f]:
                                self.move=1
                        self.xy[0]=xy[0]
                        self.xy[1]=xy[1]
                        
                else:
                        if self.toward==1:
                                self.xy[1]-=self.v
                        if self.toward==2:
                                self.xy[1]+=self.v
                                self.image=py.transform.rotate(self.image,180)
                        if self.toward==3:
                                self.xy[0]-=self.v
                                self.image=py.transform.rotate(self.image,90)
                        if self.toward==4:
                                self.xy[0]+=self.v
                                self.image=py.transform.rotate(self.image,-90)
                self.posi=posi.move(self.xy)
                        

           
        
        


#////////////////////sprite//////////////////////////////#

        

