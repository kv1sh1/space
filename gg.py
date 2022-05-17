from pygame import*
class gameobject(sprite.Sprite):
    def __init__(self,imag,x,y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(imag),(100,100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
window = display.set_mode((500,500))
game = True
class player(gameobject):
    def control(self):
        butn = key.get_pressed()
        if butn[K_RIGHT] or butn[K_d] and self.rect.x < 400:
            self.rect.x+=5
        if butn[K_LEFT] or butn[K_a] and self.rect.x > 0:
            self.rect.x-=5
background = transform.scale(image.load('space.jpeg'), (500,500))
ship = player('ship.png', 200 , 350)
clock = time.Clock()
from random import*
class enemy(gameobject):
    def fly(self):
        self.draw()
        self.rect.y +=3
        if self.rect.y > 500:
            self.rect.y = -100
            self.rect.x = randint(0,400)
class bullet(gameobject):
    def fly(self):
        self.draw()
        self.rect.y -= 6
bullet1 = bullet('bullet.png', -100,-100)
enemy1 =  [
    enemy('vrag.png',0,0),
    enemy('vrag.png',0,0)
]
font.init()
writer = font.Font(None,50)
score = 0
hp = 100
finish = False
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
        if i.type == KEYDOWN:
            if i.key == K_SPACE:
                bullet1.rect.x= ship.rect.x
                bullet1.rect.y = ship.rect.y
    window.blit(background,(0,0))
    bullet1.fly()
    ship.draw()
    ship.control()
    hpText = writer.render(str(hp), True,(100,100,0))
    for i in enemy1:
        i.fly()
        if sprite.collide_rect(i,bullet1):
            i.rect.x = randint(0,400)
            i.rect.y = -100
            bullet1.rect.y = -100
        if sprite.collide_rect(i,ship):
            i.rect.x = randint(0,400)
            i.rect.y = -100
            hp -= 10
            if hp < 1:
                hp =1
                game=False
                finish = True
    window.blit(hpText,(410,10))
    display.update()
    clock.tick(60)
    
