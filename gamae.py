import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
clock=pygame.time.Clock()
player1=pygame.Rect(30,30,50,75)
runing=True
floor=pygame.Rect(0,590,800,10)
platform1=pygame.Rect(100,500,200,10)
platform2=pygame.Rect(400,450,200,10)
wall1=pygame.Rect(0,0,5,600)
wall2=pygame.Rect(795,0,5,600)
player1_vl_x=0
player1_vl_y=0

while runing:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runing=False
    if player1_vl_y<5:
        player1_vl_y+=1 
    player1.y+=player1_vl_y
    key=pygame.key.get_pressed()

    if key[pygame.K_d]:
        player1.x+=1
    elif key[pygame.K_a]:
        player1.x-=1

    if player1.colliderect(floor):
        player1.y=floor.y-player1.height
        player1_vl_y=0
    
    if player1.colliderect(platform1):
        player1.y=platform1.y-player1.height
        player1_vl_y=0

    if player1.colliderect(platform2):
        player1.y=platform2.y-player1.height
        player1_vl_y=0

    if player1.colliderect(wall1):
        player1.x=wall1.x+wall1.width
        player1_vl_x=0

    if player1.colliderect(wall2):
        player1.x=wall2.x-player1.width
        player1_vl_x=0

    if key[pygame.K_SPACE]:
        player1_vl_y=-2

    screen.fill('purple')
    pygame.draw.rect(screen,'red',player1)
    pygame.draw.rect(screen,'brown',floor)
    pygame.draw.rect(screen,'brown',platform1)
    pygame.draw.rect(screen,'brown',platform2)
    pygame.draw.rect(screen,'purple',wall2)
    pygame.draw.rect(screen,'purple',wall1)
    pygame.display.flip()
    clock.tick(150)

pygame.quit()