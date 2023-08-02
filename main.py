import pygame
import sys

from Player import Player
from system import Chapter

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960

pygame.init()
pygame.display.set_caption("Ripley")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
player = Player()
chapter = Chapter(1, 'manager', screen, player, clock)  # chapter 1 설정
# 배경 설정

chapter.start()
