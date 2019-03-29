import cv2
import numpy as np
img = cv2.imread("face.jpg")
print(img)

cv2.imshow("Face",img)
cv2.waitKey(0)
cv2.destroyAllWindows()