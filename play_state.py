from pico2d import *
import game_framework
import logo_state
import pause_state
from monster import *
from state import *
import random
import time

class Map:
    def __init__(self):
        self.image = load_image('forest.png')
        self.image2 = load_image('black.png')
        self.image3 = load_image('hp.png')
        self.background_music = load_music('background.mp3')
        self.background_music.set_volume(5)
        self.background_music.repeat_play()
        self.decrease = 0
        self.before_hp = 1000
        self.after_hp = 1000

    def update(self):
        self.after_hp = hunter.hp
        if self.before_hp - self.after_hp > 0:
            if hunter.hp > 0:
                self.decrease += (self.before_hp - self.after_hp) // 4.2 # 1000/220 (체력//(체력/hp바 크기)
                self.decrease = int(self.decrease) # 정수형으로 바꾸면서 생기는 값의 누락 때문에 정확한 hp 감소가 안됨.
                self.before_hp = self.after_hp

    def draw(self):
        self.image2.draw(400, 350)
        self.image.draw(400, 350)
        self.image3.draw(550, 330)
        self.image3.clip_draw(750-self.decrease, 400, 300, 100, 136-self.decrease, 525)

class Player:
    def __init__(self):
        self.x, self.y = 400, 90
        self.offense = 60 # 변경 시 업그레이드 후 공격력, 방어력 변경 부분도 수정 필요
        self.defense = 1
        self.hp = 1000
        self.frame, self.frame2, self.frame3 = 0, 0, 0
        self.div, self.div3, self.div4 = 0, 0, 0
        self.dir = 0
        self.non_zero_dir = 1
        self.fire = False
        self.clear = False
        self.die = False
        self.jump = False
        self.jump_count = 0
        self.boost = False
        self.time = 0
        self.cur_time = 0
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
        # if self.boost == True:
        #     self.cur_time = time.time()
        #     if self.cur_time - self.time < 10:
        #         hunter.offense = hunter.offense * 2
        #     else:
        #         hunter.offense = hunter.offense * 2
        if self.die == False:
            self.x += self.dir * 0.5
        if self.x > 750:
            self.x = 750
        elif self.x < 50:
            self.x = 50
        if self.jump == True and self.die == False: # 점프부분
            if self.jump_count <= 80:
                self.y += (80-self.jump_count) * 0.03
            elif self.jump_count >= 81 and self.jump_count <= 160:
                self.y -= (self.jump_count-80) * 0.03
            self.jump_count += 1
            if self.jump_count == 161:
                self.jump_count = 0
                self.jump = False
                # self.dir = 0
        if self.hp <= 0:
            if self.die == False:
                self.die = True
            self.div3 += 1
            self.frame3 = self.div3 // 20
        if self.clear == True:
            self.div4 += 1
        self.row_x, self.high_x, self.row_y, self.high_y = self.x - 30, self.x + 30, self.y - 30, self.y + 30

    def draw(self):
        if self.non_zero_dir > 0 and self.hp > 0:
            if self.jump == True and self.fire == True:
                self.image.clip_draw(300, 330, 62, 90, self.x, self.y)
                self.image.clip_draw(320 + 60 * self.frame2, 225, 40, 80, self.x + 30, self.y - 15)
            elif self.jump == True: # 여기까지 점프
                self.image.clip_draw(240, 330, 62, 90, self.x, self.y)
            elif self.fire == False and self.dir != 0: # 돌아다니는 모션
                self.image.clip_draw(40 + self.frame * 62, 450, 62, 90, self.x, self.y)
            elif self.fire == False and self.dir == 0: # 정지 모션
                self.image.clip_draw(40, 450, 62, 90, self.x, self.y)
            elif self.fire == True: # 발사 모션
                self.image.clip_draw(40, 320, 62, 90, self.x, self.y)
                self.image.clip_draw(320 + 60 * self.frame2, 225, 40, 80, self.x + 40, self.y)


        elif self.non_zero_dir < 0 and self.hp > 0: # 방향만 반대고 모션은 똑같음
            if self.jump == True and self.fire == True:
                self.image.clip_composite_draw(300, 330, 62, 90, 0, 'h', self.x, self.y, 62, 90)
                self.image.clip_composite_draw(320 + 60 * self.frame2, 225, 40, 80, 0, 'h', self.x - 30, self.y - 15, 40, 80)
            elif self.jump == True:
                self.image.clip_composite_draw(240, 330, 62, 90, 0, 'h', self.x, self.y, 62, 90)
            elif self.fire == False and self.dir != 0:
                self.image.clip_composite_draw(40 + self.frame * 62, 450, 62, 90, 0, 'h', self.x, self.y, 62, 90)
            elif self.fire == False and self.dir == 0:
                self.image.clip_composite_draw(40, 450, 62, 90, 0, 'h', self.x, self.y, 62, 90)
            elif self.fire == True:
                self.image.clip_composite_draw(40, 320, 62, 90, 0, 'h', self.x, self.y, 62, 90)
                self.image.clip_composite_draw(320 + 60 * self.frame2, 225, 40, 80, 0, 'h', self.x - 40, self.y, 40, 80)
        elif self.hp <= 0:
            if self.frame3 == 0:
                self.image.clip_draw(170, 100, 62, 90, self.x, 90)
            elif self.frame3 > 0:
                self.image.clip_draw(240, 100, 90, 90, self.x, 90)
            if self.frame3 > 5:
                self.image2.draw(400, 300)
            if self.frame3 == 20:
                delay(2)
                game_framework.change_state(logo_state)
        if self.clear == True:
            if self.div4 < 1000:
                self.image3.draw(400, 300)
            elif self.div4 == 1000:
                delay(2)
                game_framework.change_state(logo_state)

