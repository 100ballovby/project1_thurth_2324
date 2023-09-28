import sys
import pygame as pg


def run_game(W, H, window_name):
    pg.init()
    screen = pg.display.set_mode((W, H))
    pg.display.set_caption(window_name)
    bg_color = (230, 230, 230)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        screen.fill(bg_color)
        pg.display.flip()


run_game(1200, 800, 'Alien invasion game')
