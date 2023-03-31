from player import xy
import pygame
import random
ST2=0
size=[40,55]
class EmeCar(pygame.sprite.Sprite):
    def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.xy=[0,0]
                self.image=pygame.image.load("./img/tanke.png").convert_alpha()
                self.image=pygame.transform.scale(self.image,size)
                self.rect=self.image.get_rect()
                self.re=0
                self.V=1
                self.posi=self.rect
    def update(self):#the main function of enemy
        posi=self.rect
        self.image=pygame.image.load("./img/tanke.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,size)
        self.move=random.randint(1,2)
        if xy[0]<self.xy[0]:
                self.xy[0]-=self.V
                self.image=pygame.transform.rotate(self.image,90)
                pygame.time.wait(ST2)
        if xy[0]>self.xy[0]:
                self.xy[0]+=self.V
                self.image=pygame.transform.rotate(self.image,-90)
                pygame.time.wait(ST2)
        if xy[1]>self.xy[1]:
                self.xy[1]+=self.V
                self.image=pygame.transform.rotate(self.image,180)
                pygame.time.wait(ST2)
        if xy[1]<self.xy[1]:
                self.xy[1]-=self.V
                pygame.time.wait(ST2)
        self.posi=posi.move(self.xy)
    def Create(self):
        if self.re==0:
                self.xy[0]=random.randint(0,1550)
                self.xy[1]=random.randint(0,850)
                if xy[1]-100<=self.xy[1]<=xy[1]+100 and xy[0]-100<=self.xy[0]<=xy[0]+100:
                        self.re=0
                self.re+=1