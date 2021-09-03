import cv2 as cv
import numpy as np



#### events = [i for i in dir(cv) if 'EVENT' in i]
### print(events)

def click_event(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x,',',y)
        font = cv.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ',' + str(y)
        cv.putText(img, strXY, (x,y),font,1,(0,0,255),2)            ### cv.putText(RESİM,TEXT, NEREDE CIKACAK, FONT, FONTBUYUKLUGU,RENK,TEXT_KALINLIK)
        cv.imshow("image",img)





### img = np.zeros((700,800,3),np.uint8)
img = cv.imread("galatower.jpg")
cv.imshow("image",img)

cv.setMouseCallback('image',click_event)

cv.waitKey(0)
cv.destroyAllWindows()
