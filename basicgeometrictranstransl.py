import cv2
import numpy as np
img = cv2.imread("face.jpg")
cv2.imshow("ORIGINAL",img)
rows,cols,ch = img.shape
matrix = np.float32([[1,0,50],[0,1,50]])
trans_img = cv2.warpAffine(img,matrix,(cols,rows))
cv2.imshow("tran",trans_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