class Bullet:
    def __init__(self):
        self.image = load_image('Player.png')
        self.x = hunter.x
        self.y = hunter.y
        self.fire_sound = load_wav('fire_sound.wav')
        self.fire_sound.set_volume(8)
        self.sound = True
        self.bullet_dir = hunter.non_zero_dir
        self.div = 0
        self.jump = hunter.jump

    def update(self):
        if self.bullet_dir > 0:
            self.x += 3
        elif self.bullet_dir < 0:
            self.x -= 3

    def draw(self):
        if self.bullet_dir > 0:
            if self.jump == False:
                self.image.clip_draw(320 + 60 * 2, 225, 20, 80, self.x + 40, self.y)
            else:
                self.image.clip_draw(320 + 60 * 2, 225, 20, 80, self.x + 40, self.y - 10)
        elif self.bullet_dir < 0:
            if self.jump == False:
                self.image.clip_draw(320 + 60 * 2, 225, 20, 80, self.x - 40, self.y)
            else:
                self.image.clip_draw(320 + 60 * 2, 225, 20, 80, self.x - 40, self.y - 10)

def handle_events():
    global bullets, fire_sound
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.push_state(pause_state)
            elif event.key == SDLK_d:
                hunter.dir += 1
                hunter.non_zero_dir = 1
            elif event.key == SDLK_a:
                hunter.dir += -1
                hunter.non_zero_dir = -1
            if event.key == SDLK_k or event.key == SDLK_l:
                bullets.append(Bullet())
                # hunter.dir = 0
                hunter.fire = True
            if event.key == SDLK_w:
                if hunter.jump == False:
                    hunter.jump = True
            if event.key == SDLK_1:
                if state.g1 >= 3 and state.at < 9:
                    state.at += 1
                    state.g1 -= 3
                    hunter.offense = (state.at * 6) + 60  # 급한대로 그냥 여기다 집어넣음.
            if event.key == SDLK_2:
                if state.g1 >= 2 and state.de < 9:
                    state.de += 1
                    state.g1 -= 2
                    hunter.defense = 1 - 0.05*state.de
            if event.key == SDLK_4:
                if item.heal_use == False:
                    hunter.hp = 1000
                    forest.before_hp = 1000
                    forest.before_hp = 1000
                    forest.decrease = 0
                    item.heal_use = True
            # if event.key == SDLK_5:
            #     if item.boost_use == False:
            #         hunter.time = time.time()
            #         hunter.boost = True
            #         item.boost_use = True



        elif event.type == SDL_KEYUP:
            # hunter.dir = 0
            if event.key == SDLK_d:
                hunter.dir += -1
            elif event.key == SDLK_a:
                hunter.dir += 1
            if event.key == SDLK_k or event.key == SDLK_l:
                # hunter.dir = 0
                hunter.fire = False


