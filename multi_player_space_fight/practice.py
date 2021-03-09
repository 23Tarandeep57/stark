import pygame
import os
import sys
pygame.init()
pygame.font.init()
pygame.mixer.init()


WIDTH,HEIGHT = 1000,600
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 50,40
screen = pygame.display.set_mode(( WIDTH,HEIGHT))
pygame.display.set_caption('pygame practice')
red_bullets = []
yellow_bullets = []
WHITE = (255,255,255)
YELLOW = (255,255,0)
RED = (255,0,0)
BLACK = (0,0,0)
FPS = 60
VEL = 5
BULLET_VEL = 10
MAX_BULLETS = 5
RED_HIT = pygame.USEREVENT +1
YELLOW_HIT = pygame.USEREVENT+2
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets','Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets','Gun+Silencer.mp3'))
HEALTH_FONT = pygame.font.SysFont('comicsans',40)
WINNER_FONT = pygame.font.SysFont('comicsans',100)

def winner_font(winner_text):
    winner_font = WINNER_FONT.render(winner_text,1,WHITE)
    screen.blit(winner_font,
            (WIDTH//2-winner_font.get_width()//2,HEIGHT//2))

    pygame.display.update()
    pygame.time.delay(2000)

YELLOW_SPACE_SHIP = pygame.image.load(os.path.join
        ('Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP =pygame.transform.rotate(pygame.transform.scale
        (YELLOW_SPACE_SHIP,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
RED_SPACE_SHIP = pygame.image.load(os.path.join
        ('Assets','spaceship_red.png'))
RED_SPACESHIP =pygame.transform.rotate(pygame.transform.scale
        (RED_SPACE_SHIP,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)
SPACE_bg = pygame.image.load(os.path.join('Assets','space.png'))
SPACE = pygame.transform.scale(SPACE_bg,(WIDTH,HEIGHT))
BORDER = pygame.Rect(WIDTH//2+2,0,5,HEIGHT)

def update_screen(red,yellow,yellow_bullets,red_bullets,red_health,yellow_health):
    screen.fill(WHITE)
    screen.blit(SPACE,(0,0))
    screen.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    screen.blit(RED_SPACESHIP, (red.x, red.y))
    red_health_text = HEALTH_FONT.render("HEALTH: " +str(red_health),1,WHITE)
    yellow_health_text = HEALTH_FONT.render("HEALTH: " + str(yellow_health), 1, WHITE)
    screen.blit(red_health_text,(WIDTH - red_health_text.get_width() - 10,10))
    screen.blit(yellow_health_text, (10 , 10))

    pygame.draw.rect(screen,BLACK,BORDER)
    for bullet in yellow_bullets:
        pygame.draw.rect(screen,YELLOW,bullet)
    for bullet in red_bullets:
        pygame.draw.rect(screen,RED,bullet)
    pygame.display.update()


def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        if bullet.colliderect(red):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        if bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        if bullet.colliderect(yellow):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        if bullet.x <0:
            red_bullets.remove(bullet)

def bullet_movements(yellow_bullets,red_bullets):
    for bullet in yellow_bullets:
        bullet.x +=BULLET_VEL
    for bullet in red_bullets:
        bullet.x -=BULLET_VEL


def spaceship_movements(keys_pressed,yellow,red):

    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # left
        yellow.x -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL < HEIGHT - 30:  # down
        yellow.y += VEL
    if keys_pressed[pygame.K_d] and yellow.x +VEL < BORDER.x-30:  # right
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y -VEL >0 :  # up
        yellow.y -= VEL

    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x:  # left
        red.x -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL <HEIGHT - 30:  # down
        red.y += VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL < WIDTH -30:  # right
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # up
        red.y -= VEL

def main_game():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow_health = 10
    red_health = 10
    clock = pygame.time.Clock()
    run = True
    while run:

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets)<MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width -10,yellow.y + yellow.height//2 +2,10,5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets)<MAX_BULLETS:
                    bullet = pygame.Rect(red.x ,red.y + red.height//2  ,10,5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type==RED_HIT:
                red_health -=1
                BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health -=1
                BULLET_HIT_SOUND.play()

        handle_bullets(yellow_bullets,red_bullets,yellow,red)
        keys_pressed = pygame.key.get_pressed()
        spaceship_movements(keys_pressed,yellow, red,)
        bullet_movements(yellow_bullets,red_bullets)

        update_screen(red,yellow,yellow_bullets,red_bullets,red_health,yellow_health)

        winner_text = ""
        if red_health <= 0:
            winner_text = "YELLOW WINS!"
        if yellow_health <= 0:
            winner_text = "RED WINS!"
        if winner_text != "":
            
            winner_font(winner_text)
            red_bullets.clear()
            yellow_bullets.clear()
           
            break

    main_game()


if __name__ == "__main__":
    main_game()
