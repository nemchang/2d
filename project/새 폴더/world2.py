import random
from pico2d import *
import gfw
import gobj
from pattern import Pattern
import pattern
from skil import Skil
import skil
from skileffect import Skileffect
from skileffect import Skileffect2
from player import Player
from enemy2 import Enemy
import enemy2
import highscore


SCORE_HEIGHT = 30
PADDING = 10
canvas_width = PADDING + (Pattern.WIDTH + PADDING) * 3
canvas_height = PADDING + (Pattern.WIDTH + PADDING) * 4 + SCORE_HEIGHT
aa=0
Ehp=100
skilefx=500
skilefy=450
TIME=100
score=0
print("Canvas Size:", (canvas_width, canvas_height))

score_x = canvas_width/2 - 60
score_y = canvas_height - SCORE_HEIGHT * 8 // 10
SCORE_TEXT_COLOR = (255, 255, 255)

start_x = 270 + Pattern.WIDTH // 2
start_y = Pattern.HEIGHT // 2 + 200

theme = 'lv1'

def enter():

    enemy2.dead=0




    gfw.world.init(['bg', 'card','state','ui'])

    gfw.world.remove(highscore)
    center = get_canvas_width()//2, get_canvas_height()//1.4
    center2 = get_canvas_width() // 2, 250
    hp=150,700
    gfw.world.add(gfw.layer.bg, gobj.ImageObject(theme + '/black.png', center2))
    gfw.world.add(gfw.layer.bg, gobj.ImageObject(theme + '/bg.png', center))
    #gfw.world.add(gfw.layer.bg, gobj.ImageObject(theme + '/gaugefg.png', hp))

    x,y = start_x, start_y
    idxs = [n + 1 for n in range(9)]
    #print('before:', idxs)
    #random.shuffle(idxs)
    #print('after: ', idxs)


    for i in range(0, 9, +3):
        print(idxs[i:i+3])
    for i in idxs:
        c = Pattern(i, (x, y), theme)
        gfw.world.add(gfw.layer.card, c)
        x += Pattern.WIDTH + PADDING - 100
        if x > get_canvas_width():
            x = start_x
            y -= Pattern.HEIGHT + PADDING - 100

    icon = Skil(1, (150, 200), theme)
    gfw.world.add(gfw.layer.card, icon)



    pla=Player(1, (550, 450), theme)



    gfw.world.add(gfw.layer.card, pla)
    ene = Enemy(1, (150, 450), theme)
    gfw.world.add(gfw.layer.card, ene)





    global last_card
    last_card = None


    global TIME, font
    TIME = 10000
    font = gfw.font.load(gobj.res('ENCR10B.TTF'), 20)
    highscore.load()

    global bg_music, flip_wav





    bg_music = load_music(gobj.res('bg3.mp3'))
    bg_music.set_volume(60)
    flip_wav = load_wav(gobj.res('pipe.wav'))
    bg_music.repeat_play()




def update():


    global lose_image,win_image,TIME,Ehp
    count=0
    center=(320,640)
    Ehp = enemy2.life








    global aa,skilefx,skilefy,ene

    if Ehp <= 0:
        gfw.world.add(gfw.layer.state, gobj.ImageObject(theme + '/win.png', (320,800)))
        gfw.world.add(gfw.layer.ui, highscore)



        return



    gfw.world.update()

    if skil.active == True or pattern.active == True:
        aa += gfw.delta_time

        skilx = Skileffect(1, (skilefx, skilefy), theme)
        gfw.world.add(gfw.layer.card, skilx)
        gfw.world.remove(skilx)

        if aa >= 1.2:
            aa = 0
            skilefx = 500
            skil.active = 0
            pattern.active = 0
            pattern.skil = 0

        skilefx = skilefx - aa * 7
    else:
        skilefx = 500
        aa = 0
















    if gfw.world.count_at(gfw.layer.card) > 0:
        if TIME <= 1:
            return
        else:
            TIME -= gfw.delta_time*30

        # print(gfw.world.count_at(gfw.layer.card), score, gfw.delta_time, gfw.frame_interval)
    if enemy2.dead==1:
        highscore.add(TIME)

def draw():
    gfw.world.draw()
    global Ehp,score


    global TIME, font

    if Ehp<=0:
        font.draw(100, 550, "HP: %.1f" % Ehp, SCORE_TEXT_COLOR)
        return



    else:
        font.draw(100, 550, "HP: %.1f" % Ehp, SCORE_TEXT_COLOR)
        font.draw(score_x, score_y, "SCORE: %.1f" % TIME, SCORE_TEXT_COLOR)




def handle_event(e):
    if e.type == SDL_QUIT:
        return gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            return gfw.pop()

    global last_card, flip_wav
    for card in gfw.world.objects_at(gfw.layer.card):
        if card == last_card:
            continue
        if card.handle_event(e):
            flip_wav.play()
            if last_card is None:
                #last_card = card
                break
            if last_card.index == card.index:
                #last_card.remove()
                #card.remove()
                break
            last_card.toggle()
            last_card = card

def exit():
    global bg_music
    bg_music.stop()
    del bg_music

if __name__ == '__main__':
    gfw.run_main()
