import random
from pico2d import *
import gfw
import gobj
import time
#1 767 987 67 287
list=[{0,0},{0,0},{0,0},{0,0},{0,0},{0,0},{0,0},{0,0},{0,0}]
aa=0
i=0
j=0
skil1=[0,0,0,0,0,0,0,0,0]

class Player:
        WIDTH, HEIGHT = 200, 200

        def __init__(self, index, pos, theme='.'):
            fps = random.randrange(3,5)
            fps2 = random.randrange(3, 6)
            self.bg = gobj.AnimObject(theme + '/magician.png', pos,fps)
            self.fg = gobj.AnimObject2(theme + '/magicianskil.png', pos,fps)
            self.image = self.bg
            self.index = index

        def draw(self):
            self.image.draw()

        def update(self):
            global aa
            if self.image == self.fg:
                aa += gfw.delta_time
                print(aa)
                if aa>1:
                    self.image = self.bg
                    aa=0

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
            hw = Player.WIDTH // 6
            hh = Player.HEIGHT // 6
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

