import cv2
# import numpy as np
#
# def get8n(x, y, shape):
#     out = []
#     if y-1 > 0 and x-1 > 0:
#         out.append( (y-1, x-1) )
#     if y-1 > 0 :
#         out.append( (y-1, x))
#     if y-1 > 0 and x+1 < shape[1]:
#         out.append( (y-1, x+1))
#     if x-1 > 0:
#         out.append( (y, x-1))
#     if x+1 < shape[1]:
#         out.append( (y, x+1))
#     if y+1 < shape[0] and x-1 > 0:
#         out.append( ( y+1, x-1))
#     if y+1 < shape[0] :
#         out.append( (y+1, x))
#     if y+1 < shape[0] and x+1 < shape[1]:
#        out.append( (y+1, x+1))
#     return out
#
# def region_growing(img, seed):
#     list = []
#     outimg = np.zeros_like(img)
#     list.append((seed[0], seed[1]))
#     processed = []
#     while(len(list) > 0):
#         pix = list[0]
#         outimg[pix[0], pix[1]] = 255
#         for coord in get8n(pix[0], pix[1], img.shape):
#             if img[coord[0], coord[1]] != 0:
#                 outimg[coord[0], coord[1]] = 255
#                 if not coord in processed:
#                     list.append(coord)
#                 processed.append(coord)
#         list.pop(0)
#         #cv2.imshow("progress",outimg)
#         #cv2.waitKey(1)
#     return outimg


# def on_mouse(event, x,y, flags , params):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print('Seed: ' + 'Point' + '('+str(x) + ', ' + str(y)+')', img[y, x])
#         clicks.append((y, x))

# clicks = []
# image = cv2.imread('lena.jpg', 0)
# ret, img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
# cv2.namedWindow('Input')
# cv2.setMouseCallback('Input', on_mouse, 0, )
# cv2.imshow('Input', img)
# cv2.waitKey()
# seed = clicks[-1]
# out = region_growing(img, seed)
# cv2.imshow('Region Growing', out)
# cv2.waitKey()
# import numpy as np
import cv2
#
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def getX(self):
#         return self.x
#
#     def getY(self):
#         return self.y
#
#
# def getGrayDiff(img, currentPoint, tmpPoint):
#         return abs(int(img[currentPoint.x, currentPoint.y]) - int(img[tmpPoint.x, tmpPoint.y]))
#
#
# def selectConnects(p):
#     if p != 0:
#         connects = [Point(-1, -1), Point(0, -1), Point(1, -1), Point(1, 0), Point(1, 1), \
#                     Point(0, 1), Point(-1, 1), Point(-1, 0)]
#     else:
#         connects = [Point(0, -1), Point(1, 0), Point(0, 1), Point(-1, 0)]
#     return connects
#
#
# def regionGrow(img, seeds, thresh, p=1):
#     height, weight = img.shape
#     seedMark = np.zeros(img.shape)
#     seedList = []
#     for seed in seeds:
#         seedList.append(seed)
#     label = 1
#     connects = selectConnects(p)
#     while (len(seedList) > 0):
#         currentPoint = seedList.pop(0)
#
#         seedMark[currentPoint.x, currentPoint.y] = label
#         for i in range(8):
#             tmpX = currentPoint.x + connects[i].x
#             tmpY = currentPoint.y + connects[i].y
#             if tmpX < 0 or tmpY < 0 or tmpX >= height or tmpY >= weight:
#                 continue
#             grayDiff = getGrayDiff(img, currentPoint, Point(tmpX, tmpY))
#             if grayDiff < thresh and seedMark[tmpX, tmpY] == 0:
#                 seedMark[tmpX, tmpY] = label
#                 seedList.append(Point(tmpX, tmpY))
#     return seedMark
#
# #
# img = cv2.imread('lena.jpg', 0)
# seeds = [Point(10, 10), Point(82, 150), Point(20, 300)]
# binaryImg = regionGrow(img, seeds, 10)
# cv2.imshow(' ', binaryImg)
# cv2.waitKey()
# import numpy
# from scipy.ndimage import label
# def region_growing(img, seed, minthr, maxthr, structure = None):
# 	img[seed] = minthr
# 	thrimg = (img < maxthr) & (img >= minthr)
# 	lmap, _ = label(thrimg, structure = structure)
# 	lids = numpy.unique(lmap[seed])
# 	region = numpy.zeros(img.shape, numpy.bool)
# 	for lid in lids:
# 		region |= lmap == lid
# 	return region
#
# img = cv2.imread('lena.jpg', 0)
# seeds=100
# binaryImg = region_growing(img, seeds , 0 , 10)
#
# cv2.imshow(' ', binaryImg)
# cv2.waitKey()
import numpy as np
import cv2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y
#
#
#     def getGrayDiff(self, currentPoint, tmpPoint):
#         return abs(int(self.image[currentPoint.x, currentPoint.y]) - int(self.image[tmpPoint.x, tmpPoint.y]))
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
#                 grayDiff = self.getGrayDiff(self.image, currentPoint, Point(tmpX, tmpY))
#                 if grayDiff < thresh and seedMark[tmpX, tmpY] == 0:
#                     seedMark[tmpX, tmpY] = label
#                     seedList.append(Point(tmpX, tmpY))
#         return seedMark
#
#
# img = cv2.imread('lena.jpg', 0)
# p=Point(0,0,img)
# seeds = [Point(10, 10,img), Point(82, 150,img), Point(20, 300,img)]
#
# binaryImg = p.regionGrow(seeds, 10)
# cv2.imshow(' ', binaryImg)
# cv2.waitKey(0)
