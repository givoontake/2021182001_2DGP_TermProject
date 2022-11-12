from pico2d import *
import game_framework
import play_state
# image = None
# logo_time = 0.0

class Mainscreen:
    def __init__(self):
        self.image = load_image('mainscreen.png')

    def draw(self):
        self.image.draw(400, 300)


running = True
xera = None

def enter():
    global xera, running
    xera = Mainscreen()
    running = True
    pass

def exit():
    global xera
    del xera
    pass

def update():
    pass
    # delay(0.05)
    # logo_time +=0.05
    # if logo_time > 1.0:
    #     game_framework.change_state(play_state)
    # pass

def draw():
    global xera
    clear_canvas()
    xera.draw()
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RETURN:
                game_framework.change_state(play_state)





