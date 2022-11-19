from pico2d import *
import game_framework
import pause_state

class Manual:
    def __init__(self):
        self.image = load_image('manual.png')

    def draw(self):
        self.image.draw(400, 300)


running = True
manual = None

def enter():
    global manual, running
    manual = Manual()
    running = True
    pass

def exit():
    global manual
    del manual
    pass

def update():
    pass
    # delay(0.05)
    # logo_time +=0.05
    # if logo_time > 1.0:
    #     game_framework.change_state(play_state)
    # pass

def draw():
    global manual
    clear_canvas()
    manual.draw()
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.pop_state()
                game_framework.push_state(pause_state)





