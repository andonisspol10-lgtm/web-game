import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
clock=pygame.time.Clock()
player=pygame.Rect(100,400,50,50)
runing=True
while runing:
    screen.fill('blue')
    pygame.draw.rect(screen,'red',player)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()