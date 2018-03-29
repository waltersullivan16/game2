import csv
import pygame
import os
import xmltodict

import settings as s
from characters import Entity


class Tile(Entity):
    def __init__(self, image, x, y, w, h, passable):
        Entity.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.rect.width, self.rect.height = w, h
        self.passable = passable


class BaseMap(object):
    def __init__(self):
        self.walls = []
        self.reset_all()

    def reset_all(self):
        self.tiles_by_index = {}
        self.all_tiles = []

    def load_map(self, file):
        self.reset_all()
        with open(file, 'r') as f:
            map_data = xmltodict.parse(f.read())['map']
        print('=== loading map ===')
        for k, v in map_data.items():
            print(k, v)

        self.width = int(map_data['@width'])
        self.height = int(map_data['@height'])

        # there could be multiple layers i guess
        self.name = map_data['layer']['@name']
        assert self.width == int(map_data['layer']['@width'])
        assert self.height == int(map_data['layer']['@height'])
        assert map_data['layer']['data']['@encoding'] == 'csv'

        text_data = map_data['layer']['data']['#text'] + ','
        csv_reader = csv.reader(text_data.split('\n'), delimiter=',')
        tiles_array = []
        for row in csv_reader:
            tiles_array.append(list(map(int, row[:-1])))
        print(tiles_array)

        tile_ids_to_load = set([a for a in sum(tiles_array, []) if a > 0])

        tilesets = map_data['tileset']
        if type(tilesets) != list:
            tilesets = [tilesets]
        for t in tilesets:
            tiles_path = os.path.join(os.path.dirname(os.path.abspath(file)), t['@source'])
            first_gid = int(t['@firstgid'])
            print(first_gid)
            self.load_tileset(tiles_path, tile_ids_to_load, first_gid)
        self.tiles_by_index[0] = pygame.Surface((s.TILE_DRAW_WIDTH, s.TILE_DRAW_HEIGHT))

        for r_i, row in enumerate(tiles_array):
            for c_i, col in enumerate(row):
                self.all_tiles.append(Tile(self.tiles_by_index[col],
                                           c_i * s.TILE_DRAW_WIDTH,
                                           r_i * s.TILE_DRAW_HEIGHT,
                                           s.TILE_DRAW_WIDTH,
                                           s.TILE_DRAW_HEIGHT,
                                           col == 0))
                print(c_i * s.TILE_DRAW_WIDTH, r_i * s.TILE_DRAW_HEIGHT)
        self.tiles_array = tiles_array


    def load_tileset(self, file, tile_ids=None, first_gid=1):
        print(file)
        with open(file, 'r') as f:
            tileset_data = xmltodict.parse(f.read())['tileset']

        print('=== loading tileset ===')
        for k, v in tileset_data.items():
            print(k, v)

        tile_width = int(tileset_data['@tilewidth'])
        tile_height = int(tileset_data['@tileheight'])
        tile_count = int(tileset_data['@tilecount'])

        source_image = tileset_data['image']['@source']
        source_width = int(tileset_data['image']['@width'])
        source_height = int(tileset_data['image']['@height'])

        tile_rows = source_height / tile_height
        tile_cols = source_width / tile_width

        print(file)
        print(os.path.dirname(file))

        fff = os.path.join(os.path.dirname(file), source_image)
        print(fff)
        print(os.path.abspath(fff))

        spritesheet = pygame.image.load(fff)
        print(spritesheet)

        tile_ids = tile_ids or range(first_gid, first_gid + tile_count)

        for tile_id in tile_ids:
            if tile_id < first_gid or tile_id >= first_gid + tile_count:
                continue
            pos = tile_id - first_gid
            row = pos // tile_cols
            col = pos % tile_cols
            print(pos, first_gid, tile_id, tile_count)
            print(tile_width * col, tile_height * row, tile_width, tile_height)
            tile_raw = spritesheet.subsurface(tile_width * col, tile_height * row, tile_width, tile_height)
            self.tiles_by_index[tile_id] = pygame.transform.scale(tile_raw, (s.TILE_DRAW_WIDTH, s.TILE_DRAW_HEIGHT))
            #print(self.tiles[tile_id].rect)

    def get_all_tiles(self):
        return self.all_tiles

    def get_width(self):
        return len(self.tiles_array[0]) * s.TILE_DRAW_WIDTH

    def get_height(self):
        return len(self.tiles_array) * s.TILE_DRAW_HEIGHT

if __name__ == '__main__':
    m = BaseMap()
    #m.load_map('resources/tiled/untitled.tmx')
    m.load_map('resources/tiled/map2')
