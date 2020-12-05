import random
from pico2d import *
import gfw
import gobj
import pattern

list=[{0,0},{0,0},{0,0},{0,0},{0,0},{0,0},{0,0},{0,0},{0,0}]

i=0
j=0
active=0
skil1=[0,0,0,0,0,0,0,0,0]

class Skileffect:
    WIDTH,HEIGHT = 200,200
    def __init__(self, index, pos, theme='.'):
        self.image = gobj.ImageObject(theme + '/skil1.png', pos)
        if pattern.skil==9:
            self.image = gobj.ImageObject(theme + '/9.png', pos)

        elif pattern.skil==3:
            self.image = gobj.ImageObject(theme + '/3.png', pos)

        elif pattern.skil==2:
            self.image = gobj.ImageObject(theme + '/2.png', pos)

        elif pattern.skil==5:
            self.image = gobj.ImageObject(theme + '/5.png', pos)


        else:
            self.image = gobj.ImageObject(theme + '/skil1.png', pos)
        fps = random.randrange(20, 30)


        self.index = index
    def draw(self):
        self.image.draw()
    def update(self):
        pass
    def handle_event(self, e):
        global active
        if e.type == SDL_MOUSEBUTTONDOWN and e.button == SDL_BUTTON_LEFT:
            pos = gobj.mouse_xy(e)
            if gobj.pt_in_rect(pos, self.get_bb()):
                self.toggle()
                active=True
                print("111")
                return True

        return False
    def skilactive(self):
        if self.image == self.fg:
            return True


    def toggle(self):
        self.image = self.bg if self.image == self.fg else self.fg
    def get_bb(self):
        hw = Skileffect.WIDTH // 6
        hh = Skileffect.HEIGHT // 6
        x,y = self.bg.pos
        #print(x,y)




        return x - hw, y - hh, x + hw, y + hh

    def remove(self):
        gfw.world.remove(self)


class Skileffect2:
    WIDTH,HEIGHT = 200,200
    def __init__(self, index, pos, theme='.'):
        self.bg = gobj.ImageObject(theme + '/skilicon2.png', pos)
        fps = random.randrange(20, 30)
        self.fg = gobj.ImageObject(theme + '/skilicon2.png', pos)
        self.image = self.bg
        self.index = index
    def draw(self):
        self.image.draw()
    def update(self):
        pass
    def handle_event(self, e):
        global active
        if e.type == SDL_MOUSEBUTTONDOWN and e.button == SDL_BUTTON_LEFT:
            pos = gobj.mouse_xy(e)
            if gobj.pt_in_rect(pos, self.get_bb()):
                self.toggle()
                active=True
                print("111")
                return True

        return False
    def skilactive(self):
        if self.image == self.fg:
            return True


    def toggle(self):
        self.image = self.bg if self.image == self.fg else self.fg
    def get_bb(self):
        hw = Skileffect.WIDTH // 6
        hh = Skileffect.HEIGHT // 6
        x,y = self.bg.pos
        #print(x,y)




        return x - hw, y - hh, x + hw, y + hh

    def remove(self):
        gfw.world.remove(self)