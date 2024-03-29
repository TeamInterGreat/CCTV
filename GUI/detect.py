import cv2 as cv
import numpy as np



#Write down conf, nms thresholds,inp width/height
confThreshold = 0.1
nmsThreshold = 0.40
inpWidth = 416
inpHeight = 416
frame_count = 0

file = open('data.txt', 'w')

#Load names of classes and turn that into a list
classesFile = "coco.names"
classes = None
image =0
with open(classesFile,'rt') as f:
    classes = f.read().rstrip('\n').split('\n')

#Model configuration
modelConf = 'weights/yolov3.cfg'
modelWeights = 'weights/yolov3.weights'

def postprocess(frame, outs):
    frameHeight = frame.shape[0]
    frameWidth = frame.shape[1]

    classIDs = []
    confidences = []
    boxes = []
    detections = list()

    

    for out in outs:
        for detection in out:
            
            scores = detection [5:]
            classID = np.argmax(scores)
            confidence = scores[classID]

            if confidence > confThreshold:
                centerX = int(detection[0] * frameWidth)
                centerY = int(detection[1] * frameHeight)

                width = int(detection[2]* frameWidth)
                height = int(detection[3]*frameHeight )

                left = int(centerX - width/2)
                top = int(centerY - height/2)

                classIDs.append(classID)
                confidences.append(float(confidence))
                boxes.append([left, top, width, height])

    indices = cv.dnn.NMSBoxes(boxes, confidences, confThreshold, nmsThreshold)

    for i in indices:
        i = i[0]
        box = boxes[i]
        left = box[0]
        top = box[1]
        width = box[2]
        height = box[3]

        if classIDs[i] == 0:
            detections.append(np.array([left, top, left + width, top + height ]))

        drawPred(classIDs[i], confidences[i], left, top, left + width, top + height)

    return detections

def drawPred(classId, conf, left, top, right, bottom):
    # Draw a bounding box.
    if classId == 24 or classId == 0  :

        cv.rectangle(image, (left, top), (right, bottom), (255, 178, 50), 3)


def getOutputsNames(net):
    # Get the names of all the layers in the network
    layersNames = net.getLayerNames()
   
    # Get the names of the output layers, i.e. the layers with unconnected outputs
    return [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]


#Set up the net

net = cv.dnn.readNetFromDarknet(modelConf, modelWeights)
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)


#Process inputs







# while cv.waitKey(1) < 0:
#     frame_count = frame_count +1
#     print(frame_count)
#     #get frame from video
#     hasFrame, frame = cap.read()
#
#     #Create a 4D blob from a frame
#
#     blob = cv.dnn.blobFromImage(frame, 1/255, (inpWidth, inpHeight), [0,0,0], 1, crop = False)
#
#     #Set the input the the net
#     net.setInput(blob)
#     outs = net.forward (getOutputsNames(net))
#
#
#     print(postprocess (frame, outs))
#
#     #show the image
#     cv.imshow(winName, frame)


def getDetections(img):

    image =img
    blob = cv.dnn.blobFromImage(image, 1 / 255, (inpWidth, inpHeight), [0, 0, 0], 1, crop=False)
    net.setInput(blob)
    outs = net.forward(getOutputsNames(net))

    return postprocess(image, outs)















