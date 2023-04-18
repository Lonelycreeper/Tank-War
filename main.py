import pygame
from enemy import EmeCar, EnBullet
from player import Player, Bullet
from map import map,drawMap
import sys
import os
import ctypes
from pygame.locals import *
import random

FPS = 290
py = pygame
clock = pygame.time.Clock()
py.init()
black=(000,000,000)
score=0
life=3
strlif=str(life)
strsc=str(score)
myfont=pygame.font.Font(None,60)
overtext=myfont.render("Game Over",True,black)
scr = py.display.set_mode((1550, 850), pygame.NOFRAME)
py.display.set_caption("Tank War")
all_sprites = pygame.sprite.Group()
brick_sprites = pygame.sprite.Group()
boom = py.image.load("./img/boom.png").convert_alpha()
player = Player()
enemy = EmeCar()
bullet = Bullet()
enbullet = EnBullet()
all_sprites.add(player, enemy)


class MapSprite(pygame.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./img/brick.png")
        self.rect = self.image.get_rect()
    
def MainPlayer():
        player.update()
        bullet.update()
        scr.blit(player.image, player.posi)
        if bullet.move == 1:
            scr.blit(bullet.image, bullet.posi)
        else:
            scr.blit(bullet.image, player.posi)
        if enemy.xy[0] - 40 <= bullet.xy[0] <= enemy.xy[0] + 40 and enemy.xy[1] - 20 <= bullet.xy[1] <= enemy.xy[1] + 20 and bullet.move == 1:
            bullet.move = 0
            enemy.re = 0
            global score,strsc
            score+=1
            strsc=str(score)
        if bullet.xy[1]-20<=enbullet.xy[1]<bullet.xy[1]+20 and bullet.xy[0]-20<=enbullet.xy[0]<=bullet.xy[0]+20 and bullet.move == 1:
            scr.blit(boom, bullet.posi)
            bullet.move = 2
            enbullet.move = 2
            enemy.bmove = 2

def EnemyMove():
    enemy.Create()
    if enemy.re==1:
        enemy.update()
    scr.blit(enemy.image,enemy.posi)
    enbullet.update()
    if enbullet.move==0:
        enbullet.image=pygame.transform.rotate(enbullet.image,enemy.angle)
        enbullet.toward=enemy.towards
        enbullet.move=enemy.bmove
        scr.blit(enbullet.image, enemy.posi)
    if enbullet.move==1:
        scr.blit(enbullet.image, enbullet.posi)
        enemy.bmove=0
    if player.xy[0]-40<=enbullet.xy[0]<=player.xy[0]+40 and player.xy[1]-20<=enbullet.xy[1]<=player.xy[1]+20 and enbullet.move == 1:
        player.life-=1
        enbullet.move = 2
        enemy.bmove = 2
        global life,strlif
        life=player.life
        strlif=str(life)
    if player.life<=0:
        global overtext
        scr.blit(overtext,(600,400))
        enemy.re=3


def main():
    MainPlayer()
    EnemyMove()

run = True

scr.fill((255, 255, 255))
while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_0:
                pygame.quit()
                sys.exit()
    main()
    pygame.display.update()
    scr.fill((255, 255, 255))# 更新屏幕
    sctext=myfont.render("Score:"+strsc,True,black)
    liftext=myfont.render("Life:"+strlif,True,black)
    scr.blit(sctext,(3,0))
    scr.blit(liftext,(1380,0))
    clock.tick(FPS)  # 控制帧率
