import pygame

pygame.init()
screen=pygame.display.set_mode((400,300))
pygame.draw.circle(window,(0,200,55),(300,200),3)
done=False

while not done:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            done=True
    pygame.draw.rect(screen,(0,125,255),pygame.Rect,(30,30,60,60))
    pygame.display.flip()

