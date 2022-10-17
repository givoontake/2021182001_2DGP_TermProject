
from pico2d import *
import game_framework
import gameplay

image = None
forest = None

def handle_events():
    global running, forest
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_b:
                running = False
                game_framework.change_state(gameplay)
                # clear_canvas()
                # forest.draw(400, 350)
def enter():
    global image, forest
    image = load_image('mainscreen.png')
    forest = load_image('forest.png')
def exit():
    global image
    del image
    pass

def update():
    pass

def draw():
    global image
    clear_canvas()
    # gameplay.draw_world()
    # image.draw(400, 300)
    image.draw_now(400, 300)
    update_canvas()
    pass

def pause():
    pass

def resume():
    pass

running = True
open_canvas()
while running:
    clear_canvas()
    enter()
    draw()
    handle_events()




