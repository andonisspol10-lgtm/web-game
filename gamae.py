import pygame
import time
pygame.init()
screen=pygame.display.set_mode((800,600))
clock=pygame.time.Clock()
player1=pygame.Rect(0,0,50,50)
runing=True
floor=pygame.Rect(0,590,800,10)
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
        
    if key[pygame.K_SPACE]:
        player1_vl_y=-2

    screen.fill('purple')
    pygame.draw.rect(screen,'red',player1)
    pygame.draw.rect(screen,'brown',floor)
    pygame.display.flip()
    clock.tick(150)

pygame.quit()