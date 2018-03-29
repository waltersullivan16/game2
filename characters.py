from bullets import Bullet
import pygame
import settings as s

from enum import Enum



class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Enemy(Entity):
    def __init__(self, image, pos):
        Entity.__init__(self)
        self.image = image
        self.pos = pos


class Controls(object):
    def __init__(self, rect):
        self.rect = rect
    def do_move(self):
        raise NotImplemented()


class VerticalState(Enum):
    STANDING = 0
    CHARING = 1
    IN_AIR = 2


class PhysicalState(object):
    def __init__(self, rect):
        self.rect = rect
        self.vertical_state = VerticalState.STANDING
        #self.vertical_acc = 0
        self.vertical_speed = 0
        self.horizontal_speed = 0

    def set_vertical_state(self, state):
        self.vertical_state = state

    def update(self):
        self.rect.x += self.horizontal_speed
        self.rect.y -= self.vertical_speed
        if self.vertical_state != VerticalState.STANDING:
            self.vertical_speed -= s.GRAVITY_ACC

    def land(self):
        self.vertical_speed = 0
        self.vertical_state = VerticalState.STANDING


class Player(Entity):
    def __init__(self, image, pos, **kwargs):
        Entity.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

        self.state = PhysicalState(self.rect)

    def set_vertical_state(self, state):
        self.state.set_vertical_state(state)

    def jump(self):
        if self.state.vertical_state == VerticalState.STANDING:
            self.set_vertical_state(VerticalState.IN_AIR)
            self.state.vertical_speed = 20

    def read_input(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.state.horizontal_speed = min(self.state.horizontal_speed, 0)
            self.state.horizontal_speed -= s.HORIZONTAL_ACC
            self.state.horizontal_speed = max(self.state.horizontal_speed, -s.MAX_HORIZONTAL_SPEED)
        if keystate[pygame.K_RIGHT]:
            self.state.horizontal_speed = max(self.state.horizontal_speed, 0)
            self.state.horizontal_speed += s.HORIZONTAL_ACC
            self.state.horizontal_speed = min(self.state.horizontal_speed, s.MAX_HORIZONTAL_SPEED)
        if not keystate[pygame.K_LEFT] and not keystate[pygame.K_RIGHT]:
            self.state.horizontal_speed = 0
        if keystate[pygame.K_UP]:
            self.jump()

    def land(self):
        self.state.land()

    def update(self):
        self.read_input()
        self.state.update()
