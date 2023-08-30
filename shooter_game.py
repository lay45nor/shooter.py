#Создай собственный Шутер!

from pygame import *
from random import *
mixer.init()
font.init()

window_wight = 700
window_hight = 500
fps = 120
bg_name = "galaxy.jpg"
#mixer.music.load('space.ogg')
#mixer.music.play()
win = display.set_mode((window_wight, window_hight))


#задай фон сцены
bg = transform.scale(image.load(bg_name

    ), (window_wight, window_hight))

clock = time.Clock()
lost = 0
score = 0
class Gamesprit(sprite.Sprite):
    def __init__(self, filename, x, y, wight, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(filename), (wight, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        win.blit(self.image,(self.rect.x, self.rect.y))  

class Player(Gamesprit):

    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("bullet.png",self.rect.centerx -10, self.rect.top, 15 ,15, 10)
        bullets.add(bullet)

class Enemy(Gamesprit):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > window_hight:  
            self.rect.y = -100
            self.rect.x = randint(0, window_wight-100)
            lost +=1


class Bullet(Gamesprit):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

player = Player('rocket.png', 200, 400, 80, 80, 5)

monster = sprite.Group()
bullets = sprite.Group()



for i in range(5):
    enemy = Enemy("ufo.png",randint(0, window_wight-100), -100, 100, 70,randint(2,7))
    monster.add(enemy)









    






game = True
state = ''
finish = False
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

        if e.type == KEYDOWN:
            if e.key == K_z:
                
                player.fire()


    if finish !=True:
        win.blit(bg,(0,0))

        player.reset()  
        player.update()

        monster.draw(win)
        monster.update()

        bullets.draw(win)
        bullets.update()

        killed = sprite.groupcollide(monster, bullets, True, True)
        for i in killed:
            enemy = Enemy("ufo.png",randint(0, window_wight-100), -100, 100, 70,randint(2,7))
            monster.add(enemy)
            score +=1


        score_text = font.SysFont("Arial", 38).render('сбито' + str(score), True, (255,255,255))
        lost_text = font.SysFont("Arial", 38).render('пропущено' + str(lost), True, (255,255,255))
        win_text = font.SysFont("Arial", 98).render('ты победитель', True, (0,255,0))



        if score == 3:
            state = 'lose'
        if state == 'lose':
            win.blit(win_text, (50, 50))
            finish = True



        win.blit(score_text,(20,20))
        win.blit(lost_text,(20,70))


       
    display.update()
    clock.tick(fps)

        