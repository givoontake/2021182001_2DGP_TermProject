from pico2d import *
import game_framework

open_canvas()

mainscreen = load_image('mainscreen.png')
forest = load_image('forest.png')
shop = load_image('shop.png')

running = True
run_main = True
run_game = None
run_shop = None

def handle_events():
    global run_main, run_game, run_shop
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                if run_game == True:
                    run_main = False
                    run_game = True
                elif run_shop == True:
                    run_shop = False
                    run_main = True
            if event.key == SDLK_p:
                if run_main == True:
                    run_main = False
                    run_game = True
                elif run_game == True:
                    run_game = False
                    run_shop = True




def mainscreen():
    global run_main
    while run_main == True:
        clear_canvas()
        mainscreen.draw(400, 300)
        update_canvas()
        handle_events()
        if(run_main == False):
            break

def game():
    global run_game
    while run_game == True:
        clear_canvas()
        forest.draw(400, 350)
        update_canvas()
        handle_events()
        if (run_game == False):
            break


def shop():
    global run_shop
    while run_shop == True:
        clear_canvas()
        forest.draw_now(400, 300)
        update_canvas()
        handle_events()
        if (run_shop == False):
            break

while running:
    if run_main == True:
        mainscreen()
    elif run_game == True:
        game()
    elif run_shop == True:
        shop()

close_canvas()