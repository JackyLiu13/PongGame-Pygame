#Jacky
#June 28 2020 
#test 

import pygame
#import pygame functions
import math
#import more math functions
pygame.init()
font = pygame.font.SysFont("Courier New",30)
#set font style and sizes
font_1 = pygame.font.SysFont("Courier New", 24)
font_2 = pygame.font.SysFont("Courier New", 18)
font_intro = pygame.font.SysFont("Courier New", 60)
def main():
    #where the program begins
    WIDTH = 1000
    #set the game window's resolution(width and height)
    HEIGHT = 600
    game_window = pygame.display.set_mode ((WIDTH, HEIGHT))
    #set a variable for the game resolution
    BLACK = (0, 0 ,0)#set colours in RGB and give variables for them
    WHITE = (225, 225, 225)
    PINK= (255,192,203)
    RED = (220, 20, 60)
    YELLOW = (255, 255, 0)
    paddleX = 950 #set player2 paddle coordinates
    paddleY = 200
    paddleX2 = 50#set player1 paddle coordinates
    paddleY2 = 200
    score1 = 0 #set player 1 score to 0
    score2 = 0 #set player 2 score to 0
    BallX = 400 #set the ball coordinates
    BallY = 20
    game = False #set game to False
    ballspeed = False #set ballspeed to False
    pause = False
    pygame.event.get()
    keys = pygame.key.get_pressed()
    UI = pygame.mixer.music.load("PongGame-Pygame\\Ultra Instinct Theme Music.mp3") #load music from file
    pygame.mixer.music.play(-1)#loop the music
    dank = False
