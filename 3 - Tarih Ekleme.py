import cv2 as cv
import numpy as np
import datetime

cam = cv.VideoCapture(0)

print(cam.get(cv.CAP_PROP_FRAME_WIDTH))
print(cam.get(cv.CAP_PROP_FRAME_HEIGHT))

cam.set(cv.CAP_PROP_FRAME_WIDTH,1280)
cam.set(cv.CAP_PROP_FRAME_HEIGHT,720)

while (cam.isOpened()):

    ret,frame = cam.read()
    if ret == True:
        font = cv.FONT_HERSHEY_SIMPLEX
        text = str(datetime.datetime.now())
        cv.putText(frame,(text,(20,50),font,2,(0,255,255),2,cv.LINE_AA))


        cv.imshow('Kamera', frame)

        if cv.waitKey(0) & 0xFF == ord('q'):
            break

    else:
        break


cam.release()
cv.destroyAllWindows()
