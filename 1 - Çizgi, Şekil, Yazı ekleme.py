import cv2 as cv
import numpy as np

img = np.zeros([1000,1000,3],np.uint8)

#img = cv.imread("manzara2.jpg")

img = cv.line(img,(0,0),(255,70),(0,96,44),10)
img = cv.arrowedLine(img,(50,50),(50,150),(100,100,100),6)
img = cv.rectangle(img,(384,500),(510,700),(0,0,255),5)
img = cv.rectangle(img,(380,50),(580,250),(0,0,255),3)
img = cv.circle(img,(480,150),100,(0,255,255),-1)

font = cv.FONT_HERSHEY_SIMPLEX

img = cv.putText(img,"OpenCv",(480,500),font,4,(255,255,255),10,cv.LINE_AA)


cv.imshow("Image", img)




cv.waitKey(0)
cv.destroyAllWindows()
