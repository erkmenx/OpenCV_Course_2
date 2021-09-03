import cv2 as cv
import numpy as np



#### events = [i for i in dir(cv) if 'EVENT' in i]
### print(events)

def click_event(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),3,(0,0,255),-1)
        points.append((x,y))
        if len(points)>=2:
            cv.line(img,points[-1],points[-2],(255,0,0),5)          ### cv.putText(RESİM,TEXT, NEREDE CIKACAK, FONT, FONTBUYUKLUGU,RENK,TEXT_KALINLIK)
        cv.imshow("image",img)





img = np.zeros((700,800,3),np.uint8)
###img = cv.imread("galatower.jpg")
cv.imshow("image",img)
points = []


cv.setMouseCallback('image',click_event)

cv.waitKey(0)
cv.destroyAllWindows()
