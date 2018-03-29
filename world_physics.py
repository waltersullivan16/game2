from characters import VerticalState


class NazwijMnie(object):
    def __init__(self, player, map):
        self.player = player
        self.map = map

    def is_standing_on_tile(self, target, tile):
        if tile.passable:
            return False
        if abs(target.rect.bottom - tile.rect.top) <= 2 and target.rect.left <= tile.rect.right - 1 and target.rect.right -1 >= tile.rect.left:
            print(target.rect, tile.rect, tile.passable)
            return True
        return False

    def is_standing_on_any_tile(self, target, map):
        for tile in map.get_all_tiles():
            if self.is_standing_on_tile(target, tile):
                return True
        return False

    def fix_pos_wrt(self, target, tile):
        def _in(x, a, b):
            return a <= x < b
        if tile.passable:
            return
        if not target.rect.colliderect(tile.rect):
            return
        a = target.rect
        b = tile.rect

        if a.bottom > b.top and a.bottom - b.top < 25:
            a.bottom = b.top
        if a.top < b.bottom and b.bottom - a.top < 25:
            a.top = b.bottom
        if a.left < b.right and b.right - a.left < 25:
            a.left = b.right
        if a.right > b.left and a.right - b.left < 25:
            a.right = b.left

    def fix_pos_wrt_map(self, target, map):
        for tile in map.get_all_tiles():
            self.fix_pos_wrt(target, tile)

    def player_collisions(self, player, map):
        if not self.is_standing_on_any_tile(player, map):
            in_air = True
        else:
            in_air = False
        return in_air

    def domything(self):
        self.fix_pos_wrt_map(self.player, self.map)
        if self.player_collisions(self.player, self.map):
            self.player.set_vertical_state(VerticalState.IN_AIR)
        else:
            self.player.land()
