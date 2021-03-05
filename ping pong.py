import pygame,sys
import random

pygame.init()
WIDTH,HEIGHT = 700,600
BLACK = (0,0,0)
WHITE = (250,250,250)
score_font = pygame.font.SysFont('comicsans',40)
screen = pygame.display.set_mode((WIDTH,HEIGHT))
winner_font = pygame.font.SysFont('comicsans',60)
pygame.display.set_caption('ping pong'.title())
bar_lenght = HEIGHT/8 +10
bar_width = 10
start_x =5
start_y = HEIGHT/2-bar_lenght/2
bar_vel = 3.5

RADIUS = 7

def draw_screen(bar1,bar2,ball_x,ball_y,score1,score2):
    screen.fill(BLACK)
    score1_text = score_font.render('Score: '+str(score1),1,WHITE)
    score2_text = score_font.render('Score: '+str(score2),1,WHITE)
    screen.blit(score1_text,(10,10))
    screen.blit(score2_text,(WIDTH-score2_text.get_width()-10,10))
    pygame.draw.rect(screen,WHITE,bar1)
    pygame.draw.rect(screen,WHITE,bar2)
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), RADIUS)

def main():
    FPS = 60
    clock = pygame.time.Clock()
    bar1 = pygame.Rect(start_x, start_y, bar_width, bar_lenght)
    bar2 = pygame.Rect(WIDTH - start_x - bar_width, start_y, bar_width, bar_lenght)
    ball_x = WIDTH / 2
    ball_y = HEIGHT / 2
    ball_ve_x = random.randint(-1,1)
    score1 = 0
    score2 = 0
    move_ball = False
    if ball_ve_x ==0:
        ball_vel_x = 5
    else:
        ball_vel_x = ball_ve_x*5
    ball_vel_y = random.randint(-10,10)/10
    while True:
#setting number of frames per  sECOND
        clock.tick(FPS)
#drawing screen
        draw_screen(bar1,bar2,ball_x,ball_y,score1,score2)
#exit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
#movementr of bars
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] and bar1.y - bar_vel > 0:  # up
            bar1.y -= bar_vel
            move_ball = True
        if keys_pressed[pygame.K_s] and bar1.y + bar_vel + bar_lenght < HEIGHT:  # down
            bar1.y += bar_vel
            move_ball = True
        if keys_pressed[pygame.K_UP] and bar2.y - bar_vel > 0:  # up
            bar2.y -= bar_vel
            move_ball = True
        if keys_pressed[pygame.K_DOWN] and bar2.y + bar_vel + bar_lenght < HEIGHT:  # down
            bar2.y += bar_vel
            move_ball = True
#ball's movement
        if move_ball == True:
            ball_x += ball_vel_x
            ball_y += ball_vel_y
#changing ordinate of ball when hit celing or floor
        if ball_y+RADIUS>=HEIGHT:
            ball_vel_y*=-1
        elif ball_y-RADIUS<=0:
            ball_vel_y*=-1
#changing absicsa of ball when collide with bar and changing ordinate to make the ball swing somewhart more
        if ball_x+RADIUS>=bar2.x and 0<=ball_y-bar2.y<=bar_lenght:
            ball_vel_x*=-1
            if ball_vel_y<=5:
                ball_vel_y +=(random.randint(-1,1))/1.5
            else:
                ball_vel_y-=3
        elif ball_x-RADIUS<=bar1.x+bar_width and 0<=ball_y-bar1.y<=bar_lenght:
            ball_vel_x*=-1
            if ball_vel_y<=5:
                ball_vel_y +=((random.randint(-1,1))/3)
            else:
                ball_vel_y-=3
#ball hitting the side of screen
        if ball_x + RADIUS >= WIDTH:
            pygame.time.delay(1000)
            score1 += 1
            ball_x = WIDTH / 2
            ball_y = HEIGHT / 2
            bar1.y = HEIGHT/2-bar_lenght/2
            bar2.y = HEIGHT / 2 - bar_lenght / 2
            move_ball = False
            ball_vel_y*=random.randint(-1,1)

        elif ball_x - RADIUS <= 0:
            pygame.time.delay(1000)
            score2 += 1
            ball_x = WIDTH / 2
            ball_y = HEIGHT / 2
            bar1.y = HEIGHT / 2 - bar_lenght / 2
            bar2.y = HEIGHT / 2 - bar_lenght / 2
            move_ball = False
            ball_vel_y *= random.randint(-1, 1)

        if score1 >=10:
            winner_text = winner_font.render('player 1 won'.title(), 1, WHITE)
            screen.blit(winner_text, (WIDTH / 2 - winner_text.get_width() / 2, HEIGHT / 2 - winner_text.get_height()))
            pygame.time.delay(2000)
        elif score2>=10:
            winner_text = winner_font.render('player 2 won'.title(), 1, WHITE)
            screen.blit(winner_text,(WIDTH/2-winner_text.get_width()/2,HEIGHT/2-winner_text.get_height()))
            pygame.time.delay(2000)
        pygame.display.update()
if __name__ == '__main__':
    main()
