import random
import numpy as np


class Person:

    def __init__(self, idNo, time):
        self.ID = idNo
        self.color = [random.randint(100, 256), random.randint(100, 256), random.randint(100, 256)]
        self.active = True
        self.enterTime = time
        self.box = []
        self.leftTime = 0
        self.photo = []
        self.pos = []  # x,y,t

    def updatePic(self, pic):
        self.photo = pic

    def getLastPos(self):
        return self.pos[-1]

    def left(self, time):
        self.active = False
        self.leftTime = time

    def update(self, point, boxes):
        self.pos.append(point)
        self.box.append(boxes)

    def getLastBox(self, frameNo):
        return self.box[-1][frameNo]