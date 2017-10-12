import os
import numpy as np
import cv2 as cv
import argparse

abs_path = os.path.abspath(__file__)
current_path = os.path.dirname(abs_path)
file_path = ""

nArgParse = 0
if nArgParse == 1 :
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--image", required = True, help = "path to the image file")
	args = vars(ap.parse_args())
	
	file_path = os.path.abspath(os.path.join(current_path, args["image"]))
else:
	file_path = os.path.abspath(os.path.join(current_path, "images\\barcode_03.jpg"))

#read image
image = cv.imread(file_path)

#gray image
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

#
gradX = cv.Sobel(gray, ddepth = cv.CV_32F, dx = 1, dy = 0, ksize = -1)
gradY = cv.Sobel(gray, ddepth = cv.CV_32F, dx = 0, dy = 1, ksize = -1)
 
#
gradient = cv.subtract(gradX, gradY)
gradient = cv.convertScaleAbs(gradient)

#
blurred = cv.blur(gradient, (4, 4))
(_, thresh) = cv.threshold(blurred, 225, 255, cv.THRESH_BINARY)

#
kernel = cv.getStructuringElement(cv.MORPH_RECT, (21, 7))
closed = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel)

#
closed = cv.erode(closed, None, iterations = 9)
closed = cv.dilate(closed, None, iterations = 9)

#
(_, cnts, _,) = cv.findContours(closed.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
c = sorted(cnts, key = cv.contourArea, reverse = True)[0]

#
rect = cv.minAreaRect(c)
box = np.int0(cv.boxPoints(rect))

#
cv.drawContours(image, [box], -1, (255, 0, 0), 5)
cv.imshow("Image", image)
cv.waitKey(0)	