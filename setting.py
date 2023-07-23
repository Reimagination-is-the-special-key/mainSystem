import pygame as pg

from system import Chapter


class Settings(pg.sprite.Sprite):

    def __init__(self, chapter: Chapter):
        pg.sprite.Sprite.__init__(self)
        self.chapter = chapter

    def save(self):
        self.chapter.save()

    def quit(self):
        self.save()
        pg.quit()
