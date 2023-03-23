import pygame
import sys
import time
import os
import random
py=pygame
py.init
scr=py.display.set_mode((600,450),pygame.RESIZABLE)
py.display.set_caption("Tank War")
WIDTH=60
HEIGHT=60
x=0
y=0
clock = pygame.time.Clock()
pygame.display.flip()
size=[40,55]
size2=[55,43]
xy=[0,0]
ST=2
ST2=2    
class Player(pygame.sprite.Sprite):
        def __init__(self):
        pygame.sprite.Sprite.__init__(self)
     
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image =py.image.load("./img/Tank.png").convert_alpha()#load image
                self.rect = self.image.get_rect()
                self.image = pygame.transform.scale(self.image, size)
                self.v=1
                self.angle=0 
                
        def update(self):
                posi=self.rect
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                        xy[0] -=self.v
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
                if keys[pygame.K_UP]:
                        xy[1] -=self.v
                        self.image =py.image.load("./img/Tank.png").convert_alpha()
                        self.image = pygame.transform.scale(self.image, size)
                        pygame.time.wait(ST)
                if keys[pygame.K_DOWN]:
                        xy[1] +=self.v
                        self.image =py.image.load("./img/Tank.png").convert_alpha()
                        self.image = pygame.transform.scale(self.image, size)
                        self.image=py.transform.rotate(self.image,180)
                        pygame.time.wait(ST)
                if keys[pygame.K_a]:
                        self.angle+=1
                        self.image =py.image.load("./img/Tank.png").convert_alpha()
                        self.image = pygame.transform.scale(self.image, size)
                        self.image=py.transform.rotate(self.image,self.angle)
                        
                elif keys[py.K_d]:
                        self.angle-=1
                        self.image =py.image.load("./img/Tank.png").convert_alpha()
                        self.image = pygame.transform.scale(self.image, size)
                        self.image=py.transform.rotate(self.image,self.angle)
                posi=posi.move(xy)
                scr.blit(self.image,posi)
                pygame.display.flip()

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)   
class EmeCar(pygame.sprite.Sprite):
    def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.xy=[0,0]
                self.image=pygame.image.load("./img/hehe.png").convert_alpha()
                self.rect=self.image.get_rect()
                self.re=0
                self.V=1
    def update(self):
        posi=self.rect
        self.image=pygame.image.load("./img/hehe.png").convert_alpha()
        self.move=random.randint(1,4)
        if xy[0]<self.xy[0]:
                self.xy[0]-=self.V
                pygame.time.wait(ST2)
        if xy[0]>self.xy[0]:
                self.xy[0]+=self.V
                pygame.time.wait(ST2)
        if xy[1]>self.xy[1]:
                self.xy[1]+=self.V
                pygame.time.wait(ST2)
        if xy[1]<self.xy[1]:
                self.xy[1]-=self.V
                pygame.time.wait(ST2)
        posi=posi.move(self.xy)
        scr.blit(self.image,posi)
    def Create(self):
        if self.re==0:
                self.xy[0]=random.randint(0,1000)
                self.xy[1]=random.randint(0,500)
                self.re+=1
        
        


#////////////////////sprite//////////////////////////////#

all_sprites = pygame.sprite.Group()
player=Player()
enemy=EmeCar()
all_sprites.add(player,enemy)
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
    enemy.Create()
    enemy.update()
        

