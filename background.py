import cv2
from cv2 import VideoCapture
import numpy as np

video = VideoCapture(1) #See with other numbers: 0 works
image = cv2.imread("Dog.png")

while True: #Check without
    ret, frame = video.read()
    #print(frame) #Arrays upon arrays
    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))

    upperBlack = np.array([104, 153, 70])
    lowerBlack = np.array([30, 30, 0])

    mask = cv2.inRange(frame, upperBlack, lowerBlack)
    res = cv2.bitwise_and(frame, frame, mask= mask)

    f = frame - res
    f = np.where(f == 0, image, f)

    cv2.imshow("video", frame)
    cv2.imshow("mask", f)# Check with f: Much better if they are the same variable; else, go with the bottom one

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()