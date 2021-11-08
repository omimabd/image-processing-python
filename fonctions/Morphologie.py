import numpy as np
class Morphologie:

    def __init__(self,image):
        self.image = image

    def Dilatation1(self,h):
        img = self.image.copy()
        Dilate = [0] * (img.shape[1] - 2) * (img.shape[0] - 2)
        h = 0
        for i in range(1, img.shape[0] - 1):
            for j in range(1, img.shape[1] - 1):
                Dilate[h] = max(
                    [img[i - 1][j - 1], img[i][j - 1], img[i + 1][j - 1], img[i - 1][j], img[i][j], img[i + 1][j],
                     img[i - 1][j + 1], img[i][j + 1], img[i + 1][j + 1]])

                h += 1

        Dilate = np.array(Dilate)
        Dilate = np.reshape(Dilate, (img.shape[0] - 2, img.shape[1] - 2))
        return Dilate

    def dilatation(self, H):
        imagecopy = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                s = 0;
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        s = s + self.image[k, l] * H[k - i + 1][l - j + 1]
                if (s == 0):
                    imagecopy[i][j] = 0
                else:
                    imagecopy[i][j] = 255
        return imagecopy

    def Erosion(self, H):
        imagecopy = self.image.copy()

        for i in range(0, self.image.shape[0]):
            for j in range(0, self.image.shape[1]):
                if (self.image[i][j] > 128):
                    self.image[i][j] = 255
                else:
                    self.image[i][j] = 0

        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                s = 0;
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        s = s + self.image[k, l] * H[k - i + 1][l - j + 1]
                if (s == 2295):
                    imagecopy[i][j] = 255
                else:
                    imagecopy[i][j] = 0
        return imagecopy

    def Ouverture(self, H):
        img = self.Erosion(self.image, H)
        image1 = self.dilatation(img, H)
        return image1

    def Fermeture(self, H):
        img = self.Erosion(self.image, H)
        image1 = self.Dilatation1(img, H)
        return image1
