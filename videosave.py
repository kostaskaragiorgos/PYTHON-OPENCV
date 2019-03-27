import cv2
vid = cv2.VideoCapture("Passive Income Ideas 💡- 10 Ways I Make $1,000 Per Month.mp4")
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("fliped_video.avi",fourcc,25,(720, 1280))
while True:
    ret, frame = vid.read()
    cv2.imshow("VIDEO",frame)
    frame2 = cv2.flip(frame,1)
    cv2.imshow("VIDEO flip",frame2)
    out.write(frame2)
    #print(frame.shape) just to save the video
    key = cv2.waitKey(30)
    if key == 27:
        break
    
out.release() 
vid.release()
cv2.destroyAllWindows()