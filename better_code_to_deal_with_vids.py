import cv2
import numpy as np
count=1
cap = cv2.VideoCapture('Resources/30-30_1.mp4')

survive = np.zeros((13,13), dtype=int)

while cap.isOpened():

    ret, img = cap.read()
    if ret == True:
        count = count + 1
        if count%48 ==0:
            width, height = 1000, 1000
            pts1 = np.float32([[871, 354], [971, 351], [968, 432], [863, 434]])
            pts2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
            matrix = cv2.getPerspectiveTransform(pts1, pts2)
            img_warp = cv2.warpPerspective(img, matrix, (width, height))

            img_gray = cv2.cvtColor(img_warp, cv2.COLOR_BGR2GRAY)

            (thresh, img_WB) = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)

            x = 0
            y = 0
            a = int(width / 26)

            b = int(height / 26)

            pixel = img_WB[a, b]

            while x <= 12:
                while y <= 12:
                    pixel = img_WB[a, b]
                    if pixel == 0:
                        survive[x, y] = count/24

                    b = int(b + height / 13)
                    y += 1

                b = int(height / 26)
                y = 0
                a = int(a + width / 13)
                x += 1



    else:
        break
print(int(count))

print(survive)

cap.release()
cv2.destroyAllWindows()


