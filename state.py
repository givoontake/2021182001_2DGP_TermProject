from pico2d import *

class State:
    def __init__(self):
        self.g1, self.g2 = 0, 0
        self.at = 0
        self.de = 0
        self.image = load_image('state.png')

    def draw(self):
        self.image.clip_draw(0, 16, 279, 48, 650, 550)
        if self.g1 == 0:
            self.image.clip_draw(90, 0, 10, 16, 555, 535) # 맨 왼쪽부터 총 4자리
        else:
            self.image.clip_draw((self.g1-1) * 10, 0, 10, 16, 555, 535) # 이미지 잘못 만들어서 식이 이상해짐
        if self.g2 == 0:
            self.image.clip_draw(90, 0, 10, 16, 555+10, 535)
        else:
            self.image.clip_draw((self.g2-1) * 10, 0, 10, 16, 555+10, 535)
        self.image.clip_draw(90, 0, 10, 16, 555 + 20, 535)
        self.image.clip_draw(90, 0, 10, 16, 555 + 30, 535)
        if self.at == 10:
            self.image.clip_draw(260, 0, 19, 16, 725, 569)
        else:
            self.image.clip_draw(170+10*self.at, 0, 10, 16, 725, 569) # 공격 레벨
        if self.de == 10:
            self.image.clip_draw(260, 0, 19, 16, 725, 552) # 방어 레벨
        self.image.clip_draw(170 + 10 * self.de, 0, 10, 16, 725, 552)  # 방어 레벨

class Item:
    def __init__(self):
        self.x, self.y = 0, 0
        self.boost_use = False
        self.boost_temp = False
        self.heal_use = False
        self.frame = 0
        self.div = 0
        self.image = load_image('icon.png')
        self.image2 = load_image('heal.png')

    def update(self):
        if self.heal_use == True:
            if self.frame <= 9:
                self.frame = self.div // 30
                self.div += 1


    def draw(self):
        if self.boost_use == False and self.boost_temp == False:
            self.image.clip_draw(0, 0, 65, 50, 400, 550)
        elif self.boost_use == True and self.boost_temp == False:
            self.image2.clip_draw(200, 500, 200, 100, self.x, self.y+10)

        if self.heal_use == False:
            self.image.clip_draw(65, 0, 65, 50, 450, 550)
        else:
            if self.frame <= 4:
                self.image2.clip_draw(200*self.frame, 100, 200, 100, self.x, self.y)
            elif self.frame >= 5 and self.frame <= 9:
                self.image2.clip_draw(200*(self.frame-5), 0, 200, 100, self.x, self.y)

