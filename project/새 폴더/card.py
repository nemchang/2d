import random
from pico2d import *
import gfw
import gobj

#1 767 987 67 287
list=[{0,0},{0,0},{0,0},{0,0},{0,0},{0,0},{0,0},{0,0},{0,0}]

i=0
j=0
skil1=[0,0,0,0,0,0,0,0,0]

class Card:
        WIDTH, HEIGHT = 200, 200

        def __init__(self, index, pos, theme='.'):
            self.bg = gobj.ImageObject(theme + '/f_01.png', pos)
            fps = random.randrange(20, 30)
            self.fg = gobj.ImageObject(theme + '/f_02.png', pos)
            self.image = self.bg
            self.index = index

        def draw(self):
            self.image.draw()

        def update(self):
            pass

        def handle_event(self, e):
            if e.type == SDL_MOUSEBUTTONDOWN and e.button == SDL_BUTTON_LEFT:
                pos = gobj.mouse_xy(e)
                if gobj.pt_in_rect(pos, self.get_bb()):
                    self.toggle()
                    if list[i] == {0, 0}:
                        list[i] = 1
                        print(i)

                    return True

            return False

        def toggle(self):
            self.image = self.bg if self.image == self.fg else self.fg

        def get_bb(self):
            hw = Card.WIDTH // 6
            hh = Card.HEIGHT // 6
            x, y = self.bg.pos
            # print(x,y)
            for i in range(9):
                if skil1[i] == 0:
                    if x < 1050 and 0 < y < 350:
                        skil1[i] = 1
                        break

            return x - hw, y - hh, x + hw, y + hh

        def remove(self):
            gfw.world.remove(self)


    # def __del__(self):
    #     print('Del Card:', self)

