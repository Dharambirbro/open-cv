#stack images
import cv2
import numpy as np

def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]

    if rowsAvailable:
        for x in range(rows):
            for y in range(cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)

                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)

        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows

        for x in range(rows):
            hor[x] = np.hstack(imgArray[x])

        ver = np.vstack(hor)
    else:
        for x in range(rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)

            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)

        hor = np.hstack(imgArray)
        ver = hor

    return ver

# Example usage:
img1 = cv2.imread('assets/download.jpg')
img2 = cv2.imread('assets/face1.jpg')
img3 = cv2.imread('assets/shape2.jpg')
imgGrey=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
imgStack = stackImages(0.8, [[img1, img2], [img3, imgGrey]])
cv2.imshow("Stacked Images", imgStack)
cv2.waitKey(0)
cv2.destroyAllWindows()
