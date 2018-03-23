import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos
        self.speed = 0
        self.boost = 1

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            if self.rect.left > 0:
                self.speed = -1
        elif keystate[pygame.K_RIGHT]:
            if self.rect.right < 931:
                self.speed = 1
        if keystate[pygame.K_LSHIFT]:
            self.boost = 2
        self.rect.x += self.boost * self.speed * self.walk
        self.speed = 0
        self.boost = 1
