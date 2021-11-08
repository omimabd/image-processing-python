# # import cv2
# # import numpy as np
# # from matplotlib import pyplot as plt
# #
# # # bgr_img = cv2.imread('squares2.png') # read as it is
# # #
# # # if bgr_img.shape[-1] == 3:           # color image
# # #     b,g,r = cv2.split(bgr_img)       # get b,g,r
# # #     rgb_img = cv2.merge([r,g,b])     # switch it to rgb
# # #     gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
# # # else:
# # #     gray_img = bgr_img
# # #
# # # img = cv2.medianBlur(gray_img, 5)
# # # cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
# # #
# # # circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
# # #                             param1=50,param2=30,minRadius=0,maxRadius=0)
# # #
# # # circles = np.uint16(np.around(circles))
# # #
# # # for i in circles[0,:]:
# # #     # draw the outer circle
# # #     cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
# # #     # draw the center of the circle
# # #     cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
# # #
# # # plt.subplot(121),plt.imshow(rgb_img)
# # # plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# # # plt.subplot(122),plt.imshow(cimg)
# # # plt.title('Hough Transform'), plt.xticks([]), plt.yticks([])
# # # plt.show()
# import cv2
# import numpy as np
# def kirsch(image):
#     m,n = image.shape
#     list=[]
#     kirsch = np.zeros((m,n))
#     for i in range(2,m-1):
#         for j in range(2,n-1):
#             d1 = np.square(5 * image[i - 1, j - 1] + 5 * image[i - 1, j] + 5 * image[i - 1, j + 1] -
#                   3 * image[i, j - 1] - 3 * image[i, j + 1] - 3 * image[i + 1, j - 1] -
#                   3 * image[i + 1, j] - 3 * image[i + 1, j + 1])
#             d2 = np.square((-3) * image[i - 1, j - 1] + 5 * image[i - 1, j] + 5 * image[i - 1, j + 1] -
#                   3 * image[i, j - 1] + 5 * image[i, j + 1] - 3 * image[i + 1, j - 1] -
#                   3 * image[i + 1, j] - 3 * image[i + 1, j + 1])
#             d3 = np.square((-3) * image[i - 1, j - 1] - 3 * image[i - 1, j] + 5 * image[i - 1, j + 1] -
#                   3 * image[i, j - 1] + 5 * image[i, j + 1] - 3 * image[i + 1, j - 1] -
#                   3 * image[i + 1, j] + 5 * image[i + 1, j + 1])
#             d4 = np.square((-3) * image[i - 1, j - 1] - 3 * image[i - 1, j] - 3 * image[i - 1, j + 1] -
#                   3 * image[i, j - 1] + 5 * image[i, j + 1] - 3 * image[i + 1, j - 1] +
#                   5 * image[i + 1, j] + 5 * image[i + 1, j + 1])
#             d5 = np.square((-3) * image[i - 1, j - 1] - 3 * image[i - 1, j] - 3 * image[i - 1, j + 1] - 3
#                   * image[i, j - 1] - 3 * image[i, j + 1] + 5 * image[i + 1, j - 1] +
#                   5 * image[i + 1, j] + 5 * image[i + 1, j + 1])
#             d6 = np.square((-3) * image[i - 1, j - 1] - 3 * image[i - 1, j] - 3 * image[i - 1, j + 1] +
#                   5 * image[i, j - 1] - 3 * image[i, j + 1] + 5 * image[i + 1, j - 1] +
#                   5 * image[i + 1, j] - 3 * image[i + 1, j + 1])
#             d7 = np.square(5 * image[i - 1, j - 1] - 3 * image[i - 1, j] - 3 * image[i - 1, j + 1] +
#                   5 * image[i, j - 1] - 3 * image[i, j + 1] + 5 * image[i + 1, j - 1] -
#                   3 * image[i + 1, j] - 3 * image[i + 1, j + 1])
#             d8 = np.square(5 * image[i - 1, j - 1] + 5 * image[i - 1, j] - 3 * image[i - 1, j + 1] +
#                   5 * image[i, j - 1] - 3 * image[i, j + 1] - 3 * image[i + 1, j - 1] -
#                   3 * image[i + 1, j] - 3 * image[i + 1, j + 1])
#
#                          # : Take the maximum value in each direction, the effect is not good, use another method
#             list=[d1, d2, d3, d4, d5, d6, d7, d8]
#             kirsch[i,j]= int(np.sqrt(max(list)))
#                          # : Rounding the die length in all directions
#             #kirsch[i, j] =int(np.sqrt(d1+d2+d3+d4+d5+d6+d7+d8))
#     for i in range(m):
#         for j in range(n):
#             if kirsch[i,j]>127:
#                 kirsch[i,j]=255
#             else:
#                 kirsch[i,j]=0
#     return kirsch
# image = cv2.imread('3-5-2019-8-42-57-pm.png',0)
# # image = cv2.resize(image,(800,800))
#
# out=kirsch(image)
# # output_6 = cv2.resize(out, (800, 600))
# cv2.imshow('sharpen_6 Image', out)
# cv2.waitKey()
#
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('3-5-2019-8-42-57-pm.png',cv.IMREAD_GRAYSCALE)
roihist = cv.calcHist([img],[0], None, [256], [ 0, 256] )
xs=np.linspace(0,255,256)

plt.subplot(2,1,1)
plt.title("niveau de gris")
plt.plot(xs,roihist,color='k')

img = cv.imread('3-5-2019-8-42-57-pm.png',cv.IMREAD_COLOR)
color = ('b','g','r')
plt.subplot(2,1,2)
plt.title("couleur")
for i,col in enumerate(color):
    histr = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()