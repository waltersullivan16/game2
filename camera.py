from pygame import Rect


class Camera(object):
    def __init__(self, cam_width, cam_height, map_width, map_height, marigin_x=0.25, marigin_y=0.):
        self.cam_width = cam_width
        self.cam_height = cam_height
        self.map_width = map_width
        self.map_height = map_height
        self.state = Rect(0, 0, cam_width, cam_height)

        self.marigin_x_px = int(marigin_x * self.cam_width)
        self.marigin_y_px = int(marigin_y * self.cam_height)

    def follow(self, target):
        #pass
        x1, y1, w, h = target.rect
        x2, y2 = x1 + w, y1 + h

        if target.rect.left - self.marigin_x_px < self.state.left:
            self.state.left = max(0, target.rect.left - self.marigin_x_px)
        if target.rect.right + self.marigin_x_px > self.state.right:
            self.state.right = min(self.map_width, target.rect.right + self.marigin_x_px)


        # x_left = self.state.left + self.marigin_x_px - target.rect.left
        # if x_left < 0:
        #     self.state = self.state.move(x_left, 0)
        #
        # x_right = target.rect.right - (self.state.right - self.marigin_x_px)
        # if x_right > 0:
        #     self.state = self.state.move(x_right, 0)
        #
        # y_up = self.state.top + self.marigin_y_px - target.rect.top
        # if y_up < 0:
        #     self.state = self.state.move(0, y_up)
        #
        # y_down = target.rect.bottom - (self.state.bottom - self.marigin_y_px)
        # if y_down > 0:
        #     self.state = self.state.move(0, y_down)

    def apply(self, target):
        #print(target.rect, target.rect.move(0, 0))
        #return target.rect.move(0, 0)
        #print('cam state', self.state)
        return target.rect.move(-self.state.left, -self.state.top)
