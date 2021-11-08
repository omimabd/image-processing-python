
# quelques fonctions prend beaucoup de temps pour être exécutées (surtout de Kirsch)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QFileDialog, QLabel, QTextEdit, \
    QVBoxLayout, qApp
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from teest import *
from growing import Point



from PyQt5.QtGui import QPixmap
import cv2
from cv2 import *
from matplotlib.pyplot import *
import sys
import numpy as np
from numpy import *
import numpy as np

from random import randint
from matplotlib import pyplot as plt
from PIL import Image

from filtres import Filtres
from operations import *
from binarisation import *
from contours import *
from Morphologie import *
from growing import *
from segmentation import Segmentation


class Ui_OtherWindow(QtWidgets.QWidget):
    path = ''

    def setupUi(self, OtherWindow):
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(818, 600)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 167, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 167, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 167, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 167, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        OtherWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 231, 111))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 50, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(570, 110, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 110, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_R = QtWidgets.QLabel(self.centralwidget)
        self.label_R.setGeometry(QtCore.QRect(450, 190, 361, 351))
        self.label_R.setObjectName("label_R")
        self.label_Ori = QtWidgets.QLabel(self.centralwidget)
        self.label_Ori.setGeometry(QtCore.QRect(10, 190, 361, 351))
        self.label_Ori.setObjectName("label_Ori")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(390, 140, 31, 381))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 70, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 70, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(160, 70, 121, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(590, 70, 121, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        OtherWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OtherWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 818, 21))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuOperations = QtWidgets.QMenu(self.menubar)
        self.menuOperations.setObjectName("menuOperations")
        self.menuHistogramme = QtWidgets.QMenu(self.menuOperations)
        self.menuHistogramme.setObjectName("menuHistogramme")
        self.histoColor = QtWidgets.QMenu(self.menuHistogramme)
        self.histoColor.setObjectName("histoColor")
        self.menuBinarisation = QtWidgets.QMenu(self.menuOperations)
        self.menuBinarisation.setObjectName("menuBinarisation")
        self.menuFiltrage = QtWidgets.QMenu(self.menubar)
        self.menuFiltrage.setObjectName("menuFiltrage")
        self.menuGaussien = QtWidgets.QMenu(self.menuFiltrage)
        self.menuGaussien.setObjectName("menuGaussien")
        self.menuM_dian = QtWidgets.QMenu(self.menuFiltrage)
        self.menuM_dian.setObjectName("menuM_dian")
        self.menuMoyenneur = QtWidgets.QMenu(self.menuFiltrage)
        self.menuMoyenneur.setObjectName("menuMoyenneur")
        self.menuExtraire_des_contours = QtWidgets.QMenu(self.menubar)
        self.menuExtraire_des_contours.setObjectName("menuExtraire_des_contours")
        self.menuMorphologie = QtWidgets.QMenu(self.menubar)
        self.menuMorphologie.setObjectName("menuMorphologie")
        self.menuSegmentation = QtWidgets.QMenu(self.menubar)
        self.menuSegmentation.setObjectName("menuSegmentation")
        self.menuExtraire_les_points_d_int_r_t = QtWidgets.QMenu(self.menubar)
        self.menuExtraire_les_points_d_int_r_t.setObjectName("menuExtraire_les_points_d_int_r_t")
        self.menu_Hough = QtWidgets.QMenu(self.menubar)
        self.menu_Hough.setObjectName("menu_Hough")
        OtherWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OtherWindow)
        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)
        self.actionOuvrir = QtWidgets.QAction(OtherWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionOuvrir.setFont(font)
        self.actionOuvrir.setObjectName("actionOuvrir")
        self.actionEnregistrer = QtWidgets.QAction(OtherWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionEnregistrer.setFont(font)
        self.actionEnregistrer.setObjectName("actionEnregistrer")
        self.actionReset_2 = QtWidgets.QAction(OtherWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionReset_2.setFont(font)
        self.actionReset_2.setObjectName("actionReset_2")
        self.actionNegative = QtWidgets.QAction(OtherWindow)
        self.actionNegative.setObjectName("actionNegative")
        self.action = QtWidgets.QAction(OtherWindow)
        self.action.setObjectName("action")

        self.actionEtirement_2 = QtWidgets.QAction(OtherWindow)
        self.actionEtirement_2.setObjectName("actionEtirement_2")
        self.actionEgalization_2 = QtWidgets.QAction(OtherWindow)
        self.actionEgalization_2.setObjectName("actionEgalization_2")
        self.actionGlobale = QtWidgets.QAction(OtherWindow)
        self.actionGlobale.setObjectName("actionGlobale")
        self.actionManuel = QtWidgets.QAction(OtherWindow)
        self.actionManuel.setObjectName("actionManuel")
        self.actionGradient = QtWidgets.QAction(OtherWindow)
        self.actionGradient.setObjectName("actionGradient")
        self.actionSobel = QtWidgets.QAction(OtherWindow)
        self.actionSobel.setObjectName("actionSobel")
        self.actionKirsch = QtWidgets.QAction(OtherWindow)
        self.actionKirsch.setObjectName("actionKirsch")
        self.actionRobinson = QtWidgets.QAction(OtherWindow)
        self.actionRobinson.setObjectName("actionRobinson")
        self.actionLaplacien = QtWidgets.QAction(OtherWindow)
        self.actionLaplacien.setObjectName("actionLaplacien")
        self.actionErosion = QtWidgets.QAction(OtherWindow)
        self.actionErosion.setObjectName("actionErosion")
        self.actionDilatation = QtWidgets.QAction(OtherWindow)
        self.actionDilatation.setObjectName("actionDilatation")
        self.actionOuverture = QtWidgets.QAction(OtherWindow)
        self.actionOuverture.setObjectName("actionOuverture")
        self.actionFermeture = QtWidgets.QAction(OtherWindow)
        self.actionFermeture.setObjectName("actionFermeture")
        self.actionCroissance_de_r_gions = QtWidgets.QAction(OtherWindow)
        self.actionCroissance_de_r_gions.setObjectName("actionCroissance_de_r_gions")
        self.actionPartition_de_r_gions = QtWidgets.QAction(OtherWindow)
        self.actionPartition_de_r_gions.setObjectName("actionPartition_de_r_gions")
        self.actionM_thode_des_k_means = QtWidgets.QAction(OtherWindow)
        self.actionM_thode_des_k_means.setObjectName("actionM_thode_des_k_means")
        self.actionM_thode_Sift = QtWidgets.QAction(OtherWindow)
        self.actionM_thode_Sift.setObjectName("actionM_thode_Sift")
        self.actionM_thode_Harris = QtWidgets.QAction(OtherWindow)
        self.actionM_thode_Harris.setObjectName("actionM_thode_Harris")
        self.actionExtraire_des_lignes = QtWidgets.QAction(OtherWindow)
        self.actionExtraire_des_lignes.setObjectName("actionExtraire_des_lignes")
        self.actiondes_cercles = QtWidgets.QAction(OtherWindow)
        self.actiondes_cercles.setObjectName("actiondes_cercles")
        self.actions_0_1 = QtWidgets.QAction(OtherWindow)
        self.actions_0_1.setObjectName("actions_0_1")
        self.actions_0_2 = QtWidgets.QAction(OtherWindow)
        self.actions_0_2.setObjectName("actions_0_2")
        self.actions_0_8 = QtWidgets.QAction(OtherWindow)
        self.actions_0_8.setObjectName("actions_0_8")
        self.action3_3 = QtWidgets.QAction(OtherWindow)
        self.action3_3.setObjectName("action3_3")

        self.action3_4 = QtWidgets.QAction(OtherWindow)
        self.action3_4.setObjectName("action3_4")

        self.actionQuitter = QtWidgets.QAction(OtherWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionQuitter.setFont(font)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionS_lectionner_manuellement = QtWidgets.QAction(OtherWindow)
        self.actionS_lectionner_manuellement.setObjectName("actionS_lectionner_manuellement")
        self.actionniveaux_de_gris = QtWidgets.QAction(OtherWindow)
        self.actionniveaux_de_gris.setObjectName("actionniveaux_de_gris")
        self.actioncouleur = QtWidgets.QAction(OtherWindow)
        self.actioncouleur.setObjectName("actioncouleur")
        self.menuFichier.addAction(self.actionOuvrir)
        self.menuFichier.addAction(self.actionEnregistrer)
        self.menuFichier.addAction(self.actionReset_2)
        self.menuFichier.addAction(self.actionQuitter)
        self.histoColor.addAction(self.actionniveaux_de_gris)
        self.histoColor.addAction(self.actioncouleur)
        self.menuHistogramme.addAction(self.histoColor.menuAction())

        self.menuHistogramme.addAction(self.actionEtirement_2)
        self.menuHistogramme.addAction(self.actionEgalization_2)
        self.menuBinarisation.addAction(self.actionGlobale)
        self.menuBinarisation.addAction(self.actionManuel)
        self.menuOperations.addAction(self.actionNegative)
        self.menuOperations.addSeparator()
        self.menuOperations.addAction(self.menuHistogramme.menuAction())
        self.menuOperations.addSeparator()
        self.menuOperations.addAction(self.menuBinarisation.menuAction())
        self.menuOperations.addSeparator()
        self.menuOperations.addAction(self.actionS_lectionner_manuellement)
        self.menuGaussien.addAction(self.actions_0_1)
        self.menuGaussien.addAction(self.actions_0_8)
        self.menuGaussien.addAction(self.actions_0_2)
        self.menuM_dian.addAction(self.action3_3)

        self.menuMoyenneur.addAction(self.action3_4)

        self.menuFiltrage.addAction(self.menuGaussien.menuAction())
        self.menuFiltrage.addAction(self.menuM_dian.menuAction())
        self.menuFiltrage.addAction(self.menuMoyenneur.menuAction())
        self.menuExtraire_des_contours.addAction(self.actionGradient)
        self.menuExtraire_des_contours.addAction(self.actionSobel)
        self.menuExtraire_des_contours.addAction(self.actionKirsch)
        self.menuExtraire_des_contours.addAction(self.actionRobinson)
        self.menuExtraire_des_contours.addAction(self.actionLaplacien)
        self.menuMorphologie.addAction(self.actionErosion)
        self.menuMorphologie.addAction(self.actionDilatation)
        self.menuMorphologie.addAction(self.actionOuverture)
        self.menuMorphologie.addAction(self.actionFermeture)
        self.menuSegmentation.addAction(self.actionCroissance_de_r_gions)
        self.menuSegmentation.addAction(self.actionPartition_de_r_gions)
        self.menuSegmentation.addAction(self.actionM_thode_des_k_means)
        self.menuExtraire_les_points_d_int_r_t.addAction(self.actionM_thode_Sift)
        self.menuExtraire_les_points_d_int_r_t.addAction(self.actionM_thode_Harris)
        self.menu_Hough.addAction(self.actionExtraire_des_lignes)
        self.menu_Hough.addAction(self.actiondes_cercles)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuOperations.menuAction())
        self.menubar.addAction(self.menuFiltrage.menuAction())
        self.menubar.addAction(self.menuExtraire_des_contours.menuAction())
        self.menubar.addAction(self.menuMorphologie.menuAction())
        self.menubar.addAction(self.menuSegmentation.menuAction())
        self.menubar.addAction(self.menuExtraire_les_points_d_int_r_t.menuAction())
        self.menubar.addAction(self.menu_Hough.menuAction())

        self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "Traitement d'image : Boudouaia Oumayma"))
        self.label.setText(_translate("OtherWindow", "Saisir L'ongle de rotation"))
        self.label_2.setText(_translate("OtherWindow", "Saisir un pourcentage"))
        self.label_3.setText(_translate("OtherWindow", "Image Resultat"))
        self.label_4.setText(_translate("OtherWindow", "Image Originale"))
        self.label_R.setText(_translate("OtherWindow", "resultat"))
        self.label_Ori.setText(_translate("OtherWindow", "Originale"))
        self.pushButton.setText(_translate("OtherWindow", "Tourner"))
        self.pushButton_2.setText(_translate("OtherWindow", "Redemenssioner"))
        self.menuFichier.setTitle(_translate("OtherWindow", "Fichier"))
        self.menuOperations.setTitle(_translate("OtherWindow", "Operations"))
        self.menuHistogramme.setTitle(_translate("OtherWindow", "Histogramme"))
        self.histoColor.setTitle(_translate("OtherWindow", "Histogramme"))
        self.menuBinarisation.setTitle(_translate("OtherWindow", "Binarisation "))
        self.menuFiltrage.setTitle(_translate("OtherWindow", "Filtrage"))
        self.menuGaussien.setTitle(_translate("OtherWindow", "Gaussien "))
        self.menuM_dian.setTitle(_translate("OtherWindow", "Médian"))
        self.menuMoyenneur.setTitle(_translate("OtherWindow", "Moyenneur"))
        self.menuExtraire_des_contours.setTitle(_translate("OtherWindow", "Extraction des contours "))
        self.menuMorphologie.setTitle(_translate("OtherWindow", "Morphologie "))
        self.menuSegmentation.setTitle(_translate("OtherWindow", "Segmentation"))
        self.menuExtraire_les_points_d_int_r_t.setTitle(_translate("OtherWindow", "Extraction les points d’intérêt"))
        self.menu_Hough.setTitle(_translate("OtherWindow", " Hough "))
        self.actionOuvrir.setText(_translate("OtherWindow", "Ouvrir"))
        self.actionOuvrir.setShortcut(_translate("OtherWindow", "Ctrl+N"))
        self.actionEnregistrer.setText(_translate("OtherWindow", "Enregistrer"))
        self.actionEnregistrer.setShortcut(_translate("OtherWindow", "Ctrl+S"))
        self.actionReset_2.setText(_translate("OtherWindow", "Réinitialiser"))
        self.actionReset_2.setShortcut(_translate("OtherWindow", "Ctrl+R"))
        self.actionNegative.setText(_translate("OtherWindow", "Negative"))
        self.action.setText(_translate("OtherWindow", "Etirement"))

        self.actionEtirement_2.setText(_translate("OtherWindow", "Etirement"))
        self.actionEgalization_2.setText(_translate("OtherWindow", "Egalization"))
        self.actionGlobale.setText(_translate("OtherWindow", "Seuillage manuel"))
        self.actionManuel.setText(_translate("OtherWindow", "Algorithme d\'otsu"))
        self.actionGradient.setText(_translate("OtherWindow", "Gradient "))
        self.actionSobel.setText(_translate("OtherWindow", "Sobel"))
        self.actionKirsch.setText(_translate("OtherWindow", "Kirsch"))
        self.actionRobinson.setText(_translate("OtherWindow", "Robinson"))
        self.actionLaplacien.setText(_translate("OtherWindow", "Laplacien"))
        self.actionErosion.setText(_translate("OtherWindow", "Erosion "))
        self.actionDilatation.setText(_translate("OtherWindow", "Dilatation"))
        self.actionOuverture.setText(_translate("OtherWindow", "Ouverture"))
        self.actionFermeture.setText(_translate("OtherWindow", "Fermeture"))
        self.actionCroissance_de_r_gions.setText(_translate("OtherWindow", "Croissance de régions"))
        self.actionPartition_de_r_gions.setText(_translate("OtherWindow", "Partition de régions"))
        self.actionM_thode_des_k_means.setText(_translate("OtherWindow", "Méthode des k-means"))
        self.actionM_thode_Sift.setText(_translate("OtherWindow", "Méthode Sift"))
        self.actionM_thode_Harris.setText(_translate("OtherWindow", "Méthode Harris "))
        self.actionExtraire_des_lignes.setText(_translate("OtherWindow", "Extraire des lignes"))
        self.actiondes_cercles.setText(_translate("OtherWindow", "Extraire des cercles"))
        self.actions_0_1.setText(_translate("OtherWindow", "s=0.2"))
        self.actions_0_2.setText(_translate("OtherWindow", "s=0.8"))
        self.actions_0_8.setText(_translate("OtherWindow", "s=0.4"))
        self.action3_3.setText(_translate("OtherWindow", "3*3"))
        self.actionniveaux_de_gris.setText(_translate("OtherWindow", "niveaux de gris"))
        self.actioncouleur.setText(_translate("OtherWindow", "couleur"))

        self.action3_4.setText(_translate("OtherWindow", "3*3"))

        self.actionQuitter.setText(_translate("OtherWindow", "Quitter"))
        self.actionQuitter.setShortcut(_translate("OtherWindow", "Esc"))
        self.actionS_lectionner_manuellement.setText(_translate("OtherWindow", "Sélectionner manuellement "))

        # ici on controlle les action de chaque element

        self.actionS_lectionner_manuellement.triggered.connect(self.selectionner)
        self.actionOuvrir.triggered.connect(self.openFile)
        self.actionQuitter.triggered.connect(self.quit_trigger)
        self.actionEnregistrer.triggered.connect(self.enregistrer)
        self.actionNegative.triggered.connect(self.negatif)
        self.actionReset_2.triggered.connect(self.rest)

        self.actionEtirement_2.triggered.connect(self.Etirer)
        self.actionEgalization_2.triggered.connect(self.Egaliser)
        self.actions_0_1.triggered.connect(self.gaussian1)
        self.actions_0_8.triggered.connect(self.gaussian2)
        self.actions_0_2.triggered.connect(self.gaussian3)
        self.action3_3.triggered.connect(self.median)
        self.action3_4.triggered.connect(self.moyenneur)
        self.actionGlobale.triggered.connect(self.binarise)
        self.actionManuel.triggered.connect(self.Otsu)
        self.actionGradient.triggered.connect(self.grad)
        self.actionSobel.triggered.connect(self.Sobel)
        self.actionRobinson.triggered.connect(self.Robinson)
        self.actionLaplacien.triggered.connect(self.laplacien)
        self.actionErosion.triggered.connect(self.Erosion)
        self.actionDilatation.triggered.connect(self.dilatation)
        self.actionOuverture.triggered.connect(self.ouverture)
        self.actionFermeture.triggered.connect(self.fermeture)
        self.actionCroissance_de_r_gions.triggered.connect(self.GrowingRegii)
        self.actionM_thode_Sift.triggered.connect(self.Sift)
        self.actionM_thode_Harris.triggered.connect(self.Harris)
        self.actiondes_cercles.triggered.connect(self.CerclesHough)
        self.actionExtraire_des_lignes.triggered.connect(self.LinesHough)
        self.actionM_thode_des_k_means.triggered.connect(self.kmeans)
        self.actionKirsch.triggered.connect(self.kirsch)
        self.actionniveaux_de_gris.triggered.connect(self.histoN)
        self.actioncouleur.triggered.connect(self.histoC)


        self.pushButton.clicked.connect(self.rotation)
        self.pushButton_2.clicked.connect(self.redimention)

    #pour quitter l'interface graphique , on utilise cette requete

    def quit_trigger(self):
        qApp.quit()

    #pour réinitialiser notre résultat est notre image originale
    def rest(self):
        self.label_Ori.setText(" ")
        self.label_R.setText(" ")

    # pour ouvrir l'image qui on va traiter
    def openFile(self):
        nom_fichier = QFileDialog.getOpenFileName()
        self.path = nom_fichier[0]
        pathx = self.path

        # on utilise QPixmap pour représenter notre image dans notre GUI
        pixmap = QtGui.QPixmap(pathx)
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)

        # on va mettre la photo dans label
        self.label_Ori.setPixmap(QtGui.QPixmap(pixmap4))
        self.label_Ori.adjustSize()

    # pour sauvegarder la photo résultat avec la requete 'cv2.imwrite()'
    def enregistrer(self):
        fileName = QFileDialog.getSaveFileName(None, 'some text', "untitled.png",
                                               "Image Files (*.jpg *.gif *.bmp *.png)")
        self.fileName = fileName[0]

        cv2.imwrite(fileName[0], self.mat)


    def negatif(self):
        image = cv2.imread(self.path)
        img = 255 - image
        self.mat = img
        # pour obtenir la taille de l'image et les octets (byte= 1 octet)
        height, width, byteValue = img.shape

        print(byteValue) # affichage des octets utilisées

        # si le nbr de octets = 3 alors :
        if byteValue == 3:

            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # ici on reformate  l'image en RGB888.
            # Utilisez 4 octets par pixel au lieu de 3, car Numpy ne prend pas en charge 3.
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)

        # sinon
        else:

            #img.shape [1]: largeur de l'image, img.shape [0]: hauteur de l'image, img.shape [2]: numéro de canal de l'image
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)

        #pour afficher notre image resultat
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        self.label_R.setPixmap(QtGui.QPixmap(pixmap4))
        self.label_R.adjustSize()

    def selectionner(self):


        # image_path
        img_path = self.path

        # read image
        img_raw = cv2.imread(img_path)

        # la fonction ROI pour faire la selection
        roi = cv2.selectROI(img_raw)



        # Recadrer le ROI sélectionné à partir de notre image
        roi_cropped = img_raw[int(roi[1]):int(roi[1] + roi[3]), int(roi[0]):int(roi[0] + roi[2])]

        random = randint(1, 2000)
        print("rand", random)
        x = "image" + str(random)
        print("0")
        cv2.imwrite("resultats//"+x+".jpg",roi_cropped)
        print("1")
        pixmap = QtGui.QPixmap("resultats//" + x + ".jpg")
        print("2")
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        print("3")
        self.label_R.setPixmap(pixmap4)
        self.label_R.adjustSize()




    def rotation(self):

         #on recupere la valeur entrée par utilisateur
        angle = int(self.textEdit.toPlainText())
        image = cv2.imread(self.path)

        #on faire l'appele a la fonction rotate_image qui prend angle comme parametre
        o = Operations(image)
        img = o.rotate_image(angle)
         # forme matricielle
        self.mat = img
        height, width, byteValue = img.shape
        print(byteValue)
        if byteValue == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        self.label_R.setPixmap(QtGui.QPixmap(pixmap4))
        self.label_R.adjustSize()

    def redimention(self):
        image = cv2.imread(self.path)
        pourcentage = int(self.textEdit_2.toPlainText())
        scale_percent = pourcentage
        #traitement sur les lignes
        width = int(image.shape[1] * scale_percent / 100)
        #traitement sur les colonnes
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        # redimensionner par fonction resize
        img = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        self.mat = img
        height, width, byteValue = img.shape
        print(byteValue)
        if byteValue == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        self.label_R.setPixmap(QtGui.QPixmap(pixmap4))
        self.label_R.adjustSize()

    # histogramme de niveaux de gris
    def histoN(self):

        img = cv.imread(self.path, cv.IMREAD_GRAYSCALE)
        roihist = cv.calcHist([img], [0], None, [256], [0, 256])
        xs = np.linspace(0, 255, 256)

        # plt.subplot(1, 1, 1)
        plt.title("L'histogramme à niveaux de gris")
        plt.plot(xs, roihist, color='k')
        plt.show()
        random = randint(1, 2000)
        print("rand",random)
        x = "image" + str(random)
        print("0")
        plt.savefig("resultats//" + x + ".jpg")
        print("1")
        pixmap = QtGui.QPixmap("resultats//" + x + ".jpg")
        print("2")
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        print("3")
        self.label_R.setPixmap(pixmap4)
        self.label_R.adjustSize()

    # histogramme de couleurs

    def histoC(self):


        img = cv.imread(self.path, cv.IMREAD_COLOR)
        color = ('b', 'g', 'r')

        plt.title("L'histogramme à couleur")
        for i, col in enumerate(color):
            histr = cv.calcHist([img], [i], None, [256], [0, 256])
            plt.plot(histr, color=col)
            plt.xlim([0, 256])
        plt.show()

        random = randint(1, 2000)
        print("rand", random)
        x = "image" + str(random)
        print("0")
        plt.savefig("resultats//" + x + ".jpg")
        print("1")
        pixmap = QtGui.QPixmap("resultats//" + x + ".jpg")
        print("2")
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        print("3")
        self.label_R.setPixmap(pixmap4)
        self.label_R.adjustSize()

    def Egaliser(self):
        image = cv2.imread(self.path)
        imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        o = Operations(imag)
        img = o.histeq()
        self.mat = img
        random = randint(1, 2000)
        print("rand", random)
        x = "image" + str(random)
        print("0")
        cv2.imwrite("resultats//" + x + ".jpg", img)
        print("1")
        pixmap = QtGui.QPixmap("resultats//" + x + ".jpg")
        print("2")
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        print("3")
        self.label_R.setPixmap(pixmap4)
        self.label_R.adjustSize()
        print("4")

    def Etirer(self):
        print("it's work")
        image = cv2.imread(self.path)
        imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        o = Operations(imag)
        img = o.etire()
        self.mat = img

        random = randint(1, 2000)
        print("rand", random)
        x = "image" + str(random)
        print("0")
        cv2.imwrite("resultats//" + x + ".jpg", img)
        print("1")
        pixmap = QtGui.QPixmap("resultats//" + x + ".jpg")
        print("2")
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        print("3")
        self.label_R.setPixmap(pixmap4)
        self.label_R.adjustSize()
        print("4")

    def binarise(self):
        # afficher une interface dialogue pour utilisateur pour saisir le seuil de binarisation
        name, test = QtWidgets.QInputDialog.getInt(self, 'Binarisation', 'Entrez le seuil: ')
        # si il a saisi le seuil , alors :
        if test:
            image = cv2.imread(self.path)
            height, width, byteValue = image.shape
            print(byteValue)
            if byteValue == 3:
                imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                f = Binarisation(imag)
                img = f.Seuil(name)
                self.mat = img
                img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
                imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
            else:
                f = Binarisation(image)
                img = f.Seuillage(name)
                self.mat = img
                imag = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
            pixmap = QtGui.QPixmap(imag)
            pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
            self.label_R.setPixmap(QtGui.QPixmap(pixmap4))
            self.label_R.adjustSize()



    def Otsu(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        if byteValue == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            b = Binarisation(image)
            img = b.Otsu()
            self.mat = img
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            b = Binarisation(image)
            img = b.Otsu()
            self.mat = img
            imag = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        self.label_R.setPixmap(QtGui.QPixmap(pixmap4))
        self.label_R.adjustSize()

    def gaussian1(self):
        image = cv2.imread(self.path)
        f = Filtres(image)
        img = f.Gaussien(0.2)
        self.mat = img
        height, width, byteValue = img.shape
        print(byteValue)
        if byteValue == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        self.label_R.setPixmap(QtGui.QPixmap(pixmap4))
        self.label_R.adjustSize()

    def gaussian2(self):
        image = cv2.imread(self.path)
        f = Filtres(image)
        img = f.Gaussien(0.4)
        self.mat = img
        height, width, byteValue = img.shape
        print(byteValue)
        if byteValue == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        self.label_R.setPixmap(QtGui.QPixmap(pixmap4))
        self.label_R.adjustSize()

    def gaussian3(self):
        image = cv2.imread(self.path)
        f = Filtres(image)
        img = f.Gaussien(0.8)
        self.mat = img
        height, width, byteValue = img.shape
        print(byteValue)
        if byteValue == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        self.label_R.setPixmap(QtGui.QPixmap(pixmap4))
        self.label_R.adjustSize()

    def median(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        if byteValue == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            f = Filtres(image)
            img = f.Median(3)
            self.mat = img
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            f = Filtres(image)
            img = f.Median(3)
            self.mat = img
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        self.label_R.setPixmap(QtGui.QPixmap(pixmap4))
        self.label_R.adjustSize()

    def moyenneur(self):
        image = cv2.imread(self.path)
        f = Filtres(image)
        img = f.Moyenneur(3)
        self.mat = img
        height, width, byteValue = img.shape
        print(byteValue)
        if byteValue == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        self.label_R.setPixmap(QtGui.QPixmap(pixmap4))
        self.label_R.adjustSize()

    def grad(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            c = Contours(imag)
            img = c.grad(20)
            self.mat = img
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            c = Contours(image)
            img = c.grad(20)
            self.mat = img
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)

        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        self.label_R.setPixmap(QtGui.QPixmap(pixmap4))
        self.label_R.adjustSize()

    def Robinson(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            c = Contours(imag)
            img = c.Robinson(20)
            self.mat = img
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            c = Contours(image)
            img = c.Robinson(20)
            self.mat = img
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)

        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        self.label_R.setPixmap(QtGui.QPixmap(pixmap4))
        self.label_R.adjustSize()


    def kirsch(self):
        image = cv2.imread(self.path,0)
        c=Contours(image)
        out=c.kirsch()


        print("22")
        # out=kirsch(image)
        print("44")
        random = randint(1, 2000)
        print("rand", random)
        x = "image" + str(random)
        print("0")
        cv2.imwrite("resultats//" + x + ".jpg", out)
        print("1")
        pixmap = QtGui.QPixmap("resultats//" + x + ".jpg")
        print("2")
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        print("3")
        self.label_R.setPixmap(pixmap4)
        self.label_R.adjustSize()
        print("4")

    def Sobel(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            c = Contours(imag)
            img = c.Sobel(50)
            self.mat = img
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            c = Contours(image)
            img = c.Sobel(50)
            self.mat = img
            imag = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)

        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        self.label_R.setPixmap(QtGui.QPixmap(pixmap4))
        self.label_R.adjustSize()

    def laplacien(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            c = Contours(imag)
            img = c.Laplacien(20)
            self.mat = img
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            c = Contours(image)
            img = c.Laplacien(20)
            self.mat = img
            imag = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        self.label_R.setPixmap(QtGui.QPixmap(pixmap4))
        self.label_R.adjustSize()

    def Erosion(self):
        image = cv2.imread(self.path)

        imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        m = Morphologie(imag)
        h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        img = m.Erosion(h)
        self.mat = img

        random = randint(1, 2000)
        print("rand", random)
        x = "image" + str(random)
        print("0")
        cv2.imwrite("resultats//" + x + ".jpg", img)


        print("1")
        pixmap = QtGui.QPixmap("resultats//" + x + ".jpg")
        print("2")
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        print("3")
        self.label_R.setPixmap(pixmap4)
        self.label_R.adjustSize()
        print("4")

    def dilatation(self):
        image = cv2.imread(self.path)

        imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        m = Morphologie(imag)
        h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        img = m.Dilatation1(h)
        self.mat = img

        random = randint(1, 2000)
        print("rand", random)
        x = "image" + str(random)
        print("0")
        cv2.imwrite("resultats//" + x + ".jpg", img)

        print("1")
        pixmap = QtGui.QPixmap("resultats//" + x + ".jpg")
        print("2")
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        print("3")
        self.label_R.setPixmap(pixmap4)
        self.label_R.adjustSize()
        print("4")

    def ouverture(self):
        image = cv2.imread(self.path)

        imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        m = Morphologie(imag)
        h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        imaag = m.Erosion(h)
        m1 = Morphologie(imaag)

        h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        img = m1.dilatation(h)
        self.mat = img

        random = randint(1, 2000)
        print("rand", random)
        x = "image" + str(random)
        print("0")
        cv2.imwrite("resultats//" + x + ".jpg", img)

        print("1")
        pixmap = QtGui.QPixmap("resultats//" + x + ".jpg")
        print("2")
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        print("3")
        self.label_R.setPixmap(pixmap4)
        self.label_R.adjustSize()
        print("4")

    def fermeture(self):
        image = cv2.imread(self.path)

        imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        m = Morphologie(imag)
        h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        imaag = m.Dilatation1(h)
        m1 = Morphologie(imaag)
        h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        img = m1.Erosion(h)
        self.mat = img

        random = randint(1, 2000)
        print("rand", random)
        x = "image" + str(random)
        print("0")
        cv2.imwrite("resultats//" + x + ".jpg", img)

        print("1")
        pixmap = QtGui.QPixmap("resultats//" + x + ".jpg")
        print("2")
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        print("3")
        self.label_R.setPixmap(pixmap4)
        self.label_R.adjustSize()
        print("4")

    def GrowingRegii(self):
        # def on_mouse(event, x, y, flags, params):
        #     if event == cv2.EVENT_LBUTTONDOWN:
        #         print('Seed: ' + 'Point' + '(' + str(x) + ', ' + str(y) + ')', img[y, x])
        #         clicks.append((y, x))
        # clicks = []
        # image = cv2.imread(self.path)
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # ret, img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
        # cv2.namedWindow('Input')
        # cv2.setMouseCallback('Input', on_mouse, 0, )
        # cv2.imshow('Input', img)
        # cv2.waitKey()
        # seed = clicks[-1]
        # out = region_growing(img, seed)
        # cv2.imshow('Region Growing', out)
        # cv2.waitKey()
        # image = QtGui.QImage(out.data, out.shape[1], out.shape[0], QtGui.QImage.Format_Grayscale8)
        # pixmap = QtGui.QPixmap(image)
        # pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        # self.label_R.setPixmap(QtGui.QPixmap(pixmap4))
        # self.label_R.adjustSize()
        image=cv2.imread(self.path,0)

        seeds = [Point(10, 10), Point(82, 150), Point(20, 300)]
        out = regionGrow(image, seeds, 10)

        random = randint(1, 2000)
        print("rand", random)
        x = "image" + str(random)
        print("0")
        cv2.imwrite("resultats//" + x + ".jpg", out)

        print("1")
        pixmap = QtGui.QPixmap("resultats//" + x + ".jpg")
        print("2")
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        print("3")
        self.label_R.setPixmap(pixmap4)
        self.label_R.adjustSize()
        print("4")
        cv2.imshow("",out)
        cv2.waitKey()

    def Sift(self):
        img = cv2.imread(self.path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        sift = cv2.SIFT_create()
        kp = sift.detect(gray, None)
        img = cv2.drawKeypoints(gray, kp, img)
        random = randint(1, 2000)
        print("rand", random)
        x = "image" + str(random)
        print("0")
        cv2.imwrite("resultats//" + x + ".jpg", img)
        print("1")
        pixmap = QtGui.QPixmap("resultats//" + x + ".jpg")
        print("2")
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        print("3")
        self.label_R.setPixmap(pixmap4)
        self.label_R.adjustSize()
        print("4")


    def Harris(self):
        # filename = 'NY.jpg'
        img = cv2.imread(self.path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        gray = np.float32(gray)
        dst = cv2.cornerHarris(gray, 2, 3, 0.04)

        # Threshold for an optimal value, it may vary depending on the image.
        img[dst > 0.01 * dst.max()] = [0, 0, 255]
        # img = cv2.imread(cv2.samples.findFile(self.path))
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # edges = cv2.Canny(gray, 50, 150, apertureSize=3)
        # lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
        # for line in lines:
        #     rho, theta = line[0]
        #     a = np.cos(theta)
        #     b = np.sin(theta)
        #     x0 = a * rho
        #     y0 = b * rho
        #     x1 = int(x0 + 1000 * (-b))
        #     y1 = int(y0 + 1000 * (a))
        #     x2 = int(x0 - 1000 * (-b))
        #     y2 = int(y0 - 1000 * (a))
        #     cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

        random = randint(1, 2000)
        print("rand", random)
        x = "image" + str(random)
        print("0")
        cv2.imwrite("resultats//" + x + ".jpg", img)
        print("1")
        pixmap = QtGui.QPixmap("resultats//" + x + ".jpg")
        print("2")
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        print("3")
        self.label_R.setPixmap(pixmap4)
        self.label_R.adjustSize()
        print("4")

    def CerclesHough(self):
        # image = cv2.imread(self.path)
        # output = image.copy()
        # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # # detect circles in the image
        # circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
        # # ensure at least some circles were found
        # if circles is not None:
        #     # convert the (x, y) coordinates and radius of the circles to integers
        #     circles = np.round(circles[0, :]).astype("int")
        #     # loop over the (x, y) coordinates and radius of the circles
        #     for (x, y, r) in circles:
        #         # draw the circle in the output image, then draw a rectangle
        #         # corresponding to the center of the circle
        #         cv2.circle(output, (x, y), r, (0, 255, 0), 4)
        #         cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
        #     # show the output image
        #     random = randint(1, 2000)
        #     print("rand", random)
        #     x = "image" + str(random)
        #     print("0")
        #     cv2.imwrite("resultats//" + x + ".jpg", output)
        #     print("1")
        #     pixmap = QtGui.QPixmap("resultats//" + x + ".jpg")
        #     print("2")
        #     pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        #     print("3")
        #     self.label_R.setPixmap(pixmap4)
        #     self.label_R.adjustSize()
        #     print("4")
        bgr_img = cv2.imread(self.path)  # read as it is

        if bgr_img.shape[-1] == 3:  # color image
            b, g, r = cv2.split(bgr_img)  # get b,g,r

            gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
        else:
            gray_img = bgr_img

        img = cv2.medianBlur(gray_img, 5)
        cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

        circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20,
                                   param1=50, param2=30, minRadius=0, maxRadius=0)

        circles = np.uint16(np.around(circles))

        for i in circles[0, :]:
            # draw the outer circle
            cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

        # plt.subplot(121), plt.imshow(rgb_img)
        # plt.title('Input Image'), plt.xticks([]), plt.yticks([])
        # plt.subplot(122), plt.imshow(cimg)
        # plt.title('Hough Transform'), plt.xticks([]), plt.yticks([])
        # plt.show()
        random = randint(1, 2000)
        print("rand", random)
        x = "image" + str(random)
        print("0")
        cv2.imwrite("resultats//" + x + ".jpg", cimg)
        print("1")
        pixmap = QtGui.QPixmap("resultats//" + x + ".jpg")
        print("2")
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        print("3")
        self.label_R.setPixmap(pixmap4)
        self.label_R.adjustSize()
        print("4")

    def LinesHough(self):
        def drawhoughLinesOnImage(image, houghLines):
            for line in houghLines:
                for rho, theta in line:
                    a = np.cos(theta)
                    b = np.sin(theta)
                    x0 = a * rho
                    y0 = b * rho
                    x1 = int(x0 + 1000 * (-b))
                    y1 = int(y0 + 1000 * (a))
                    x2 = int(x0 - 1000 * (-b))
                    y2 = int(y0 - 1000 * (a))

                    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

        def blend_images(image, final_image, alpha=0.7, beta=1., gamma=0.):
            return cv2.addWeighted(final_image, alpha, image, beta, gamma)

        image = cv2.imread(self.path)  # load image in grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        blurredImage = cv2.GaussianBlur(gray_image, (5, 5), 0)
        edgeImage = cv2.Canny(blurredImage, 50, 120)

        # Detect points that form a line
        dis_reso = 1  # Distance resolution in pixels of the Hough grid
        theta = np.pi / 180  # Angular resolution in radians of the Hough grid
        threshold = 170  # minimum no of votes

        houghLines = cv2.HoughLines(edgeImage, dis_reso, theta, threshold)

        houghLinesImage = np.zeros_like(image)  # create and empty image

        drawhoughLinesOnImage(houghLinesImage, houghLines)  # draw the lines on the empty image
        orginalImageWithHoughLines = blend_images(houghLinesImage, image)  # add two images together, using image blending


        random = randint(1, 2000)
        print("rand", random)
        x = "image" + str(random)
        print("0")
        cv2.imwrite("resultats//" + x + ".jpg", orginalImageWithHoughLines)
        print("1")
        pixmap = QtGui.QPixmap("resultats//" + x + ".jpg")
        print("2")
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        print("3")
        self.label_R.setPixmap(pixmap4)
        self.label_R.adjustSize()
        print("4")

    def kmeans(self):
        image = cv2.imread(self.path)
        imag = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, byteValue = imag.shape
        s = Segmentation(imag)
        img = s.k_means()
        self.mat = img
        imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        self.label_R.setPixmap(pixmap4)
        self.label_R.adjustSize()








if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())
