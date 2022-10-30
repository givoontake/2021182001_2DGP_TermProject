from pico2d import *

def handle_events_character():
    global run_game, xdir
    global running
    global dir
    global fire

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_d:
                xdir += 1
            elif event.key == SDLK_a:
                xdir -= 1
            elif event.key == SDLK_k:
                fire = True
        elif event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_d:
                xdir -= 1
            elif event.key == SDLK_a:
                xdir += 1
            elif event.key == SDLK_k:
                fire = False
def test():
    global image
    clear_canvas()
    image.draw(400, 350)


def player():
    while running:
        global cha, image, x, xdir, frame
        clear_canvas()
        image.draw(400, 350)
        if(fire == False):
            cha.clip_draw(40+frame * 62, 450, 62, 90, x, 90)
        else:
            cha.clip_draw(40, 450, 62, 90, x, 90)
        update_canvas()
        handle_events_character()
        frame = (frame + 1) % 4
        x += xdir * 10
        delay(0.1)

fire = False
running = True
x = 400
frame = 0
xdir = 0

open_canvas()

image = load_image('forest.png')
cha = load_image('player.png')

player()
delay(3)

close_canvas()