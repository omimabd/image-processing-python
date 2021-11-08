import cv2
import numpy as np
import matplotlib.pyplot as plt
from growing import Point

class Segmentation:

    def __init__(self,image):
        self.image = image

    def k_means(self):

        #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        pixel_values = self.image.reshape((-1, 3))
        # convert to float
        pixel_values = np.float32(pixel_values)
        #pixel_values = np.float32(image)

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

        k = 3
        #attempts=10
        ret, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

        centers = np.uint8(centers)

        segmented_image = centers[labels.flatten()]

        segmented_image = segmented_image.reshape(self.image.shape)

        return segmented_image

#     def getGrayDiff(self, currentPoint, tmpPoint):
#        return abs(int(img[currentPoint.x, currentPoint.y]) - int(img[tmpPoint.x, tmpPoint.y]))
#
#
#     def selectConnects(self,p):
#         if p != 0:
#             connects = [Point(-1, -1), Point(0, -1), Point(1, -1), Point(1, 0), Point(1, 1), \
#                         Point(0, 1), Point(-1, 1), Point(-1, 0)]
#         else:
#             connects = [Point(0, -1), Point(1, 0), Point(0, 1), Point(-1, 0)]
#         return connects
#
#
#     def regionGrow(self, seeds, thresh, p=1):
#         height, weight = self.image.shape
#         seedMark = np.zeros(self.image.shape)
#         seedList = []
#         for seed in seeds:
#             seedList.append(seed)
#         label = 1
#         connects = self.selectConnects(p)
#         while (len(seedList) > 0):
#             currentPoint = seedList.pop(0)
#
#             seedMark[currentPoint.x, currentPoint.y] = label
#             for i in range(8):
#                 tmpX = currentPoint.x + connects[i].x
#                 tmpY = currentPoint.y + connects[i].y
#                 if tmpX < 0 or tmpY < 0 or tmpX >= height or tmpY >= weight:
#                     continue
#                 grayDiff = self.getGrayDiff(self.image, currentPoint, Point(tmpX,tmpY))
#                 if grayDiff < thresh and seedMark[tmpX, tmpY] == 0:
#                     seedMark[tmpX, tmpY] = label
#                     seedList.append(Point(tmpX, tmpY))
#         return seedMark
# img = cv2.imread('3-5-2019-8-42-57-pm.png',0)
# seeds = [Point(10,10),Point(82,150),Point(20,300)]
# s=Segmentation(img)
# binaryImg = s.regionGrow(seeds,10)
# cv2.imshow(' ',binaryImg)
# cv2.waitKey(0)