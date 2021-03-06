import pygame
import sys
import random
print("100 lines")


def ball_animation():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


def player_animation():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_ai():
    if opponent.top < ball.y:
        opponent.y += opponent_speed*2
    if opponent.bottom > ball.y:
        opponent.y -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def ball_restart():
    global ball_speed_x,ball_speed_y
    ball.center = (screen_width/2,screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1, -1))


pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

light_grey = (200,200,200)
bg_color = pygame.Color('grey12')
player_color = (0,128,0)
opponent_color = (255,0,0)
background = (23,76,59)

ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 15, 15)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 7, 95)
opponent = pygame.Rect(10, screen_height / 2 - 70, 7, 95)

ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= 6
            if event.key == pygame.K_DOWN:
                player_speed += 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 6
            if event.key == pygame.K_DOWN:
                player_speed -= 6

    ball_animation()
    player_animation()
    opponent_ai()

    screen.fill(bg_color)
    pygame.draw.rect(screen, player_color, player)
    pygame.draw.rect(screen,opponent_color, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))

    pygame.display.flip()
    clock.tick(60)
