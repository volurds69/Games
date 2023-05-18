import pygame
import os
pygame.init()
largura,altura = 800,680
screen = pygame.display.set_mode((largura,altura))
espaco_img = pygame.image.load(os.path.join("assets","img","espaco.png")).convert_alpha()
pygame.display.set_caption("Space Kombat")
nave_img = pygame.image.load(os.path.join("assets","img","ship.png")).convert_alpha()
nave_img = pygame.transform.scale(nave_img,(25,25))

loop=True

speed=600

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop=False
    screen.fill((0,0,0))
    screen.blit(espaco_img,(0,0))
    screen.blit(nave_img,(350,speed))
    speed-=1
    if speed <=0:
        speed = 720
   
    pygame.display.update()


pygame.quit()