# 게임 초기화 : 객체들을 생성
hunter = None
forest = None
bullet = None
bullet_sound = None
state = None
item = None
# zombie = None
bullets = []
zombies = []
skeletons = []
balloons = []

running = True
zombie_num = 50
skeleton_num = 30
balloon_num = 10

zombie_in = 20 # in 부분은 처음에 enter에서 추가하는 좀비 수와 같다.
skeleton_in = 10
balloon_in = 5

def remain_monster_check():
    if (len(zombies) + len(skeletons) + len(balloons)) == 0:
        hunter.clear = True

def collision_check():
    for zombie in zombies:
        if ((zombie.row_x < hunter.high_x and zombie.high_x > hunter.row_x and zombie.dir < 0) or (zombie.high_x > hunter.row_x and zombie.row_x < hunter.high_x and zombie.dir > 0)):
            if zombie.high_y > hunter.row_y:
                # if zombie.dir < 0:
                #     zombie.x += 0.3
                # else:
                #     zombie.x -= 0.3
                zombie.of_frequency += 1
                if zombie.of_frequency % 200 == 0:
                    hunter.hp -= zombie.offense * hunter.defense
                    # forest.after_hp -= zombie.offense
                    # hunter.dir = 0

    for skeleton in skeletons:
        if ((skeleton.row_x < hunter.high_x and skeleton.high_x > hunter.row_x and skeleton.dir < 0) or (skeleton.high_x > hunter.row_x and skeleton.row_x < hunter.high_x and skeleton.dir > 0)):
            if skeleton.high_y > hunter.row_y:
                skeleton.collision = True
                # if skeleton.dir < 0:
                #     skeleton.x += 0.3
                # else:
                #     skeleton.x -= 0.3
                skeleton.of_frequency += 1
                if skeleton.of_frequency % 200 == 0:
                    hunter.hp -= skeleton.offense * hunter.defense
        else:
            skeleton.collision = False

    for balloon in balloons:
        if (balloon.row_x < hunter.high_x and balloon.dir < 0) or (balloon.high_x > hunter.row_x and balloon.dir > 0):
            if balloon.die == False:
                hunter.hp -= balloon.offense * hunter.defense
                balloon.hp = -1

def bullet_draw():
    for bullet in bullets:
        bullet.draw()
        if bullet.sound == True: # 처음 총알 객체 생성 때만 소리를 출력
            bullet.fire_sound.play()
            bullet.sound = False

def monster_draw():
    for zombie in zombies:
        if zombie.hp > 0:
            zombie.draw()
        else:
            zombie.die_draw()
    for skeleton in skeletons:
        if skeleton.hp > 0:
            if skeleton.collision == True:
                skeleton.attack_draw()
            else:
                skeleton.draw()
        else:
            skeleton.die_draw()
    for balloon in balloons:
        if balloon.hp > 0:
            balloon.draw()
        else:
            balloon.burst_draw()

def state_draw():
    state.draw()

remove = False

