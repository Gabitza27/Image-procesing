import cv2
from matplotlib import pyplot as plt

image_path = "D:\\Licenta 2018-2019\\Boch future mobility\\autobahn-wiki.jpg"
img = cv2.imread(image_path, 0)
cv2.imshow('STREET', img)

for thr in range(5, 255, 5):
    ret, img_bin = cv2.threshold(img, thr, 255, cv2.THRESH_BINARY)
    cv2.imshow('STREET', img_bin)
    cv2.waitKey(0)