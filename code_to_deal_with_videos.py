import cv2
import numpy as np

count=1
cap = cv2.VideoCapture('Resources/pre_1.MOV')
A = np.zeros((10, 10), dtype=int)
survive = np.zeros((10,10), dtype=int)
def sum1(input):
    return sum(map(sum, input))

#get frames from video
while cap.isOpened():

    ret, img = cap.read()
	#straighten/ gray scale/ black and white
    if ret == True:
        count = count + 1
        if count%60 ==0:
            width, height = 1000, 1000
            pts1 = np.float32([[922, 410], [916, 60], [1175, 33], [1187, 379]])
            pts2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
            matrix = cv2.getPerspectiveTransform(pts1, pts2)
            img_warp = cv2.warpPerspective(img, matrix, (width, height))

            img_gray = cv2.cvtColor(img_warp, cv2.COLOR_BGR2GRAY)

            (thresh, img_WB) = cv2.threshold(img_gray, 155, 255, cv2.THRESH_BINARY)

            x = 0
            y = 0
            a = int(width / 20)

            b = int(height / 20)

            pixel = img_WB[a, b]

            while x <= 9:
				#check chosen pixel for brightness value
                while y <= 9:
                    pixel = img_WB[a, b]
                    if pixel == 255:
                        A[x, y] = 0
                        survive[x,y]+=1
                    else:
                        A[x, y] = 1

                    b = int(b + height / 10)
                    y += 1

                b = int(height / 20)
                y = 0
                a = int(a + width / 10)
                x += 1

            print(A)
            print(sum1(A)/100)

        #else:
            #print("skip")

    else:
        break
print(int((count-1)/2))

print(survive)

cap.release()
cv2.destroyAllWindows()


