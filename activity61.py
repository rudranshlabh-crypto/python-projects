import pygame
import random

pygame.init()
spritecolorchangeevent=pygame.USEREVENT+1
backgruondcolorchangeevent=pygame.USEREVENT+2
blue=pygame.Color("Blue")
lightblue=pygame.Color("Light blue")
darkblue=pygame.Color("Dark blue")

yellow=pygame.Color("Yellow")
magenta=pygame.Color("Magenta")
orange=pygame.Color("Orange")
white=pygame.Color("White")
class Sprite(pygame.sprite.Sprite):
    def __init__ (self,color,height,weight):
        super().__init__()
        self.image=pygame.Surface([weight,hieght])
        self.rect=self.image.rect()
        self.velocity=[random.choice(-1,1),random.choice(-1,1)]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundryhit=False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[1]=-self.velocity[1]
            boundryhit=True
        if boundryhit:
            pygame.event.post(pygame.event.Event(spritecolorchangeevent))
            pygame.event.post(pygame.event.Event(backgrondcolorchangeevent))
    def changecolor(self):
        self.image.fill(random.choice(blue,lightblue,darkblue))