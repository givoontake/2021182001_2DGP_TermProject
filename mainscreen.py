
from pico2d import *
import game_framework
import gameplay

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE:
                running = False
                game_framework.change_state(gameplay)

running = True
open_canvas()
while running:
    clear_canvas()
    mainscreen = load_image('mainscreen.png')
    mainscreen.draw_now(400, 300)
    update_canvas()
    handle_events()


