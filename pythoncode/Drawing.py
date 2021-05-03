import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")
cv2.imshow("Canvas", canvas)

blue = (255, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)
white = (255, 255, 255)

cv2.line(canvas, (0,0), (300,300), green, thickness=5)
cv2.line(canvas, (0,300), (300,0), red, thickness=5)
cv2.line(canvas, (150,0), (150,300), blue, thickness=5)
cv2.line(canvas, (0,150), (300,150), white, thickness=5)
cv2.rectangle(canvas, (50,200), (200,255), red, 5)
cv2.rectangle(canvas, (200,50), (255,125), blue, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)