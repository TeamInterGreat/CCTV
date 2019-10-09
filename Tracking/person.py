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
        self.vel = []

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

    def updateVel(self,vel):
        self.vel.append(vel)

    def getLastBox(self, frameNo):
        return self.box[-1][frameNo]

    def getLastVel(self):
        if len(self.vel):
            return self.vel[-1]
        return [0,0]