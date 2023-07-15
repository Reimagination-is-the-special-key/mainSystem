import pygame
import sys

from system import Chapter

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
pygame.display.set_caption("Ripley")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pos_x = 200
pos_y = 200

clock = pygame.time.Clock()
chapter = Chapter(1)  # chapter 1 설정
screen.blit(pygame.image.load(chapter.background), (0, 0))  # 배경 설정

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
