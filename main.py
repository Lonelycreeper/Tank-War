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
x=0
y=0
clock = pygame.time.Clock()
pygame.display.flip()
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
        x=0
         y=0
        posi=self.rect
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
                x = 1

                if x == 1:
                    if y == 0:
                            xy[0] -= V
                            self.image =py.image.load("./img/Tank-l.png").convert()
                            self.image = pygame.transform.scale(self.image, size2)
                            pygame.time.wait(ST)

                        
                        
        if keys[pygame.K_RIGHT]:
                x = 1
                
                

                if x== 1:
                    if y == 0:
                            xy[0] += V
                            self.image = py.image.load(
                                "./img/Tank-r.png").convert()

                            self.image = pygame.transform.scale(self.image, size2)
                            pygame.time.wait(ST)            
                
        if keys[pygame.K_UP]:
                y = 1
                
                

                if y == 1:
                    if x ==0:
                        xy[1] -= V
                        self.image = py.image.load("./img/Tank.png").convert()
                        self.image = pygame.transform.scale(self.image, size)
                        pygame.time.wait(ST)

        if keys[pygame.K_DOWN]:
                y = 1    
                if y == 1:
                    if x == 0:
                        xy[1] += V
                        self.image = py.image.load("./img/Tank-d.png").convert()
                        self.image = pygame.transform.scale(self.image, size)
                        pygame.time.wait(ST)

        posi=posi.move(xy)
        scr.blit(self.image,posi)
        pygame.display.flip()
=======
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
                
>>>>>>> 68b35db02a2a8c01bdd7ec0d8640e07d169abe3b

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
        

