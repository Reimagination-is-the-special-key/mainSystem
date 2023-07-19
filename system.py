import json
import os
import pygame
from npc import NPC


class Chapter:
    def __init__(self, 
                 chapter, 
                 manager, 
                 screen, 
                 player: pygame.sprite.Sprite ):
        self.chapter = chapter
        self.manager = manager
        self.screen = screen
        self.player = player
        self.main_background_path = './data/imgs/windows.png'
        self.backgrounds_path = f'./data/imgs/chapter{chapter}/'
        self.background = self.main_background_path
        self.background = pygame.image.load(self.background)
        self.npcs = pygame.sprite.Group()

    def switch_background(self, way: int):
        pos = self.background.split('/')[-1].replace('.png', '').split('-')
        pos[way] += 1
        n = '-'.join(pos)
        self.background = f'./data/imgs/{n}.png'
        for i in xrange(255):
            delay (30)
            screen.set_alpha(i)
        sleep(2)
        for i in xrange(255):
            delay (30)
            screen.set_alpha(255-i)
        self.background = pygame.image.load(self.backgrounds_path+way+'.png')
    
    def configure_npc(self, img, text):
        self.npcs.add(NPC(self.manager, self.screen, text, img))

    def save(self, extra_data:dict):
        data = {
            "pos": self.player.user_position,
            "npc": [[i.img, i.text] for i in self.npcs],
            "extra_data": extra_data
        }
        with open(f'./data/chapter{self.chapter}.json', 'w') as F:
            json.dump(data, F, ensure_ascii=False, indent=4)

    def load(self):
        with open(f'./data/chapter{self.chapter}.json', 'r') as F:
            data = json.load(f)
            self.__init__(self.chapter, self.manager, self.screen, self.player)
            for i in data['npc']:
                self.configure_npc(i[0], i[1])
            self.player.pos
            
    def start(self):
        while True:
            clock.tick(60)
            # 플레이어 벽 충돌 구현
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.npcs.clear(self.screen, self.background)
            self.npcs.draw(screen)

        pygame.display.update()
