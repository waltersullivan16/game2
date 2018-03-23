from characters import Player
import os
import pygame

WIDTH = 931
HEIGHT = 360
FPS = 30

##Colors##
RED = (255, 0 ,0)

###Resources###
resources = "resources"
background_path = os.path.join(resources, "background.jpg")
alucard_path = os.path.join(resources, "images.png")

###Backgrounds###
background = pygame.image.load(background_path)

###Characters###
alucard = Player(image=pygame.image.load(alucard_path), pos=(20, 200), walk=10)

