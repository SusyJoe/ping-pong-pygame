from pygame import *
from random import *

FPS = 50
WIDTH = 800
HEIGHT = 500
dx = 3
dy = 3
score_1 = 0
score_2 = 0 
screen = display.set_mode((WIDTH,HEIGHT))
display.set_caption("Pong Ping")
clock = time.Clock()
font.init()
style = font.Font(None, 50)

class Main(sprite.Sprite):
    def __init__(self, img, speed, x, y,w,h):
        super().__init__()
        self.image = transform.scale(image.load(img),(w,h))
        self.speed = 5
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def abracadabra(self):
        screen.blit(self.image, (self.rect.x , self.rect.y))
class Player(Main):
    def control_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    def control_2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
ball = Main("Ball.png", 3, WIDTH/2-25, HEIGHT/2-25, 50, 50)
p1 = Player("unnamed.png", 3, 70, HEIGHT/2-50, 20, 100)
p2 = Player("unnamed.png", 3, WIDTH-70, HEIGHT/2-50, 20, 100)

end = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if end != True:

        screen.fill((0,0,0))
        p1.abracadabra()
        p2.abracadabra()
        ball.abracadabra()
        p1.control_1()
        p2.control_2()

        word1 = style.render("P1 Score: " + str(score_1), True, (255,255,255))
        word2 = style.render("P2 Score: " + str(score_2), True, (255,255,255))
        screen.blit(word1, (50,50))
        screen.blit(word2, (550,50))
        
        ball.rect.x += dx
        ball.rect.y += dy

        if ball.rect.y > 450 or ball.rect.y < 0:
            dy *= -1
        if sprite.collide_rect(p1,ball) or sprite.collide_rect(p2,ball):
            dx *= -1

            
        if ball.rect.x <= 0:
            score_2 += 1
            ball = Main("Ball.png", 3, WIDTH/2-25, HEIGHT/2-25, 50, 50)
            time.delay(1000)
        if score_1 >= 10:
            end = True
            win = style.render("Player 2 Wins!",True,(250,250,250))
            screen.blit(win,(WIDTH//2-100,HEIGHT//2-50))

        if ball.rect.x >= 800:
            score_1 += 1
            ball = Main("Ball.png", 3, WIDTH/2-25, HEIGHT/2-25, 50, 50)
            time.delay(1000)

        if score_2 >= 10:
            end = True
            win = style.render("Player 1 Wins!",True,(250,250,250))
            screen.blit(win,(WIDTH//2-100,HEIGHT//2-50))


    else:
        end = False
        ball = Main("Ball.png", 3, WIDTH/2-25, HEIGHT/2-25, 50, 50)
        score_1 = 0
        score_2 = 0
        time.delay(3000)
    display.update()

    clock.tick(60)