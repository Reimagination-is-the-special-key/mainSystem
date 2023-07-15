import json
import os


def save_data(name, data):
    with open(f'./data/{name}.txt') as F:
        F.write(data)


class Chapter:
    def __init__(self, chapter):
        self.chapter = chapter
        self.main_background_path = './data/imgs/windows.png'
        self.backgrounds_path = './data/imgs/chapter1'
        self.background = self.main_background_path

    def switch_background(self, way: int):
        pos = self.background.split('/')[-1].replace('.png', '').split('-')
        pos[way] += 1
        n = '-'.join(pos)
        self.background = f'./data/imgs/{n}.png'
        return self.background

    def save(self, pos, extra_data:dict):
        data = {
            "pos": pos,
            "extra_data": extra_data
        }
        with open('./data/chapter1.json', 'w') as F:
            json.dump(data, F, ensure_ascii=False, indent=4)
