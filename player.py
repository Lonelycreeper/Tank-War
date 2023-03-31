import pygame
import sys
import time
import os
import enemy
import random
move=0
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
                if not keys[pygame.K_UP] and not keys[pygame.K_w] and not keys[pygame.K_DOWN] and not keys[pygame.K_s]:
                        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                                xy[0] -= self.v
                                self.image =py.image.load("./img/tankt.png").convert_alpha()
                                self.image = pygame.transform.scale(self.image, size)
                                self.image=py.transform.rotate(self.image,90)
                                pygame.time.wait(ST)
                        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                                xy[0] +=self.v
                                self.image =py.image.load("./img/tankt.png").convert_alpha()
                                self.image = pygame.transform.scale(self.image, size)
                                self.image=py.transform.rotate(self.image,-90)
                                pygame.time.wait(ST)
                if not keys[pygame.K_RIGHT] and not  keys[pygame.K_d] and not keys[pygame.K_LEFT] and not keys[pygame.K_a]:
                        if keys[pygame.K_UP] or keys[pygame.K_w]:
                                xy[1] -=self.v
                                self.image =py.image.load("./img/tankt.png").convert_alpha()
                                self.image = pygame.transform.scale(self.image, size)
                                pygame.time.wait(ST)
                        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
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
                self.angle=0
                self.toward=1
                self.posi=self.rect
        def update(self):
                posi=self.rect
                self.image =py.image.load("./img/bullet.png").convert_alpha()
                self.image = pygame.transform.scale(self.image, size)
                keys=pygame.key.get_pressed()
                if self.move==0:
                        if keys[pygame.K_UP] or keys[pygame.K_w]:
                                self.toward=1
                                self.angle=0
                        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                                self.toward=2
                                self.angle=180
                        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                                self.toward=3
                                self.angle=90
                        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                                self.toward=4
                                self.angle=-90
                                
                        if keys[pygame.K_f]:
                                self.move=1
                        self.xy[0]=xy[0]
                        self.xy[1]=xy[1]
                        self.image=py.transform.rotate(self.image,self.angle)
                        
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
                        if self.xy[0]<0 or self.xy[0]>1550 or self.xy[1]>850 or self.xy[1] < 0:
                                self.move=0              
                self.posi=posi.move(self.xy)
                        

           
        
        


#////////////////////sprite//////////////////////////////#

        

