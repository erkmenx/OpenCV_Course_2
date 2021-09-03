import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)

print(cam.get(cv.CAP_PROP_FRAME_WIDTH))
print(cam.get(cv.CAP_PROP_FRAME_HEIGHT))

cam.set(cv.CAP_PROP_FRAME_WIDTH,1280)
cam.set(cv.CAP_PROP_FRAME_HEIGHT,720)

while (cam.isOpened()):

    ret,frame = cam.read()
    if ret == True:
        cv.imshow('Kamera', frame)

        if cv.waitKey(0) & 0xFF == ord('q'):
            break

    else:
        break


cam.release()
cv.destroyAllWindows()
