from pygame import*
init()

W = 800
H = 500
back = (190, 220, 210)

window = display.set_mode((W, H))#Створення вікна
display.set_caption("Balls")
display.set_icon(image.load('tenis_ball.png'))
window.fill(back)

class Gamespite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.size_x = size_x
        self.size_y = size_y
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Racket(Gamespite):
    def update_left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < H-self.size_y:
            self.rect.y += self.speed

        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < H-self.size_x:
            self.rect.x += self.speed

    def update_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < H-self.size_y:
            self.rect.y += self.speed
        
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < H-self.size_x:
            self.rect.x += self.speed



class Ball(Gamespite):
    pass

racket_l = Racket('racket.png', 50, 180, 50, 140, 5)
racket_r = Racket('racket.png', 700, 180, 50, 140, 5)

game = True
finish = False
while game:
    time.delay(5)
    window.fill(back)
    racket_l.reset()
    racket_l.update_left()
    racket_r.reset()
    racket_r.update_right()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    









































































