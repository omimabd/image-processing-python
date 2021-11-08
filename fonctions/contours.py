from numpy import *
import numpy as np
np.seterr(over='ignore')
import cv2
from matplotlib.pyplot import *
import matplotlib.pyplot as plt

class Contours:

    def __init__(self,image):
        self.image = image

    def grad(self,seuil):
        imageX = self.image.copy()
        imageY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageX[i, j]= self.image[i, j+1] -self.image[i, j]
                imageY[i, j] = self.image[i+1,j] -self.image[i, j]
        imageXY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageXY[i, j] = sqrt(imageX[i, j] ** 2 + imageY[i, j] ** 2)
                if imageXY[i, j] < seuil:
                    imageXY[i, j] = 0
                else:
                    imageXY[i, j] = 255
        return imageXY

    def Robinson(self,seuil):
        imageX = self.image.copy()
        imageY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageX[i, j] = self.image[i, j] - self.image[i - 1, j - 1]
                imageY[i, j] = self.image[i, j] - self.image[i + 1, j + 1]
        imageXY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageXY[i, j] = sqrt(imageX[i, j] ** 2 + imageY[i, j] ** 2)
                if imageXY[i, j] < seuil:
                    imageXY[i, j] = 0
                else:
                    imageXY[i, j] = 255
        return imageXY

    def Sobel(self,seuil):
        imageX = self.image.copy()
        imageY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageY[i, j] = -self.image[i-1, j-1] -2*self.image[i, j-1] -self.image[i+1, j-1] \
                               + self.image[i - 1, j + 1] +2*self.image[i, j + 1] +self.image[i + 1, j + 1]
                imageX[i, j] = self.image[i-1, j-1] + 2*self.image[i-1, j] +self.image[i - 1, j + 1]\
                                -self.image[i+1, j-1] - 2*self.image[i+1, j] - self.image[i + 1, j + 1]
        imageXY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageXY[i, j] = sqrt(imageX[i, j] ** 2 + imageY[i, j] ** 2)
                if imageXY[i, j] < seuil:
                    imageXY[i, j] = 0
                else:
                    imageXY[i, j] = 255
        return imageXY

    def Laplacien(self,seuil):
        imageXY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageXY[i, j] = -4*self.image[i, j] +self.image[i-1, j] +self.image[i+1, j] \
                               + self.image[i , j - 1] +self.image[i, j + 1]
                if imageXY[i, j] < seuil:
                    imageXY[i, j] = 0
                else:
                    imageXY[i, j] = 255
        return imageXY

    def kirsch(self):
        image=self.image
        m, n = image.shape
        list = []
        kirsch = np.zeros((m, n))
        for i in range(2, m - 1):
            for j in range(2, n - 1):
                d1 = np.square(5 * image[i - 1, j - 1] + 5 * image[i - 1, j] + 5 * image[i - 1, j + 1] -
                               3 * image[i, j - 1] - 3 * image[i, j + 1] - 3 * image[i + 1, j - 1] -
                               3 * image[i + 1, j] - 3 * image[i + 1, j + 1])
                d2 = np.square((-3) * image[i - 1, j - 1] + 5 * image[i - 1, j] + 5 * image[i - 1, j + 1] -
                               3 * image[i, j - 1] + 5 * image[i, j + 1] - 3 * image[i + 1, j - 1] -
                               3 * image[i + 1, j] - 3 * image[i + 1, j + 1])
                d3 = np.square((-3) * image[i - 1, j - 1] - 3 * image[i - 1, j] + 5 * image[i - 1, j + 1] -
                               3 * image[i, j - 1] + 5 * image[i, j + 1] - 3 * image[i + 1, j - 1] -
                               3 * image[i + 1, j] + 5 * image[i + 1, j + 1])
                d4 = np.square((-3) * image[i - 1, j - 1] - 3 * image[i - 1, j] - 3 * image[i - 1, j + 1] -
                               3 * image[i, j - 1] + 5 * image[i, j + 1] - 3 * image[i + 1, j - 1] +
                               5 * image[i + 1, j] + 5 * image[i + 1, j + 1])
                d5 = np.square((-3) * image[i - 1, j - 1] - 3 * image[i - 1, j] - 3 * image[i - 1, j + 1] - 3
                               * image[i, j - 1] - 3 * image[i, j + 1] + 5 * image[i + 1, j - 1] +
                               5 * image[i + 1, j] + 5 * image[i + 1, j + 1])
                d6 = np.square((-3) * image[i - 1, j - 1] - 3 * image[i - 1, j] - 3 * image[i - 1, j + 1] +
                               5 * image[i, j - 1] - 3 * image[i, j + 1] + 5 * image[i + 1, j - 1] +
                               5 * image[i + 1, j] - 3 * image[i + 1, j + 1])
                d7 = np.square(5 * image[i - 1, j - 1] - 3 * image[i - 1, j] - 3 * image[i - 1, j + 1] +
                               5 * image[i, j - 1] - 3 * image[i, j + 1] + 5 * image[i + 1, j - 1] -
                               3 * image[i + 1, j] - 3 * image[i + 1, j + 1])
                d8 = np.square(5 * image[i - 1, j - 1] + 5 * image[i - 1, j] - 3 * image[i - 1, j + 1] +
                               5 * image[i, j - 1] - 3 * image[i, j + 1] - 3 * image[i + 1, j - 1] -
                               3 * image[i + 1, j] - 3 * image[i + 1, j + 1])

                # : Take the maximum value in each direction, the effect is not good, use another method
                list = [d1, d2, d3, d4, d5, d6, d7, d8]
                kirsch[i, j] = int(np.sqrt(max(list)))
                # : Rounding the die length in all directions
                # kirsch[i, j] =int(np.sqrt(d1+d2+d3+d4+d5+d6+d7+d8))
        for i in range(m):
            for j in range(n):
                if kirsch[i, j] > 127:
                    kirsch[i, j] = 255
                else:
                    kirsch[i, j] = 0
        return kirsch