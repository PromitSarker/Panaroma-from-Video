import cv2
import os
import math
import glob
import numpy as np
import matplotlib.pyplot as plt #install matplotlib first

cam = cv2.VideoCapture("demo.mp4")
try:
    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

except OSError:
    print ('Error: Creating directory of data')

currentframe = 0

while(True):
    ret,frame = cam.read()

    if ret:
        name = './data/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)
        currentframe += 1
    else:
        break
cam.release()

imagefiles = glob.glob("data/*")
imagefiles.sort()

images = []
for filename in imagefiles:
    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    images.append(img)

# Stitching
stitcher = cv2.Stitcher_create()
status, result = stitcher.stitch(images)

if status == 0:
    plt.figure(figsize=[30, 10])
    plt.imshow(result)