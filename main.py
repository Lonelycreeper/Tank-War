import pygame
from enemy import EmeCar,EnBullet
from player import Player
from player import Bullet
import sys,os
import ctypes
import random

FPS = 290
py = pygame
clock = pygame.time.Clock()
py.init()
scr = py.display.set_mode((1550,850), pygame.NOFRAME)
py.display.set_caption("Tank War")

all_sprites = pygame.sprite.Group()
brick_sprites = pygame.sprite.Group()
boom = py.image.load("./img/boom.png").convert_alpha()
player = Player()
enemy = EmeCar()
bullet = Bullet()
enbullet = EnBullet()
brick_sprites.add(brick_sprites)
all_sprites.add(player, enemy)


class MapSprite(pygame.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./img/brick.png")
        self.rect = self.image.get_rect()


def map():
    brick_sprites = pygame.sprite.Group()
    brick_image_path = './img/brick.png"'
    brick_image = pygame.image.load(brick_image_path)
    brick_size = (32, 32)
    num_bricks = random.randint(10, 30)  # 随机生成 10-30 个障碍物
    placed_bricks = []  # 已经放置的障碍物坐标
    for i in range(num_bricks):
        while True:
            # 随机生成砖块的位置和朝向
            x = random.randint(0, 1550 - brick_size[0])
            y = random.randint(0, 850 - brick_size[1])
            toward = random.choice(['left', 'right', 'up', 'down'])
            rect = pygame.Rect(x, y, *brick_size)
            # 检查当前砖块是否重叠到已经放置的砖块上，如果是则重新生成位置和朝向
            overlap = False
            for placed_brick in placed_bricks:
                placed_rect = pygame.Rect(*placed_brick, *brick_size)
                if placed_rect.colliderect(rect):
                    overlap = True
                    break
            if not overlap:
                break
        # 记录已经放置的砖块坐标
        placed_bricks.append((x, y))
        # 创建砖块精灵并加入精灵组中
        brick_sprite = MapSprite()
        brick_sprite.rect.x = x
        brick_sprite.rect.y = y
        if toward == 'left':
            brick_sprite.image = pygame.transform.rotate(brick_sprite.image, 90)
        elif toward == 'right':
            brick_sprite.image = pygame.transform.rotate(brick_sprite.image, -90)
        elif toward == 'up':
            brick_sprite.image = pygame.transform.rotate(brick_sprite.image, 180)
        brick_sprites.add(brick_sprite)
    brick_sprites.draw(scr) # 绘制砖块精灵到屏幕上


def MainPlayer():
        player.update()
        bullet.update()
        scr.blit(player.image, player.posi)
        if bullet.move == 1:
            scr.blit(bullet.image, bullet.posi)
        else:
            scr.blit(bullet.image, player.posi)
        if enemy.xy[0]-40<=bullet.xy[0]<=enemy.xy[0]+40 and enemy.xy[1]-20<=bullet.xy[1]<=enemy.xy[1]+20 and bullet.move == 1:
            bullet.move = 0
            enemy.re = 0
        if bullet.xy[1]-20<=enbullet.xy[1]<bullet.xy[1]+20 and bullet.xy[0]-20<=enbullet.xy[0]<=bullet.xy[0]+20 and bullet.move == 1:
            scr.blit(boom, bullet.posi)
            bullet.move = 2
            enbullet.move = 2
            enemy.bmove = 2
        
def EnemyMove():
    enemy.Create()
    enemy.update()
    scr.blit(enemy.image, enemy.posi)
    enbullet.update()
    if enbullet.move==0:
        enbullet.image=pygame.transform.rotate(enbullet.image,enemy.angle)
        enbullet.toward=enemy.towards
        enbullet.move=enemy.bmove
        scr.blit(enbullet.image, enemy.posi)
    if enbullet.move==1:
        scr.blit(enbullet.image, enbullet.posi)
        enemy.bmove=0

def main():
    all_sprites.draw(scr)  # 将所有精灵绘制到屏幕上
    map()                   # 绘制障碍物
    MainPlayer()
    EnemyMove() 

run = True
scr.fill((255, 255, 255))
all_sprites.draw(scr)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    scr.fill((255, 255, 255))  # 清空屏幕
    all_sprites.draw(scr)     # 将所有精灵绘制到屏幕上
    map()                     # 绘制障碍物
    main()
    pygame.display.flip()     # 更新屏幕

    clock.tick(FPS)  # 控制帧率
