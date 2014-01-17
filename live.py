from SimpleCV import Camera, Image, Display
from numpy import *
import time
import sys
from matplotlib import pyplot as plt

def diff(img):
    rows, cols = img.size()
    countW = 0
    countB = 0
    for i in range(rows):
        for j in range(cols):
            if img[i, j] == (255.00, 255.00, 255.00):
                countW += 1
            else:
                countB += 1
    try :
        k = 1.0/countW
        if k > 0.02:
            k = 0.000000000000001
    except :
        k = 0.000000000000001
    return k

def simpleDiff():
    cam = Camera()
    img = cam.getImage().scale(.20)
    disp = Display(img.size())
    img.save(disp)
    X = range(100)
    Y = [0 for i in range(100)]
    count = 0
    imgA = cam.getImage().scale(0.20).grayscale()
    while not disp.isDone():
        ax.clear()
        count += 1
        time.sleep(0.1)
        imgB = cam.getImage().scale(0.20).grayscale()
        #imgB.save(disp)
        motion = (imgB - imgA).binarize().invert().erode(1).dilate(1)
        motion.save(disp)
        s = diff(motion)
        imgA = imgB
        if count < 100:
            Y[count] = s
        else:
            Y.append(s)
            Y = Y[1:]
            X.append(count)
            X = X[1:]
        ax.bar(X, Y)
        plt.xlim(X[0], X[-1])
        plt.draw()
        imgA = imgB
        
def opticalFlow():
    cam = Camera()
    img = cam.getImage().scale(.20)
    disp = Display(img.size())
    img.save(disp)
    X = range(100)
    Y = [0 for i in range(100)]
    flag = 0
    count = 0
    while not disp.isDone():
        ax.clear()
        count += 1
        if flag == 0:
            imgA = cam.getImage().scale(0.20)
            flag += 1
        else:
            imgB = cam.getImage().scale(0.20)
            imgB.save(disp)
            motion = imgB.findMotion(imgA)
            s = sum([i.magnitude() for i in motion])
            imgA = imgB
            if count < 100:
                Y[count] = s
            else:
                Y.append(s)
                Y = Y[1:]
                X.append(count)
                X = X[1:]
            ax.bar(X, Y)
            plt.xlim(X[0], X[-1])
            plt.draw()

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
if str(sys.argv[1])=="1" :
    opticalFlow()
else :
    simpleDiff()
