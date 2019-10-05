import cv2
import numpy as np
import math
from PeopleTracking import person
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def transform(pts, matrix):
    p = np.float32([pts[0], pts[1], 1])
    res = np.matmul(matrix, p)
    res = res // res[2]
    return (int(res[0]), int(res[1]))


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def intersectsCircle(c1, c2, r1, r2):
    d = dist(c1, c2)
    if d == 0:
        return 100
    return (r1 + r2) / d


def groupCircles(centers, radii, bodies):
    points = []
    retBodies = []
    marked1 = [False] * len(centers[0])
    marked2 = [False] * len(centers[1])
    for x in range(len(centers[0])):
        for y in range(len(centers[1])):
            if intersectsCircle(centers[0][x], centers[1][y], radii[0][x], radii[1][y]) >= 1:
                points.append(((centers[0][x][0] + centers[1][y][0]) // 2, (centers[0][x][1] + centers[1][y][1]) // 2))
                retBodies.append([bodies[0][x], bodies[1][y]])
                marked1[x] = True
                marked2[y] = True
    for a in range(len(centers[0])):
        if not marked1[a]:
            points.append(centers[0][a])
            retBodies.append([bodies[0][a], []])
    for a in range(len(centers[1])):
        if not marked2[a]:
            points.append(centers[1][a])
            retBodies.append([[], bodies[1][a]])
    return points, retBodies

def toPosint(a):
    b = int(a)
    return b if b>0 else 0


fig = plt.figure()
ax = Axes3D(fig)

#### LOAD DATA AND GET PERSPECTIVE TRANSFORM ####
pts = [[(178, 261), (361, 221), (344, 356), (540, 265)],
       [(274, 224), (70, 284), (453, 258), (247, 372)]]

xoff = 0
yoff = 0
ptsf = [(0 + xoff, 0 + yoff), (600 + xoff, 0 + yoff), (0 + xoff, 600 + yoff), (600 + xoff, 600 + yoff)]

m = [cv2.getPerspectiveTransform(np.float32(pts[x]), np.float32(ptsf)) for x in range(2)]

ptst = [[transform(pts[x][y], m[x]) for y in range(4)] for x in range(2)]

cap = [cv2.VideoCapture('E:\Projects\CCTV\outs\\vid1.avi'),
       cv2.VideoCapture('E:\Projects\CCTV\outs\\vid2.avi')]

bodyFiles = [open('E:\Projects\CCTV\outs\\boxes1.txt', 'r'),
             open('E:\Projects\CCTV\outs\\boxes2.txt', 'r')]

allPeople = []
activePeople = []
peopleCount = 0

for count in range(1101):

    frame = [0] * 2
    _, frame[0] = cap[0].read()
    _, frame[1] = cap[1].read()

    # refreshes frame
    res = np.zeros((600, 600, 3))

    # body data for each frame
    bodies = [[], []]

    # Reads bounding boxes for bodies
    for x in range(2):
        line = bodyFiles[x].readline().rstrip()
        if line != '#':
            boxes = line.split(';')
            boxes.pop(-1)
            for box in boxes:
                cords = list(map(toPosint, box.split(',')))
                bodies[x].append([(cords[0], cords[1]), (cords[2], cords[3])])

    # position of bottom line of bounding box
    pos = [[[(body[0][0], body[1][1]), body[1]] for body in camBodies] for camBodies in bodies]

    # transformed coordinate of above box
    linePos = [[[transform(pos[x][y][0], m[x]), transform(pos[x][y][1], m[x])] for y in range(len(pos[x]))] for x in
               range(len(pos))]

    # radii and centers of transformed  lines
    radii = [[int(dist(line[0], line[1]) // 2) for line in view] for view in linePos]
    centers = [[((line[0][0] + line[1][0]) // 2, (line[0][1] + line[1][1]) // 2) for line in view] for view in linePos]

    for x in range(2):
        for y in range(len(centers[x])):
            cv2.circle(res, centers[x][y], radii[x][y], [0, 0, 255], thickness=2)

    framePoints, gpBod = groupCircles(centers, radii, bodies)

    frameCenters = []
    frameBodies = []

    for i in range(len(framePoints)):
        if 900 > framePoints[i][0] > -300 and 900 > framePoints[i][1] > -300:
            frameCenters.append(framePoints[i])
            frameBodies.append(gpBod[i])

    for i in range(len(frameCenters)):
        c = frameCenters[i]
        fb = frameBodies[i]
        found = False
        for p in activePeople:
            lp = p.getLastPos()
            if lp[2] >= count - 50 and lp[2] != count:
                distance = (c[0] - lp[0]) ** 2 + (c[1] - lp[1]) ** 2
                if distance < 3000:
                    p.update([*c, count],fb)
                    if lp[2]<count-10:
                        if fb[0] != []:
                            p.photo = frame[0][fb[0][0][1]:fb[0][1][1], fb[0][0][0]:fb[0][1][0]]
                        else:
                            p.photo = frame[1][fb[1][0][1]:fb[1][1][1], fb[1][0][0]:fb[1][1][0]]
                    found = True
                    break
        if not found:
            p = person.Person(peopleCount,count)
            p.update([*c, count],fb)
            if fb[0] != []:
                p.photo = frame[0][fb[0][0][1]:fb[0][1][1], fb[0][0][0]:fb[0][1][0]]
            else:
                p.photo = frame[1][fb[1][0][1]:fb[1][1][1], fb[1][0][0]:fb[1][1][0]]
            activePeople.append(p)
            peopleCount += 1

    for p in activePeople:
        lp = p.getLastPos()
        if lp[2] >= count - 5:
            lb0 = p.getLastBox(0)
            lb1 = p.getLastBox(1)
            if lb0 != []:
                cv2.rectangle(frame[0], lb0[0], lb0[1], p.color, thickness=2)
            if lb1 != []:
                cv2.rectangle(frame[1], lb1[0], lb1[1], p.color, thickness=2)

    frame[1] = cv2.flip(frame[1], 1)
    cv2.imshow('frame1', frame[0])
    cv2.imshow('frame2', frame[1])
    cv2.imshow("res", res)

    if cv2.waitKey(1) != -1:
        break

for p in activePeople:
    pp = np.array(p.pos)
    ax.scatter(pp[:, 0], pp[:, 1], pp[:, 2])
plt.show()
