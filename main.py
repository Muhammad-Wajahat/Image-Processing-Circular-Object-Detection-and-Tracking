import cv2
import numpy as np

src = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not src.isOpened():
    raise IOError("cannot open webcam")
# default_file = 'circles.jpg'
re, frame2 = src.read()
dotCenter = []
while True:
    re, frame = src.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 100)
    rows = gray.shape[0]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                               param1=100, param2=30,
                               minRadius=1, maxRadius=70)
    if dotCenter is not None:
        for j in dotCenter:
            cv2.circle(frame, j, 1, (0, 100, 100), 3)
        if len(dotCenter) > 50:
            dotCenter.pop(0)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            dotCenter.append(center)
            radius = i[2]
            frame = cv2.circle(frame, center, radius, (255, 0, 255), 3)
    cv2.imshow("Circular Tracker:", frame)
    c = cv2.waitKey(1)
    if c == 27:
        break
