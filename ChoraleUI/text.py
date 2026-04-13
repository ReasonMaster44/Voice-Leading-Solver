import pygame as pg

pg.font.init()

class Text:
    def __init__(self, x, y, text, size=20):
        font = pg.font.SysFont("Arial", size)

        self.surf = font.render(text, True, (255, 255, 255))
        self.rect = self.surf.get_rect(center=(x, y))

    def draw(self, surf: pg.Surface):
        surf.blit(self.surf, self.rect)

    def set_pos(self, x, y):
        self.rect = self.surf.get_rect(center=(x, y))