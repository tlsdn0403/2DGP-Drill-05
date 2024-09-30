from pico2d import *

open_canvas()

ground = load_image('TUK_GROUND.png')
character = load_image('movingCat.jpg')
running=True
def right_event():
    pass
def left_event():
    pass
def up_event():
    pass
def down_event():
    pass
def idle_event():
    pass
def escaspe_event():
    pass

def handle_events():
    global running
    global dir
    events = get_events()

def draw_right():
    character.clip_draw(frame * 160, 4 + 640, 160, 160, x, 10, 100, 100)



running=True
x=800//2
frame=0
dir=0
while running:
    clear_canvas()
    ground.draw(400,300,800,600)
    draw_right()
    update_canvas()
    handle_events()
    frame = (dir + 1) % 8
    x+=dir*5
    delay(0.05)

close_canvas()