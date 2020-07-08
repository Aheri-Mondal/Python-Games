import pygame

pygame.init()

#Defining Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#Defining font for Game over message
font= pygame.font.SysFont('Calibri', 25, False, False)

#Initializing the display window
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong Game")

clock=pygame.time.Clock()

def myquit():
    pygame.quit()
    sys.exit(0)

#Function to display game over message 
def message_to_screen(msg, color):
    screen_text=font.render(msg,True,color)
    screen.blit(screen_text,[150,300])

#draws the paddle. Also restricts its movement between the edges of the window.
def drawrect(screen,x,y):
    if x <= 0:
        x = 0

    if x >= 699:
        x = 699    

    pygame.draw.rect(screen,RED,[x,y,100,20])
   
#game's main loop
def gameLoop():  

    done = False #done means game exit
    gameover = False

    #Starting coordinates of the paddle
    rect_x = 400
    rect_y = 580

    #initial speed of the paddle
    rect_change_x = 0
    rect_change_y = 0

    #initial position of the ball
    ball_x = 50
    ball_y = 50

    #speed of the ball
    ball_change_x = 5
    ball_change_y = 5

    #initial score
    score = 0  

    while not done:

        #When game is over
        while gameover == True:
            screen.fill(RED)
            message_to_screen("Game over, press C to play again or Q to quit",WHITE)
            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    gameover = False
                    done = True                    

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_q:
                        done = True
                        gameover = False

                    if event.key == pygame.K_c:
                        gameLoop() 

        #Gaming controls
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    myquit()  

                if event.key == pygame.K_LEFT:
                    rect_change_x = -6

                elif event.key == pygame.K_RIGHT:
                    rect_change_x = 6

            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    rect_change_x = 0

                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    rect_change_y = 0            
            

        screen.fill(BLACK)
        rect_x += rect_change_x
        rect_y += rect_change_y

        ball_x += ball_change_x
        ball_y += ball_change_y    

        #this handles the movement of the ball.
        if ball_x<0:
            ball_x=0
            ball_change_x = ball_change_x * -1

        elif ball_x>785:
            ball_x=785
            ball_change_x = ball_change_x * -1

        elif ball_y<0:
            ball_y=0
            ball_change_y = ball_change_y * -1

        elif ball_x>rect_x and ball_x<rect_x+100 and ball_y==565:
            ball_change_y = ball_change_y * -1
            score = score + 1

        elif ball_y>600:
            score = 0
            ball_change_y = ball_change_y * -1
            gameover=True     
            
 
        pygame.draw.rect(screen,WHITE,[ball_x,ball_y,15,15])
       
        #drawball(screen,ball_x,ball_y)
        drawrect(screen,rect_x,rect_y)
       
        #score board
        font= pygame.font.SysFont('Calibri', 20, False, False)
        text = font.render("Score = " + str(score), True, WHITE)
        
        screen.blit(text,[600,100])  
        pygame.display.flip()         
        clock.tick(60)    

    pygame.quit()

    quit()

gameLoop()