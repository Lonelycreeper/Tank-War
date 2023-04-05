import pygame
from enemy import EmeCar,EnBullet
from player import Player
from player import Bullet
import sys,os
import ctypes
py=pygame
clock = pygame.time.Clock()
clock.tick(60)
py.init
scr=py.display.set_mode((1550,850),pygame.NOFRAME)#init of screen
py.display.set_caption("Tank War")
all_sprites = pygame.sprite.Group()
boom=py.image.load("./img/boom.png").convert_alpha()
player=Player()
enemy=EmeCar()
bullet=Bullet()
enbullet=EnBullet()
all_sprites.add(player,enemy)
def MainPlayer():
        player.update()
        bullet.update()
        scr.blit(player.image,player.posi)
        if bullet.move==1:
            scr.blit(bullet.image,bullet.posi)
        else:
            scr.blit(bullet.image,player.posi)
        if enemy.xy[0]-40<=bullet.xy[0]<=enemy.xy[0]+40 and enemy.xy[1]-20<=bullet.xy[1]<=enemy.xy[1]+20 and bullet.move==1:
            bullet.move=0
            enemy.re=0
        if bullet.xy[1]-20<=enbullet.xy[1]<bullet.xy[1]+20 and bullet.xy[0]-20<=enbullet.xy[0]<=bullet.xy[0]+20 and bullet.move==1:
            scr.blit(boom,bullet.posi)
            bullet.move=2
            enbullet.move=2
            enemy.bmove=2
        
def EnemyMove():
    enemy.Create()
    enemy.update()
    scr.blit(enemy.image,enemy.posi)
    enbullet.update()
    if enbullet.move==0:
        enbullet.image=pygame.transform.rotate(enbullet.image,enemy.angle)
        enbullet.toward=enemy.towards
        enbullet.move=enemy.bmove
        scr.blit(enbullet.image,enemy.posi)
    if enbullet.move==1:
        scr.blit(enbullet.image,enbullet.posi)
        enemy.bmove=0
def main():
    scr.fill((255,255,255))
    MainPlayer()
    EnemyMove()
        
run = True
scr.fill((255,255,255))
all_sprites.draw(scr)
while run:#main function of this game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    main()
    pygame.display.update()

