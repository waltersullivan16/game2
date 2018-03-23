import pygame
from base import WIDTH, HEIGHT, FPS, background, alucard

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
all_sprites.add(alucard)

running = True
while running:
    clock.tick(FPS)
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
