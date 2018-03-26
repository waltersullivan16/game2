import pygame
import settings as s

class Bullet(pygame.sprite.Sprite):
    def __init__(self, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.image = pygame.Surface((10, 10))
        self.image.fill(s.GREY)
        self.rect = self.image.get_rect()
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        self.speed = 5
        self.time = self.calculate_time()

    def calculate_time(self):
        dist = ((self.pos_x - self.goal_x)**2 + (self.pos_y - self.goal_y)**2)**(1/2)
        return dist // self.speed

    def calculate_dist(self):
        x = abs(self.rect.x - self.pos_x) // self.time
        y = abs(self.rect.y - self.pos_y) // self.time
        return (x, y)

    def update(self):
        x_len, y_len = self.calculate_dist()
        self.rect.x += x_len
        self.rect.y += y_len
        hits = pygame.sprite.spritecollide(self, self.stones_sprites, True)
        for h in hits:
            h.kill()

