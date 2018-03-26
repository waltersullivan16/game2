import pygame
import settings as s
import base as b

pygame.init()
screen = pygame.display.set_mode((s.WIDTH, s.HEIGHT))
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
stones_sprites = pygame.sprite.Group()
all_sprites.add(b.alucard)

for stone in b.stones:
    all_sprites.add(stone)
    stones_sprites.add(stone)

running = True
while running:
    clock.tick(s.FPS)
    screen.blit(b.background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            #print("prawy przycick myszka")
            pos = pygame.mouse.get_pos()
            b.alucard.shoot(pos)
    all_sprites.update()
    hits = pygame.sprite.spritecollide(b.alucard, stones_sprites, False)
    if hits:
        print("pedal")
        #running = False
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
