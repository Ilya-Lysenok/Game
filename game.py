# Подключить нужные модули
from random import randint 
from pygame import *
init() 

# Глобальные переменные (настройки)
win_width = 1280 
win_height = 720

# класс-родитель для других спрайтов
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
background = transform.scale(image.load("images/bgr.png"), (win_width, win_height))

# во время игры пишем надписи размера 40
font2 = font.Font(None, 40)
font1 = font.Font(None, 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))

items = sprite.Group()
#Персонажи игры:
level=['                           ',
'                               d   ',
'   t      l                       ',
'                r         o    l ',
'r-------/         / ------------ ',
'                                 ',
'                                 ',
'           l                      ',
'    r          o   c   o       l  ',
'      /----------------------/      ',
'                                     ',
'                                     ', 
'    r    l                  r     l  ',
'                                   ',
'r    s         r   k  c          l ',
'---------------------------------  ',
]
platforms = []
stairs=[]
coins=[]
monsters=[]
blocks_r=[]
blocks_l=[]
manas = sprite.Group() # группа що клонує атакуючі шари


k_door = False # чи підібрано ключ для дверей

o_chest = False # чи відкрита скриня

c_count = 0 # лічильник монет
x=0
y=0

for r in level:
        for c in r:
            if c == 'r':
                n = GameSprite('nothing.png',x, y, 40, 80 ,0)
                blocks_r.append(n)
                items.add(n)
            if c == 'l':
                n = GameSprite('nothing.png',x, y, 40, 80 ,0)
                blocks_l.append(n)
                items.add(n)
            if c == '-':
                platform = GameSprite('platform.png',x, y, 40, 40 ,0)
                platforms.append(platform)
                items.add(platform)
            if c=='c':
                monster = Enemy('monster_crow.png', x, y,40,40, 2,'left')
                monsters.append(monster)
                items.add(monster)
