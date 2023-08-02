import json
import sys
import keyboard

from pygame import Surface
from typing import Dict

import pygame

from Player import Player
# from npc import NPC
from setting import Settings


class Chapter:
    def __init__(self,
                 chapter,
                 manager,
                 screen: Surface,
                 player: Player,
                 clock: pygame.time.Clock):
        self.chapter = chapter
        self.manager = manager
        self.screen = screen
        self.player = player
        self.playergroup = pygame.sprite.GroupSingle(player)
        self.main_background_path = './data/imgs/windows.png'
        self.backgrounds_path = f'./data/imgs/chapter{chapter}/'
        self.background = self.main_background_path
        self.background = pygame.transform.scale(pygame.image.load(self.background), self.screen.get_size())
        self.pos = [0, 0, 0, 0]
        self.npcs = pygame.sprite.Group()
        self.clock = clock
        self.directiony = {
            'w': -1,
            's': 1,
        }
        self.directionx = {
            'a': -1,
            'd': 1,
        }

    def switch_background(self, way: int):
        self.pos[way] += 1
        for i in range(255):
            self.clock.tick(30)
            self.screen.set_alpha(i)
        self.clock.tick(150)
        for i in range(255):
            self.clock.tick(30)
            self.screen.set_alpha(255 - i)
        self.background = pygame.image.load(self.backgrounds_path + ''.join([str(i) for i in self.pos]) + '.png')

    # def configure_npc(self, img, text):
    #     self.npcs.add(NPC(self.manager, self.screen, text, img))

    def save(self, extra_data: dict = {}):
        data = {
            "pos": self.player.get_pos(),
            "npc": [[i.img, i.text] for i in self.npcs],
            "extra_data": extra_data
        }
        with open(f'./data/chapter{self.chapter}.json', 'w') as F:
            json.dump(data, F, ensure_ascii=False, indent=4)

    def load(self):
        with open(f'./data/chapter{self.chapter}.json', 'r') as F:
            data: Dict = json.load(F)
            self.__init__(self.chapter, self.manager, self.screen, self.player, self.clock)
            for i in data['npc']:
                self.configure_npc(i[0], i[1])
            self.player.set_pos(*data['pos'].split('|'))
        return data['extra_data']

    def draw_grid(self):
        # 0부터 TILESIZE씩 건너뛰면서 WIDTH까지 라인을 그려준다
        for x in range(0, self.screen.get_width(), 40):
            # 첫번째 인자부터 game_world(게임 화면)에 (0,0,0,50)의 색으로 차례대로 라인을 그려준다
            pygame.draw.line(self.screen, (0, 0, 0, 50), (x, 0), (x, self.screen.get_height()))
        for y in range(0, self.screen.get_height(), 40):
            pygame.draw.line(self.screen, (0, 0, 0, 50), (0, y), (self.screen.get_width(), y))

    def start(self):
        while True:
            self.clock.tick(60)
            self.screen.blit(self.background, (0, 0))
            self.draw_grid()
            # 플레이어 벽 충돌 구현
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            if keyboard.is_pressed('w'):
                self.player.dy = -1
            if keyboard.is_pressed('a'):
                self.player.dx = -1
            if keyboard.is_pressed('s'):
                self.player.dy = 1
            if keyboard.is_pressed('d'):
                self.player.dx = 1

            self.playergroup.clear(self.screen, self.background)
            self.playergroup.update()
            self.playergroup.draw(self.screen)
            self.npcs.clear(self.screen, self.background)
            self.npcs.update()
            self.npcs.draw(self.screen)
            pygame.display.update()

    def stop(self):
        while True:
            setting = Settings(self)
            setting.open_setting()
            # 게임 정지 및 게임 설정 띄우기
