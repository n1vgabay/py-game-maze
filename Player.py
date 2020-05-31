import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        self.width = 50
        self.height = 50
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill(color)
        self.x = x
        self.y = y
        self.life = 6
        self.lifeDelay = 0
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.score = 0
    def draw(self, window):
        window.blit(self.image,(self.x, self.y))
    def hit(self):
       return