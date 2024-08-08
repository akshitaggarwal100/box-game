# importing modules
import pygame
from random import randint

# initialising module
pygame.init()
pygame.mixer.init()

# initialising game window
width = 800
height = 800
gameWindow = pygame.display.set_mode((width,height))

# setting game title
pygame.display.set_caption("The Box Game")

# defining game specific variables
exit_game = False
game_over = False
fps = 60

# colors
red = (230, 57, 70)
sky_blue = (168, 218, 220)
violet = (69, 123, 157)
dark_blue = (29, 53, 87)
white = (241, 250, 238)
orange = (255, 107, 53)

# snake
snake_x = randint(30,width - 60)
snake_y = randint(40,height - 40)
snake_size = 40
snake_y_velocity = 0
snake_x_velocity = 0
init_velocity = 7

# food
food_x = randint(100,width - 100)
food_y = randint(200,height - 200)
food_size = 40

# difficulty levels
hard = 10
medium = 25
easy = 35

score = 0
high_score = 0

# initialising the game clock
clock = pygame.time.Clock()

# loading the music
score_sound = pygame.mixer.Sound("pop.mp3")
lose_sound = pygame.mixer.Sound("over.mp3")
up_sound = pygame.mixer.Sound("up.mp3")
down_sound = pygame.mixer.Sound("down.mp3")
left_sound = pygame.mixer.Sound("left.mp3")
right_sound = pygame.mixer.Sound("right.mp3")
pygame.mixer.music.load("df2.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

# loading the image
trophy = pygame.image.load('trophy.png').convert_alpha()
trophy = pygame.transform.smoothscale(trophy, (20, 20))

# initialising the font
font = pygame.font.Font(None,30)

# function for displaying text on screen
def text_screen(num,x,y):
    text = font.render(str(num), True, white)
    gameWindow.blit(text,[x, y])

# creating game loop
while not exit_game:

    # getting any event done in gameWindow
    for event in pygame.event.get():
        
        # handling the key down event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                up_sound.play()
                snake_y_velocity = -init_velocity
                snake_x_velocity = 0

            elif event.key == pygame.K_a:
                left_sound.play()
                snake_x_velocity = -init_velocity
                snake_y_velocity = 0

            elif event.key == pygame.K_s:
                down_sound.play()
                snake_y_velocity = init_velocity
                snake_x_velocity = 0

            elif event.key == pygame.K_d:
                right_sound.play()
                snake_x_velocity = init_velocity
                snake_y_velocity = 0

        # handling the quit event
        elif event.type == pygame.QUIT:
            exit_game = True
        # the loop of getting and handling events gets over

    # checking if snake head touched food and updating position of food
    if abs(snake_x - food_x) < easy and abs(snake_y - food_y) < easy:
        score += 10
        score_sound.play()
        food_x = randint(70,720) 
        food_y = randint(70,720)

    # updating the position of snake head
    snake_y += snake_y_velocity
    snake_x += snake_x_velocity

    # filling the background of display(gameWindow)
    gameWindow.fill(white)

    # checking if snake head touched the boundary and handling the event appropriately
    if snake_y < 30 or snake_y > height - snake_size or snake_x < 0 or snake_x > width - snake_size:
        lose_sound.play()

        if score > high_score:
            high_score = score

        # to keep the snake head just at the boundary
        # snake_x -= snake_x_velocity
        # snake_y -= snake_y_velocity

        # to stop the snake head
        snake_x_velocity = 0
        snake_y_velocity = 0

        # to take the food out of window
        food_x = -40
        food_y = -40

        # displaying the other elements appropriately
        pygame.draw.rect(gameWindow, red, [food_x,food_y,food_size,food_size])
        pygame.draw.rect(gameWindow, dark_blue, [snake_x,snake_y,snake_size,snake_size])
        pygame.draw.rect(gameWindow, violet, [0,0,width,30])
        gameWindow.blit(trophy,(5,5))
        text_screen(high_score,30,5)
        text_screen(score, width//2, 5)

        # displaying the game over message
        pygame.draw.rect(gameWindow, red, [0, height//2 - 20, width, 60])
        text_screen("GAME OVER", width//2 - 60, height//2)
        pygame.display.update()

        pygame.time.wait(2000)

        # restarting the game
        snake_x = randint(30,width - 60)
        snake_y = randint(40,height - 40)
        food_x = randint(100,width - 100)
        food_y = randint(200,height - 200)
        score = 0

    # making food
    pygame.draw.rect(gameWindow, red, [food_x,food_y,food_size,food_size])

    # making the snake head
    pygame.draw.rect(gameWindow, dark_blue, [snake_x,snake_y,snake_size,snake_size])

    # making background for score
    pygame.draw.rect(gameWindow, violet, [0,0,width,30])

    # displaying the high score and trophy
    gameWindow.blit(trophy,(5,5))
    text_screen(high_score,30,5)

    # updating score on screen
    text_screen(score, width//2, 5)
    
    # updating the display and ticking the clock
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()