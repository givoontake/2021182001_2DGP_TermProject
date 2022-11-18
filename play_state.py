from pico2d import *
import game_framework
import logo_state
import item_state
import random
import time

class Map:
    def __init__(self):
        self.image = load_image('forest.png')
        self.image2 = load_image('black.png')
        self.background_music = load_music('background.mp3')
        self.background_music.set_volume(15)
        self.background_music.repeat_play()

    def draw(self):
        self.image2.draw(400, 350)
        self.image.draw(400, 350)

class Zombie:
    def __init__(self):
        self.x, self.y = random.randint(-100, 100), 90 # 충돌 검사 등 뭔가 까다로워서 왼쪽 객체는 일단 따로 만들 계획
        self.random_location = False
        self.offense = 30
        self.of_frequency = 0
        self.hp = 200
        self.frame = 0
        self.frame2 = 0
        self.div = random.randint(0, 200)
        self.div2 = 0
        self.dir = 0
        self.image = load_image('zombie.png')
        # self.zombie_sound = load_wav('zombie_sound.wav') # 엑세스 위반..
        # self.zombie_sound.set_volume(1)
        # self.zombie_sound.repeat_play() # 객체 생성 시 보이지도 않는데 좀비 소리가 나겠네;
        self.row_x, self.high_x, self.row_y, self.high_y = self.x - 30, self.x + 30, self.y - 30, self.y + 30

    def update(self):
        if self.random_location == False:
            if self.x >= 0:
                self.x = random.randint(1000, 2000)
                self.dir = -1
            else:
                self.x = random.randint(-1200, -200)
                self.dir = 1
            self.random_location = True
        if self.hp > 0:
            self.div += 1
            self.frame = self.div // 50
            if self.div > 200:
                self.div = 0
        else:
            self.div2 += 1
            self.frame2 = self.div2 // 30
        if self.hp > 0:
            if self.dir < 0:
                self.x -= 0.3
            else:
                self.x += 0.3
        self.row_x, self.high_x, self.row_y, self.high_y = self.x - 30, self.x + 30, self.y - 30, self.y + 30

    def draw(self):
        if self.dir < 0:
            self.image.clip_draw(self.frame * 120, 680, 120, 90, self.x, 90)
        else:
            self.image.clip_composite_draw(self.frame * 120, 680, 120, 90, 0, 'h', self.x, 90, 120, 90)

    def die_draw(self):
        if self.dir < 0:
            if self.frame2 < 4:
                self.image.clip_draw(self.frame2 * 120, 340, 120, 90, self.x, 90)
            elif self.frame2 >= 4 and self.frame2 <= 7:
                self.image.clip_draw((self.frame2-4) * 120, 220, 120, 90, self.x, 90)
            else:
                self.image.clip_draw(3 * 120, 220, 120, 90, self.x, 90)
        else:
            if self.frame2 < 4:
                self.image.clip_composite_draw(self.frame2 * 120, 340, 120, 90, 0, 'h', self.x, 90, 120, 90)
            elif self.frame2 >= 4 and self.frame2 <= 7:
                self.image.clip_composite_draw((self.frame2 - 4) * 120, 220, 120, 90, 0, 'h', self.x, 90, 120, 90)
            else:
                self.image.clip_composite_draw(3 * 120, 220, 120, 90, 0, 'h', self.x, 90, 120, 90)

class Player:
    def __init__(self):
        self.x, self.y = 400, 90
        self.offense = 50
        self.hp = 500
        self.frame, self.frame2, self.frame3 = 0, 0, 0
        self.div = 0
        self.div3 = 0
        self.div4 = 0
        self.dir = 0
        self.non_zero_dir = 1
        self.fire = False
        self.clear = False
        self.image = load_image('Player.png')
        self.image2 = load_image('mission_failed.png')
        self.image3 = load_image('mission_success.png')
        self.row_x, self.high_x, self.row_y, self.high_y = self.x - 30, self.x + 30, self.y - 30, self.y + 30

    def update(self):
        self.div += 1
        if self.div > 200:
            self.div = 0
        self.frame = self.div // 50
        # self.frame = (self.frame + 1) % 4
        self.frame2 = (self.frame + 1) % 2
        self.x += self.dir * 0.5
        if self.x > 750:
            self.x = 750
        elif self.x < 50:
            self.x = 50
        if self.hp <= 0:
            self.div3 += 1
            self.frame3 = self.div3 // 20
        if self.clear == True:
            self.div4 += 1
        self.row_x, self.high_x, self.row_y, self.high_y = self.x - 30, self.x + 30, self.y - 30, self.y + 30

    def draw(self):
        if self.non_zero_dir > 0 and self.hp > 0:
            if self.fire == False and self.dir != 0: # 돌아다니는 모션
                self.image.clip_draw(40 + self.frame * 62, 450, 62, 90, self.x, 90)
            elif self.fire == False and self.dir == 0: # 정지 모션
                self.image.clip_draw(40, 450, 62, 90, self.x, 90)
            elif self.fire == True: # 발사 모션
                self.image.clip_draw(40, 320, 62, 90, self.x, 90)
                self.image.clip_draw(320 + 60 * self.frame2, 225, 40, 80, self.x + 40, 90)

        elif self.non_zero_dir < 0 and self.hp > 0: # 방향만 반대고 모션은 똑같음
            if self.fire == False and self.dir != 0:
                self.image.clip_composite_draw(40 + self.frame * 62, 450, 62, 90, 0, 'h', self.x, 90, 62, 90)
            elif self.fire == False and self.dir == 0:
                self.image.clip_composite_draw(40, 450, 62, 90, 0, 'h', self.x, 90, 62, 90)
            elif self.fire == True:
                self.image.clip_composite_draw(40, 320, 62, 90, 0, 'h', self.x, 90, 62, 90)
                self.image.clip_composite_draw(320 + 60 * self.frame2, 225, 40, 80, 0, 'h', self.x - 40, 90, 40, 80)
        if self.hp <= 0:
            if self.frame3 == 0:
                self.image.clip_draw(170, 100, 62, 90, self.x, 90)
            elif self.frame3 > 0:
                self.image.clip_draw(240, 100, 90, 90, self.x, 90)
            if self.frame3 > 5:
                self.image2.draw(400, 300)
            if self.frame3 == 20:
                delay(2)
                game_framework.change_state(logo_state)
        elif self.clear == True:
            if self.div4 < 1000:
                self.image3.draw(400, 300)
            elif self.div4 == 1000:
                self.clear = False
                game_framework.push_state(item_state)

