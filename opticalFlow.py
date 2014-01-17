from SimpleCV import *
from numpy import *
import time
import os
from matplotlib import pyplot as plt
import sys

imgSet = ["./conc", "./distract"]

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

def plotAverage(name):
    flag = 0
    total = 0
    count = 0
    X = range(100)
    Y = [0 for i in range(100)]
    disp = Display((600,600))
    for root, subFolders, files in os.walk(name):
        ax.clear()
        for f in files:
            count += 1
            if flag == 0:
                imgA = Image(name + "/" + f).scale(0.20)
                imgB = Image(name + "/" + f).scale(0.20)
                flag += 1
            else:
                imgB = Image(name + "/" + f)
                imgB.save(disp)
                imgB = imgB.scale(0.20)
                motion = imgB.findMotion(imgA)
                s = sum([i.magnitude() for i in motion])
                total += s
                imgA = imgB
                if count < 100:
                    Y[count] = total*1.0/count
                else:
                    Y.append(total*1.0/count)
                    Y = Y[1:]
                    X.append(count)
                    X = X[1:]
                ax.bar(X, Y)
                plt.xlim(X[0], X[-1])
                plt.draw()

def results():
    for name in imgSet:
        flag = 0
        total = 0
        count = 0
        for root, subFolders, files in os.walk(name):
            ax.clear()
            for f in files:
                count += 1
                if flag == 0:
                    imgA = Image(name + "/" + f).scale(0.20)
                    imgB = Image(name + "/" + f).scale(0.20)
                    flag += 1
                else:
                    imgB = Image(name + "/" + f).scale(0.20)
                    motion = imgB.findMotion(imgA)
                    s = sum([i.magnitude() for i in motion])
                    total += s
                    imgA = imgB
        print "name : ", name, "score : ", total*1.0/count 

if str(sys.argv[1])=="1":
    plotAverage(name="./conc")
elif str(sys.argv[1])=="2":
    plotAverage(name="./distract")
else:
    results()