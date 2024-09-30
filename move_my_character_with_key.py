from pico2d import *

open_canvas()

ground = load_image('TUK_GROUND.png')
character = load_image('movingCat.jpg')
running=True

x=800//2
frame=0
dir=0
def right_event():
    global dir
    dir+=1
    draw_right()
def left_event():
    global dir
    dir -= 1
    draw_left()
def up_event():
    pass
def down_event():
    pass
def idle_event():
    pass
def escape_event():
    global running
    running=False

def handle_events():
    global dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            escape_event()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
               right_event()
            elif event.key == SDLK_LEFT:
                left_event()
            elif event.key == SDLK_ESCAPE:
                escape_event()
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                left_event()
            elif event.key == SDLK_LEFT:
                right_event()

def draw_right():
    clear_canvas()
    ground.draw(400, 300, 800, 600)
    global frame
    global x
    x += dir * 5
    character.clip_draw(frame * 160, 4 + 640, 160, 160, x, 10, 100, 100)

def draw_left():
    clear_canvas()
    ground.draw(400, 300, 800, 600)
    update_canvas()
    global frame
    global x
    x += dir * 5
    character.clip_draw(frame * 160, 4 + 320, 160, 160, x, 10, 100, 100)



while running:
    clear_canvas()
    ground.draw(400,300,800,600)
    update_canvas()
    handle_events()
    frame = (dir + 1) % 8
    x+=dir*5
    delay(0.05)

close_canvas()