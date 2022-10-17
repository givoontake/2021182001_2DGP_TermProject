from pico2d import *

running = True
run_screen = True
run_game = None
run_shop = None

screen = None
forest = None
shop = None
LV = None

s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0

def handle_events():
    global run_screen, run_game, run_shop, LV, s1, s2, s3, s4, s5
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                if run_game == True:
                    run_screen = True
                    run_game = False
                elif run_shop == True:
                    run_shop = False
                    run_game = True
            elif event.key == SDLK_p:
                if run_screen == True:
                    run_screen = False
                    run_game = True
                elif run_game == True:
                    run_game = False
                    run_shop = True
            elif event.key == SDLK_1:
                if run_shop == True and s1 < 6:
                    s1 += 1
                    LV = load_image('LV.png')
                    LV.clip_draw(31 * s1, 0, 35, 31, 725, 407)
                    update_canvas()

def mainscreen():
    global screen
    clear_canvas()
    screen = load_image('mainscreen.png')
    screen.draw(400, 300)
    update_canvas()
    handle_events()


def game():
    global forest
    clear_canvas()
    forest = load_image('forest.png')
    forest.draw(400, 350)
    update_canvas()
    handle_events()


def upgrade_shop():
    global shop
    clear_canvas()
    shop = load_image('shop.png')
    shop.draw(430, 270)
    update_canvas()
    handle_events()


open_canvas()

while running:
    if run_screen == True:
        mainscreen()
    elif run_game == True:
        game()
    elif run_shop == True:
        upgrade_shop()


close_canvas()