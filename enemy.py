from player import xy
import pygame
import random
ST2=1
class EmeCar(pygame.sprite.Sprite):
    def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.xy=[0,0]
                self.image=pygame.image.load("./img/hehe.png").convert_alpha()
                self.rect=self.image.get_rect()
                self.re=0
                self.V=3
                self.posi=self.rect
    def update(self):
        posi=self.rect
        self.image=pygame.image.load("./img/hehe.png").convert_alpha()
        self.move=random.randint(1,2)
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
        if xy[0]+10 ==self.xy[0]:
                if self.move==1:
                    for x in range(200):
                        self.xy[1]+=1
                else:
                    for x in range(200):
                        self.xy[1]-=1
        if xy[1]+10==self.xy[1]:
                if self.move==1:
                    for x in range(200):
                        self.xy[0]-=1
                else:
                    for x in range(200):
                        self.xy[0]+=1    
        self.posi=posi.move(self.xy)
    def Create(self):
        if self.re==0:
                self.xy[0]=random.randint(0,1000)
                self.xy[1]=random.randint(0,500)
                self.re+=1