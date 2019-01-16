#-*-encoding:utf-8-*-
import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.ai_settings = ai_settings
        #初始化飞船并设置其初始位置
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    #根据移动标志调整飞船位置
    def update(self):
        # if self.moving_right:
        #     #self.rect.centerx += 1
        #     self.center += self.ai_settings.ship_speed_factor
        # if self.moving_left:
        #     #self.rect.centerx -= 1
        #     self.center -= self.ai_settings.ship_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx