import random
import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure()
ax = Axes3D(fig)

cap = cv2.VideoCapture('sample.3gp')

file = np.loadtxt('data.txt',delimiter=',').astype(np.int)
frameNo = file[:,0]
centers = []

#[x,y,t]
cars = []

#[(x1,y1),(x2,y2),(B,G,R)]
carBoxes = []

for x in range(1793):
    _,frame = cap.read()
    boxes = file[frameNo==x]
    frameCenters = np.array([(boxes[:, 1] + boxes[:, 3]) // 2, (boxes[:, 2] + boxes[:, 4]) // 2]).T
    for y in range(len(frameCenters)):
        centers.append([x, frameCenters[y, 0], frameCenters[y, 1]])
        cv2.circle(frame, (frameCenters[y, 0], frameCenters[y, 1]), 5, [0, 0, 255], thickness=-1)

    for i in range(len(frameCenters)):
        c = frameCenters[i]
        b = boxes[i]
        found = False
        for j in range(len(cars)):
            p = cars[j]
            pb = carBoxes[j]
            if p[-1][0] >= x - 5 and p[-1][0] != x:
                distance = (c[0] - p[-1][0]) ** 2 + (c[1] - p[-1][1]) ** 2
                if distance < 3000:
                    p.append([*c[:],x])
                    pb.append([(b[1],b[2]),(b[3],b[4]), pb[-1][2]])
                    found = True
                    break
        if not found:
            cars.append([[*c[:],x]])
            carBoxes.append([[(b[1],b[2]),(b[3],b[4]), (random.randint(100, 256), random.randint(100, 256), random.randint(100, 256))]])

    for i in range(len(cars)):
        if cars[i][-1][2] >= x - 5:
            if carBoxes[i][-1][0] != []:
                # print(carBoxes[i][-1])
                cv2.rectangle(frame, carBoxes[i][-1][0], carBoxes[i][-1][1], carBoxes[i][-1][2],thickness=2)
    for c in cars:
        if len(c)>5:
            print(c[-1])
            # cov = np.cov(c[])
    cv2.imshow('frame',frame)

    if cv2.waitKey(10) != -1:
        break

for car in cars:
    pp = np.array(car)
    ax.scatter(pp[:, 0], pp[:, 1], pp[:, 2])
plt.show()

