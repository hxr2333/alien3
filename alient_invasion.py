#-*-encoding:utf-8-*-
import pygame
from settings import Settings
from ship import Ship
#from alien import Alien
import game_function as gf
from pygame.sprite import Group
def run_game():
    #初始化pygame 设置和屏幕对象
    pygame.init()
    ai_setting = Settings()
    # screen = pygame.display.set_mode((1200,800))
    screen = pygame.display.set_mode(
        (ai_setting.screen_width,ai_setting.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")
   # aliens = Alien(ai_setting, screen)
    ship = Ship(ai_setting, screen)

    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_setting, screen, ship, aliens)
    #bg_color = (230,230,230)
    #开始游戏主循环
    while True:
        gf.check_events(ai_setting, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(ai_setting,screen, ship, aliens, bullets)
        gf.update_aliens(ai_setting, aliens)
        gf.update_screen(ai_setting, screen, ship, aliens, bullets)
run_game()