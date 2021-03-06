import random
from pico2d import *
import gfw
import gobj
import skil
import pattern
import time
#1 767 987 67 287
list=[{0,0},{0,0},{0,0},{0,0},{0,0},{0,0},{0,0},{0,0},{0,0}]
aa=0
i=0
j=0
skil1=[0,0,0,0,0,0,0,0,0]
hp=100
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

            if skil.active==True or pattern.active==True:
                self.image = self.fg

            if self.image == self.fg:
                aa += gfw.delta_time
                #print(aa)
                if aa>1.2:
                    self.image = self.bg
                    aa=0
                    skil.active=0

        def handle_event(self, e):
            if e.type == SDL_MOUSEBUTTONDOWN and e.button == SDL_BUTTON_LEFT:
                pos = gobj.mouse_xy(e)
                if gobj.pt_in_rect(pos, self.get_bb()):
                    self.toggle()


                    return True

            return False

        def toggle(self):
            self.image = self.bg if self.image == self.fg else self.fg



        def get_bb(self):
            hw = Player.WIDTH // 6
            hh = Player.HEIGHT // 6
            x, y = self.bg.pos
            # print(x,y)


            return x - hw, y - hh, x + hw, y + hh

        def remove(self):
            gfw.world.remove(self)


    # def __del__(self):
    #     print('Del Card:', self)

