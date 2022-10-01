import pygame
from pygame import mixer
import random
import math
pygame.init()

screen=pygame.display.set_mode((1920,1080))

running=True
#game title and icon
title=pygame.display.set_caption("Nanovaders")
image=pygame.image.load('nanobot.png')
icon=pygame.display.set_icon(image)


    
    
#player
playerchar=pygame.image.load('nanobotchar.png')
playerX=800
playerY=750
playerXchange=0
playerYchange=0

#redbloodcell
rbcchar=pygame.image.load('rbc.png')
enemyX=random.randint(500,1000)
enemyY=0
enemyYchange=0

#redbloodcell2
rbcchar1=pygame.image.load('rbc.png')
enemyX1=random.randint(1000,1400)
enemyY1=-500
enemyYchange1=0

#redbloodcell3
rbcchar2=pygame.image.load('rbc.png')
enemyX2=random.randint(200,900)
enemyY2=-900
enemyYchange2=0

#redbloodcell4
rbcchar3=pygame.image.load('rbc.png')
enemyX3=random.randint(1000,1400)
enemyY3=-200
enemyYchange3=0

#capsule
capsule = pygame.image.load('capsule.png')
capsuleX = 0
capsuleY = 750
capsuleXchange = 0
capsuleYchange = 5
capsule_state = "ready"

#cancer
cancer=pygame.image.load('cank.png')
cancerX=500
cancerY=-600
cancerYchange=0 



def cancerchar(x,y):
    cancernew=pygame.transform.scale(cancer,(750,750))
    screen.blit(cancernew,(x,y))

def player(x,y):
    playernew=pygame.transform.scale(playerchar,(100,100))
    screen.blit(playernew,(x,y))
    
def rbc(x,y):
    rbcnew=pygame.transform.scale(rbcchar,(300,300))
    screen.blit(rbcnew,(x,y))

def rbc1(x,y):
    rbcnew1=pygame.transform.scale(rbcchar1,(300,300))
    screen.blit(rbcnew1,(x,y))

def rbc2(x,y):
    rbcnew2=pygame.transform.scale(rbcchar2,(300,300))
    screen.blit(rbcnew2,(x,y))
    
def rbc3(x,y):
    rbcnew3=pygame.transform.scale(rbcchar3,(300,300))
    screen.blit(rbcnew3,(x,y))
        
def fire_capsule(x, y):
    global capsule_state
    capsule_state = "fire"
    screen.blit(capsule, (x + 16, y + 10))
    


#game loop
while running:
    screen.fill((102,0,0))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                playerXchange=-3
            if event.key == pygame.K_RIGHT:
                playerXchange=3
            if event.key == pygame.K_UP:
                playerYchange=-3
            if event.key == pygame.K_DOWN:
                playerYchange=3
            if event.key == pygame.K_SPACE:
                if capsule_state is "ready":
                    capsuleY=playerY
                    capsuleX=playerX
                    fire_capsule(capsuleX, capsuleY)
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXchange=0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerYchange=0
        enemyYchange=2
        enemyYchange1=2
        enemyYchange2=2
        cancerYchange=0.5
        enemyYchange3=2
    #capsule movement
    if capsuleY <= 0:
        capsuleY = 480
        capsule_state = "ready"

    if capsule_state is "fire":
        fire_capsule(capsuleX, capsuleY)
        capsuleY -= capsuleYchange
        
    
    
    #enemymovement
    enemyY+=enemyYchange
    if enemyX<-200:
        enemyX=-200
    elif enemyX>1650:
        enemyX=1650 
    
    #enemymovement2
    enemyY1+=enemyYchange1
    if enemyX1<-200:
        enemyX1=-200
    elif enemyX1>1650:
        enemyX1=1650
        
    #enemymovement3
    enemyY2+=enemyYchange2
    if enemyX2<-200:
        enemyX2=-200
    elif enemyX2>1650:
        enemyX2=1650

    #enemymovement4
    enemyY3+=enemyYchange3
    if enemyX3<-200:
        enemyX3=-200
    elif enemyX3>1650:
        enemyX3=1650 
    
    
    #cancer movement
    cancerY+=cancerYchange
    if cancerY>= -300:
        cancerY= -300   
        
    #player movement
    playerX+=playerXchange
    playerY+=playerYchange
    if playerX<0:
        playerX=0
    elif playerY<0:
        playerY=0
    elif playerY>825:
        playerY=825
    elif playerX>1650:
        playerX=1650
    elif playerX==enemyX:
        playerX=enemyX-20
    elif playerY==enemyY:
        playerY=enemyY-20
    
    cancerchar(cancerX,cancerY)
    rbc1(enemyX1,enemyY1)
    rbc(enemyX,enemyY)
    rbc2(enemyX2,enemyY2)
    rbc3(enemyX3,enemyY3)
    player(playerX,playerY)
    pygame.display.update()
    