# Import necessary libraries
import pygame
from pygame.locals import *
import pygame_gui

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

# Define font properties
font = pygame.font.SysFont('휴먼둥근헤드라인',24)

# Player properties
player = pygame.image.load("npc.png")
player = pygame.transform.scale(player, (80, 100))
player_speed = 3
player_Rect = player.get_rect()
player_Rect.x = 400
player_Rect.y = 400

# Enemy properties
class npc:
    def __init__(self, manager, screen, button_width = 100, button_height = 30, button_x = 400, button_y = 100):
        self.screen = screen
        self.manager = manager
        self.npc = pygame.transform.scale(pygame.image.load("npc.png"), (80, 100))
        self.npc_speed = 2
        self.npc_Rect = npc.get_rect()
        self.npc_Rect.x = 400
        self.npc_Rect.y = 100
        self.npc_moving = True  # 움직임을 제어하는 변수
        self.button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(button_x, button_y, button_width, button_height),
                                text='Click Me',
                                manager=manager)
        self.dialogue_box = pygame.transform.scale(pygame.image.load("gray_box.png"), (700, 300))
        self.dialogue_box_Rect = dialogue_box.get_rect()
        self.dialogue_box_Rect.x = (screen_width - 700) // 2
        self.dialogue_box_Rect.y = (screen_height - 300) // 2
        self.rendered_text = font.render("안녕하세요! 저는 최윤종이에요. 오늘 날씨가 좋네요!", True, BLACK)  # npc가 띄울 문구
        self.text_rect = rendered_text.get_rect(center=(self.dialogue_box_Rect.x + 700 // 2,
                                            self.dialogue_box_Rect.y + 300 // 2))

        
    def progress(self, event):
        if pygame.Rect(player_Rect.x, player_Rect.y, 50, 50).colliderect(pygame.Rect(self.npc_Rect.x, self.npc_Rect.y, 50, 50)):
            self.manager.update(pygame.time.get_ticks() / 1000.0)
            self.manager.draw_ui(self.screen)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    screen.blit(self.dialogue_box, self.dialogue_box_Rect)
                    screen.blit(self.rendered_text, self.text_rect)
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

npc1 = npc(manager, screen)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        manager.process_events(event)

    if event.type == pygame.KEYDOWN: # 키가 눌리면
        if event.key == pygame.K_RETURN: # 키가 눌린 값이 엔터값이면
            dialogue_box_ = False
            k = False
            player_speed = 3
            npc1.start()

    keys = pygame.key.get_pressed()
    # Player movement
    if keys[K_a] and player_Rect.x > 0:
        player_Rect.x -= player_speed
    if keys[K_d] and player_Rect.x < screen_width - player_speed:
        player_Rect.x += player_speed
    if keys[K_w] and player_Rect.y > 0:
        player_Rect.y -= player_speed
    if keys[K_s] and player_Rect.y < screen_height - player_speed:
        player_Rect.y += player_speed

    npc1.progress(event)

    button_x = npc1.npc_Rect.x
    button_y = npc1.npc_Rect.y
    button.rect.x = button_x
    button.rect.y = button_y
    # Check collision
    screen.fill(BLACK)
        # Add dialogue text and buttons here
    screen.blit(player, player_Rect)
    screen.blit(npc1.npc, npc1.npc_Rect)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
