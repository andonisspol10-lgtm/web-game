from ast import Global
from pdb import run
from tkinter import ALL

import pygame
import asyncio
screen=pygame.display.set_mode((800,600))

player_goust_img=pygame.image.load('phatasma-Photoroom.png')
player_goust_img=pygame.transform.scale(player_goust_img,(85,60))

player_death_img=pygame.image.load('death.png')
player_death_img=pygame.transform.scale(player_death_img,(800,600))

player1img=pygame.image.load('untiteld4.png')
player1img=pygame.transform.scale(player1img,(60,85))
player1imgleft=pygame.transform.flip(player1img,True,False)

player1attack=pygame.image.load('untiteld4_attack.png')
player1attack=pygame.transform.scale(player1attack,(60,85))
player1attackleft=pygame.transform.flip(player1attack,True,False)

countdown=30

player2img=pygame.image.load('Untitled5.png')
player2img=pygame.transform.scale(player2img,(60,85))
player2imgleft=pygame.transform.flip(player2img,True,False)

player2attack=pygame.image.load('Untitled5_attack.png')
player2attack=pygame.transform.scale(player2attack,(60,85))
player2attackleft=pygame.transform.flip(player2attack,True,False)

clock=pygame.time.Clock()

player1=pygame.Rect(30,30,60,85)
player2=pygame.Rect(700,30,60,85)


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

player1_health=100
player2_health=100

runing=True

onetime1=True
onetime2=True

player1_death=True
player2_death=True

player1_cooldown=0
player2_cooldown=0
click1=True
click2=True

player1_health_bar_damege=pygame.Rect(10,10,200,20)
player2_health_bar_damege=pygame.Rect(590,10,200,20)

async def main():
    pygame.init()
    global runing, countdown, player1_cooldown, player2_cooldown
    global onetime1, onetime2, player1_death, player2_death
    global player1_health, player2_health
    global player1_vl_x, player1_vl_y, player2_vl_x, player2_vl_y
    global grounded1, grounded2, flag1, flag2, click1, click2


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



    def player_attack(player_health,player,flag,enemy,cooldown,click):
        if cooldown<=0 and click:
            if flag:
                attack_box=pygame.Rect(player.right,player.y,45,35)
            elif flag==False:
                attack_box=pygame.Rect(player.left-45,player.y,45,35)

            if attack_box.colliderect(enemy) and player_health>0:
                player_health-=5
                if player_health<0:
                    player_health=0
            #pygame.draw.rect(screen,'yellow',attack_box)
            cooldown=15
            click=False

        return player_health,cooldown,click





    while runing:
        if onetime1==False or onetime2==False:
            countdown-=1
        player1_cooldown-=1
        player2_cooldown-=1

        key=pygame.key.get_pressed()
        mouse=pygame.mouse.get_pressed()
        player1_health_bar=pygame.Rect(10,10,player1_health*2,20)
        player2_health_bar=pygame.Rect(590,10,player2_health*2,20)

        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                runing=False
        grounded1=False
        grounded2=False

        if player1_health<=0  and onetime1:
            player1_death=False
            onetime1=False

        if player2_health<=0 and onetime2:
            player2_death=False
            onetime2=False


        if player1_death:
            player1.y+=player1_vl_y
            player1.x+=player1_vl_x
        if player2_death:
            player2.y+=player2_vl_y
            player2.x+=player2_vl_x

        if not mouse[0] and not click1 and player1_death:
            click1=True
        if not mouse[2] and not click2:
            click2=True
        
        #region
        if player1_death:
            player1_vl_x,player1_vl_y,grounded1=world(player1_vl_x,player1_vl_y,grounded1,platforms,wall1,wall2,floor,player1,1)
            player1_vl_x,player1_vl_y,grounded1,flag1=player_movement(player1_vl_x,player1_vl_y,grounded1,key,flag1,floor,platform1,platform2,player1,1)
        if player2_death:
            player2_vl_x,player2_vl_y,grounded2=world(player2_vl_x,player2_vl_y,grounded2,platforms,wall1,wall2,floor,player2,2)

            player2_vl_x,player2_vl_y,grounded2,flag2=player_movement(player2_vl_x,player2_vl_y,grounded2,key,flag2,floor,platform1,platform2,player2,2)
        #endregion

        screen.fill('purple')
        
        pygame.draw.rect(screen,'red',player1_health_bar_damege)
        pygame.draw.rect(screen,'red',player2_health_bar_damege)

        pygame.draw.rect(screen,'green',player1_health_bar)
        pygame.draw.rect(screen,'green',player2_health_bar)

        
        #pygame.draw.rect(screen,'gray',player1) # --hitbox--
        #pygame.draw.rect(screen,'gray',player2) # --hitbox--

        if mouse[0] and click1 and player1_cooldown<=0 and player1_death:
            
            player2_health,player1_cooldown,click1=player_attack(player2_health,player1,flag1,player2,player1_cooldown,click1)

            if flag1==True:
                screen.blit(player1attack, (player1.x, player1.y))

            elif flag1==False:
                screen.blit(player1attackleft, (player1.x, player1.y))   

        elif flag1==True and player1_death:
            screen.blit(player1img, (player1.x, player1.y))

        elif flag1==False and player1_death:
            screen.blit(player1imgleft, (player1.x, player1.y))


        if mouse[2] and click2 and player2_cooldown<=0 and player2_death:
            player1_health,player2_cooldown,click2=player_attack(player1_health,player2,flag2,player1,player2_cooldown,click2)

            if flag2==True:
                screen.blit(player2attack, (player2.x, player2.y))

            elif flag2==False:
                screen.blit(player2attackleft, (player2.x, player2.y))

        elif flag2==True and player2_death:
            screen.blit(player2img, (player2.x, player2.y))

        elif flag2==False and player2_death:
            screen.blit(player2imgleft, (player2.x, player2.y))

        if onetime1==False:
            screen.blit(player_goust_img,(player1.x,player1.y))
        if onetime2==False:
            screen.blit(player_goust_img,(player2.x,player2.y))
        pygame.draw.rect(screen,'brown',floor)
        pygame.draw.rect(screen,'brown',platform1)
        pygame.draw.rect(screen,'brown',platform2)
        pygame.draw.rect(screen,'purple',wall2)
        pygame.draw.rect(screen,'purple',wall1)

        if countdown<1:
            screen.blit(player_death_img, (0,0))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
asyncio.run(main())