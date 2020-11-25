import random
from pico2d import *
import gfw
import gobj

#1 767 987 67 287
list=[0,0,0,0,0,0,0,0,0]

i=0
j=0
skil1=[0,0,0,0,0,0,0,0,0]

class pattern:
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
                x, y = self.bg.pos
                print(x, y)
                hw = pattern.WIDTH // 6
                hh = pattern.HEIGHT // 6





                if gobj.pt_in_rect(pos, self.get_bb()):
                    self.toggle()
                    if 370 - hw < x < 370 + hw and 300-hh<y<300+hh:
                        list[0] = 1
                    elif 480 - hw < x < 480 + hw and 300-hh<y<300+hh:
                        list[1] = 1
                    elif 590 - hw < x < 590 + hw and 300-hh<y<300+hh:
                        list[2] = 1
                    elif 370 - hw < x < 370 + hw and 190-hh<y<190+hh:
                        list[3] = 1
                    elif 480 - hw < x < 480 + hw and 190-hh<y<190+hh:
                        list[4] = 1
                    elif 590 - hw < x < 590 + hw and 190-hh<y<190+hh:
                        list[5] = 1
                    elif 370 - hw < x < 370 + hw and 80-hh<y<80+hh:
                        list[6] = 1
                    elif 480 - hw < x < 480 + hw and 80-hh<y<80+hh:
                        list[7] = 1
                    elif 590 - hw < x < 590 + hw and 80-hh<y<80+hh:
                        list[8] = 1




                    print(list)
                    return True

            return False

        def toggle(self):
            self.image = self.bg if self.image == self.fg else self.fg

        def get_bb(self):
            hw = pattern.WIDTH // 6
            hh = pattern.HEIGHT // 6
            x, y = self.bg.pos


            return x - hw, y - hh, x + hw, y + hh

        def remove(self):
            gfw.world.remove(self)


    # def __del__(self):
    #     print('Del Card:', self)

