import sys
import pygame
import os
import math
import random
pygame.init()
pygame.font.init()
WIDTH,HEIGHT = 800,550
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('HANGMAN Game')


FPS = 60

lost_image = pygame.transform.scale(pygame.image.load(os.path.join('images','hangman6.png')),(100,100))
WHITE = (255,255,255)
BLACK = (0,0,0)
ANSWERING_FONT = pygame.font.SysFont('comicsans',60)
LETTER_FONT = pygame.font.SysFont('comicsans',40)
WORD_FONT = pygame.font.SysFont('comicsans',60)
WINNER_FONT= pygame.font.SysFont('comicsans',80)
HINT_FONT = pygame.font.SysFont('comicsans',30)
letters = []
RADIUS = 20
GAP = 20
startx = (WIDTH - (26 * RADIUS + 12 * GAP)) / 2
starty =450
A =65
#determining the position of each letter in circle
for i in range(26):
    x = startx+ RADIUS+((RADIUS*2 + GAP)*(i%13))
    y = starty +((i//13)*(2*RADIUS + GAP))
    visible = True
    #letter[3] is the character representation of numbers A=65,B=66,C=67......
    letters.append([x,y,chr(A+i),visible])

#empty list to append the guessed letters
guessed = []

#loading the images
images = []
for i in range(7):
    image = pygame.image.load(os.path.join('images','hangman'+str(i)+'.png'))
    
    images.append(image)

#craeting the winingh or losing results in a function
def results(message,letters,word):
    screen.fill(WHITE)
    text = WINNER_FONT.render(message, 1, BLACK)
    answer = ANSWERING_FONT.render('The Word Was ' + word,1,BLACK)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    screen.blit(answer,(WIDTH / 2 - answer.get_width()/2, HEIGHT / 2 - answer.get_height() / 2 + 100))
    pygame.display.update()
    pygame.time.delay(3000)
    guessed.clear()
    for letter in letters:
        x,y,ltr,visible = letter
        letter[3] = True
def resulting_hungman():

    screen.blit(lost_image,(50,50))

#all drawing stuff in game
def draw(hangman_status,word,word_pos,hints):
    screen.fill(WHITE)
#when we click on a letter if it is part of word to be guessed it is appended to empty list created 'guessed'
#then we add the letter in guessed in display_word and blit it on screen

    display_word = ''
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += '_ '
    text = WORD_FONT.render(display_word, 1, BLACK)
    screen.blit(text, (400, 300))

#displaying hint for list hints the position of hint is same for word in words
    hint_text = HINT_FONT.render('HINT: '+ hints[word_pos],1,BLACK)
    screen.blit(hint_text,(20,10))

#if letter guessed is wrong hangman status increases and therefore different images are displayed
    screen.blit(images[hangman_status],(100,100))

# removing the letters from screen when we click them
    for letter in letters:
        x,y,ltr,visible = letter
        if visible == True:
            pygame.draw.circle(screen,BLACK,(x,y),RADIUS,3)
            text = LETTER_FONT.render(ltr,1,BLACK)
            screen.blit(text,(x-text.get_width()/2,y-text.get_height()/2))

    pygame.display.update()
def main():
    hangman_status = 0
    words = ['PYGAME', 'PYTHON', 'IDE', 'RYTHM', 'PIANO', 'VIOLIN',
             "DEVELOPER",'AVENGERS','CAT','GAME','TABLET','ZEN',
             'YELLOW','BLACK','COFFEE','MOVIE','ITALIAN']

    word_pos = random.randint(0,len(words)-1)

    hints = ['ONE OF THE FIRST WORDS IN GAME CODE','LANGUAGE NO ONE SPEAKS',
            'WHERE YOU CODE','NO VOWEL ALLOWED','MUSIC INSTRUMENT',
            'MUSIC INSTRUMENT','SOMEONE WHO MADE THIS GAME','BEST TEAM EVER',
            'ANIMAL','WORD IS IN FRONT OF YOU','TAKE IT WHEN GET SICK',
            'PEACCCCCE','COLOUR','COLOUR','DRINK IT AND GET UP','LIKE TO WATCH','LANGUAGE YOU CANNOT SPEAK' ]

    word = words[word_pos]
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        


        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()


            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                m_x,m_y = pos
                for letter in letters:
                    x,y,ltr,visible = letter
                    dis = math.sqrt(((x-m_x)**2) +((y-m_y)**2))
                    if dis<=RADIUS:
                        guessed.append(ltr)
                        letter[3] = False
                        if ltr not in word:
                            hangman_status +=1

#drawing the screen and other drawing stuff
        draw(hangman_status,word,word_pos,hints)

#creating a winning variable if it is true we win
        won = True
        for letter in word:
            if letter not in guessed:
                won = False

        if won:
            pygame.time.delay(1000)
            results('You Won !',letters,word)
            break
        if hangman_status >= 6:
            pygame.time.delay(1000)
              
            results('You Lost !',letters,word)  
            resulting_hungman()  
            break
#restart the game
    main()

if __name__=='__main__':
    main()
