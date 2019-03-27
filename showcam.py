import cv2
#import numpy as np 
cap = cv2.VideoCapture(0)
while True:
    ret , frame = cap.read()
    
    cv2.imshow("FRAME",frame)
    key = cv2.waitKey(1)
    if key == 27:  # press esc key
        break
    
        
    
cap.release()
cv2.destroyAllWindows()