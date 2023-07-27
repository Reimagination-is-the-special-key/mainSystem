from typing import Any, List

import pygame as pg


# from system import Chapter


class Btn(pg.sprite.Sprite):
    def __init__(self, type_: int, group, call):
        super(Btn, self).__init__()
        pg.sprite.Sprite.__init__(self, group)
        self.call = call
        # self.image = pg.image.load(f'./data/imgs/btn_{type_}.png')
        self.image = pg.Surface((10, 10))
        self.image.set_colorkey(pg.Color(255, 255, 255))
        self.rect = self.image.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.x = self.rect.x
        self.y = self.rect.y


class Settings(pg.sprite.Sprite):

    def __init__(self, chapter):
        super(Settings, self).__init__()
        self.chapter = chapter
        # self.image = pg.image.load('./data/imgs/setting.png')
        self.image = pg.Surface((30, 30))
        self.rect = self.image.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y
        self.btnGroup = pg.sprite.Group()
        self.btnList: List[Btn] = []
        self.initbtn()

    def initbtn(self):
        btn1 = Btn(1, self.btnGroup, self.save)
        btn2 = Btn(2, self.btnGroup, self.quit)
        btn3 = Btn(3, self.btnGroup, None)
        self.btnList.append(btn1)
        self.btnList.append(btn2)
        self.btnList.append(btn3)

    def save(self):
        self.chapter.save()

    def open_dev(self):
        self.image = pg.image.load('./data/imgs/dev.png')

    def update(self):
        self.x = self.rect.x
        self.y = self.rect.y
        mouse = pg.mouse.get_pos()
        clicked = pg.mouse.get_pressed()
        if clicked:
            for i in self.btnList:
                print(mouse)
                if i.image.get_width() + i.x > mouse[0] > i.x and i.image.get_height() + i.y > mouse[1] > i.y:
                    print(self.btnList.index(i))

    def quit(self):
        self.save()
        pg.quit()

