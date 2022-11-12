from pico2d import *
import game_framework
import play_state

class Shop:
    def __init__(self):
        self.image = load_image('shop.png')
        self.LV = load_image('LV.png')
        self.s1, self.s2, self.s3, self.s4, self.s5 = 0, 0, 0, 0, 0

    def draw(self):
        self.image.draw(430, 270)
        if self.s1 >= 0:
            self.LV.clip_draw(31 * self.s1, 0, 35, 31, 725, 407)
        if self.s2 >= 0:
            self.LV.clip_draw(31 * self.s2, 0, 35, 31, 725, 320)
        if self.s3 >= 0:
            self.LV.clip_draw(31 * self.s3, 0, 35, 31, 725, 233)
        if self.s4 > 0:
            self.LV.clip_draw(0, 0, 35, 31, 725, 146)
        if self.s5 > 0:
            self.LV.clip_draw(0, 0, 35, 31, 725, 59)


shop = None

def enter():
    global shop
    shop = Shop()
    running = True
    pass

def exit():
    global shop
    del shop
    pass

def update():
    pass

def draw():
    clear_canvas()
    shop.draw()
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_1:
                    shop.s1 += 1
                case pico2d.SDLK_2:
                    shop.s2 += 1
                case pico2d.SDLK_3:
                    shop.s3 += 1
                case pico2d.SDLK_4:
                    shop.s4 += 1
                case pico2d.SDLK_5:
                    shop.s5 += 1






def test_self(): # 자기 자신 실행
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()



