import pygame
import settings as s
import base as b

from camera import Camera
from map import BaseMap
from world_physics import NazwijMnie


def main():
    pygame.init()

    screen = pygame.display.set_mode((s.WIDTH, s.HEIGHT))
    clock = pygame.time.Clock()

    map = BaseMap()
    map.load_map('resources/tiled/map3')

    camera = Camera(cam_width=s.WIDTH, cam_height=s.HEIGHT, map_width=map.get_width(), map_height=map.get_height())

    handler = NazwijMnie(b.alucard, map)

    ####
    all_sprites = pygame.sprite.Group()
    stones_sprites = pygame.sprite.Group()

    for sp in map.get_all_tiles():
        all_sprites.add(sp)

    all_sprites.add(b.alucard)
    for stone in b.stones:
        all_sprites.add(stone)
        stones_sprites.add(stone)


    running = True
    while running:
        clock.tick(s.FPS)
        #screen.blit(b.background, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: raise (SystemExit, "QUIT")

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

        handler.domything()
        camera.follow(b.alucard)
        print(camera.state)
        for sprite in all_sprites:
            screen.blit(sprite.image, camera.apply(sprite))

        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
