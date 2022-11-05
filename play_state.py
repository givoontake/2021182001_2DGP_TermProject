from pico2d import *
# import winsound
import game_framework
import item_state

class Map:
    def __init__(self):
        self.image = load_image('forest.png')
        self.image2 = load_image('black.png')

    def draw(self):
        self.image2.draw(400, 350)
        self.image.draw(400, 350)

class Player:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.frame2 = 0
        self.dir = 0
        self.fire = False
        self.image = load_image('Player.png')
        self.item = None

    def update(self):
        self.frame = (self.frame + 1) % 4
        self.frame2 = (self.frame + 1) % 2
        if hunter.fire == True:
            self.bul += 1
        else:
            self.bul = 1
        self.x += self.dir * 15
        if self.x > 750:
            self.x = 750
        elif self.x < 50:
            self.x = 50

    def draw(self):
        # if self.dir > 0:
        if hunter.fire == False:
            self.image.clip_draw(40 + self.frame * 62, 450, 62, 90, self.x, 90)
        else:
            self.image.clip_draw(40, 320, 62, 90, self.x, 90)
            self.image.clip_draw(320 + 60 * self.frame2, 225, 40, 80, self.x + 40, 90)
        # elif self.dir < 0:
        #     self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)



class Bullet:
    def __init__(self):
        self.image = load_image('Player.png')
        self.x = hunter.x
        self.y = hunter.y
        self.bul = 0

    def draw(self):
        self.image.clip_draw(320 + 60 * 2, 225, 20, 80, self.x + 40 + 40 * self.bul, 90)
        self.bul += 1


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
            elif event.key == SDLK_a:
                hunter.dir = -1
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

def bullet_del():
    for bullet in bullets:
        print(bullet.x)
        if bullet.x > 900:
            bullets.remove(Bullet())

def check_delay():
    if hunter.fire == False:
        if len(bullets) > 0:
            delay(0.01)
        else:
            delay(0.1)

def enter():
    global hunter, forest, bullet, running
    hunter = Player()
    forest = Map()
    bullet = Bullet
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
    bullet_del()

# 게임 월드 랜더링
def draw_world():
    check_delay()
    forest.draw()
    hunter.draw()
    bullet_draw()
    print(len(bullets))

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




