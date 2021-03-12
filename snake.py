import pygame
import sys
import time
pygame.font.init()
BLACK = (0,0,0)
RED = (255,0,0)


WHITE = (255,255,255)
WIDTH,HEIGHT = 600,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('snake')
startbox_x =40
box_side = WIDTH-startbox_x-40
startbox_y = (HEIGHT-box_side)/2+30
score_font = pygame.font.SysFont('comicsans',40)
grid_size = 20
gridbox_len = box_side/grid_size
def draw_grid():
    for i in range(grid_size-1):
        for j in range(grid_size-1):
            pygame.draw.line(screen,WHITE,(startbox_x,startbox_y+(j+1)*gridbox_len),(startbox_x+box_side,startbox_y+(j+1)*gridbox_len))
            pygame.draw.line(screen,WHITE,((i+1)*gridbox_len+startbox_x,startbox_y),((i+1)*gridbox_len+startbox_x,startbox_y+box_side))
        

def redraw_screen(score):
    screen.fill(BLACK)
    pygame.draw.rect(screen,RED,(startbox_x,startbox_y,box_side,box_side),1)
    score_text = score_font.render('SCORE: '+str(score),1,WHITE)  
    screen.blit(score_text,(10,10))
    draw_grid()
    
    pygame.display.update()
def main():
    FPS = 10
    clock = pygame.time.Clock()
    score = 0
   
    while True:
        clock.tick(FPS)
        redraw_screen(score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

                
if __name__ =="__main__":
    main()
