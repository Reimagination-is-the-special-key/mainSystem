# Import necessary libraries
import pygame
from pygame.locals import *
import pygame_gui
import os
import random
from time import sleep
vec = pygame.math.Vector2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)


pygame.init()

k = False
button_ = False

# Set up the game window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Initialize Pygame GUI manager
manager = pygame_gui.UIManager((screen_width, screen_height))

player_posX = 400
player_posY = 300

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.  
        self.image = pygame.image.load('data\imgs\npc.png')
        self.image = pygame.transform(self.image, (80, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = player_posX
        self.rect.centery = player_posY
        self.speed = 4

# Define font properties
font = pygame.font.SysFont('휴먼둥근헤드라인',24)

font2 = pygame.font.SysFont('휴먼둥근헤드라인',12)

# Enemy properties
class npc:
    def __init__(self, manager, screen, name, txt):

        self.screen = screen
        self.txt = txt
        self.manager = manager
        self.dialogue_box_ = False

        self.npc = pygame.transform.scale(pygame.image.load("npc.png"), (80, 100))
        self.npc_speed = 2
        self.npc_Rect = self.npc.get_rect()
        self.npc_Rect.x = 400
        self.npc_Rect.y = 100
        self.npc_moving = True  # 움직임을 제어하는 변수

        # Create a button
        self.button_width = 100
        self.button_height = 30
        self.button_x = 400
        self.button_y = 100

        self.dialogue_box = pygame.transform.scale(pygame.image.load("gray_box.png"), (700, 300))
        self.dialogue_box_Rect = self.dialogue_box.get_rect()
        self.dialogue_box_Rect.x = (screen_width - 700) // 2
        self.dialogue_box_Rect.y = (screen_height - 300) // 2
        self.rendered_text = font.render(txt, True, BLACK)
        self.rendered_name = font2.render(name, True, BLACK)  # npc가 띄울 문구
        self.text_rect = self.rendered_text.get_rect(center=(self.dialogue_box_Rect.x + 700 // 2,
                                        self.dialogue_box_Rect.y + 300 // 2))
        
        self.button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(self.button_x, self.button_y, 100, 30),
            text='Click Me',
            manager=manager
            ) # 버튼 만들기
    def progress(self, event):
        if pygame.Rect(player_Rect.x, player_Rect.y, 80, 100).colliderect(pygame.Rect(self.npc_Rect.x, self.npc_Rect.y, 80, 100)):
            self.stop()
            self.npc = pygame.transform.scale(pygame.image.load("npc2.png"), (80, 100))
            self.manager.update(pygame.time.get_ticks() / 1000.0)
            self.manager.draw_ui(screen) # 버튼 그리기
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.button_ = True
                    self.dialogue_box_ = True
        else:
            self.button_ =False
            self.start()
            self.npc = pygame.transform.scale(pygame.image.load("npc.png"), (80, 100))

        if self.button_:
            self.manager.update(pygame.time.get_ticks() / 1000.0)
            self.manager.draw_ui(screen)

        if self.dialogue_box_:
            screen.blit(self.dialogue_box, self.dialogue_box_Rect)
            screen.blit(self.rendered_text, self.text_rect)
            screen.blit(self.rendered_name, (100, 200))
            self.stop() 

        if self.npc_moving:  # npc_moving이 True일 때만 움직입니다.
            self.npc_Rect.y += self.npc_speed 
            if self.npc_Rect.y >= 500 or self.npc_Rect.y <= 0:
                self.npc_speed = -self.npc_speed
                self.npc_moving = False  # npc가 벽에 닿으면 멈춥니다.
                pygame.time.set_timer(USEREVENT + 1, 2000)  # 2초 동안 멈추도록 타이머를 설정합니다.

        else:
            # 타이머 이벤트가 발생했을 때, 다시 움직이도록 설정합니다.
            if event.type == USEREVENT + 1:
                self.npc_moving = True
                self.npc_stop_timer = None
        
    def stop(self):
        self.npc_moving = False
        self.npc_stop_timer = None
    def start(self):
        self.npc_moving = True


running = True
clock = pygame.time.Clock()

# Dialogue box properties

npc1 = npc(manager, screen, "최윤종", "안녕하세요! 저는 최윤종이에요. 여자랑은 말을 못해요")
npc2 = npc(manager, screen, "호플리스", """안녕하세요! 저는 호플리스에요. 이젠 희망이 없어요...""")
npc2.npc_Rect.x += 200


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        npc1.manager.process_events(event)
        npc2.manager.process_events(event)

    if event.type == pygame.KEYDOWN: # 키가 눌리면
        if event.key == pygame.K_RETURN: # 키가 눌린 값이 엔터값이면
            if npc1.dialogue_box_ or npc2.dialogue_box_:
                npc1.dialogue_box_ = False
                npc2.dialogue_box_ = False
                player_speed = 3
                npc1.start()
                npc2.start()

    keys = pygame.key.get_pressed()

    npc1.button.rect.x = npc1.npc_Rect.x
    npc1.button.rect.y = npc1.npc_Rect.y+100

    npc2.button.rect.x = npc2.npc_Rect.x
    npc2.button.rect.y = npc2.npc_Rect.y+100
    
    # Player movement
    if keys[K_a] and player_Rect.x > 0:
        player_Rect.x -= player_speed
    if keys[K_d] and player_Rect.x < screen_width - player_speed:
        player_Rect.x += player_speed
    if keys[K_w] and player_Rect.y > 0:
        player_Rect.y -= player_speed
    if keys[K_s] and player_Rect.y < screen_height - player_speed:
        player_Rect.y += player_speed

    # Check collision
    screen.fill(BLACK)
        # Add dialogue text and buttons here

    screen.blit(player, player_Rect)
    screen.blit(npc1.npc, npc1.npc_Rect)
    screen.blit(npc2.npc, npc2.npc_Rect)

    npc1.progress(event)
    npc2.progress(event)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()