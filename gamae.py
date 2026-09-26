import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
player1img=pygame.image.load('untiteld4.png')
player1img=pygame.transform.scale(player1img,(60,85))
player1imgleft=pygame.transform.flip(player1img,True,False)
clock=pygame.time.Clock()
player1=pygame.Rect(30,30,60,85)
runing=True
flag=True
floor=pygame.Rect(0,590,800,10)
platform1=pygame.Rect(100,450,200,10)
platform2=pygame.Rect(400,400,200,10)
wall1=pygame.Rect(0,0,5,600)
wall2=pygame.Rect(795,0,5,600)
player1_vl_x=0
player1_vl_y=0
grounded=False

while runing:
    key=pygame.key.get_pressed()

    if key[pygame.K_SPACE] :
                if player1.bottom==floor.top and grounded:
                    player1_vl_y=-20
    
                if player1.bottom==platform1.top and grounded:
                    player1_vl_y=-20
    
                if player1.bottom==platform2.top and grounded:
                    player1_vl_y=-20
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            runing=False
    
    if player1_vl_y<5:
        player1_vl_y+=1

    if player1_vl_x>0:
        player1_vl_x-=0.5
    elif player1_vl_x<0:
        player1_vl_x+=0.5
    player1.y+=player1_vl_y
    player1.x+=player1_vl_x

    if key[pygame.K_d] and player1_vl_x<5:
        player1_vl_x+=1
        flag=True
    elif key[pygame.K_a] and player1_vl_x>-5:
        player1_vl_x-=1
        flag=False
    grounded=False  
    if player1.colliderect(floor):
        player1.bottom=floor.top
        player1_vl_y=0
        grounded=True
    
    if player1.colliderect(platform1):

        if player1_vl_y>0:
            player1.bottom=platform1.top
            player1_vl_y=0
            grounded=True
        elif player1_vl_y<0:
            player1.top=platform1.bottom
            player1_vl_y=0
            grounded=True
        
    if player1.colliderect(platform2):
        if player1_vl_y>0:
            player1.bottom=platform2.top
            player1_vl_y=0
            grounded=True
        elif player1_vl_y<0:
            player1.top=platform2.bottom
            player1_vl_y=0
            grounded=True

    if player1.colliderect(wall1):
        player1.x=wall1.x+wall1.width
        player1_vl_x=0

    if player1.colliderect(wall2):
        player1.x=wall2.x-player1.width
        player1_vl_x=0

    screen.fill('purple')
    #pygame.draw.rect(screen,'gray',player1) # --hitbox--
    if flag:
        screen.blit(player1img, (player1.x, player1.y))
    else:
        screen.blit(player1imgleft, (player1.x, player1.y))
    
    pygame.draw.rect(screen,'brown',floor)
    pygame.draw.rect(screen,'brown',platform1)
    pygame.draw.rect(screen,'brown',platform2)
    pygame.draw.rect(screen,'purple',wall2)
    pygame.draw.rect(screen,'purple',wall1)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()