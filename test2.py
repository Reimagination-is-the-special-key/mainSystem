import pygame

vec = pygame.math.Vector2
pygame.init()

class Sprite(pygame.sprite.Sprite):
    
    def __init__(self, position):
        super(Sprite, self).__init__
        size = (100, 100) #이미지 사이즈
        
        images = [] #이미지 애니메이션 리스트
        
        images.append(pygame.image.load('C:\\Users\\최윤종\\Desktop\\테스트\\일러스트2.png')) #이미지 애니메이션 리스트 추가

        self.rect = pygame.Rect(position,size)
        
        self.images = [pygame.transform.scale(image, size) for image in images]
        
        self.index = 0
        self.image = images[self.index]
        
        
    def update(self):
        
        self.index += 1
        
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        
        

        




    
         
    