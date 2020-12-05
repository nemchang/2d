import random
from pico2d import *
import gfw
import gobj
import skil
import time
import pattern

#1 767 987 67 287
list=[{0,0},{0,0},{0,0},{0,0},{0,0},{0,0},{0,0},{0,0},{0,0}]
aa=0
i=0
j=0
skil1=[0,0,0,0,0,0,0,0,0]
life = 1000
dead=0
class Enemy:
        SIZE = 96
        WIDTH, HEIGHT = 200, 200

        def __init__(self, index, pos, theme='.'):
            fps = random.randrange(3,5)
            fps2 = random.randrange(3, 6)

            self.x,self.y=pos
            self.bg = gobj.AnimObject3(theme + '/enemyn1.png', pos,fps)
            self.fg =  gobj.ImageObject(theme + '/enemyn2.png', pos)
            self.bbg = gobj.AnimObject3(theme + '/enemyn3.png', pos, fps)



            self.image = self.bg



            self.index = index

        def draw(self):
            self.image.draw()

        def update(self):
            global aa,life,dead

            if life<500:
                self.image = self.bbg



            if skil.active == True or pattern.active == True:
                self.image = self.fg

            if self.image == self.fg:
                aa += gfw.delta_time



                if aa > 1.2:
                    self.image = self.bg
                    aa = 0
                    if life < 500:
                        life -= (10 + pattern.skildmg)/2
                    else:
                        life -= 10+pattern.skildmg
                    pattern.skildmg=0
                    skil.active = 0
                    if life == 0:
                        self.image = self.fg
                        dead=1




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
            hw = Enemy.WIDTH // 6
            hh = Enemy.HEIGHT // 6
            x, y = self.bg.pos
            # print(x,y)


            return x - hw, y - hh, x + hw, y + hh

        def remove(self):
            gfw.world.remove(self)




    # def __del__(self):
    #     print('Del Card:', self)

