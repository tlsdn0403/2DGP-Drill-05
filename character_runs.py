from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')

# fill here
frame=0
for x in range(0,800,10):
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame*100,0,100,100,x,130,200,200)
    update_canvas()
    frame=(frame+1)%8
    delay(0.05)

close_canvas()

