import pygame
import time
import random
import numpy

pygame.init()

pygame.mixer.music.load("Faded.wav")
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
pink= (201,255,128)

display_width = 700
display_height  = 500

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Furious Snake Game')


icon = pygame.image.load('apple.png')
pygame.display.set_icon(icon)

img = pygame.image.load('snake_head.png')
appleimg = pygame.image.load('apple.png')

clock = pygame.time.Clock()

AppleThickness = 30
block_size = 20
FPS = 15

high_score=[]

direction = "right"

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largemedfont = pygame.font.SysFont("chiller", 70)
largefont = pygame.font.SysFont("comicsansms", 80)


def pause():

    paused = True
    message_to_screen("Paused",
                      black,
                      -100,
                      size="large")

    message_to_screen("Press C to continue or Q to quit.",
                      black,
                      25)
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pygame.mixer.music.play(-1)
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        #gameDisplay.fill(white)
        
        clock.tick(5)
                    

def score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0,0])

def highscore(highscore):
    high_score.append(highscore)
    m=max(high_score)
    text = smallfont.render("Highscore: "+str(m), True, black)
    gameDisplay.blit(text, [640,0])

def randAppleGen():
    randAppleX = round(random.randrange(0, display_width-AppleThickness))
    randAppleY = round(random.randrange(0, display_height-AppleThickness))

    return randAppleX,randAppleY



def game_intro():

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
   
        gameDisplay.fill(white)
        message_to_screen("Welcome to Furious Snake Game The Real Battle Ground",
                          green,
                          -100,
                          "largemed")
        message_to_screen("The objective of the game is to eat red apples",
                          black,
                          -30)

        message_to_screen("The more apples you eat, the longer you get",
                          black,
                          10)

        message_to_screen("If you run into yourself, or the edges, you die!",
                          black,
                          50)

        message_to_screen("Use w,s,a,d for up,down,left,right respectively.",
                          black,
                          90)

        message_to_screen("Press C to play, P to pause or Q to quit.",
                          black,
                          180)
    
        pygame.display.update()
        clock.tick(20)

        
def game_intro1():                                                                ##################################################################

    intro1 = True
    global FPS

    while intro1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro1 = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_KP1:
                    FPS=8
                    intro1 = False
                if event.key == pygame.K_KP2:
                    FPS=15
                    intro1 = False
                if event.key == pygame.K_KP3:
                    FPS=22
                    intro1 = False
                if event.key == pygame.K_KP4:
                    FPS=35
                    intro1 = False
                
   
        gameDisplay.fill(white)
        message_to_screen("Choose the difficulty for the game:",
                          green,
                          -100,
                          "largemed")
        message_to_screen("EASY: Press the numeric key 1",
                          black,
                          -30)

        message_to_screen("NORMAL: Press the numeric key 2",
                          black,
                          10)

        message_to_screen("HARD: Press the numeric key 3",
                          black,
                          50)

        message_to_screen("IMPOSSIBLE: Press the numeric key 4",
                          black,
                          90)

        message_to_screen("OR: Press C to play at default Normal speed, P to pause or Q to quit.",
                          black,
                          180)
    
        pygame.display.update()
        clock.tick(15)        


def snake(block_size, snakelist):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img, 180)
        
    
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    elif size == "largemed":
        textSurface = largemedfont.render(text, True, color)
    
    return textSurface, textSurface.get_rect()
    
    
def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)


def gameLoop():
    pygame.mixer.music.play(-1)
    global direction,m

    direction = 'right'
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX,randAppleY = randAppleGen()
    
    while not gameExit:

        if gameOver == True:
            message_to_screen("Game over",
                              red,
                              y_displace=-50,
                              size="large")
            
            message_to_screen("Press C to play again or Q to quit",
                              blue,
                              50,
                              size="medium")
            pygame.display.update()
            

        while gameOver == True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_d:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_w:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_s:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0

                elif event.key == pygame.K_p:
                    pygame.mixer.music.stop()    
                    pause()

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:   ####Boundary conditions to out
            gameOver = True
            pygame.mixer.music.stop()
      

        lead_x += lead_x_change
        lead_y += lead_y_change
        
        gameDisplay.fill(pink)

        
        gameDisplay.blit(appleimg, (randAppleX, randAppleY))


        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
                pygame.mixer.music.stop()

        
        snake(block_size, snakeList)

        score(snakeLength-1)
        m=snakeLength-1
        highscore(m)
        
        pygame.display.update()

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:

            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:

                randAppleX,randAppleY = randAppleGen()
                snakeLength += 1

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:

                randAppleX,randAppleY = randAppleGen()
                snakeLength += 1

            
            

        
            
        
        

        clock.tick(FPS)
        
    pygame.quit()
    quit()
    
game_intro()
game_intro1()
gameLoop()
