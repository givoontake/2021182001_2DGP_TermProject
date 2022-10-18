from pico2d import *

running = True
run_screen = True
run_game = None
run_shop = None

s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0

x = 400
frame = 0
xdir = 0

def handle_events():
    global run_screen, run_game, run_shop, LV, s1, s2, s3, s4, s5, xdir

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
            elif event.key == SDLK_d:
                xdir += 1
            elif event.key == SDLK_a:
                xdir -= 1
            elif event.key == SDLK_1 and run_shop == True:
                if s1 < 4:
                    s1 += 1
            elif event.key == SDLK_2 and run_shop == True:
                if s2 < 4:
                    s2 += 1
            elif event.key == SDLK_3 and run_shop == True:
                if s3 < 4:
                    s3 += 1
            elif event.key == SDLK_4 and run_shop == True:
                if s4 < 1:
                    s4 += 1
            elif event.key == SDLK_5 and run_shop == True:
                if s5 < 1:
                    s5 += 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_d:
                    xdir -= 1
            elif event.key == SDLK_a:
                    xdir += 1
def handle_events_character():
    global run_game, xdir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_d:
                xdir += 1
            elif event.key == SDLK_a:
                xdir -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_d:
                xdir -= 1
            elif event.key == SDLK_a:
                xdir += 1

def mainscreen():
    global screen
    clear_canvas()
    screen.draw(400, 300)
    update_canvas()
    handle_events()


def upgrade_shop():
    global shop, LV, s1, s2, s3, s4, s5
    clear_canvas()
    shop.draw(430, 270)
    if s1 > -1:
        LV.clip_draw(31 * s1, 0, 35, 31, 725, 407)
    if s2 > -1:
        LV.clip_draw(31 * s2, 0, 35, 31, 725, 320)
    if s3 > -1:
        LV.clip_draw(31 * s3, 0, 35, 31, 725, 233)
    if s4 > 0:
        LV.clip_draw(0, 0, 35, 31, 725, 146)
    if s5 > 0:
        LV.clip_draw(0, 0, 35, 31, 725, 59)
    update_canvas()
    handle_events()


def game():
    global character, forest, x, xdir, frame
    clear_canvas()
    forest.draw(400, 350)
    character.clip_draw(27 + frame * 42, 300, 42, 60, x, 90)
    update_canvas()
    handle_events()
    # handle_events_character()
    frame = (frame + 1) % 4
    x += xdir * 5
    delay(0.1)


open_canvas()

character = load_image('player.png')
forest = load_image('forest.png')
screen = load_image('mainscreen.png')
shop = load_image('shop.png')
LV = load_image('LV.png')

while running:
    if run_screen == True:
        mainscreen()
    elif run_game == True:
        game()
    elif run_shop == True:
        upgrade_shop()


close_canvas()