from pico2d import *
import game_framework
import item_state

class Map:
    def __init__(self):
        self.image = load_image('forest.png')
        self.image2 = load_image('black.png')
        self.background_music = load_music('background.mp3')
        self.background_music.set_volume(25)
        self.background_music.repeat_play()

    def draw(self):
        self.image2.draw(400, 350)
        self.image.draw(400, 350)

class Player:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.frame2 = 0
        self.div = 0
        self.dir = 0
        self.non_zero_dir = 1
        self.fire = False
        self.image = load_image('Player.png')
        self.item = None

    def update(self):
        self.div += 1
        if(self.div > 90):
            self.div = 0
        self.frame = self.div // 30
        # self.frame = (self.frame + 1) % 4
        self.frame2 = (self.frame + 1) % 2
        self.x += self.dir * 0.5
        if self.x > 750:
            self.x = 750
        elif self.x < 50:
            self.x = 50

    def draw(self):
        if self.non_zero_dir > 0:
            if hunter.fire == False:
                self.image.clip_draw(40 + self.frame * 62, 450, 62, 90, self.x, 90)
            else:
                self.image.clip_draw(40, 320, 62, 90, self.x, 90)
                self.image.clip_draw(320 + 60 * self.frame2, 225, 40, 80, self.x + 40, 90)
        elif self.non_zero_dir < 0:
            if hunter.fire == False:
                self.image.clip_composite_draw(40 + self.frame * 62, 450, 62, 90, 0, 'h', self.x, 90, 62, 90)
            else:
                self.image.clip_composite_draw(40, 320, 62, 90, 0, 'h', self.x, 90, 62, 90)
                self.image.clip_composite_draw(320 + 60 * self.frame2, 225, 40, 80, 0, 'h', self.x - 40, 90, 40, 80)



class Bullet:
    def __init__(self):
        self.image = load_image('Player.png')
        self.x = hunter.x
        self.y = hunter.y
        self.fire_sound = load_wav('fire_sound.wav')
        self.fire_sound.set_volume(25)
        self.sound = True
        self.bullet_dir = hunter.non_zero_dir

    def update(self):
        if self.bullet_dir > 0:
            self.x += 3
        elif self.bullet_dir < 0:
            self.x -= 3

    def draw(self):
        if self.bullet_dir > 0:
            self.image.clip_draw(320 + 60 * 2, 225, 20, 80, self.x + 40, 90)
        elif self.bullet_dir < 0:
            self.image.clip_draw(320 + 60 * 2, 225, 20, 80, self.x - 40, 90)


def handle_events():
    global bullets
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_b:
                game_framework.push_state(item_state)
            elif event.key == SDLK_d:
                hunter.dir = 1
                hunter.non_zero_dir = 1
            elif event.key == SDLK_a:
                hunter.dir = -1
                hunter.non_zero_dir = -1
            elif event.key == SDLK_k:
                bullets.append(Bullet())
                hunter.dir = 0
                hunter.fire = True

        elif event.type == SDL_KEYUP: # 키를 동시에 누를 경우 생기는 문제는 여기서 처리를 해줘야 하나..
            hunter.dir = 0
            # if event.key == SDLK_d:
            #     boy.x -= 5
            # elif event.key == SDLK_a:
            #     boy.x += 5
            if event.key == SDLK_k:
                hunter.fire = False


# 게임 초기화 : 객체들을 생성
hunter = None
forest = None
bullet = None
bullets = []

running = True

def bullet_draw():
    for bullet in bullets:
        bullet.draw()
        if bullet.sound == True: # 처음 총알 객체 생성 때만 소리를 출력
            bullet.fire_sound.play()
            bullet.sound = False

def bullet_del():
    for bullet in bullets:
        if bullet.x > 800 or bullet.x < 0:
            bullets.remove(bullet)

def bullet_update():
    for bullet in bullets:
        bullet.update()

def enter():
    global hunter, forest, bullet, running
    hunter = Player()
    forest = Map()
    bullet = Bullet()
    running = True


# 게임 종료 - 객체를 소멸
def exit():
    global hunter, forest
    del hunter
    del forest

    delay(0.1)


# 게임 월드에 객체를 업데이트 - 게임 로직
def update():
    hunter.update()
    bullet_update()
    bullet_del()

# 게임 월드 랜더링
def draw_world():
    forest.draw()
    hunter.draw()
    bullet_draw()
    delay(0.001)

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass


def test_self(): # 자기 자신 실행
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()

if __name__ == '__main__':  # 단독 실행이면
    test_self()




