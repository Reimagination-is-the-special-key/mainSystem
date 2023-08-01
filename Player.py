import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x=300, y=400, style=0):  # 초기화
        super(Player, self).__init__()
        self.game = game
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.images = []
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 4
        self.direction = 0
        self.images.append(pygame.transform.scale(pygame.image.load(f'data/imgs/player_{style}_front.png'), (80, 100)))
        self.images.append(pygame.transform.scale(pygame.image.load(f'data/imgs/player_{style}_back.png'), (80, 100)))
        self.images.append(pygame.transform.scale(pygame.image.load(f'data/imgs/player_{style}_left.png'), (80, 100)))
        self.images.append(pygame.transform.scale(pygame.image.load(f'data/imgs/player_{style}_right.png'), (80, 100)))
        self.image = pygame.transform.scale(self.images[0], (80, 100))

    def get_pos(self):  # 플레이어 위치 얻기
        return f'{self.rect.x}|{self.rect.y}'

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self) -> None:  # 이동
        self.image = self.images[self.direction]
        if self.direction == 0:
            self.rect.y += self.speed
        elif self.direction == 1:
            self.rect.y -= self.speed
        elif self.direction == 2:
            self.rect.x -= self.speed
        elif self.direction == 3:
            self.rect.x += self.speed


Player('game')