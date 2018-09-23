import cv2
import numpy as np

def emptyfunction():
    pass


def main():
    img1 = np.zeros((515, 512, 3), np.uint8)
    windowName = "BGR Color Palate"
    cv2.namedWindow(windowName)

    cv2.createTrackbar("B", windowName, 0, 255, emptyfunction)
    cv2.createTrackbar("G", windowName, 0, 255, emptyfunction)
    cv2.createTrackbar("R", windowName, 0, 255, emptyfunction)

    while(True):
        cv2.imshow(windowName, img1)

        if cv2.waitKey(1) == 27:
            break

        blue = cv2.getTrackbarPos("B", windowName)
        green = cv2.getTrackbarPos("G", windowName)
        red = cv2.getTrackbarPos("R", windowName)

        img1[:] = [blue, green, red]

        print(blue, green, red)



    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()
