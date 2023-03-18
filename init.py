import pygame
import sys
import time
py=pygame
py.init()
scr=py.display.set_mode((600,450),pygame.RESIZABLE)
py.display.set_caption("Fight War")
f=py.font.Font('C:/Windows/Fonts/simhei.ttf',50)
def outtext(d):
            tx=f.render(d,True,(255,255,255),(0,0,0))
            txR=tx.get_rect()
            txR.center=(325/2,200)
            scr.blit(tx,txR)
outtext("START")
