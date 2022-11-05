import pico2d
import logo_state
import play_state

pico2d.open_canvas()
states = [logo_state, play_state] # 모듈을 변수로 취급

# game main loop code
for state in states:
    state.enter()
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
        pico2d.delay(0.05)
    state.exit()

exit()
# finalization code
pico2d.close_canvas()
