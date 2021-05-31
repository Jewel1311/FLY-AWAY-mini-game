import pygame ,sys,random
from pygame.locals import *
from pygame import mixer

pygame.init()
width,height=440,600
black=(0,0,0)
red=(180,0,0)
purple=(128,0,128)
navyblue=(0,0,128)
FPS=60
image=pygame.image.load('images/forest.jpg')
image=pygame.transform.scale(image,(600,500))
image=pygame.transform.rotate(image,(90))
img=pygame.image.load('images/plane.png')
img=pygame.transform.scale(img,(100,80))
rect=img.get_rect()
rect.x=220
rect.y=400
obsplane=pygame.image.load('images/enemy.png')
obsplane=pygame.transform.scale(obsplane,(80,60))
obsplane=pygame.transform.rotate(obsplane,(180))
rect1=obsplane.get_rect()
rect2=obsplane.get_rect()
rect3=obsplane.get_rect()
rect4=obsplane.get_rect()
WIN=pygame.display.set_mode((width,height))
pygame.display.set_caption('FLY AWAY')
by=0
by2=-600
x=0
count=0
obx=100
obspos=0
points=0
vel=5
p=5
crash=False
flag=0
fp=True
cp=False


def start():
   global fp,cp
   fp=True
   cp=False
   mixer.music.load('fly sound/intro.mp3')
   mixer.music.play(-1)
   play=True
   while play:
    WIN.blit(image,(0,0))
    WIN.blit(img,(220,400))
    font=pygame.font.Font('freesansbold.ttf',30)
    start=font.render('Press space to start',True,black)
    WIN.blit(start,(70,280))
    for event in pygame.event.get():
     if event.type==pygame.QUIT:
         pygame.quit()
         sys.exit()
     if event.type==pygame.KEYDOWN:
        if event.key==K_SPACE:
            play=False
            main()
    pygame.display.update()



def show_points():
    font=pygame.font.Font('freesansbold.ttf',32)
    score=font.render('Points:'+str(points),True,navyblue)
    WIN.blit(score,(10,10))

def crashed():
     global crash,fp,cp
     crash=True
     fp=False
     cp=True
     sound()


def speed():
    global flag
    font=pygame.font.Font('freesansbold.ttf',50)
    speed=font.render('SPEEDING UP',True,red)
    WIN.blit(speed,(45,250))
    pygame.display.update()
    pygame.time.delay(1500)
    flag=1
    main()



def sound():
    global fp,cp
    if fp==True:
      mixer.music.load('fly sound/fly.mp3')
      mixer.music.play()
    if fp==False:
       mixer.music.stop()
    if cp==True:
       mixer.music.load('fly sound/crash.mp3')
       mixer.music.play()

class plane:


    def movement_left(self):
            if rect.x>40:
               rect.x-=100

    def movement_right(self):
            if rect.x<230:
               rect.x+=100

    def plane_display(self):
            WIN.blit(img,rect)


class obstacle:

    def __init__(self):
        rect1.y=-40
        rect2.y=-300
        rect3.y=-600
        rect4.y=-900
    def obstacle_display_one(self):
         global points,p,vel
         if rect1.y<600:
            rect1.y+=vel
         if rect1.y==520:
            points+=p
         if rect.colliderect(rect1):
             crashed()
         WIN.blit(obsplane,rect1)

    def obstacle_display_two(self):
         global points,p,vel
         if rect2.y<600:
            rect2.y+=vel
         if rect2.y==500:
              points+=p
         if rect.colliderect(rect2):
             crashed()
         WIN.blit(obsplane,rect2)

    def obstacle_display_three(self):
         global points,p,vel
         if rect3.y<600:
            rect3.y+=vel
         if rect3.y==520:
            points+=p
         if rect.colliderect(rect3):
              crashed()
         WIN.blit(obsplane,rect3)

    def obstacle_display_four(self):
         global points,p,vel
         if rect4.y<600:
            rect4.y+=vel
         if rect4.y==500:
            points+=p
         if rect4.y>=600:
            main()
         if rect.colliderect(rect4):
             crashed()
         WIN.blit(obsplane,rect4)


def background():
        global by,by2,x
        by+=2
        by2+=2
        if by==600:
           by=0
        if by2==0:
           by2=-600
        WIN.blit(image,(x,by))
        WIN.blit(image,(x,by2))


def main():
        global vel,p,points,crash,flag
        ob=obstacle()
        sound()
        rect1.x=random.randrange(30,180)
        rect2.x=random.randrange(180,300)
        rect3.x=random.randrange(30,180)
        rect4.x=random.randrange(180,300)
        clock=pygame.time.Clock()
        run=True
        while run:
            if points==80:
                p=10
                vel=8
                if flag==0:
                 speed()
            background()
            o.plane_display()
            ob.obstacle_display_one()
            ob.obstacle_display_two()
            ob.obstacle_display_three()
            ob.obstacle_display_four()
            show_points()
            for event in pygame.event.get():
                 if event.type==pygame.QUIT:
                     pygame.quit()
                     sys.exit()
                 if event.type==pygame.KEYDOWN:
                    if event.key==K_LEFT:
                      o.movement_left()
                    elif event.key==K_RIGHT:
                      o.movement_right()
            if crash==1:
                font=pygame.font.Font('freesansbold.ttf',70)
                crash=font.render('CRASHED',True,red)
                font=pygame.font.Font('freesansbold.ttf',50)
                score=font.render("POINTS:"+str(points),True,purple)
                WIN.blit(crash,(40,230))
                WIN.blit(score,(90,330))
                pygame.display.update()
                pygame.time.delay(2000)
                crash=False
                points=0
                vel=5
                p=5
                flag=0
                start()
            pygame.display.update()
            clock.tick(FPS)

o=plane()
start()
