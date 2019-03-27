import cv2
vid = cv2.VideoCapture("Passive Income Ideas 💡- 10 Ways I Make $1,000 Per Month.mp4")
while True:
    ret, frame = vid.read()
    cv2.imshow("VIDEO",frame)
    frame2 = cv2.flip(frame,1)
    frame3 = cv2.flip(frame,0)
    cv2.imshow("VIDEO flip",frame2)
    cv2.imshow("VIDEO2",frame3)
    key = cv2.waitKey(30)
    if key == 27:
        break
    
vid.release()
cv2.destroyAllWindows()