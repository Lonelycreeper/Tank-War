from player import xy
import pygame
import random
ST=5
size=[40,55]
size2=[20,25]
xye=[0,0]
class EmeCar(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.xy=xye
                self.image=pygame.image.load("./img/tanke.png").convert_alpha()
                self.image=pygame.transform.scale(self.image,size)
                self.rect=self.image.get_rect()
                self.re=0
                self.V=1
                self.angle=0
                self.bmove=0
                self.towards=4
                self.posi=self.rect
        def update(self):#the main function of enemy
                posi=self.rect
                self.image=pygame.image.load("./img/tanke.png").convert_alpha()
                self.image=pygame.transform.scale(self.image,size)
                self.move=random.randint(1,200)
                if xy[0]<xye[0]:
                        xye[0]-=self.V
                        self.image=pygame.transform.rotate(self.image,90)
                        self.angle=90
                        self.towards=1
                if xy[0]>xye[0]:
                        xye[0]+=self.V
                        self.image=pygame.transform.rotate(self.image,-90)
                        self.angle=-90
                        self.towards=3
                if xy[1]>xye[1]:
                        xye[1]+=self.V
                        self.image=pygame.transform.rotate(self.image,180)
                        self.angle=180
                        self.towards=2
                if xy[1]<xye[1]:
                        xye[1]-=self.V
                        self.angle=0
                        self.towards=4
                if self.move<=100 and self.bmove==0:
                        self.bmove=1
                if self.bmove==2:
                        pygame.time.wait(ST)
                        self.bmove=0
                self.posi=posi.move(self.xy)
                
        def Create(self):
                if self.re==0:
                        xye[0]=random.randint(0,1550)
                        xye[1]=random.randint(0,850)
                        if xy[1]-100<=xye[1]<=xy[1]+100 and xy[0]-100<=xye[0]<=xy[0]+100:
                                self.re=0
                        self.re+=1
                
class EnBullet(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image=pygame.image.load("./img/bullete.png").convert_alpha()
                self.image=pygame.transform.scale(self.image,size)
                self.v=5
                self.rect=self.image.get_rect()
                self.posi=self.rect
                self.move=0
                self.toward=4
                self.angle=0
                self.xy=[0,0]
        def update(self):
                posi=self.rect
                if self.move==0:
                        self.image=pygame.image.load("./img/K.png").convert_alpha()
                        self.xy[0]=xye[0]
                        self.xy[1]=xye[1]
                else:
                        if self.move==1:
                                self.image=pygame.image.load("./img/bullete.png").convert_alpha()
                                self.image = pygame.transform.scale(self.image, size)
                                if self.toward==4:
                                        self.xy[1]-=self.v
                                if self.toward==2:
                                        self.xy[1]+=self.v
                                        self.image=pygame.transform.rotate(self.image,180)
                                if self.toward==3:
                                        self.xy[0]+=self.v
                                        self.image=pygame.transform.rotate(self.image,-90)
                                if self.toward==1:
                                        self.xy[0]-=self.v
                                        self.image=pygame.transform.rotate(self.image,90)
                                if self.xy[0]<0 or self.xy[0]>1550 or self.xy[1]>850 or self.xy[1] < 0:
                                        self.move=0
                        if self.move==2:
                                pygame.time.wait(ST)
                                self.move=0
                self.posi=posi.move(self.xy)
                