from pico2d import *
open_canvas()
import os
os.chdir('C:/Users/cksnd/Desktop/2학년 2학기/2d 겜프/새 폴더')
image=load_image('run_animation.png')
gra=load_image('grass.png')


for x in range (0,800,2):
	clear_canvas()
	gra.draw(400,30)
	
	image.clip_draw(0,0,100,100,x,80)
	update_canvas()
	delay(0.01)
	

delay(5)
close_canvus()