def bullet_del():
    global remove
    for bullet in bullets:
        remove = False
        for zombie in zombies:
            if (zombie.row_x < bullet.x and zombie.hp > 0 and zombie.dir < 0) or (zombie.high_x > bullet.x and zombie.hp > 0 and zombie.dir > 0):
                if zombie.row_y < bullet.y and zombie.high_y > bullet.y:
                    bullets.remove(bullet)
                    zombie.hp -= hunter.offense
                    remove = True
                    break
        if (bullet.x > 800 or bullet.x < 0) and remove == False: # remove는 800 근처에서 충돌 검사시 두번 삭제 오류 방지
            bullets.remove(bullet)

    for bullet in bullets:
        remove = False
        for skeleton in skeletons:
            if (skeleton.row_x < bullet.x and skeleton.hp > 0 and skeleton.dir < 0) or (skeleton.high_x > bullet.x and skeleton.hp > 0 and skeleton.dir > 0):
                if skeleton.row_y < bullet.y and skeleton.high_y > bullet.y:
                    bullets.remove(bullet)
                    skeleton.hp -= hunter.offense
                    remove = True
                    break
        if (bullet.x > 800 or bullet.x < 0) and remove == False: # remove는 800 근처에서 충돌 검사시 두번 삭제 오류 방지
            bullets.remove(bullet)

    for bullet in bullets:
        remove = False
        for balloon in balloons:
            if (balloon.row_x < bullet.x and balloon.hp > 0 and balloon.dir < 0) or (balloon.high_x > bullet.x and balloon.hp > 0 and balloon.dir > 0):
                if balloon.row_y < bullet.y and balloon.high_y > bullet.y:
                    bullets.remove(bullet)
                    balloon.hp -= hunter.offense
                    remove = True
                    break
        if (bullet.x > 800 or bullet.x < 0) and remove == False: # remove는 800 근처에서 충돌 검사시 두번 삭제 오류 방지
            bullets.remove(bullet)

def monster_del():
    global zombie_num, skeleton_num, balloon_num, zombie_in, skeleton_in, balloon_in
    for zombie in zombies:
        if zombie.hp <= 0 and zombie.frame2 > 10:
            zombies.remove(zombie)
            state.g2 += 1
            if zombie_num > zombie_in:
                zombies.append(Zombie())
                zombie_in += 1

    for skeleton in skeletons:
        if skeleton.hp <= 0 and skeleton.frame3 > 10:
            skeletons.remove(skeleton)
            state.g2 += 2
            if skeleton_num > skeleton_in:
                skeletons.append(Skeleton())
                skeleton_in += 1

    for balloon in balloons:
        if balloon.hp <= 0 and balloon.frame2 > 12:
            balloons.remove(balloon)
            state.g2 += 3
            if balloon_num > balloon_in:
                balloons.append(Balloon())
                balloon_in += 1

    if state.g2 >= 10:
        state.g2 -= 10
        state.g1 += 1
    if state.g1 >= 9:
        state.g1 = 9
        state.g2 = 0

def bullet_update():
    for bullet in bullets:
        bullet.update()

def monster_update():
    for zombie in zombies:
        zombie.update()
    for skeleton in skeletons:
        skeleton.update()
    for balloon in balloons:
        balloon.update()

def item_update():
    item.update()
    item.x, item.y = hunter.x, hunter.y

def enter():
    global hunter, forest, bullet, running, state, item
    global zombies, skeletons, balloons, zombie_in, skeleton_in, balloon_in
    hunter = Player()
    forest = Map()
    bullet = Bullet()
    state = State()
    item = Item()
    zombies = [Zombie() for i in range(zombie_in)]
    skeletons = [Skeleton() for i in range(skeleton_in)]
    balloons = [Balloon() for i in range(balloon_in)]
    running = True


# 게임 종료 - 객체를 소멸
def exit():
    global hunter, forest
    del hunter
    del forest

    delay(0.1)


# 게임 월드에 객체를 업데이트 - 게임 로직
def update():
    forest.update()
    hunter.update()
    bullet_update()
    monster_update()
    item_update()
    collision_check()
    bullet_del()
    monster_del()
    remain_monster_check()

# 게임 월드 랜더링
def draw_world():
    forest.draw()
    hunter.draw()
    bullet_draw()
    monster_draw()
    state_draw()
    item.draw()
    delay(0.001)

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass


# def test_self(): # 자기 자신 실행
#     import sys
#     this_module = sys.modules['__main__']
#     pico2d.open_canvas()
#     game_framework.run(this_module)
#     pico2d.close_canvas()
#
# if __name__ == '__main__':  # 단독 실행이면
#     test_self()




