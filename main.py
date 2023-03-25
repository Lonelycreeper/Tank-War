import pygame
from enemy import EmeCar
from player import Player
import sys
py=pygame
py.init
scr=py.display.set_mode((600,450),pygame.RESIZABLE)
py.display.set_caption("Tank War")
all_sprites = pygame.sprite.Group()
player=Player()
enemy=EmeCar()
all_sprites.add(player,enemy)
def MainPlayer():
        player.update()
        scr.blit(player.image,player.posi)
        pygame.display.flip()
def EnemyMove():
    enemy.Create()
    enemy.update()
    scr.blit(enemy.image,enemy.posi)
run = True
all_sprites.draw(scr)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    scr.fill((255,255,255))
    MainPlayer()
    EnemyMove()
