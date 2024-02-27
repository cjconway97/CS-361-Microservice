import pygame
import time
import random

pygame.init()

# Set screen size
width = 1000
height = 600

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (50, 153, 213)
dark_blue = (32, 64, 86)
red = (213, 50, 80)

block_size = 20
speed = 20

# Create the display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

def message(msg, color, pos):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, pos)


def gameLoop():
    # Reset score at the beginning of each game
    score = 0
    
    game_over = False

    while not game_over:
        game_close = False

        # Set snake position
        y_snake = height / 2
        x_snake = width / 2

        y_change = 0
        x_change = 0

        snake_list = []
        length_of_snake = 1

        # Random food generator on the grid
        food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
        food_y = round(random.randrange(0, height - block_size) / block_size) * block_size

        while not game_close and not game_over:            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True

#----------- Insert snake movement here---------------#

#----------- Insert if snake hits wall here ----------#

            # Update the snake's position and body segments
            snake_head = [x_snake, y_snake]

            snake_list.append(snake_head)

            if len(snake_list) > length_of_snake:
                # Ensures snake doesn't grow indefinitely
                del snake_list[0]

            # Clear the screen by filling it with the blue color
            screen.fill(blue)

            # Generates the food block
            pygame.draw.rect(screen, green, [food_x, food_y, block_size, block_size])

            # Generates snake body
            for segment in snake_list[:-1]:
                pygame.draw.rect(screen, black, [segment[0], segment[1], block_size, block_size])

            # Draw snake head
            pygame.draw.rect(screen, black, [snake_list[-1][0], snake_list[-1][1], block_size, block_size])

                        
            # Display score
            message("Score: " + str(score), black, (10, 10))

            pygame.display.update()

            # Increases snake length when food is eaten
            if x_snake == food_x and y_snake == food_y:
                food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
                food_y = round(random.randrange(0, height - block_size) / block_size) * block_size
                length_of_snake += 1
                score += 1

            pygame.display.update()
            clock.tick(speed)

        # Display the final score before restarting the game 
        screen.fill(blue)
        message("You Lost :( Press Q to Quit or E to Play Again", dark_blue, (200, 200))
        message("Score: " + str(score), black, (350, 250))
        pygame.display.update()

        while game_close:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False



# Menu at the beginning of the game
def menu():
    menu_display = True

    while menu_display:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        start_button = pygame.Rect(350, 200, 300, 50)
        pygame.draw.rect(screen, green, start_button)

        exit_button = pygame.Rect(350, 300, 300, 50)
        pygame.draw.rect(screen, red, exit_button)


        smallText = pygame.font.Font(None, 50)
        textSurf, textRect = text_objects("Start", smallText)
        textRect.center = ((350 + (300 / 2)), (200 + (50 / 2)))
        screen.blit(textSurf, textRect)

        smallText = pygame.font.Font(None, 50)
        textSurf, textRect = text_objects("Exit", smallText)
        textRect.center = ((350 + (300 / 2)), (300 + (50 / 2)))
        screen.blit(textSurf, textRect)

        if start_button.collidepoint((mouse[0], mouse[1])):
            if click[0] == 1:
                menu_display = False
                gameLoop()

        if exit_button.collidepoint((mouse[0], mouse[1])):
            if click[0] == 1:
                pygame.quit()
                quit()

        pygame.display.update()
        clock.tick(15)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

menu()
