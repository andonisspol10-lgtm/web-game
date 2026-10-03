import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))

player1img=pygame.image.load('untiteld4.png')
player1img=pygame.transform.scale(player1img,(60,85))
player1imgleft=pygame.transform.flip(player1img,True,False)

player2img=pygame.image.load('Untitled5.png')
player2img=pygame.transform.scale(player2img,(60,85))
player2imgleft=pygame.transform.flip(player2img,True,False)

clock=pygame.time.Clock()

player1=pygame.Rect(30,30,60,85)
player2=pygame.Rect(700,30,60,85)

runing=True

flag1=True
flag2=True

floor=pygame.Rect(0,590,800,10)
platforms=['platform1','platform2']
platform1=pygame.Rect(100,450,200,10)
platform2=pygame.Rect(400,400,200,10)

wall1=pygame.Rect(0,0,5,600)
wall2=pygame.Rect(795,0,5,600)

player1_vl_x=0
player1_vl_y=0
player2_vl_x=0
player2_vl_y=0
grounded1=False
grounded2=False 

def world(player_vl_x,player_vl_y,grounded,platforms,wall1,wall2,floor,player,player_num):



    if player.colliderect(floor):
            player.bottom=floor.top
            player_vl_y=0
            grounded=True
    for x in range(len(platforms)):
        if player.colliderect(eval(platforms[x])):
            if player_vl_y>0:
                player.bottom=eval(platforms[x]).top
                player_vl_y=0
                grounded=True
            elif player_vl_y<0:
                player.top=eval(platforms[x]).bottom
                player_vl_y=0
                grounded=True
    
        
    if player.colliderect(wall1):
        player.x=wall1.x+wall1.width
        player_vl_x=0

    if player.colliderect(wall2):
        player.x=wall2.x-player.width
        player_vl_x=0

    if player_num==1:
        if player.colliderect(player2):
            if player_vl_x>0:
                player.right=player2.left
                player_vl_x=0
            elif player_vl_x<0:
                player.left=player2.right
                player_vl_x=0
    elif player_num==2:
        if player.colliderect(player1):
            if player_vl_x>0:
                player.right=player1.left
                player_vl_x=0
            elif player_vl_x<0:
                player.left=player1.right
                player_vl_x=0

    return player_vl_x,player_vl_y,grounded

def player_movement(player_vl_x,player_vl_y,grounded,key,flag,floor,platform1,platform2,player,player_num):
    print(player)
    if player_num==1:    
        if key[pygame.K_d] and player_vl_x<5:
            player_vl_x+=1
            flag=True
        elif key[pygame.K_a] and player_vl_x>-5:
            player_vl_x-=1
            flag=False

        if key[pygame.K_SPACE] :
        
            if player.bottom==floor.top and grounded:
                player_vl_y=-20
            
            if player.bottom==platform1.top and grounded:
                player_vl_y=-20
            
            if player.bottom==platform2.top and grounded:
                player_vl_y=-20

    elif player_num==2:        
        if key[pygame.K_RIGHT] and player_vl_x<5:
            player_vl_x+=1
            flag=True
        elif key[pygame.K_LEFT] and player_vl_x>-5:
            player_vl_x-=1
            flag=False

        if key[pygame.K_UP] :
        
                if player.bottom==floor.top and grounded:
                    player_vl_y=-20
                
                if player.bottom==platform1.top and grounded:
                    player_vl_y=-20
                
                if player.bottom==platform2.top and grounded:
                    player_vl_y=-20

    if player_vl_y<5:
            player_vl_y+=1
        
    if player_vl_x>0:
            player_vl_x-=0.5

    elif player_vl_x<0:
            player_vl_x+=0.5
        
    

    return player_vl_x,player_vl_y,grounded,flag

    

while runing:
    key=pygame.key.get_pressed()

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            runing=False
    grounded1=False
    grounded2=False

    player1.y+=player1_vl_y
    player1.x+=player1_vl_x
    player2.y+=player2_vl_y
    player2.x+=player2_vl_x

    player1_vl_x,player1_vl_y,grounded1=world(player1_vl_x,player1_vl_y,grounded1,platforms,wall1,wall2,floor,player1,1)
    player2_vl_x,player2_vl_y,grounded2=world(player2_vl_x,player2_vl_y,grounded2,platforms,wall1,wall2,floor,player2,2)
    player1_vl_x,player1_vl_y,grounded1,flag1=player_movement(player1_vl_x,player1_vl_y,grounded1,key,flag1,floor,platform1,platform2,player1,1)
    player2_vl_x,player2_vl_y,grounded2,flag2=player_movement(player2_vl_x,player2_vl_y,grounded2,key,flag2,floor,platform1,platform2,player2,2)

    screen.fill('purple')
    #pygame.draw.rect(screen,'gray',player1) # --hitbox--
    #pygame.draw.rect(screen,'gray',player2) # --hitbox--
    if flag1==True:
        screen.blit(player1img, (player1.x, player1.y))
    elif flag1==False:
        screen.blit(player1imgleft, (player1.x, player1.y))
    
    if flag2==True:
        screen.blit(player2img, (player2.x, player2.y))
    elif flag2==False:
        screen.blit(player2imgleft, (player2.x, player2.y))

    pygame.draw.rect(screen,'brown',floor)
    pygame.draw.rect(screen,'brown',platform1)
    pygame.draw.rect(screen,'brown',platform2)
    pygame.draw.rect(screen,'purple',wall2)
    pygame.draw.rect(screen,'purple',wall1)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()