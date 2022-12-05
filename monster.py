from pico2d import *
import random

class Zombie:
    def __init__(self):
        self.x, self.y = random.randint(-100, 100), 90
        self.random_location = False
        self.offense = 30
        self.of_frequency = 0
        self.hp = 200
        self.frame, self.frame2 = 0, 0
        self.div = random.randint(0, 200)
        self.div2 = 0
        self.dir = 0
        self.image = load_image('zombie.png')
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
            if self.div >= 200:
                self.div = 0
        else:
            self.div2 += 1
            self.frame2 = self.div2 // 30
        if self.hp > 0: # 유동적인 움직임을 구현하기 위해서는 업데이트를 함수를 만들어서 해줘야 할 것 같은데..
            if self.dir < 0:
                if self.x < 50:
                    self.dir = 1
            else:
                if self.x > 750:
                    self.dir = -1

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


class Skeleton:
    def __init__(self):
        self.x, self.y = random.randint(-100, 100), 90
        self.random_location = False
        self.offense = 100
        self.of_frequency = 0
        self.hp = 300
        self.frame, self.frame2, self.frame3 = 0, 0, 0
        self.div = random.randint(0, 200)
        self.div2, self.div3 = 0, 0
        self.dir = 0
        self.collision = False
        self.image = load_image('skeleton.png')
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
            if self.div >= 250:
                self.div = 0

            if self.dir < 0:
                if self.x < 50:
                    self.dir = 1
            else:
                if self.x > 750:
                    self.dir = -1

            if self.dir < 0:
                self.x -= 0.3
            else:
                self.x += 0.3

            if self.collision == True:
                self.div2 += 1
                self.frame2 = self.div2 // 50
                if self.div2 >= 200:
                    self.div2 = 0
            else:
                self.div2 = 0
        else:
            self.div3 += 1
            self.frame3 = self.div3 // 30

        self.row_x, self.high_x, self.row_y, self.high_y = self.x - 30, self.x + 30, self.y - 30, self.y + 30

    def draw(self):
        if self.dir < 0:
            if self.frame == 0:
                self.image.clip_draw(20, 210, 48, 70, self.x, self.y)
            elif self.frame == 1:
                self.image.clip_draw(69, 210, 47, 70, self.x, self.y)
            elif self.frame == 2:
                self.image.clip_draw(116, 210, 47, 70, self.x, self.y)
            elif self.frame == 3:
                self.image.clip_draw(213, 210, 49, 70, self.x, self.y)
            elif self.frame == 4:
                self.image.clip_draw(262, 210, 49, 70, self.x, self.y)
        else:
            if self.frame == 0:
                self.image.clip_composite_draw(20, 210, 48, 70, 0, 'h', self.x, self.y, 48, 70)
            elif self.frame == 1:
                self.image.clip_composite_draw(69, 210, 47, 70, 0, 'h', self.x, self.y, 47, 70)
            elif self.frame == 2:
                self.image.clip_composite_draw(116, 210, 47, 70, 0, 'h', self.x, self.y, 47, 70)
            elif self.frame == 3:
                self.image.clip_composite_draw(213, 210, 49, 70, 0, 'h', self.x, self.y, 49, 70)
            elif self.frame == 4:
                self.image.clip_composite_draw(262, 210, 49, 70, 0, 'h', self.x, self.y, 49, 70)

    def attack_draw(self):
        if self.dir < 0:
            if self.frame2 == 0:
                self.image.clip_draw(0, 280, 75, 70, self.x + 10, self.y)
            elif self.frame2 == 1:
                self.image.clip_draw(76, 280, 80, 70, self.x, self.y)
            elif self.frame2 == 2:
                self.image.clip_draw(160, 280, 80, 70, self.x + 1, self.y)
            elif self.frame2 == 3:
                self.image.clip_draw(240, 280, 80, 70, self.x + 1, self.y)
        else:
            if self.frame2 == 0:
                self.image.clip_composite_draw(0, 280, 75, 70, 0, 'h', self.x-10, self.y, 75, 70)
            elif self.frame2 == 1:
                self.image.clip_composite_draw(76, 280, 80, 70, 0, 'h', self.x, self.y, 80, 70)
            elif self.frame2 == 2:
                self.image.clip_composite_draw(160, 280, 80, 70, 0, 'h', self.x-1, self.y, 80, 70)
            elif self.frame2 == 3:
                self.image.clip_composite_draw(240, 280, 80, 70, 0, 'h', self.x-1, self.y, 80, 70)

    def die_draw(self):
        if self.dir < 0:
            if self.frame3 == 0:
                self.image.clip_draw(0, 140, 80, 70, self.x, self.y)
            elif self.frame3 == 1:
                self.image.clip_draw(80, 140, 80, 70, self.x, self.y)
            elif self.frame3 == 2:
                self.image.clip_draw(160, 140, 87, 70, self.x, self.y)
            elif self.frame3 == 3:
                self.image.clip_draw(247, 140, 95, 70, self.x, self.y)
            elif self.frame3 >= 4:
                self.image.clip_draw(342, 140, 95, 60, self.x, self.y)
        else:
            if self.frame3 == 0:
                self.image.clip_composite_draw(0, 140, 80, 70, 0, 'h', self.x, self.y, 80, 70)
            elif self.frame3 == 1:
                self.image.clip_composite_draw(80, 140, 80, 70, 0, 'h', self.x, self.y, 80, 70)
            elif self.frame3 == 2:
                self.image.clip_composite_draw(160, 140, 87, 70, 0, 'h', self.x, self.y, 87, 70)
            elif self.frame3 == 3:
                self.image.clip_composite_draw(247, 140, 95, 70, 0, 'h', self.x, self.y, 95, 70)
            elif self.frame3 >= 4:
                self.image.clip_composite_draw(342, 140, 95, 60, 0, 'h', self.x, self.y, 95, 70)


