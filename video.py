import cv2
vid = cv2.VideoCapture("Passive Income Ideas 💡- 10 Ways I Make $1,000 Per Month.mp4")
while True:
    ret, frame = vid.read()
    cv2.imshow("VIDEO",frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
    