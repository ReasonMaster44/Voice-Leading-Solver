import pygame as pg
from ChoraleEngine import Chorale
from .system import System

def start(chorale: Chorale):
    pg.init()
    win_w, win_h = 800, 600
    win = pg.display.set_mode((win_w, win_h))
    pg.display.set_caption("Voice Leading Generator")

    margin = 50

    system = System(margin, (win_h - System.get_height()) / 2, win_w - (margin * 2), chorale)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        win.fill((30, 30, 30))
        
        system.draw(win)

        pg.display.update()

    pg.quit()