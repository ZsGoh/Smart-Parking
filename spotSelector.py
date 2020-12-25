# importing everything we need
import cv2
import csv
import numpy as np

# select the video source; 0 - integrated webcam; 1 - external webcam;
VIDEO_SOURCE = 1

# start the recording
cap = cv2.VideoCapture(0)
suc, image = cap.read()

# save first frame as JPEG file
cv2.imwrite("frame0.jpg", image)
img = cv2.imread("frame0.jpg")

for i in range(VIDEO_SOURCE):
    temp = cap.read()

# get the regions of interest/parking spots
r = cv2.selectROIs('ROI Selector', img, showCrosshair=False, fromCenter=False)

# convert the result to a list
rlist = r.tolist()
print(rlist)

# write the list into a csv file
with open('Desktop\parking\test.csv', 'w', newline='') as outf:
  csvw = csv.writer(outf)
  csvw.writerows(rlist)

# when everything is done, release the capture
cap.release()
cv2.destroyAllWindows()

