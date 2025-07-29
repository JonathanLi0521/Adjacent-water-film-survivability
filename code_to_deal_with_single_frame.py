import cv2
import numpy as np

img = cv2.imread("Resources/pre1_frame.jpg")

cv2.imshow("org",img)

width, height = 1000,1000
pts1 = np.float32([[922, 410], [916, 60], [1175, 33], [1187, 379]])
pts2 = np.float32([[0,0],[width,0],[width,height],[0,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
img_warp = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("output",img_warp)

img_gray = cv2.cvtColor(img_warp,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",img_gray)

(thresh,img_WB) = cv2.threshold(img_gray, 153, 255, cv2.THRESH_BINARY)
cv2.imshow("wb",img_WB)

cv2.waitKey(0)

A = np.zeros((10,10),dtype=int)
x = 0
y = 0
a = int(width/ 20)
print(a)
b = int(height/ 20)
print(b)
pixel = img_WB[a,b]
print(pixel)

while x <= 9:
    while y <= 9:
        pixel = img_WB[a,b]
        #print(pixel)
        if pixel == 255:
            A[x,y]=0
        else:
            A[x,y]=1

        b =int(b + height / 10)
        y += 1
        #print(A)

    b = int(height/20)
    y = 0
    a = int(a + width/10)
    x += 1

print (A)