#Main loop
    while game == False: #when game is equal to False (loop the program)
        pygame.event.get()
        keys = pygame.key.get_pressed() #the variable keys represents the key pressed
        game_window.fill(BLACK) #set the colour white as the background colour
        graphics_enter = font.render("Please press S to continue",1,WHITE) #display the message with the following colour and coordinates
        game_window.blit(graphics_enter,(300,450))
        graphics_pong = font_intro.render("PONG",1,WHITE)
        game_window.blit(graphics_pong,(420,250))
        if keys[pygame.K_s]: #If user press S, then ballspeed would become true
            ballspeed = True
        if keys[pygame.K_d]: #If user press d, dank mode will be true and then ballspeed would become true
            ballspeed = True
            dank = True
        pygame.display.update()#update the display

        while ballspeed == True: #when ballspeed is true (loop the following commands)
            pygame.event.get()
            keys = pygame.key.get_pressed()
            game_window.fill(BLACK)#fill the game window background to white
            graphics_slow = font.render("Press 1 for slower ball speed",1,WHITE)#create new texts and select colour for it
            game_window.blit(graphics_slow,(250,250))#locate the coordinates for the new texts
            graphics_fast = font.render("Press 2 for faster ball speed",1,WHITE)
            game_window.blit(graphics_fast,(250,300))
            if keys[pygame.K_1]:#if user press 1, then the variable game becomes true
                game = True
                speedX = 2 #change the value of speedX to 5
                speedY = 2 #change the value of speedY to 5
            elif keys[pygame.K_2]: #if user press 2, then the variable game becomes true
                game = True 
                speedX = 10 #change the value of speedX to 10
                speedY = 10 #change the value of speedY to 10
            pygame.display.update()
        
            while game == True: #when game is equal to true, run the following (loop the following commands)
                keys = pygame.key.get_pressed() 
                game_window.fill(BLACK) 
                Paddle = pygame.draw.rect(game_window,PINK,(paddleX, paddleY,6,120))
                Paddle2 = pygame.draw.rect(game_window,RED,(paddleX2, paddleY2,6,120))
                ball = pygame.image.load("C:\\Users\\Jacky\\Desktop\\Python test\\PongGame-Pygame\\Shrek.png")#load the image "Shrek.png" and import it as the ball
                ball = pygame.transform.scale(ball,(50,50))#adjust the image size
                ball = game_window.blit(ball,(BallX,BallY))#display the ball using the ball coordinates 
                graphics_score1 = font.render("Score: "+str(score1),1,WHITE) #set the scores for player 1 and 2
                game_window.blit(graphics_score1,(100,100))#display the score
                graphics_score2 = font.render("Score: "+str(score2),1,WHITE)
                game_window.blit(graphics_score2,(800,100))
                graphics_help = font_1.render("Press and hold C for controls",1, YELLOW)
                game_window.blit(graphics_help, (1,1))
                pygame.draw.rect(game_window, WHITE,(500,0,1,600))
               
                if keys[pygame.K_p]: # Pausing
                  paused = True
                if keys[pygame.K_p]:  # Unpausing
                  paused = False

                if keys[pygame.K_c]:
                    graphics_controls1 = font_2.render("Player 1 controls: W & S",1,WHITE)
                    game_window.blit(graphics_controls1, (1,20))
                    graphics_controls2 = font_2.render("Player 2 controls: UP ARROW KEY & DOWN ARROW KEY",1,WHITE)
                    game_window.blit(graphics_controls2, (1,35))
                    graphics_cheat1 = font_2.render("Player 1 cheat: click A to activate",1,WHITE)
                    game_window.blit(graphics_cheat1,(1,60))
                    graphics_cheat2 = font_2.render("Player 2 cheat: click RIGHT ARROW to activate",1,WHITE)
                    game_window.blit(graphics_cheat2,(1,75))
                #---------------#
                if keys[pygame.K_UP]:
                    paddleY = paddleY - 8 #if player press up key, the paddle would move 8 units up
                if keys[pygame.K_DOWN]:
                    paddleY = paddleY + 8 #if player press down key, the paddle would move 8 units down
                if paddleY2 > 480: #if the y-axis of the paddle is greater than 480 units
                    paddleY2 = 479 #Then set the y-axis of the paddle back 1 units, or set it to 479 unit
                if paddleY2 < 0:
                    paddleY2 = 1
                if paddleY > 480:
                    paddleY = 479
                if paddleY < 0:
                    paddleY = 1
                #--------------#
                ballRect = pygame.Rect(ball)#Set a new variable for the coordinates for pygame object
                paddleRect = pygame.Rect(Paddle2)
                if ballRect.colliderect(paddleRect):#if an object colides with another object, paddle and the ball in this case
                    if dank == False:
                        ballsound = pygame.mixer.Sound("PongGame-Pygame\\Hit 1.wav")#load sound effect from the file and set a variable for it
                    if dank == True:
                        ballsound = pygame.mixer.Sound("PongGame-Pygame\\Bruh.wav")
                    ballsound.play()#play the sound effect
                    speedX = speedX * -1# Then change the x coordinates of the ball
                if BallY == 0:
                    wallsound = pygame.mixer.Sound("PongGame-Pygame\\Coin 3.wav")#load sound effect from the file and set a variable for it
                    wallsound.play()
                    speedY = speedY * -1
                if BallY > 550:
                    wallsound = pygame.mixer.Sound("PongGame-Pygame\\Coin 3.wav")#load sound effect from the file and set a variable for it
                    wallsound.play()
                    speedY = speedY * -1
                if BallX > 1000:
                    score1 += 1
                    BallY = 20
                    BallX = 400
                    speedX = speedX * -1
                    paddleX = 950
                    paddleY = 200
                    paddleX2 = 50
                    paddleY2 = 200
                    pygame.time.delay(600)
                if BallX < -75:
                    score2 += 1
                    BallY = 20
                    BallX = 400
                    speedX = speedX *-1
                    paddleX = 950
                    paddleY = 200
                    paddleX2 = 50
                    paddleY2 = 200
                    pygame.time.delay(600)
                #-------------#
                pygame.event.get()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                    paddleY2 = paddleY2 - 8
                if keys[pygame.K_s]:
                    paddleY2 = paddleY2 + 8
                if paddleY2 == -1:
                    paddleY2 == 0
                if paddleY2 == 601:
                    paddleY2 == 600
                #-------------#
                ballRect = pygame.Rect(ball)
                paddleRect = pygame.Rect(Paddle)
                if ballRect.colliderect(paddleRect):
                    if dank == False:
                        ballsound = pygame.mixer.Sound("PongGame-Pygame\\Hit 1.wav")#load sound effect from the file and set a variable for it
                    if dank == True:
                        ballsound = pygame.mixer.Sound("PongGame-Pygame\\Bruh.wav")
                    ballsound.play()
                    speedX = speedX * -1
                #-------------#
                if score1 == 5:
                    pygame.mixer.music.stop()
                    victory = pygame.mixer.Sound("PongGame-Pygame\\Mario Victory.wav")#load sound effect from the file and set a variable for it
                    victory.play()
                    score1 += 1
                if score1 == 6 or score2 == 6:
                    game_window.fill(BLACK)
                    graphics_developer = font.render('''By Jacky and Justin  ''',1,YELLOW)
                    game_window.blit(graphics_developer,(1,1))
                    graphics_r = font.render("Press R to restart",1,YELLOW)
                    game_window .blit(graphics_r, (450, 475))
                    graphics_quit = font.render("Press ESC to quit the game",1, YELLOW)
                    game_window.blit(graphics_quit, (450,500))
                    speedX = 0
                    speedY = 0
                    if keys[pygame.K_r]:
                        main()#loops the program
                    if keys[pygame.K_ESCAPE]:
                        pygame.quit()
                    if keys[pygame.K_r]:
                        main()#loops the program
                    if keys[pygame.K_ESCAPE]:
                        pygame.quit()#Quit the game

                if score1 == 6:
                    graphics_restart = font.render("Player 1 WINS!",1,YELLOW)
                    game_window.blit(graphics_restart,(450,450))
                        
                if score2 == 5:
                    pygame.mixer.music.stop()#stop the music
                    victory = pygame.mixer.Sound("PongGame-Pygame\\Mario Victory.wav")#load sound effect from the file and set a variable for it
                    victory.play()
                    score2 +=1
                    
                if score2 == 6:
                    graphics_restart2 = font.render("Player 2 WINS!",1,YELLOW)
                    game_window.blit(graphics_restart2,(450,450))
                        
                if keys[pygame.K_RIGHT]:
                    if keys[pygame.K_UP]:
                        paddleY = paddleY - 8
                    if keys[pygame.K_DOWN]:
                        paddleY = paddleY + 8
                
                if keys[pygame.K_a]:
                    if keys[pygame.K_w]:
                        paddleY2 = paddleY2 - 8
                    if keys[pygame.K_s]:
                        paddleY2 = paddleY2 + 8
                        
                if keys[pygame.K_e]:
                    if keys[pygame.K_UP]:
                        paddleY = paddleY - 1
                    if keys[pygame.K_DOWN]:
                        paddleY = paddleY + 1
                        
                if keys[pygame.K_LEFT]:
                    if keys[pygame.K_w]:
                        paddleY2 = paddleY2 - 1
                    if keys[pygame.K_s]:
                        paddleY2 = paddleY2 + 1
                if keys[pygame.K_ESCAPE]:
                        pygame.quit()

                BallY += speedY 
                BallX += speedX
                pygame.display.update()

main()#Where the program restarts if main() was mentioned







