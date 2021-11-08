import cv2
import numpy as np
np.seterr(divide='ignore', invalid='ignore')

class Binarisation:
    def __init__(self,image):
        self.image = image

    def Seuil(self,s):
         imageX = self.image.copy()
         # parcourir les lignes
         for i in range(1,imageX.shape[0]):
             # parcourir les colonnes
            for j in range(1,imageX.shape[1]):
                #si la valeur de pixel est inférieur que le seuil saisie alors ce valeur =0
                if imageX[i,j] < s:
                    imageX[i, j] = 0
                else:

                    imageX[i, j] = 255
         return imageX

    def Otsu(self):

        pixel_number = self.image.shape[0] * self.image.shape[1]
        mean_weigth = 1.0 / pixel_number #Ce que nous faites ici est de régler tous les pixels au-dessus du seuil
        his, bins = np.histogram(self.image, np.arange(0, 257))
        seuil_final = -1
        valeur_finale = -1
        intensity_arr = np.arange(256)
        for t in bins[1:-1]:  # This goes from 1 to 254 uint8 range (Pretty sure wont be those values)
            pcb = np.sum(his[:t])
            pcf = np.sum(his[t:])
            Wb = pcb * mean_weigth
            Wf = pcf * mean_weigth

            mub = np.sum(intensity_arr[:t] * his[:t]) / float(pcb)
            muf = np.sum(intensity_arr[t:] * his[t:]) / float(pcf)

            value = Wb * Wf * (mub - muf) ** 2

            if value > valeur_finale:
                seuil_final = t
                valeur_finale = value
        final_img = self.image.copy()
        print(seuil_final)
        final_img[self.image > seuil_final] = 255
        final_img[self.image < seuil_final] = 0
        return final_img