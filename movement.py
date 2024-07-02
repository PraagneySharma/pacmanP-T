
from pygame import *

width,height=800,600
screen=display.set_mode((width,height))
RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)

def drawScene(player,picList):
    '''
    this function draws 1 of the 24 pictures from the 2D list
    '''
    screen.fill(BLACK)
    row=player[2]
    col=int(player[3])
    screen.blit(picList[row][col],(player[0],player[1]))
    display.flip()

def movePlayer(player):
    keys=key.get_pressed()
    if keys[K_RIGHT]:
        player[0]+=2
        player[2]=0#0 --> facing righ
    elif keys[K_LEFT]:
        player[0]-=2
        player[2]=3#3 --> facing left
    elif keys[K_DOWN]:
        player[1]+=2
        player[2]=1# 1-->facing down
    elif keys[K_UP]:
        player[1]-=2
        player[2]=2 #2--> facing up
    else:
        player[3]=0 #no animation (show frame 0)

    player[3]=player[3]+0.1
    if player[3]>=2:
        player[3]=0
    print(player[3])

def addPics(name,start,end):
    '''
    this function RETURNS a LIST of pictures (1-D list)
    '''
    mypics=[]
    for i in range(start,end+1):
        mypics.append(image.load(f"pacmanSprites/{name}{i:03}.png"))
    
    return mypics
    


#       X  Y   row col
pacman=[100,150,0 , 0]
      #0   1   2   3
     

pics=[]
pics.append(addPics("Pacman",5,6))#right facing pics
pics.append(addPics("Pacman",3,4))#down facing pics
pics.append(addPics("Pacman",1,2))#up facing pics
pics.append(addPics("Pacman",7,8))#left facing pics
running=True
myClock=time.Clock()

while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
            
    movePlayer(pacman)
    drawScene(pacman,pics)#pics is the 2D list with 24 pictures
    myClock.tick(60)
            
quit()
