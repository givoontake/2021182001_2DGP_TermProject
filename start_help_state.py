from pico2d import *
import game_framework
import logo_state
import start_manual_state

class Help:
    def __init__(self):
        self.image = load_image('Help.png')

    def draw(self):
        self.image.draw(400, 300)


running = True
help = None

def enter():
    global help, running
    help = Help()
    running = True
    pass

def exit():
    global help
    del help
    pass

def update():
    pass
    # delay(0.05)
    # logo_time +=0.05
    # if logo_time > 1.0:
    #     game_framework.change_state(play_state)
    # pass

def draw():
    global help
    clear_canvas()
    help.draw()
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(logo_state)
            elif event.key == SDLK_RETURN:
                game_framework.change_state(start_manual_state)





