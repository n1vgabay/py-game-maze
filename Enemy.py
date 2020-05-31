import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        self.width = 50
        self.height = 50
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill(color)
        self.x = x
        self.y = y
        self.life =100
        self.damage = 1
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
    def draw(self, window):
        window.blit(self.image,(self.x, self.y))
    def is_collided_with(self,player):
        return self.rect.colliderect(player.rect)
    def removeEnemyNoLife(self,enemies_list,player):
        if self.life <= 0:
            enemies_list.remove(self)
            player.score += 10