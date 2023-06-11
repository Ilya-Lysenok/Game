from random import randint 
from pygame import *
init() 

# Глобальные переменные (настройки)
win_width = 1280 
win_height = 720

class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.width = size_x
        self.height = size_y

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
     
#класс-наследник для спрайта-игрока (управляется стрелками)
class Player(GameSprite):
    def update_l_r(self):
        global f
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
            f=1
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
            f=0
    def update_a_d(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
           
        #класс-наследник для спрайта-врага (перемещается сам)
class Enemy(GameSprite): 
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, side='left'):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y, player_speed)        
        self.side = side
    
    def update(self):
        global side
        if self.side == 'right':
            self.rect.x -= self.speed
        if self.side == 'left':
            self.rect.x += self.speed
f=1
class Mana(GameSprite): 
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, side='left'):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y, player_speed)        
        self.side = side
    def update(self):
        global side,f      
        if self.side == 'left':
            self.rect.x -= self.speed
        if self.side == 'right':
            self.rect.x += self.speed
window = display.set_mode((win_width, win_height))
display.set_caption("Arcada")
background = transform.scale(image.load("background.png"), (win_width, win_height))
