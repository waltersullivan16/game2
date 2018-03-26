from bullets import Bullet
import pygame
import settings as s

class Player(pygame.sprite.Sprite):
    def __init__(self, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos
        self.jumping = False
        self.acc_ver = 1
        self.jump_boost = False
        self.dir_ver = 0

    def _clean_jump(self):
        self.jumping = False
        self.acc_ver = 1
        self.rect.y = self.pos[1]
        self.dir_ver = 0

    def jump(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            if (self.jump_boost):
                self.acc_ver += 0.2
            if (not self.jumping):
                self.jump_boost = True
                self.dir_ver = 1
            self.jumping = True
        else:
            self.jump_boost = False

        if (self.jumping):
            current_jump = self.dir_ver * self.acc_ver * self.jump_height * (1 + (abs(self.rect.y - s.MAX_HEIGHT) / (self.pos[1] - s.MAX_HEIGHT)))

            #print(self.rect.y - current_jump, s.MAX_HEIGHT, self.dir_ver, self.acc_ver)
            #zmiana fazy na lot w dół; nie chce mi się pisać po ang pozdrawiam serdecznie
            if (((self.rect.y - current_jump) < s.MAX_HEIGHT)) and (not self.dir_ver == -1):
                self.dir_ver = -1
            elif ((self.rect.y - current_jump) > self.pos[1]):
                self._clean_jump()
            self.rect.y -= self.acc_ver * self.dir_ver * self.jump_height * (0.1 + ((self.pos[1] - self.rect.y) / (self.pos[1] - s.MAX_HEIGHT)))
            #print(0.1 + ((self.pos[1] - self.rect.y) / (self.pos[1] - s.MAX_HEIGHT)), self.acc_ver)

    def update(self):
        keystate = pygame.key.get_pressed()
        #print(keystate[pygame.K_LEFT], keystate[pygame.K_RIGHT])
        direction = -1 * (keystate[pygame.K_LEFT] and self.rect.left > 0) + (keystate[pygame.K_RIGHT] and self.rect.right < s.WIDTH)
        boost =  keystate[pygame.K_LSHIFT]
        self.rect.x += direction * (boost + 1) * self.walk
        self.jump()
        #print(keystate[pygame.K_UP], self.rect.y, self.jumping, self.jump_height, self.pos[1], ((not self.jumping) and (self.rect.y < self.pos[1])))

    def shoot(self, pos):
        goal_x, goal_y = pos
        Bullet(pos_x=self.rect.x, pos_y=self.rect.y, goal_x=goal_x, goal_y=goal_y)
