import pygame
import sys
import time
import random
pygame.font.init()
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)
WIDTH,HEIGHT = 600,600
PLAY_WIDTH,PLAY_HEIGHT = 500,500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('snake')
score_font = pygame.font.SysFont('comicsans',40)
lost_font = pygame.font.SysFont('comicsans',80)
def main():
    FPS = 10
    clock = pygame.time.Clock()
    score = 0
    change_to = 1   # initially snake will e at rest
    direction = 0
    snake_pos = [PLAY_WIDTH/2,PLAY_HEIGHT/2]
    snake_body_pos = [[PLAY_WIDTH/2,PLAY_HEIGHT/2],[PLAY_WIDTH/2,PLAY_HEIGHT/2],[PLAY_WIDTH/2,PLAY_HEIGHT/2]]   
    food_list = []
    lost = False
    play_rect = pygame.Rect(WIDTH/2-PLAY_WIDTH/2,HEIGHT/2-PLAY_HEIGHT/2+20,PLAY_WIDTH,PLAY_HEIGHT)
    while True:
        clock.tick(FPS)        
        screen.fill(BLACK)   
        score_text = score_font.render('SCORE: '+str(score),1,WHITE)  
        screen.blit(score_text,(10,10))
        pygame.draw.rect(screen,RED,play_rect,10)
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    change_to='UP'
                elif event.key == pygame.K_s:
                    change_to='DOWN'
                elif event.key == pygame.K_a:
                    change_to='LEFT'
                elif event.key == pygame.K_d:
                    change_to='RIGHT'
                    
        #preventing snake to immideately changing direction to the opposite side
        if change_to=='UP' and direction!='DOWN':
            direction = 'UP'
        if change_to=='DOWN' and direction!='UP':
            direction = 'DOWN'
        if change_to=='LEFT' and direction!='RIGHT':
            direction = 'LEFT'
        if change_to=='RIGHT' and direction!='LEFT':
            direction = 'RIGHT'
            
        #moving snake
        if direction == 'LEFT':
            snake_pos[0]-=10                   
        elif direction == 'UP':
            snake_pos[1]-=10
        elif direction == 'DOWN':
            snake_pos[1]+=10       
        elif direction=='RIGHT':
            snake_pos[0]+=10
            
        #adding food_rect in a list 
        if len(food_list) < 1:
            food_rect = pygame.Rect(10*(random.randint(play_rect.x//10+1,(play_rect.x+PLAY_WIDTH-20)//10 -1)), 10*(random.randint(play_rect.y//10+1,(play_rect.y+PLAY_HEIGHT-20)//10-1)),10,10)
            food_list.append(food_rect)
            
        for food in food_list:
            if [food.x,food.y] in snake_body_pos:
                food_list.remove(food) #checking if the food will appear downside of snake's tail
            else:
                pygame.draw.rect(screen,GREEN,food)#if food is not downside of our tail drawing it
                
        #drawing head of snake
        pygame.draw.rect(screen,YELLOW,pygame.Rect(snake_body_pos[0][0],snake_body_pos[0][1],10,10))
        pygame.draw.rect(screen,RED,pygame.Rect(snake_body_pos[0][0],snake_body_pos[0][1],10,10),7)
        #drawing the body
        if len(snake_body_pos)>1: 
            for pos in snake_body_pos[1:]:
                 pygame.draw.rect(screen,WHITE,pygame.Rect(pos[0],pos[1],10,10))
                 pygame.draw.rect(screen,RED,pygame.Rect(pos[0],pos[1],10,10),5)
        
        #food and snake head collision
        for food in food_list:
            #inserting info for additional segment of snake
            #if we eat food the additional segment will become part snake tail otherwise removing it
            snake_body_pos.insert(0,list(snake_pos))
            if food.x == snake_pos[0] and food.y == snake_pos[1]:
                score+=1
                food_list.remove(food)
            else:
                snake_body_pos.pop()
        pygame.display.update()
        
        #colliding with our tail
        for block in snake_body_pos[1:]:
            if len(snake_body_pos)>3:
                if block[0]==snake_body_pos[0][0] and block[1]==snake_body_pos[0][1]:
                    lost = True
        if snake_body_pos[0][0]+10>=play_rect.x+PLAY_WIDTH or snake_body_pos[0][0]<=play_rect.x:
            lost =True
        if snake_body_pos[0][1]+10>=play_rect.y+PLAY_HEIGHT or snake_body_pos[0][1]<=play_rect.y:
            lost = True
        if lost:
            lost_text = lost_font.render('You Lost !',1,WHITE)
            screen.blit(lost_text,(PLAY_WIDTH/2-lost_text.get_width()/2,PLAY_HEIGHT/2-lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(3000)
            score = 0
            direction = 1
            change_to = 0
            break
    main()        
        
        

                
if __name__ =="__main__":
    main()
