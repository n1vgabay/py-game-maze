
import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = 5
        self.damage = 50
        self.rect = pygame.Rect(self.x,self.y,self.radius,self.radius)
    def draw(self, window):
        pygame.draw.circle(window, self.color, (int(self.x), int(self.y)), self.radius)
