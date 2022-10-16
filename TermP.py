import pico2d

import game_framework
import mainscreen
import gameplay

pico2d.open_canvas()
game_framework.run(mainscreen)
game_framework.run(gameplay)
pico2d.close_canvas()