class Bullet:
    def __init__(self):
        self.image = load_image('Player.png')
        self.x = hunter.x
        self.y = hunter.y
        self.fire_sound = load_wav('fire_sound.wav')
        self.fire_sound.set_volume(25)
        self.sound = True
        self.bullet_dir = hunter.non_zero_dir
        self.div = 0

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
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(logo_state)
            elif event.key == SDLK_b:
                game_framework.push_state(item_state)
            elif event.key == SDLK_d:
                hunter.dir += 1
                hunter.non_zero_dir = 1
            elif event.key == SDLK_a:
                hunter.dir += -1
                hunter.non_zero_dir = -1
            elif event.key == SDLK_k or event.key == SDLK_l:
                bullets.append(Bullet())
                hunter.dir = 0
                hunter.fire = True

        elif event.type == SDL_KEYUP: # 키를 동시에 누를 경우 생기는 문제는 여기서 처리를 해줘야 하나..
            # hunter.dir = 0
            if event.key == SDLK_d:
               hunter.dir += -1
            elif event.key == SDLK_a:
                hunter.dir += 1
            if event.key == SDLK_k or event.key == SDLK_l:
                hunter.fire = False


# 게임 초기화 : 객체들을 생성
hunter = None
forest = None
bullet = None
# zombie = None
bullets = []
zombies = []

running = True
monster_num = 40
wave_clear = False

def remain_monster_check():
    if len(zombies) == 0:
        hunter.clear = True

def collision_check():
    for zombie in zombies:
        if (zombie.row_x < hunter.high_x and zombie.dir < 0) or (zombie.high_x > hunter.row_x and zombie.dir > 0):
            if zombie.dir < 0:
                zombie.x += 0.3
            else:
                zombie.x -= 0.3
            zombie.of_frequency += 1
            if zombie.of_frequency % 100 == 0:
                hunter.hp -= zombie.offense
                hunter.dir = 0

def bullet_draw():
    for bullet in bullets:
        bullet.draw()
        if bullet.sound == True: # 처음 총알 객체 생성 때만 소리를 출력
            bullet.fire_sound.play()
            bullet.sound = False

def zombie_draw():
    for zombie in zombies:
        if zombie.hp > 0:
            zombie.draw()
        else:
            zombie.die_draw()

remove = False

def bullet_del():
    global remove
    for bullet in bullets:
        remove = False
        for zombie in zombies:
            if (zombie.row_x < bullet.x and zombie.hp > 0 and zombie.dir < 0) or (zombie.high_x > bullet.x and zombie.hp > 0 and zombie.dir > 0):
                bullets.remove(bullet)
                zombie.hp -= hunter.offense
                remove = True
                break
        if (bullet.x > 800 or bullet.x < 0) and remove == False: # remove는 800 근처에서 충돌 검사시 두번 삭제 오류 방지
            bullets.remove(bullet)

def zombie_del():
    for zombie in zombies:
        if zombie.hp <= 0 and zombie.frame2 > 10:
            zombies.remove(zombie)

def bullet_update():
    for bullet in bullets:
        bullet.update()

def zombie_update():
    for zombie in zombies:
        zombie.update()

def enter():
    global hunter, forest, bullet, zombies, running, monster_num
    hunter = Player()
    forest = Map()
    bullet = Bullet()
    zombies = [Zombie() for i in range(monster_num)]
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
    zombie_update()
    collision_check()
    bullet_del()
    zombie_del()
    remain_monster_check()

# 게임 월드 랜더링
def draw_world():
    forest.draw()
    hunter.draw()
    bullet_draw()
    zombie_draw()
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