class Balloon:
    def __init__(self):
        self.x, self.y = random.randint(-100, 100), 200
        self.random_location = False
        self.offense = 100
        self.hp = 300
        self.frame, self.frame2 = 0, 0
        self.div = random.randint(0, 200)
        self.div2 = 0
        self.dir = 0
        self.collision = False
        self.die = False
        self.image = load_image('balloon.png')
        self.image2 = load_image('explosion.png')
        self.row_x, self.high_x, self.row_y, self.high_y = self.x - 30, self.x + 30, self.y-50, self.y + 30

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
            self.frame = self.div // 30
            if self.div >= 300:
                self.div = 0

            if self.dir < 0:
                self.x -= 0.2
            else:
                self.x += 0.2

        else:
            self.die = True
            self.div2 += 1
            self.frame2 = self.div2 // 30 # 죽는 모션과 공격 모션은 터지는 모션으로 동일

        self.row_x, self.high_x, self.row_y, self.high_y = self.x - 30, self.x + 30, self.y - 55, self.y + 20

    def draw(self):
        if self.dir < 0:
            if self.frame <= 5:
                self.image.clip_draw(0, 0, 80, 85, self.x, self.y - 2 * self.frame)
            elif self.frame >= 6 and self.frame <= 9:
                self.image.clip_draw(0, 0, 80, 85, self.x, self.y - 20 + 2 * self.frame)
        else:
            if self.frame <= 5:
                self.image.clip_composite_draw(0, 0, 80, 85, 0, 'h', self.x, self.y - 2 * self.frame, 80, 85)
            elif self.frame >= 6 and self.frame <= 9:
                self.image.clip_composite_draw(0, 0, 80, 85, 0, 'h', self.x, self.y - 20 + 2 * self.frame, 80, 85)

    def burst_draw(self):
        if self.dir < 0:
            if self.frame2 <= 4:
                self.image2.clip_draw(self.frame2 * 300, 600, 300, 300, self.x, self.y)
            elif self.frame >= 5 and self.frame <= 9:
                self.image2.clip_draw((self.frame2 - 5) * 300, 300, 300, 300, self.x, self.y)
            elif self.frame >= 10 and self.frame2 <= 11:
                self.image2.clip_draw((self.frame2 - 10) * 300, 0, 300, 300, self.x, self.y)
        else:
            if self.frame2 <= 4:
                self.image2.clip_composite_draw(self.frame2 * 300, 600, 300, 300, 0, 'h', self.x, self.y, 300, 300)
            elif self.frame >= 5 and self.frame <= 9:
                self.image2.clip_composite_draw((self.frame2 - 5) * 300, 300, 300, 300, 0, 'h', self.x, self.y, 300, 300)
            elif self.frame >= 10 and self.frame2 <= 11:
                self.image2.clip_composite_draw((self.frame2 - 10) * 300, 0, 300, 300, 0, 'h', self.x, self.y, 300, 300)
