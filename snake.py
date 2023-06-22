import pygame
import time
import random

pygame.init()

# Window dimensions
width = 800
height = 600

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialize the display
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Define the snake and food sizes
snake_size = 20
food_size = 20

# Initialize clock object to control the frame rate
clock = pygame.time.Clock()
snake_speed = 15

# Font settings for displaying score
font_style = pygame.font.SysFont(None, 50)


def display_score(score):
    score_font = font_style.render("Score: " + str(score), True, white)
    window.blit(score_font, (10, 10))


def draw_snake(snake_body):
    for body_part in snake_body:
        pygame.draw.rect(window, green, pygame.Rect(
            body_part[0], body_part[1], snake_size, snake_size))


def show_game_over():
    game_over_text = "Game Over!"
    game_over_font = pygame.font.SysFont(None, 80)
    game_over_render = game_over_font.render(game_over_text, True, red)
    window.blit(game_over_render, (width / 2 - game_over_render.get_width() / 2, height / 2 - game_over_render.get_height() / 2))

    play_again_text = "Press SPACE to Play Again"
    play_again_font = pygame.font.SysFont(None, 40)
    play_again_render = play_again_font.render(play_again_text, True, white)
    window.blit(play_again_render, (width / 2 - play_again_render.get_width() / 2, height / 2 + game_over_render.get_height() / 2 + 20))


def run_game():
    game_over = False

    # Snake initial position
    x1 = width / 2
    y1 = height / 2

    # Snake's movement
    x1_change = 0
    y1_change = 0

    # Initialize snake body
    snake_body = []
    length_of_snake = 1

    # Generate initial food position
    food_x = round(random.randrange(0, width - food_size) / 20) * 20
    food_y = round(random.randrange(0, height - food_size) / 20) * 20

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0
                elif event.key == pygame.K_SPACE and game_over:
                    run_game()

        # Update snake position
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_over = True
        x1 += x1_change
        y1 += y1_change

        window.fill(black)
        pygame.draw.rect(window, red, pygame.Rect(
            food_x, food_y, food_size, food_size))
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_body.append(snake_head)
        if len(snake_body) > length_of_snake:
            del snake_body[0]

        for body_part in snake_body[:-1]:
            if body_part == snake_head:
                game_over = True

        draw_snake(snake_body)
        display_score(length_of_snake - 1)

        pygame.display.update()

        # Check if the snake has eaten the food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - food_size) / 20) * 20
            food_y = round(random.randrange(0, height - food_size) / 20) * 20
            length_of_snake += 1

        clock.tick(snake_speed)

    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        window.fill(black)
        show_game_over()
        pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            run_game()

        clock.tick(5)

    pygame.quit()


run_game()
