#Part 1:importing 
import pygame,sys
import time
import random
import ctypes

pygame.init()

white=(255,255,255)
black=(100,0,0)
red =(255,0,0)

#Setting window size according to device screen size in windows
"""user32 = ctypes.windll.user32
   screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
   window_width = user32.GetSystemMetrics(0)
   window_height = user32.GetSystemMetrics(1)"""

#Part 2: setting window size
window_width=1200
window_height= 600


gameDisplay=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Snake Game')
font=pygame.font.SysFont(None,25,bold=True)

def myquit():
	pygame.quit()
	sys.exit(0)

clock=pygame.time.Clock()  
FPS=5
blockSize=20 #intializing size of each block of snake
noPixel=0

#Part 3: Drawing snake
def snake(blockSize,snakelist):
	for size in snakelist:
		pygame.draw.rect(gameDisplay,black,[size[0]+5, size[1],blockSize,blockSize],2)

def message_to_screen(msg, color):
	screen_text=font.render(msg,True,color)
	gameDisplay.blit(screen_text,[window_width/3,window_height/2.5])

#Part4: The game
def gameLoop():
    gameExit = False
    gameOver = False

    #intial position of snake
    lead_x = window_width/2
    lead_y = window_height/2

    change_pixels_of_x = 0
    change_pixels_of_y = 0

    snakelist = []
    snakeLength = 1

    #Intial POsition of Apple
    randomAppleX = round(random.randrange(0, window_width-blockSize)/10.0)*10.0
    randomAppleY = round(random.randrange(0, window_height-blockSize)/10.0)*10.0 

    while not gameExit:       

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit",red)
            pygame.display.update()

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

		#Logic1:commands to move the snake 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    myquit()

                leftArrow = event.key == pygame.K_LEFT
                rightArrow = event.key == pygame.K_RIGHT
                upArrow = event.key == pygame.K_UP
                downArrow = event.key == pygame.K_DOWN                

                if leftArrow:
                    change_pixels_of_x = -blockSize
                    change_pixels_of_y = noPixel

                elif rightArrow:
                    change_pixels_of_x = blockSize
                    change_pixels_of_y = noPixel

                elif upArrow:
                    change_pixels_of_y = -blockSize
                    change_pixels_of_x = noPixel

                elif downArrow:
                    change_pixels_of_y = blockSize
                    change_pixels_of_x = noPixel

            if lead_x >= window_width or lead_x < 0 or lead_y >= window_height or lead_y < 0:
                gameOver = True                   

        #Logic2:snake moves and changes position 
        lead_x += change_pixels_of_x
        lead_y += change_pixels_of_y

        #Checking if snake is going out of boundary & hence game ends
        if lead_x >= window_width or lead_x < 0 or lead_y >= window_height or lead_y < 0:
            gameOver = True        

        gameDisplay.fill(white)

        AppleThickness = 25

        #Logic3:Apple gets displayed
        print([int(randomAppleX),int(randomAppleY),AppleThickness,AppleThickness])

        pygame.draw.rect(gameDisplay, red, [randomAppleX,randomAppleY,AppleThickness,AppleThickness])

        allspriteslist =[]
        allspriteslist.append(lead_x)
        allspriteslist.append(lead_y)

        snakelist.append(allspriteslist)

        if len(snakelist) > snakeLength:
            del snakelist[0]            

        for eachSegment in snakelist [:-1]:
            if eachSegment == allspriteslist:
                gameOver = True                

        #Logic4:screen is updated
        snake(blockSize, snakelist)        

        pygame.display.update() 

        #Logic5:Snake eats the apple and another apple gets drawn
        if lead_x >= randomAppleX and lead_x <= randomAppleX + AppleThickness:
            if lead_y >= randomAppleY and lead_y <= randomAppleY + AppleThickness:
                randomAppleX = round(random.randrange(0, window_width-blockSize)/10.0)*10.0
                randomAppleY = round(random.randrange(0, window_height-blockSize)/10.0)*10.0
                snakeLength += 1             

        clock.tick(FPS)

    pygame.quit()

    quit()

gameLoop()