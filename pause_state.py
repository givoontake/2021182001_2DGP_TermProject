from pico2d import *
import game_framework
import play_state
import help_state
import manual_state
# image = None
# logo_time = 0.0

class Pause:
    def __init__(self):
        self.image = load_image('pause.png')

    def draw(self):
        self.image.draw(400, 300)


running = True
pause = None

def enter():
    global pause, running
    pause = Pause()
    running = True
    pass

def exit():
    global pause
    del pause
    pass

def update():
    pass
    # delay(0.05)
    # logo_time +=0.05
    # if logo_time > 1.0:
    #     game_framework.change_state(play_state)
    # pass

def draw():
    global pause
    clear_canvas()
    pause.draw()
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
            if event.key == SDLK_1:
                game_framework.pop_state()
                game_framework.push_state(help_state)
            if event.key == SDLK_2:
                game_framework.pop_state()
                game_framework.push_state(manual_state)





