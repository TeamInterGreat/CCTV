# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_test_2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import cv2
import numpy as np
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QImage, QFont
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, Qt, QObject, QEvent







class Ui_MainWindow(object):



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1058, 886)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.gridLayout.setObjectName("gridLayout")

        self.verticalLayout_main = QtWidgets.QVBoxLayout()
        self.verticalLayout_main.setObjectName("verticalLayout_main")

        self.horizontalLayout_cameraHolder = QtWidgets.QHBoxLayout()
        self.horizontalLayout_cameraHolder.setObjectName("horizontalLayout_cameraHolder")

        self.mainCamera = QtWidgets.QLabel(self.centralwidget)
        self.mainCamera.setMinimumSize(QtCore.QSize(640, 480))
        self.mainCamera.setMaximumSize(QtCore.QSize(640, 480))
        self.mainCamera.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.mainCamera.setMouseTracking(True)
        self.mainCamera.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.mainCamera.setText("")
        self.mainCamera.setScaledContents(False)
        self.mainCamera.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.mainCamera.setObjectName("mainCamera")

        self.horizontalLayout_cameraHolder.addWidget(self.mainCamera)
        self.verticalLayout_subCameraHolder = QtWidgets.QVBoxLayout()
        self.verticalLayout_subCameraHolder.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_subCameraHolder.setObjectName("verticalLayout_subCameraHolder")

        self.subCamera1 = QtWidgets.QLabel(self.centralwidget)
        self.subCamera1.setMaximumSize(QtCore.QSize(320, 237))
        self.subCamera1.setFrameShape(QtWidgets.QFrame.Box)
        self.subCamera1.setText("")
        self.subCamera1.setObjectName("subCamera1")
        self.verticalLayout_subCameraHolder.addWidget(self.subCamera1)

        self.subCamera2 = QtWidgets.QLabel(self.centralwidget)
        self.subCamera2.setMaximumSize(QtCore.QSize(320, 237))
        self.subCamera2.setFrameShape(QtWidgets.QFrame.Box)
        self.subCamera2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.subCamera2.setText("")
        self.subCamera2.setObjectName("subCamera2")
        self.verticalLayout_subCameraHolder.addWidget(self.subCamera2)
        self.horizontalLayout_cameraHolder.addLayout(self.verticalLayout_subCameraHolder)
        self.verticalLayout_main.addLayout(self.horizontalLayout_cameraHolder)

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 200))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 1046, 198))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_8)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.thumbnail_frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
        self.thumbnail_frame_2.setMaximumSize(QtCore.QSize(50, 120))
        self.thumbnail_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnail_frame_2.setObjectName("thumbnail_frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.thumbnail_frame_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.person_thumbnail_2 = QtWidgets.QLabel(self.thumbnail_frame_2)
        self.person_thumbnail_2.setMinimumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_2.setMaximumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.person_thumbnail_2.setText("")
        self.person_thumbnail_2.setObjectName("person_thumbnail_2")
        self.verticalLayout_6.addWidget(self.person_thumbnail_2)
        self.person_colorbar_2 = QtWidgets.QLabel(self.thumbnail_frame_2)
        self.person_colorbar_2.setMaximumSize(QtCore.QSize(50, 5))
        self.person_colorbar_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.person_colorbar_2.setText("")
        self.person_colorbar_2.setObjectName("person_colorbar_2")
        self.verticalLayout_6.addWidget(self.person_colorbar_2)
        self.gridLayout_3.addWidget(self.thumbnail_frame_2, 0, 2, 1, 1)
        self.thumbnail_frame_0 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
        self.thumbnail_frame_0.setMaximumSize(QtCore.QSize(50, 120))
        self.thumbnail_frame_0.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail_frame_0.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnail_frame_0.setObjectName("thumbnail_frame_0")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.thumbnail_frame_0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.person_thumbnail_0 = QtWidgets.QLabel(self.thumbnail_frame_0)
        self.person_thumbnail_0.setMinimumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_0.setMaximumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_0.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.person_thumbnail_0.setText("")
        self.person_thumbnail_0.setObjectName("person_thumbnail_0")
        self.verticalLayout.addWidget(self.person_thumbnail_0)
        self.person_colorbar_0 = QtWidgets.QLabel(self.thumbnail_frame_0)
        self.person_colorbar_0.setMaximumSize(QtCore.QSize(50, 5))
        self.person_colorbar_0.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.person_colorbar_0.setText("")
        self.person_colorbar_0.setObjectName("person_colorbar_0")
        self.verticalLayout.addWidget(self.person_colorbar_0)
        self.gridLayout_3.addWidget(self.thumbnail_frame_0, 0, 0, 1, 1)
        self.thumbnail_frame_1 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
        self.thumbnail_frame_1.setMaximumSize(QtCore.QSize(50, 120))
        self.thumbnail_frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail_frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnail_frame_1.setObjectName("thumbnail_frame_1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.thumbnail_frame_1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.person_thumbnail_1 = QtWidgets.QLabel(self.thumbnail_frame_1)
        self.person_thumbnail_1.setMinimumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_1.setMaximumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.person_thumbnail_1.setText("")
        self.person_thumbnail_1.setObjectName("person_thumbnail_1")
        self.verticalLayout_5.addWidget(self.person_thumbnail_1)
        self.person_colorbar_1 = QtWidgets.QLabel(self.thumbnail_frame_1)
        self.person_colorbar_1.setMaximumSize(QtCore.QSize(50, 5))
        self.person_colorbar_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.person_colorbar_1.setText("")
        self.person_colorbar_1.setObjectName("person_colorbar_1")
        self.verticalLayout_5.addWidget(self.person_colorbar_1)
        self.gridLayout_3.addWidget(self.thumbnail_frame_1, 0, 1, 1, 1)
        self.thumbnail_frame_17 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
        self.thumbnail_frame_17.setMaximumSize(QtCore.QSize(50, 120))
        self.thumbnail_frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail_frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnail_frame_17.setObjectName("thumbnail_frame_17")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.thumbnail_frame_17)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.person_thumbnail_17 = QtWidgets.QLabel(self.thumbnail_frame_17)
        self.person_thumbnail_17.setMinimumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_17.setMaximumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_17.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.person_thumbnail_17.setText("")
        self.person_thumbnail_17.setObjectName("person_thumbnail_17")
        self.verticalLayout_21.addWidget(self.person_thumbnail_17)
        self.person_colorbar_17 = QtWidgets.QLabel(self.thumbnail_frame_17)
        self.person_colorbar_17.setMaximumSize(QtCore.QSize(50, 5))
        self.person_colorbar_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.person_colorbar_17.setText("")
        self.person_colorbar_17.setObjectName("person_colorbar_17")
        self.verticalLayout_21.addWidget(self.person_colorbar_17)
        self.gridLayout_3.addWidget(self.thumbnail_frame_17, 0, 17, 1, 1)
        self.thumbnail_frame_16 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
        self.thumbnail_frame_16.setMaximumSize(QtCore.QSize(50, 120))
        self.thumbnail_frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail_frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnail_frame_16.setObjectName("thumbnail_frame_16")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.thumbnail_frame_16)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.person_thumbnail_16 = QtWidgets.QLabel(self.thumbnail_frame_16)
        self.person_thumbnail_16.setMinimumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_16.setMaximumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.person_thumbnail_16.setText("")
        self.person_thumbnail_16.setObjectName("person_thumbnail_16")
        self.verticalLayout_20.addWidget(self.person_thumbnail_16)
        self.person_colorbar_16 = QtWidgets.QLabel(self.thumbnail_frame_16)
        self.person_colorbar_16.setMaximumSize(QtCore.QSize(50, 5))
        self.person_colorbar_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.person_colorbar_16.setText("")
        self.person_colorbar_16.setObjectName("person_colorbar_16")
        self.verticalLayout_20.addWidget(self.person_colorbar_16)
        self.gridLayout_3.addWidget(self.thumbnail_frame_16, 0, 16, 1, 1)
        self.thumbnail_frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
        self.thumbnail_frame_4.setMaximumSize(QtCore.QSize(50, 120))
        self.thumbnail_frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail_frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnail_frame_4.setObjectName("thumbnail_frame_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.thumbnail_frame_4)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.person_thumbnail_4 = QtWidgets.QLabel(self.thumbnail_frame_4)
        self.person_thumbnail_4.setMinimumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_4.setMaximumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.person_thumbnail_4.setText("")
        self.person_thumbnail_4.setObjectName("person_thumbnail_4")
        self.verticalLayout_8.addWidget(self.person_thumbnail_4)
        self.person_colorbar_4 = QtWidgets.QLabel(self.thumbnail_frame_4)
        self.person_colorbar_4.setMaximumSize(QtCore.QSize(50, 5))
        self.person_colorbar_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.person_colorbar_4.setText("")
        self.person_colorbar_4.setObjectName("person_colorbar_4")
        self.verticalLayout_8.addWidget(self.person_colorbar_4)
        self.gridLayout_3.addWidget(self.thumbnail_frame_4, 0, 4, 1, 1)
        self.thumbnail_frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
        self.thumbnail_frame_3.setMaximumSize(QtCore.QSize(50, 120))
        self.thumbnail_frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnail_frame_3.setObjectName("thumbnail_frame_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.thumbnail_frame_3)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.person_thumbnail_3 = QtWidgets.QLabel(self.thumbnail_frame_3)
        self.person_thumbnail_3.setMinimumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_3.setMaximumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.person_thumbnail_3.setText("")
        self.person_thumbnail_3.setObjectName("person_thumbnail_3")
        self.verticalLayout_7.addWidget(self.person_thumbnail_3)
        self.person_colorbar_3 = QtWidgets.QLabel(self.thumbnail_frame_3)
        self.person_colorbar_3.setMaximumSize(QtCore.QSize(50, 5))
        self.person_colorbar_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.person_colorbar_3.setText("")
        self.person_colorbar_3.setObjectName("person_colorbar_3")
        self.verticalLayout_7.addWidget(self.person_colorbar_3)
        self.gridLayout_3.addWidget(self.thumbnail_frame_3, 0, 3, 1, 1)
        self.thumbnail_frame_6 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
        self.thumbnail_frame_6.setMaximumSize(QtCore.QSize(50, 120))
        self.thumbnail_frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail_frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnail_frame_6.setObjectName("thumbnail_frame_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.thumbnail_frame_6)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.person_thumbnail_6 = QtWidgets.QLabel(self.thumbnail_frame_6)
        self.person_thumbnail_6.setMinimumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_6.setMaximumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.person_thumbnail_6.setText("")
        self.person_thumbnail_6.setObjectName("person_thumbnail_6")
        self.verticalLayout_10.addWidget(self.person_thumbnail_6)
        self.person_colorbar_6 = QtWidgets.QLabel(self.thumbnail_frame_6)
        self.person_colorbar_6.setMaximumSize(QtCore.QSize(50, 5))
        self.person_colorbar_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.person_colorbar_6.setText("")
        self.person_colorbar_6.setObjectName("person_colorbar_6")
        self.verticalLayout_10.addWidget(self.person_colorbar_6)
        self.gridLayout_3.addWidget(self.thumbnail_frame_6, 0, 6, 1, 1)
        self.thumbnail_frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
        self.thumbnail_frame_5.setMaximumSize(QtCore.QSize(50, 120))
        self.thumbnail_frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail_frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnail_frame_5.setObjectName("thumbnail_frame_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.thumbnail_frame_5)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.person_thumbnail_5 = QtWidgets.QLabel(self.thumbnail_frame_5)
        self.person_thumbnail_5.setMinimumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_5.setMaximumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.person_thumbnail_5.setText("")
        self.person_thumbnail_5.setObjectName("person_thumbnail_5")
        self.verticalLayout_9.addWidget(self.person_thumbnail_5)
        self.person_colorbar_5 = QtWidgets.QLabel(self.thumbnail_frame_5)
        self.person_colorbar_5.setMaximumSize(QtCore.QSize(50, 5))
        self.person_colorbar_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.person_colorbar_5.setText("")
        self.person_colorbar_5.setObjectName("person_colorbar_5")
        self.verticalLayout_9.addWidget(self.person_colorbar_5)
        self.gridLayout_3.addWidget(self.thumbnail_frame_5, 0, 5, 1, 1)
        self.thumbnail_frame_7 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
        self.thumbnail_frame_7.setMaximumSize(QtCore.QSize(50, 120))
        self.thumbnail_frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail_frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnail_frame_7.setObjectName("thumbnail_frame_7")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.thumbnail_frame_7)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.person_thumbnail_7 = QtWidgets.QLabel(self.thumbnail_frame_7)
        self.person_thumbnail_7.setMinimumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_7.setMaximumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.person_thumbnail_7.setText("")
        self.person_thumbnail_7.setObjectName("person_thumbnail_7")
        self.verticalLayout_11.addWidget(self.person_thumbnail_7)
        self.person_colorbar_7 = QtWidgets.QLabel(self.thumbnail_frame_7)
        self.person_colorbar_7.setMaximumSize(QtCore.QSize(50, 5))
        self.person_colorbar_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.person_colorbar_7.setText("")
        self.person_colorbar_7.setObjectName("person_colorbar_7")
        self.verticalLayout_11.addWidget(self.person_colorbar_7)
        self.gridLayout_3.addWidget(self.thumbnail_frame_7, 0, 7, 1, 1)
        self.thumbnail_frame_9 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
        self.thumbnail_frame_9.setMaximumSize(QtCore.QSize(50, 120))
        self.thumbnail_frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail_frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnail_frame_9.setObjectName("thumbnail_frame_9")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.thumbnail_frame_9)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.person_thumbnail_9 = QtWidgets.QLabel(self.thumbnail_frame_9)
        self.person_thumbnail_9.setMinimumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_9.setMaximumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.person_thumbnail_9.setText("")
        self.person_thumbnail_9.setObjectName("person_thumbnail_9")
        self.verticalLayout_13.addWidget(self.person_thumbnail_9)
        self.person_colorbar_9 = QtWidgets.QLabel(self.thumbnail_frame_9)
        self.person_colorbar_9.setMaximumSize(QtCore.QSize(50, 5))
        self.person_colorbar_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.person_colorbar_9.setText("")
        self.person_colorbar_9.setObjectName("person_colorbar_9")
        self.verticalLayout_13.addWidget(self.person_colorbar_9)
        self.gridLayout_3.addWidget(self.thumbnail_frame_9, 0, 9, 1, 1)
        self.thumbnail_frame_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
        self.thumbnail_frame_8.setMaximumSize(QtCore.QSize(50, 120))
        self.thumbnail_frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail_frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnail_frame_8.setObjectName("thumbnail_frame_8")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.thumbnail_frame_8)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.person_thumbnail_8 = QtWidgets.QLabel(self.thumbnail_frame_8)
        self.person_thumbnail_8.setMinimumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_8.setMaximumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.person_thumbnail_8.setText("")
        self.person_thumbnail_8.setObjectName("person_thumbnail_8")
        self.verticalLayout_12.addWidget(self.person_thumbnail_8)
        self.person_colorbar_8 = QtWidgets.QLabel(self.thumbnail_frame_8)
        self.person_colorbar_8.setMaximumSize(QtCore.QSize(50, 5))
        self.person_colorbar_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.person_colorbar_8.setText("")
        self.person_colorbar_8.setObjectName("person_colorbar_8")
        self.verticalLayout_12.addWidget(self.person_colorbar_8)
        self.gridLayout_3.addWidget(self.thumbnail_frame_8, 0, 8, 1, 1)
        self.thumbnail_frame_10 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
        self.thumbnail_frame_10.setMaximumSize(QtCore.QSize(50, 120))
        self.thumbnail_frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail_frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnail_frame_10.setObjectName("thumbnail_frame_10")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.thumbnail_frame_10)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.person_thumbnail_10 = QtWidgets.QLabel(self.thumbnail_frame_10)
        self.person_thumbnail_10.setMinimumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_10.setMaximumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.person_thumbnail_10.setText("")
        self.person_thumbnail_10.setObjectName("person_thumbnail_10")
        self.verticalLayout_14.addWidget(self.person_thumbnail_10)
        self.person_colorbar_10 = QtWidgets.QLabel(self.thumbnail_frame_10)
        self.person_colorbar_10.setMaximumSize(QtCore.QSize(50, 5))
        self.person_colorbar_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.person_colorbar_10.setText("")
        self.person_colorbar_10.setObjectName("person_colorbar_10")
        self.verticalLayout_14.addWidget(self.person_colorbar_10)
        self.gridLayout_3.addWidget(self.thumbnail_frame_10, 0, 10, 1, 1)
        self.thumbnail_frame_11 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
        self.thumbnail_frame_11.setMaximumSize(QtCore.QSize(50, 120))
        self.thumbnail_frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail_frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnail_frame_11.setObjectName("thumbnail_frame_11")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.thumbnail_frame_11)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.person_thumbnail_11 = QtWidgets.QLabel(self.thumbnail_frame_11)
        self.person_thumbnail_11.setMinimumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_11.setMaximumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.person_thumbnail_11.setText("")
        self.person_thumbnail_11.setObjectName("person_thumbnail_11")
        self.verticalLayout_15.addWidget(self.person_thumbnail_11)
        self.person_colorbar_11 = QtWidgets.QLabel(self.thumbnail_frame_11)
        self.person_colorbar_11.setMaximumSize(QtCore.QSize(50, 5))
        self.person_colorbar_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.person_colorbar_11.setText("")
        self.person_colorbar_11.setObjectName("person_colorbar_11")
        self.verticalLayout_15.addWidget(self.person_colorbar_11)
        self.gridLayout_3.addWidget(self.thumbnail_frame_11, 0, 11, 1, 1)
        self.thumbnail_frame_12 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
        self.thumbnail_frame_12.setMaximumSize(QtCore.QSize(50, 120))
        self.thumbnail_frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail_frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnail_frame_12.setObjectName("thumbnail_frame_12")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.thumbnail_frame_12)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.person_thumbnail_12 = QtWidgets.QLabel(self.thumbnail_frame_12)
        self.person_thumbnail_12.setMinimumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_12.setMaximumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.person_thumbnail_12.setText("")
        self.person_thumbnail_12.setObjectName("person_thumbnail_12")
        self.verticalLayout_16.addWidget(self.person_thumbnail_12)
        self.person_colorbar_12 = QtWidgets.QLabel(self.thumbnail_frame_12)
        self.person_colorbar_12.setMaximumSize(QtCore.QSize(50, 5))
        self.person_colorbar_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.person_colorbar_12.setText("")
        self.person_colorbar_12.setObjectName("person_colorbar_12")
        self.verticalLayout_16.addWidget(self.person_colorbar_12)
        self.gridLayout_3.addWidget(self.thumbnail_frame_12, 0, 12, 1, 1)
        self.thumbnail_frame_13 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
        self.thumbnail_frame_13.setMaximumSize(QtCore.QSize(50, 120))
        self.thumbnail_frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail_frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnail_frame_13.setObjectName("thumbnail_frame_13")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.thumbnail_frame_13)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.person_thumbnail_13 = QtWidgets.QLabel(self.thumbnail_frame_13)
        self.person_thumbnail_13.setMinimumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_13.setMaximumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.person_thumbnail_13.setText("")
        self.person_thumbnail_13.setObjectName("person_thumbnail_13")
        self.verticalLayout_17.addWidget(self.person_thumbnail_13)
        self.person_colorbar_13 = QtWidgets.QLabel(self.thumbnail_frame_13)
        self.person_colorbar_13.setMaximumSize(QtCore.QSize(50, 5))
        self.person_colorbar_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.person_colorbar_13.setText("")
        self.person_colorbar_13.setObjectName("person_colorbar_13")
        self.verticalLayout_17.addWidget(self.person_colorbar_13)
        self.gridLayout_3.addWidget(self.thumbnail_frame_13, 0, 13, 1, 1)
        self.thumbnail_frame_14 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
        self.thumbnail_frame_14.setMaximumSize(QtCore.QSize(50, 120))
        self.thumbnail_frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail_frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnail_frame_14.setObjectName("thumbnail_frame_14")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.thumbnail_frame_14)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.person_thumbnail_14 = QtWidgets.QLabel(self.thumbnail_frame_14)
        self.person_thumbnail_14.setMinimumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_14.setMaximumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.person_thumbnail_14.setText("")
        self.person_thumbnail_14.setObjectName("person_thumbnail_14")
        self.verticalLayout_18.addWidget(self.person_thumbnail_14)
        self.person_colorbar_14 = QtWidgets.QLabel(self.thumbnail_frame_14)
        self.person_colorbar_14.setMaximumSize(QtCore.QSize(50, 5))
        self.person_colorbar_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.person_colorbar_14.setText("")
        self.person_colorbar_14.setObjectName("person_colorbar_14")
        self.verticalLayout_18.addWidget(self.person_colorbar_14)
        self.gridLayout_3.addWidget(self.thumbnail_frame_14, 0, 14, 1, 1)
        self.thumbnail_frame_15 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
        self.thumbnail_frame_15.setMaximumSize(QtCore.QSize(50, 120))
        self.thumbnail_frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thumbnail_frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thumbnail_frame_15.setObjectName("thumbnail_frame_15")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.thumbnail_frame_15)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.person_thumbnail_15 = QtWidgets.QLabel(self.thumbnail_frame_15)
        self.person_thumbnail_15.setMinimumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_15.setMaximumSize(QtCore.QSize(50, 120))
        self.person_thumbnail_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.person_thumbnail_15.setText("")
        self.person_thumbnail_15.setObjectName("person_thumbnail_15")
        self.verticalLayout_19.addWidget(self.person_thumbnail_15)
        self.person_colorbar_15 = QtWidgets.QLabel(self.thumbnail_frame_15)
        self.person_colorbar_15.setMaximumSize(QtCore.QSize(50, 5))
        self.person_colorbar_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.person_colorbar_15.setText("")
        self.person_colorbar_15.setObjectName("person_colorbar_15")
        self.verticalLayout_19.addWidget(self.person_colorbar_15)
        self.gridLayout_3.addWidget(self.thumbnail_frame_15, 0, 15, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_8)
        self.verticalLayout_main.addWidget(self.scrollArea)
        self.gridLayout.addLayout(self.verticalLayout_main, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1058, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


    def setImage(self, image):
        self.mainCamera.setPixmap(QPixmap.fromImage(image))


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     main = QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(main)
#
#     main.show()
#     sys.exit(app.exec_())