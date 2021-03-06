#adapted from opencv documentation examples
#commented code is general opencv functions, above their corresponding driver function

import sys
import math
import cv2 as cv
import numpy as np
import camera-driver

color_queue = []
depth_queue = []

#cap = cv.VideoCapture(0)
pullFrames(color_queue, depth_queue)

# Check if the webcam is opened correctly
#if not cap.isOpened():
#    raise IOError("Cannot open webcam")

dest = '_________'

start = cv.getTickCount()

i = 0
while i < 33:
    #ret, src = cap.read()
    frame, depth = getImage(color_queue, depth_queue)

    dst = cv.Canny(src, 50, 200, None, 3)
    cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
    cdstP = np.copy(cdst)

    lines = cv.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)

    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv.line(cdst, pt1, pt2, (0,0,255), 3, cv.LINE_AA)
    
    
    linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)
    
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)

    #cv.imwrite(dest, src)
    #cv.imwrite(dest, cdst)
    #cv.imwrite(dest, cdstP)

    i++

end = cv.getTickCount()
time = (end - start)/cv.getTickFrequency()

#cap.release()
cv.destroyAllWindows()