#adapted from opencv documentation examples
#commented code is general opencv functions, above their corresponding driver function

import cv2
import camera-driver

color_queue = []
depth_queue = []

#cap = cv2.VideoCapture(0)
pullFrames(color_queue, depth_queue)

# Check if the webcam is opened correctly
#if not cap.isOpened():
#    raise IOError("Cannot open webcam")

dest = '_________'

start = cv.getTickCount()

i = 0
while i < 100:
    #ret, frame = cap.read()
    frame, depth = getImage(color_queue, depth_queue)
    trans = cv2.blur(frame)
    #cv2.imwrite(dest, trans)

    i++

end = cv.getTickCount()
time = (end - start)/cv.getTickFrequency()

#cap.release()
cv2.destroyAllWindows()