import numpy as np
import cv2

img = cv2.imread('Your image path here')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

class ShapeRecognition():
    
    def __init__(self,img):
        self.img = img
        
        
    def shapefinder(self):

        ret,thresh = cv2.threshold(gray,127,255,1)

        _,contours,_ = cv2.findContours(thresh,1,2)
    
        for cnt in contours:
            approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
            print (len(approx))
            if len(approx)==3:
                print ("Triangle")
                cv2.drawContours(img,[cnt],-1,(0,0,255),3)
      
shapeRecognition = ShapeRecognition(img)

contours = shapeRecognition.shapefinder()

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()