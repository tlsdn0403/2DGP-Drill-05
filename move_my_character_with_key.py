from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')
running=True

def handle_events():
    global running
    global dir
    events = get_events()
    for event in events:
        if event.type == SDL_Quit:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key==SDLK_RIGHT:
                character.clip_draw(frame * 100, 0, 100, 100, x, 130, 200, 200)
                dir+=1
            elif event.key==SDLK_LEFT:
                character.clip_composite_draw(frame * 100, 0, 100, 100, 0, 'h', x, 130, 200, 200)
                dir-=1
            elif event.key==SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1



def character_run_right():
    frame = 0
    for x in range(0, 800, 10):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, 130, 200, 200)
        update_canvas()
        handle_events()
        if not running:
            break
        frame = (frame + 1) % 8
        delay(0.05)


def character_run_left():
    frame = 0
    for x in range(800, 0, -10):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_composite_draw(frame * 100, 0, 100, 100, 0, 'h', x, 130, 200, 200)
        update_canvas()
        if not running:
            break
        frame = (frame + 1) % 8
        delay(0.05)

running=True
x=800//2
frame=0
dir=0
while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 130, 200, 200)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x+=dir*5
    delay(0.05)

close_canvas()