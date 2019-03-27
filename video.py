import cv2
vid = cv2.VideoCapture() #your video
while True:
    ret, frame = vid.read()
    cv2.imshow("VIDEO",frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
    
