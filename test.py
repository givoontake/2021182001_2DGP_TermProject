from pico2d import *

open_canvas()

image = load_image('shop.png')
image2 = load_image('LV.png')

def test():
    global image, image2
    clear_canvas()
    image.draw(430, 270)
    # for i in range(10):
    #     image2.clip_draw(31*i, 0, 35, 31, 725, 320)
    #     update_canvas()
    #     delay(1)
    image2.clip_draw(31, 0, 35, 31, 725, 233)
    update_canvas()
# 407, 320, 233

test()
delay(3)

close_canvas()