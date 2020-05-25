import pygame
import random
import math
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invader")
playerImg=pygame.image.load('player.png')
playerX=370
playerY=480
playerx_change=0
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_ene=6
for i in range(num_of_ene):
    enemyX.append(random.randint(50,480))
    enemyY.append(random.randint(40,150))
    enemyX_change.append(4)
    enemyY_change.append(10)
    enemyImg.append(pygame.image.load('images.png'))
backgrounImg=pygame.image.load('background.png')
bulletX=0
bulletY=480
bulletY_change=10
bullet_state="ready"
bulletImg=pygame.image.load('weapons.png')
score=0
textX=10
textY=10
font=pygame.font.Font("freesansbold.ttf",32)
lev=1
def lvl():
    lv=font.render("Level :"+str(lev),True,(255,255,255))
    screen.blit(lv,(660,10))
def show_score(x,y):
    score_v=font.render("Score :"+str(score),True,(255,255,255))
    screen.blit(score_v,(x,y))
def player(x,y):
    screen.blit(playerImg,(x,y))
def enemy(x,y):
    screen.blit(enemyImg[i],(x,y))
def background(x,y):
    screen.blit(backgrounImg,(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))
def iscolision(x,y,z,a):
    distance=math.sqrt((math.pow(x-z,2))+(math.pow(y-a,2)))
    if distance<=27:
        return True
    else:
        return False
run=True
while(run):
    screen.fill((0,0,0))
    background(0,0)
    for i in pygame.event.get():
        if(i.type==pygame.QUIT):
            run=False
        if(i.type==pygame.KEYDOWN):
            if(i.key==pygame.K_LEFT):
                playerx_change=-4
            if(i.key==pygame.K_RIGHT):
                playerx_change=4
            if bullet_state is "ready":
                if i.key==pygame.K_SPACE:
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)
        if i.type==pygame.KEYUP:
            if i.key==pygame.K_LEFT or i.key==pygame.K_RIGHT:
                playerx_change=0
    playerX+=playerx_change
    if playerX<=0:
        playerX=0
    elif playerX>736:
        playerX=736
    for i in range(num_of_ene):
        enemyX[i]+=enemyX_change[i]
        if enemyX[i]<=0:
            enemyX_change[i]=4
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i]>=736:
            enemyX_change[i]=-4
            enemyY[i]+=enemyY_change[i]
    if bulletY<=0:
        bulletY=480
        bullet_state="ready"
    if bullet_state is "fire":
         fire_bullet(bulletX,bulletY)
         bulletY-=bulletY_change
    for i in range(num_of_ene):
        colision=iscolision(enemyX[i],enemyY[i],bulletX,bulletY)
        if colision:
            bulletY=480
            bullet_state="ready"
            enemyX[i]=random.randint(50,480)
            enemyY[i]=random.randint(40,150)
            score+=1
        enemy(enemyX[i],enemyY[i])
    if(score==10*lev):
        lev+=1
    lvl()
    show_score(textX,textY)
    player(playerX,playerY)
    pygame.display.update()
