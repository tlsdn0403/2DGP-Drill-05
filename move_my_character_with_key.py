from pico2d import *

open_canvas()

ground = load_image('TUK_GROUND.png')
character = load_image('movingCat.png')
running=True
y=600//2
x=800//2
frame=0
dirx=0
diry=0
def right_event():
    global dirx
    dirx+=1
    draw_right()
def left_event():
    global dirx
    dirx -= 1
    draw_left()
def up_event():
    global diry
    diry+=1
    draw_up()
    pass
def down_event():
    global diry
    diry-=1
    draw_down()
    pass
def idle_event():
    pass
def escape_event():
    global running
    running=False

def handle_events():
    global dirx
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
            elif event.key==SDLK_UP:
                up_event()
            elif event.key==SDLK_DOWN:
                down_event()
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                left_event()
            elif event.key == SDLK_LEFT:
                right_event()
            elif event.key==SDLK_UP:
                down_event()
            elif event.key==SDLK_DOWN:
                up_event()

def draw_right():

    global frame
    global x
    x += dirx * 5
    frame = (frame + 1) % 4
    character.clip_draw(frame * 160, 4 + 640, 160, 160, x, y, 100, 100)

def draw_left():

    global frame
    global x
    x += dirx * 5
    frame = (frame + 1) % 4
    character.clip_draw(frame * 160, 4 + 320, 160, 160, x, y, 100, 100)
def draw_idle():
    global frame
    global x
    frame = (frame + 1) % 4
    character.clip_draw(frame * 160, 4 , 160, 160, x, y, 100, 100)
def draw_up():
    global frame
    global y
    y += diry * 5
    frame = (frame + 1) % 4
    character.clip_draw(frame * 160, 4 + 480, 160, 160, x, y, 100, 100)
def draw_down():
    global frame
    global y
    y += diry * 5
    frame = (frame + 1) % 4
    character.clip_draw(frame * 160, 4 + 800, 160, 160, x, y, 100, 100)


while running:
    clear_canvas()
    ground.draw(400, 300, 800, 600)

    # 방향에 따라 다른 그리기 함수를 호출
    if dirx > 0:
        draw_right()
    elif dirx < 0:
        draw_left()
    elif diry>0:
        draw_up()
    elif diry<0:
        draw_down()
    else:
        draw_idle()

    update_canvas()
    handle_events()
    delay(0.05)

close_canvas()