import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x=300, y=400):
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.image.load('data\imgs\npc.png')
        self.image = pygame.transform(self.image, (80, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 4


Player('game')