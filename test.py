import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)


def event_listener(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x, ' , ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ',' + str(y)
        cv2.putText(img, strXY, (x, y), font, .5, (0, 0, 255), 1)
        cv2.imshow('Video', img)
while(1):
    _,frame = cap.read()

    img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

   # cv2.imshow('Video',img)
    cv2.setMouseCallback('img',event_listener)
    print("*")

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.waitkey(0)
cv2.distroyAllWindows()




