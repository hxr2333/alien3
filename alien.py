#-*-encoding:utf-8-*-
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_setting, screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_setting = ai_setting

        self.image = pygame.image.load('image/alien.bmp')
        self.rect  = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.ai_settings.alien_speed_factor
        self.rect.x = self.x
    def blitme(self):
        self.screen.blit(self.image, self.rect)