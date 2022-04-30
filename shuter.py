#Создай собственный Шутер!
from pygame import *
from random import randint,random

col_e = 5
e_speed = 2

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,player_w,player_h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_w, player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.d = 1
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire (self):
        shot.play()
        bullet = Bullet('bullet.png',self.rect.x-5,self.rect.y+70,5,20,30)
        bullets.add(bullet)
        bullet = Bullet('bullet.png',self.rect.x+55,self.rect.y+70,5,20,30)
        bullets.add(bullet)
    def fires (self):
        bullet = Bullet('asteroid.png',-100,600,5,1000,1000)
        bullets.add(bullet)
class Enemy(GameSprite):
    def update(self):
        global mis_ships
        self.rect.y += self.speed
        if self.rect.x < 600 and self.d:
            self.rect.x += randint(1,e_speed)
        else:
            self.rect.x -= randint(1,e_speed)
            self.d = 0
            if self.rect.x < 0:
                self.d = 1
        if self.rect.y >= win_height+5 and s:
            self.rect.x = randint(0,win_width-70)
            self.speed = randint(1,e_speed)
            self.rect.y = -100
            mis_ships += 1
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= -95:
            self.kill()


win_width,win_height = 700, 500
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
shot = mixer.Sound('fire.ogg')

mis_ships = 0
font.init()
font = font.Font(None,36)
text_mis = font.render(str(mis_ships),1,(255,0,0))
killed = 0


enemies = sprite.Group()
bullets = sprite.Group()
for i in range(col_e):
    e = Enemy("ufo.png", randint(0,win_width-70),0,e_speed,70,40)
    enemies.add(e)
player = Player("rocket.png",win_width/2.2,win_height-100,5,70,100)

final = False
run = True
clock = time.Clock()
FPS = 60
s_c = 50
s = True
while run:
    window.blit(background,(0, 0))
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN and s and e.key != K_LEFT and e.key != K_RIGHT and e.key != K_r:
            player.fire()
            if s_c > 2:
                s_c -= 2
            else:
                s = False
                s_c = 'пули закончились'
        '''if e.type == KEYDOWN and e.key == K_r:
            player.fires()
            s = False'''
    sprite_list = sprite.groupcollide(enemies,bullets,True,True)
    sprite_list1 = sprite.spritecollide(player,enemies,False)
    for dead in sprite_list:
        killed += 1
        e = Enemy("ufo.png", randint(0,win_width-70),0,e_speed,70,40)
        enemies.add(e)
    if mis_ships >= 3 or len(sprite_list1) >= 1:
        final = True
        text_lost = font.render('you lost',1,(255,0,0))
        window.blit(text_lost,(win_width/2-50,win_height/2))
    if killed >= 25:
        final = True
        text_win = font.render('win',1,(0,255,0))
        window.blit(text_win,(win_width/2-50,win_height/2))
    window.blit(text_mis, (20,20))
    text_mis = font.render(str(mis_ships),1,(255,0,0))
    text_s = font.render(str(s_c),1,(255,0,0))
    window.blit(text_s, (20,50))
    if final != True:
        enemies.update()   
        player.update()
        bullets.update()
    enemies.draw(window)
    bullets.draw(window)
    player.reset()
    display.update()
    clock.tick(FPS)
