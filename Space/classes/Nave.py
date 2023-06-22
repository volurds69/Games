from typing import Any
import pygame,os,sys


class Nave(pygame.sprite.Sprite):
    def __init__(self,groups) -> None:
        super().__init__(groups)
        self.__image = pygame.image.load(os.path.join("assets","img","nave2.png")).convert_alpha
        self.__image = pygame.transform.scale(self.__image,(45,40))
        self.image = self.__image
        self.__rect = self.image.get_rect(center=(1200/2, 650/2))
        self.rect = self.__rect

        #Criando um timer para o disparo
        self.__pode_disparar = True
        self.__time_tiro = None

        #Implemento mascara
        self.mascara = pygame.mask.from_surface(self.image)

    def update(self):
        self.input_position()

    