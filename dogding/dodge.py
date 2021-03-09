import pygame
import sys
import time
import random
import os
pygame.font.init()
#defining constants
WIDTH,HEIGHT = 600,650
BLUE = (0,0,255)
BLACK= (0,0,0)
#defining screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('catch the ball'.title())
#loading images
background = pygame.transform.scale(pygame.image.load(os.path.join('images','background.png')),(WIDTH,HEIGHT))
glove = pygame.transform.scale(pygame.image.load(os.path.join('images','glove.png')),(50,50))
#defining speeds
player_vel = 4
ball_vel = 4
#ball radius
RADIUS = 10
#fonts
score_font = pygame.font.SysFont('comicsans',40)
winning_font = pygame.font.SysFont('comicsans',60)

def glove_movement(glove_rect,level):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and glove_rect.x-player_vel>=0:
        glove_rect.x-=player_vel+2*(level-1)/3  
    if keys[pygame.K_d] and glove_rect.x+player_vel+50<=WIDTH:
        glove_rect.x+=player_vel+2*(level-1)/3  

def ball_formation(balls):
    
    while len(balls)<=2:
        startx = random.randint(10,WIDTH-10)
        starty = random.randint(-5*HEIGHT,-10)
        B_COLOR = ((random.randint(2,5)*50),(random.randint(2,5)*50),(random.randint(2,5)*50))
        ball = [startx,starty,B_COLOR]
        balls.append(ball)

def ball_movements(balls,glove_rect,score,level):
    ball_formation(balls)
    for ball in balls:
        [startx,starty,ballcolor] = ball
        pygame.draw.circle(screen,ball[2],(ball[0],ball[1]),RADIUS,0)
        pygame.draw.circle(screen,BLACK,(ball[0],ball[1]),RADIUS+1,1)
        ball[1]+=ball_vel+(level-1)/3    
    
def draw_screen(glove_rect,balls,score,level,lives):
    screen.fill(BLUE)
    screen.blit(background,(0,0))
    screen.blit(glove,(glove_rect.x,glove_rect.y))
    ball_movements(balls,glove_rect,score,level)
    score_text = score_font.render('SCORE: '+str(score),1,BLACK)
    screen.blit(score_text,(10,10))
    level_text = score_font.render('LEVEL: '+str(level),1,BLACK)
    screen.blit(level_text,(WIDTH-level_text.get_width()-10,10))
    lives_text = score_font.render('LIVES: '+str(lives),1,BLACK)
    screen.blit(lives_text,(WIDTH/2-lives_text.get_width()/2,10))
        
    pygame.display.update()
    
def main():
    clock = pygame.time.Clock()
    FPS = 60
    glove_rect = pygame.Rect(WIDTH/2,HEIGHT - 50,50,50)
    balls = []
    score = 0
    level = 1
    balls_catched = []
    lives = 10
    win= False
    lost = False
    while True:
        clock.tick(FPS)      
        for ball in balls:
            [startx,starty,ballcolor] = ball
            if glove_rect.x-ball[0]-RADIUS<=0 and glove_rect.x - ball[0]+RADIUS>=-50:
                if glove_rect.y-ball[1]-RADIUS<=0:
                    balls_catched.append(ball)
                    balls.remove(ball)
                    score+=10 +int((level-1)/3)  
                    
            elif ball[1]-RADIUS-20>=HEIGHT:
                balls.remove(ball)
                lives-=1
                if score>=1:
                    score-=5
                    
        if len(balls_catched)==level*10 +level*3:
            level +=1
        if score>=1000:
            win = True
        if lives <=0:
            lost = False

        if win:
            winning_text = winning_font.render('you won !'.title(),1,BLACK)
            screen.blit(winning_text,(WIDTH/2-winning_text.get_width()/2,HEIGHT/2 - winning_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(3000)
            break
        if lost:
            losing_text = winning_font.render('you lost !'.title(),1,BLACK)
            screen.blit(losing_text,(WIDTH/2-losing_text.get_width()/2,HEIGHT/2 - losing_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(3000)
            break
            
        draw_screen(glove_rect,balls,score,level,lives)
        glove_movement(glove_rect,level)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    main()  
if __name__=='__main__':
    main()

