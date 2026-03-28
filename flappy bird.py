import sounddivice as sd 
import numpy as np 
from pygame import *
from random import randint

window_size = 1200, 800

init()
window = display.set_mode((1200, 800))
clock = time.Clock()
bird = image.load("bird.png")
PIPE_BASE = image.load("truba.png")
PIPE_W, PIPE_H = 120, 440
PIPE_BOTTOM = transform.scale(PIPE_BASE, (PIPE_W, PIPE_H))
PIPE_TOP = transform.flip(PIPE_BOTTOM, False, True)

player_rect = Rect(50, 500, 100, 100)
def generate_pipes(count, pipe_width = 140, gap = 280, min_height = 50,
max_height = 440, distance = 650):
    pipes = []
    start_x = window_size[0]
    for i in range(count):
        height = randint(min_height, max_height)
        top_pipe = Rect(start_x, 0, pipe_width, height)
        bottom_pipe = Rect(start_x, height + gap,
        pipe_width, window_size[1] - (height + gap))
        pipes.extend([top_pipe, bottom_pipe])
        start_x += distance
    return pipes
pipes = generate_pipes(150)
game = True
while game:
    window.fill("sky blue")

    for e in event.get():
        if e.type == QUIT:
            quit()
    window.blit(bird, player_rect)
    #draw.rect(window, 'yellow', player_rect)

    if len(pipes) < 8:
        pipes += generate_pipes(150)

    for pipe in pipes[:]:
        pipe.x -= 5
        draw.rect(window, 'green', pipe)

        if pipe.x <= -100:
            pipes.remove(pipe)

        if player_rect.colliderect(pipe):
            game = False

    display.update()
    clock.tick(60)
