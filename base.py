from characters import Player
from obstacles import Stone
import os
import pygame

###Resources###
resources = "resources"
background_path = os.path.join(resources, "background.jpg")

###Backgrounds###
background = pygame.image.load(background_path)

###Characters###
#alucard_path = os.path.join(resources, "images.png")
#img = pygame.image.load(alucard_path)
img = pygame.Surface((32, 48))
img.fill((255, 0, 0))
alucard = Player(image=img, pos=(20, 200), walk=10, jump_height=10)

###Obstacles###
stones = []
for i in range(10):
    s = Stone()
    stones.append(s)
