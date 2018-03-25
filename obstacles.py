import pygame
import random
import settings as s

class Stone(pygame.sprite.Sprite):
    def __init__(self, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(s.GREY)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(s.WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -10)
        self.speed = random.randrange(1, 10)

    def update(self):
        self.rect.y = (self.rect.y + self.speed) % s.HEIGHT
