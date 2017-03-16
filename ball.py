#coding=utf-8   
#pygame draw

import pygame
import math
import sys
import time
from pygame.locals import *
from sys import exit
from random import *


__version__ = '1.3'
__author__ = {'name' : 'strayboy',
              'mail' : '67718273@qq.com',
              'blog' : 'http://blog.sina.com.cn/u/1959550131',
              'version' : __version__}


#pygame 
pygame.init()
pygame.display.set_caption('Ball Game')

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500
SPEED = 1
VOLUME = 5
SCREEN_DEFAULT_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT + 20)
SCREEN_DEFAULT_COLOR = (255, 255 ,255)
READY = 0

screen = pygame.display.set_mode(SCREEN_DEFAULT_SIZE, 0, 32)
screen.fill(SCREEN_DEFAULT_COLOR)


#单摆运行位置计算
radius = 20 #半径
l = 200# 单摆摆动半径
T = 2 * math.pi * math.sqrt(l / 10) # 单摆运动周期
jiange = T / 100 # 时间间隔
W = 2 * math.pi / T # 角速率
count = 0 #计数器
angle = math.pi / 6; # 起始下落角度

SPEED = 0.1
#循环：
while 1:
    for event in pygame.event.get():
        if event.type ==  QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                SPEED += 0.01
            elif event.key == K_DOWN:
                SPEED -= 0.01
                if SPEED ==0:
                   SPEED=0.001

    
    if (jiange * count >= T) :
	count = 0;

    screen.fill(SCREEN_DEFAULT_COLOR)

    #计算第一个球的位置
    x0 = 300
    y0 = 100
    #pygame.draw.circle(screen, (255,165,0), (x0,y0), radius)
    
    #print(balls)
    if ((jiange * count >= 0 and jiange * count <= T / 4) or jiange * count >= T * 3 / 4 and jiange * count <= T) :
        circlex = -(l * math.sin(angle) * math.cos(W * jiange * count));
        circley =  math.sqrt(l * l - circlex * circlex);

        pygame.draw.line(screen, (165,42,42),(x0, y0), (int(x0+circlex),int(y0+circley)))    
        pygame.draw.circle(screen, (255,165,0), (int(x0+circlex),int(y0+circley)), radius)
    else:
        pygame.draw.line(screen, (165,42,42),(x0, y0), (x0,y0+l))
        pygame.draw.circle(screen, (255,165,0), (x0,y0+l), radius)
          
    #计算第二个球的位置
    x1 = x0+2*radius
    y1 = y0
    #pygame.draw.circle(screen, (255,165,0), (x1,y1), radius)
    pygame.draw.line(screen, (165,42,42),(x1, y1), (x1,y1+l))
    pygame.draw.circle(screen, (255,165,0), (x1,y1+l), radius)
     
    #计算第三个球的位置
    x2= x1+2*radius
    y2=y1
    #pygame.draw.circle(screen, (255,165,0), (x2,y2), radius)

    if ((jiange * count > T / 4) and jiange * count < T * 3 / 4 ) :
        circlex = -(l * math.sin(angle) * math.cos(W * jiange * count));
        circley =  math.sqrt(l * l - circlex * circlex);
        pygame.draw.line(screen, (165,42,42),(x2, y2), (int(x2+circlex),int(y2+circley))) 
        pygame.draw.circle(screen, (255,165,0), (int(x2+circlex),int(y2+circley)), radius)
    else:
        pygame.draw.line(screen, (165,42,42),(x2, y2), (x2,y2+l))  
        pygame.draw.circle(screen, (255,165,0), (x2,y2+l), radius)

    count=count+1

    #刷新
    pygame.display.update()
    #sys.exit()
    #break
    #raw_input()
    time.sleep(SPEED)
