import pandas as pd
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QWidget, QDialog
import time
from PyQt5.QtCore import QTimer

_perpetual = 'BTC-PERPETUAL'
_sep = 'BTC-25SEP20'
_dec = 'BTC-25DEC20'
_mar = 'BTC-26MAR21'
delay = 1


class Ui_MainWindow(object):
    global nameCompit

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1336, 607)
        MainWindow.setMinimumSize(QtCore.QSize(1336, 607))
        MainWindow.setMaximumSize(QtCore.QSize(1336, 607))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 351, 161))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 47, 13))
        self.label_2.setObjectName("label_2")
        self.name = QtWidgets.QLineEdit(self.groupBox)
        self.name.setGeometry(QtCore.QRect(80, 20, 113, 31))
        self.name.setObjectName("name")
        self.ok_button = QtWidgets.QPushButton(self.groupBox)
        self.ok_button.setGeometry(QtCore.QRect(210, 20, 61, 31))
        self.ok_button.setObjectName("ok_button")
        self.clear_button = QtWidgets.QPushButton(self.groupBox)
        self.clear_button.setGeometry(QtCore.QRect(280, 20, 61, 31))
        self.clear_button.setObjectName("clear_button")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 243, 248, 311))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.open_button_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.open_button_10.setObjectName("open_button_10")
        self.gridLayout.addWidget(self.open_button_10, 10, 2, 1, 1)
        self.open_button_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.open_button_9.setObjectName("open_button_9")
        self.gridLayout.addWidget(self.open_button_9, 9, 2, 1, 1)
        self.open_button_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.open_button_8.setObjectName("open_button_8")
        self.gridLayout.addWidget(self.open_button_8, 8, 2, 1, 1)
        self.close_button_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.close_button_3.setObjectName("close_button_3")
        self.gridLayout.addWidget(self.close_button_3, 3, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 1, 1, 1)
        self.open_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.open_3.setText("")
        self.open_3.setObjectName("open_3")
        self.gridLayout.addWidget(self.open_3, 3, 1, 1, 1)
        self.close_button_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.close_button_7.setObjectName("close_button_7")
        self.gridLayout.addWidget(self.close_button_7, 7, 3, 1, 1)
        self.close_button_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.close_button_10.setObjectName("close_button_10")
        self.gridLayout.addWidget(self.close_button_10, 10, 3, 1, 1)
        self.open_button_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.open_button_5.setObjectName("open_button_5")
        self.gridLayout.addWidget(self.open_button_5, 5, 2, 1, 1)
        self.open_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.open_7.setObjectName("open_7")
        self.gridLayout.addWidget(self.open_7, 7, 1, 1, 1)
        self.close_button_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.close_button_4.setObjectName("close_button_4")
        self.gridLayout.addWidget(self.close_button_4, 4, 3, 1, 1)
        self.open_button_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.open_button_7.setObjectName("open_button_7")
        self.gridLayout.addWidget(self.open_button_7, 7, 2, 1, 1)
        self.open_button_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.open_button_6.setObjectName("open_button_6")
        self.gridLayout.addWidget(self.open_button_6, 6, 2, 1, 1)
        self.open_button_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.open_button_4.setObjectName("open_button_4")
        self.gridLayout.addWidget(self.open_button_4, 4, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 7, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 6, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 5, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 8, 0, 1, 1)
        self.open_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.open_6.setObjectName("open_6")
        self.gridLayout.addWidget(self.open_6, 6, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 2, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 0, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 4, 0, 1, 1)
        self.open_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.open_8.setObjectName("open_8")
        self.gridLayout.addWidget(self.open_8, 8, 1, 1, 1)
        self.close_button_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.close_button_8.setObjectName("close_button_8")
        self.gridLayout.addWidget(self.close_button_8, 8, 3, 1, 1)
        self.open_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.open_9.setObjectName("open_9")
        self.gridLayout.addWidget(self.open_9, 9, 1, 1, 1)
        self.open_button_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.open_button_3.setObjectName("open_button_3")
        self.gridLayout.addWidget(self.open_button_3, 3, 2, 1, 1)
        self.close_button_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.close_button_6.setObjectName("close_button_6")
        self.gridLayout.addWidget(self.close_button_6, 6, 3, 1, 1)
        self.open_button_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.open_button_2.setObjectName("open_button_2")
        self.gridLayout.addWidget(self.open_button_2, 2, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 3, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 2, 1, 1)
        self.open_button_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.open_button_1.setObjectName("open_button_1")
        self.gridLayout.addWidget(self.open_button_1, 1, 2, 1, 1)
        self.close_button_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.close_button_1.setObjectName("close_button_1")
        self.gridLayout.addWidget(self.close_button_1, 1, 3, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 9, 0, 1, 1)
        self.close_button_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.close_button_9.setObjectName("close_button_9")
        self.gridLayout.addWidget(self.close_button_9, 9, 3, 1, 1)
        self.close_button_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.close_button_2.setObjectName("close_button_2")
        self.gridLayout.addWidget(self.close_button_2, 2, 3, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 1, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 10, 0, 1, 1)
        self.close_button_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.close_button_5.setObjectName("close_button_5")
        self.gridLayout.addWidget(self.close_button_5, 5, 3, 1, 1)
        self.open_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.open_10.setObjectName("open_10")
        self.gridLayout.addWidget(self.open_10, 10, 1, 1, 1)
        self.open_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.open_4.setText("")
        self.open_4.setObjectName("open_4")
        self.gridLayout.addWidget(self.open_4, 4, 1, 1, 1)
        self.open_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.open_5.setText("")
        self.open_5.setObjectName("open_5")
        self.gridLayout.addWidget(self.open_5, 5, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 0, 3, 1, 1)
        self.open_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.open_2.setText("")
        self.open_2.setObjectName("open_2")
        self.gridLayout.addWidget(self.open_2, 2, 1, 1, 1)
        self.open_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.open_1.setText("")
        self.open_1.setObjectName("open_1")
        self.gridLayout.addWidget(self.open_1, 1, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(280, 240, 248, 311))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.open_15 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.open_15.setText("")
        self.open_15.setObjectName("open_15")
        self.gridLayout_2.addWidget(self.open_15, 5, 1, 1, 1)
        self.open_20 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.open_20.setText("")
        self.open_20.setObjectName("open_20")
        self.gridLayout_2.addWidget(self.open_20, 10, 1, 1, 1)
        self.close_button_15 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.close_button_15.setObjectName("close_button_15")
        self.gridLayout_2.addWidget(self.close_button_15, 5, 3, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_34.setObjectName("label_34")
        self.gridLayout_2.addWidget(self.label_34, 9, 0, 1, 1)
        self.close_button_11 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.close_button_11.setObjectName("close_button_11")
        self.gridLayout_2.addWidget(self.close_button_11, 1, 3, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_33.setObjectName("label_33")
        self.gridLayout_2.addWidget(self.label_33, 0, 2, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_35.setObjectName("label_35")
        self.gridLayout_2.addWidget(self.label_35, 10, 0, 1, 1)
        self.close_button_12 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.close_button_12.setObjectName("close_button_12")
        self.gridLayout_2.addWidget(self.close_button_12, 2, 3, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_36.setObjectName("label_36")
        self.gridLayout_2.addWidget(self.label_36, 1, 0, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_37.setObjectName("label_37")
        self.gridLayout_2.addWidget(self.label_37, 3, 0, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_38.setObjectName("label_38")
        self.gridLayout_2.addWidget(self.label_38, 2, 0, 1, 1)
        self.close_button_19 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.close_button_19.setObjectName("close_button_19")
        self.gridLayout_2.addWidget(self.close_button_19, 9, 3, 1, 1)
        self.open_button_11 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.open_button_11.setObjectName("open_button_11")
        self.gridLayout_2.addWidget(self.open_button_11, 1, 2, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_44.setObjectName("label_44")
        self.gridLayout_2.addWidget(self.label_44, 8, 0, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_45.setObjectName("label_45")
        self.gridLayout_2.addWidget(self.label_45, 7, 0, 1, 1)
        self.open_button_12 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.open_button_12.setObjectName("open_button_12")
        self.gridLayout_2.addWidget(self.open_button_12, 2, 2, 1, 1)
        self.open_button_13 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.open_button_13.setObjectName("open_button_13")
        self.gridLayout_2.addWidget(self.open_button_13, 3, 2, 1, 1)
        self.open_17 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.open_17.setText("")
        self.open_17.setObjectName("open_17")
        self.gridLayout_2.addWidget(self.open_17, 7, 1, 1, 1)
        self.close_button_14 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.close_button_14.setObjectName("close_button_14")
        self.gridLayout_2.addWidget(self.close_button_14, 4, 3, 1, 1)
        self.open_16 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.open_16.setText("")
        self.open_16.setObjectName("open_16")
        self.gridLayout_2.addWidget(self.open_16, 6, 1, 1, 1)
        self.label_46 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_46.setObjectName("label_46")
        self.gridLayout_2.addWidget(self.label_46, 6, 0, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_47.setObjectName("label_47")
        self.gridLayout_2.addWidget(self.label_47, 5, 0, 1, 1)
        self.open_button_17 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.open_button_17.setObjectName("open_button_17")
        self.gridLayout_2.addWidget(self.open_button_17, 7, 2, 1, 1)
        self.open_button_16 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.open_button_16.setObjectName("open_button_16")
        self.gridLayout_2.addWidget(self.open_button_16, 6, 2, 1, 1)
        self.open_button_14 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.open_button_14.setObjectName("open_button_14")
        self.gridLayout_2.addWidget(self.open_button_14, 4, 2, 1, 1)
        self.open_button_19 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.open_button_19.setObjectName("open_button_19")
        self.gridLayout_2.addWidget(self.open_button_19, 9, 2, 1, 1)
        self.open_button_15 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.open_button_15.setObjectName("open_button_15")
        self.gridLayout_2.addWidget(self.open_button_15, 5, 2, 1, 1)
        self.open_button_20 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.open_button_20.setObjectName("open_button_20")
        self.gridLayout_2.addWidget(self.open_button_20, 10, 2, 1, 1)
        self.label_50 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_50.setObjectName("label_50")
        self.gridLayout_2.addWidget(self.label_50, 0, 1, 1, 1)
        self.open_button_18 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.open_button_18.setObjectName("open_button_18")
        self.gridLayout_2.addWidget(self.open_button_18, 8, 2, 1, 1)
        self.close_button_13 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.close_button_13.setObjectName("close_button_13")
        self.gridLayout_2.addWidget(self.close_button_13, 3, 3, 1, 1)
        self.close_button_17 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.close_button_17.setObjectName("close_button_17")
        self.gridLayout_2.addWidget(self.close_button_17, 7, 3, 1, 1)
        self.close_button_20 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.close_button_20.setObjectName("close_button_20")
        self.gridLayout_2.addWidget(self.close_button_20, 10, 3, 1, 1)
        self.open_12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.open_12.setText("")
        self.open_12.setObjectName("open_12")
        self.gridLayout_2.addWidget(self.open_12, 2, 1, 1, 1)
        self.open_14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.open_14.setText("")
        self.open_14.setObjectName("open_14")
        self.gridLayout_2.addWidget(self.open_14, 4, 1, 1, 1)
        self.open_13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.open_13.setObjectName("open_13")
        self.gridLayout_2.addWidget(self.open_13, 3, 1, 1, 1)
        self.open_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.open_11.setText("")
        self.open_11.setObjectName("open_11")
        self.gridLayout_2.addWidget(self.open_11, 1, 1, 1, 1)
        self.close_button_16 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.close_button_16.setObjectName("close_button_16")
        self.gridLayout_2.addWidget(self.close_button_16, 6, 3, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_40.setObjectName("label_40")
        self.gridLayout_2.addWidget(self.label_40, 0, 0, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_39.setObjectName("label_39")
        self.gridLayout_2.addWidget(self.label_39, 4, 0, 1, 1)
        self.open_18 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.open_18.setText("")
        self.open_18.setObjectName("open_18")
        self.gridLayout_2.addWidget(self.open_18, 8, 1, 1, 1)
        self.close_button_18 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.close_button_18.setObjectName("close_button_18")
        self.gridLayout_2.addWidget(self.close_button_18, 8, 3, 1, 1)
        self.open_19 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.open_19.setText("")
        self.open_19.setObjectName("open_19")
        self.gridLayout_2.addWidget(self.open_19, 9, 1, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_43.setObjectName("label_43")
        self.gridLayout_2.addWidget(self.label_43, 0, 3, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(540, 240, 248, 311))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.open_button_21 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.open_button_21.setObjectName("open_button_21")
        self.gridLayout_3.addWidget(self.open_button_21, 1, 2, 1, 1)
        self.label_57 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_57.setObjectName("label_57")
        self.gridLayout_3.addWidget(self.label_57, 0, 2, 1, 1)
        self.close_button_21 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.close_button_21.setObjectName("close_button_21")
        self.gridLayout_3.addWidget(self.close_button_21, 1, 3, 1, 1)
        self.label_58 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_58.setObjectName("label_58")
        self.gridLayout_3.addWidget(self.label_58, 9, 0, 1, 1)
        self.label_59 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_59.setObjectName("label_59")
        self.gridLayout_3.addWidget(self.label_59, 10, 0, 1, 1)
        self.close_button_25 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.close_button_25.setObjectName("close_button_25")
        self.gridLayout_3.addWidget(self.close_button_25, 5, 3, 1, 1)
        self.close_button_22 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.close_button_22.setObjectName("close_button_22")
        self.gridLayout_3.addWidget(self.close_button_22, 2, 3, 1, 1)
        self.close_button_29 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.close_button_29.setObjectName("close_button_29")
        self.gridLayout_3.addWidget(self.close_button_29, 9, 3, 1, 1)
        self.label_60 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_60.setObjectName("label_60")
        self.gridLayout_3.addWidget(self.label_60, 1, 0, 1, 1)
        self.label_61 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_61.setObjectName("label_61")
        self.gridLayout_3.addWidget(self.label_61, 3, 0, 1, 1)
        self.label_62 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_62.setObjectName("label_62")
        self.gridLayout_3.addWidget(self.label_62, 2, 0, 1, 1)
        self.label_63 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_63.setObjectName("label_63")
        self.gridLayout_3.addWidget(self.label_63, 4, 0, 1, 1)
        self.label_64 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_64.setObjectName("label_64")
        self.gridLayout_3.addWidget(self.label_64, 0, 0, 1, 1)
        self.open_28 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.open_28.setObjectName("open_28")
        self.gridLayout_3.addWidget(self.open_28, 8, 1, 1, 1)
        self.close_button_26 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.close_button_26.setObjectName("close_button_26")
        self.gridLayout_3.addWidget(self.close_button_26, 6, 3, 1, 1)
        self.close_button_28 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.close_button_28.setObjectName("close_button_28")
        self.gridLayout_3.addWidget(self.close_button_28, 8, 3, 1, 1)
        self.open_29 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.open_29.setObjectName("open_29")
        self.gridLayout_3.addWidget(self.open_29, 9, 1, 1, 1)
        self.open_button_23 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.open_button_23.setObjectName("open_button_23")
        self.gridLayout_3.addWidget(self.open_button_23, 3, 2, 1, 1)
        self.label_67 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_67.setObjectName("label_67")
        self.gridLayout_3.addWidget(self.label_67, 0, 3, 1, 1)
        self.open_button_22 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.open_button_22.setObjectName("open_button_22")
        self.gridLayout_3.addWidget(self.open_button_22, 2, 2, 1, 1)
        self.label_68 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_68.setObjectName("label_68")
        self.gridLayout_3.addWidget(self.label_68, 8, 0, 1, 1)
        self.label_69 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_69.setObjectName("label_69")
        self.gridLayout_3.addWidget(self.label_69, 7, 0, 1, 1)
        self.label_70 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_70.setObjectName("label_70")
        self.gridLayout_3.addWidget(self.label_70, 6, 0, 1, 1)
        self.label_71 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_71.setObjectName("label_71")
        self.gridLayout_3.addWidget(self.label_71, 5, 0, 1, 1)
        self.open_26 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.open_26.setObjectName("open_26")
        self.gridLayout_3.addWidget(self.open_26, 6, 1, 1, 1)
        self.open_27 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.open_27.setObjectName("open_27")
        self.gridLayout_3.addWidget(self.open_27, 7, 1, 1, 1)
        self.close_button_24 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.close_button_24.setObjectName("close_button_24")
        self.gridLayout_3.addWidget(self.close_button_24, 4, 3, 1, 1)
        self.open_button_25 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.open_button_25.setEnabled(True)
        self.open_button_25.setObjectName("open_button_25")
        self.gridLayout_3.addWidget(self.open_button_25, 5, 2, 1, 1)
        self.open_button_27 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.open_button_27.setObjectName("open_button_27")
        self.gridLayout_3.addWidget(self.open_button_27, 7, 2, 1, 1)
        self.open_button_26 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.open_button_26.setObjectName("open_button_26")
        self.gridLayout_3.addWidget(self.open_button_26, 6, 2, 1, 1)
        self.open_button_24 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.open_button_24.setObjectName("open_button_24")
        self.gridLayout_3.addWidget(self.open_button_24, 4, 2, 1, 1)
        self.open_button_29 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.open_button_29.setObjectName("open_button_29")
        self.gridLayout_3.addWidget(self.open_button_29, 9, 2, 1, 1)
        self.open_button_28 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.open_button_28.setObjectName("open_button_28")
        self.gridLayout_3.addWidget(self.open_button_28, 8, 2, 1, 1)
        self.open_button_30 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.open_button_30.setObjectName("open_button_30")
        self.gridLayout_3.addWidget(self.open_button_30, 10, 2, 1, 1)
        self.label_74 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_74.setObjectName("label_74")
        self.gridLayout_3.addWidget(self.label_74, 0, 1, 1, 1)
        self.close_button_23 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.close_button_23.setObjectName("close_button_23")
        self.gridLayout_3.addWidget(self.close_button_23, 3, 3, 1, 1)
        self.close_button_27 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.close_button_27.setObjectName("close_button_27")
        self.gridLayout_3.addWidget(self.close_button_27, 7, 3, 1, 1)
        self.close_button_30 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.close_button_30.setObjectName("close_button_30")
        self.gridLayout_3.addWidget(self.close_button_30, 10, 3, 1, 1)
        self.open_21 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.open_21.setText("")
        self.open_21.setObjectName("open_21")
        self.gridLayout_3.addWidget(self.open_21, 1, 1, 1, 1)
        self.open_22 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.open_22.setObjectName("open_22")
        self.gridLayout_3.addWidget(self.open_22, 2, 1, 1, 1)
        self.open_23 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.open_23.setObjectName("open_23")
        self.gridLayout_3.addWidget(self.open_23, 3, 1, 1, 1)
        self.open_24 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.open_24.setObjectName("open_24")
        self.gridLayout_3.addWidget(self.open_24, 4, 1, 1, 1)
        self.open_25 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.open_25.setObjectName("open_25")
        self.gridLayout_3.addWidget(self.open_25, 5, 1, 1, 1)
        self.open_30 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.open_30.setObjectName("open_30")
        self.gridLayout_3.addWidget(self.open_30, 10, 1, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(800, 240, 248, 311))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.open_button_31 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.open_button_31.setObjectName("open_button_31")
        self.gridLayout_4.addWidget(self.open_button_31, 1, 2, 1, 1)
        self.label_81 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_81.setObjectName("label_81")
        self.gridLayout_4.addWidget(self.label_81, 0, 2, 1, 1)
        self.close_button_31 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.close_button_31.setObjectName("close_button_31")
        self.gridLayout_4.addWidget(self.close_button_31, 1, 3, 1, 1)
        self.label_82 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_82.setObjectName("label_82")
        self.gridLayout_4.addWidget(self.label_82, 9, 0, 1, 1)
        self.label_83 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_83.setObjectName("label_83")
        self.gridLayout_4.addWidget(self.label_83, 10, 0, 1, 1)
        self.close_button_35 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.close_button_35.setObjectName("close_button_35")
        self.gridLayout_4.addWidget(self.close_button_35, 5, 3, 1, 1)
        self.close_button_32 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.close_button_32.setObjectName("close_button_32")
        self.gridLayout_4.addWidget(self.close_button_32, 2, 3, 1, 1)
        self.close_button_39 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.close_button_39.setObjectName("close_button_39")
        self.gridLayout_4.addWidget(self.close_button_39, 9, 3, 1, 1)
        self.label_84 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_84.setObjectName("label_84")
        self.gridLayout_4.addWidget(self.label_84, 1, 0, 1, 1)
        self.label_85 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_85.setObjectName("label_85")
        self.gridLayout_4.addWidget(self.label_85, 3, 0, 1, 1)
        self.label_86 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_86.setObjectName("label_86")
        self.gridLayout_4.addWidget(self.label_86, 2, 0, 1, 1)
        self.label_87 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_87.setObjectName("label_87")
        self.gridLayout_4.addWidget(self.label_87, 4, 0, 1, 1)
        self.label_88 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_88.setObjectName("label_88")
        self.gridLayout_4.addWidget(self.label_88, 0, 0, 1, 1)
        self.open_38 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.open_38.setObjectName("open_38")
        self.gridLayout_4.addWidget(self.open_38, 8, 1, 1, 1)
        self.close_button_36 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.close_button_36.setObjectName("close_button_36")
        self.gridLayout_4.addWidget(self.close_button_36, 6, 3, 1, 1)
        self.close_button_38 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.close_button_38.setObjectName("close_button_38")
        self.gridLayout_4.addWidget(self.close_button_38, 8, 3, 1, 1)
        self.open_39 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.open_39.setObjectName("open_39")
        self.gridLayout_4.addWidget(self.open_39, 9, 1, 1, 1)
        self.open_button_33 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.open_button_33.setObjectName("open_button_33")
        self.gridLayout_4.addWidget(self.open_button_33, 3, 2, 1, 1)
        self.label_91 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_91.setObjectName("label_91")
        self.gridLayout_4.addWidget(self.label_91, 0, 3, 1, 1)
        self.open_button_32 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.open_button_32.setObjectName("open_button_32")
        self.gridLayout_4.addWidget(self.open_button_32, 2, 2, 1, 1)
        self.label_92 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_92.setObjectName("label_92")
        self.gridLayout_4.addWidget(self.label_92, 8, 0, 1, 1)
        self.label_93 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_93.setObjectName("label_93")
        self.gridLayout_4.addWidget(self.label_93, 7, 0, 1, 1)
        self.label_94 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_94.setObjectName("label_94")
        self.gridLayout_4.addWidget(self.label_94, 6, 0, 1, 1)
        self.label_95 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_95.setObjectName("label_95")
        self.gridLayout_4.addWidget(self.label_95, 5, 0, 1, 1)
        self.open_36 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.open_36.setObjectName("open_36")
        self.gridLayout_4.addWidget(self.open_36, 6, 1, 1, 1)
        self.open_37 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.open_37.setObjectName("open_37")
        self.gridLayout_4.addWidget(self.open_37, 7, 1, 1, 1)
        self.close_button_34 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.close_button_34.setObjectName("close_button_34")
        self.gridLayout_4.addWidget(self.close_button_34, 4, 3, 1, 1)
        self.open_button_35 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.open_button_35.setObjectName("open_button_35")
        self.gridLayout_4.addWidget(self.open_button_35, 5, 2, 1, 1)
        self.open_button_37 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.open_button_37.setObjectName("open_button_37")
        self.gridLayout_4.addWidget(self.open_button_37, 7, 2, 1, 1)
        self.open_button_36 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.open_button_36.setObjectName("open_button_36")
        self.gridLayout_4.addWidget(self.open_button_36, 6, 2, 1, 1)
        self.open_button_34 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.open_button_34.setObjectName("open_button_34")
        self.gridLayout_4.addWidget(self.open_button_34, 4, 2, 1, 1)
        self.open_button_39 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.open_button_39.setObjectName("open_button_39")
        self.gridLayout_4.addWidget(self.open_button_39, 9, 2, 1, 1)
        self.open_button_38 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.open_button_38.setObjectName("open_button_38")
        self.gridLayout_4.addWidget(self.open_button_38, 8, 2, 1, 1)
        self.open_button_40 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.open_button_40.setObjectName("open_button_40")
        self.gridLayout_4.addWidget(self.open_button_40, 10, 2, 1, 1)
        self.label_98 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_98.setObjectName("label_98")
        self.gridLayout_4.addWidget(self.label_98, 0, 1, 1, 1)
        self.close_button_33 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.close_button_33.setObjectName("close_button_33")
        self.gridLayout_4.addWidget(self.close_button_33, 3, 3, 1, 1)
        self.close_button_37 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.close_button_37.setObjectName("close_button_37")
        self.gridLayout_4.addWidget(self.close_button_37, 7, 3, 1, 1)
        self.close_button_40 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.close_button_40.setObjectName("close_button_40")
        self.gridLayout_4.addWidget(self.close_button_40, 10, 3, 1, 1)
        self.open_31 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.open_31.setObjectName("open_31")
        self.gridLayout_4.addWidget(self.open_31, 1, 1, 1, 1)
        self.open_32 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.open_32.setObjectName("open_32")
        self.gridLayout_4.addWidget(self.open_32, 2, 1, 1, 1)
        self.open_33 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.open_33.setObjectName("open_33")
        self.gridLayout_4.addWidget(self.open_33, 3, 1, 1, 1)
        self.open_34 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.open_34.setObjectName("open_34")
        self.gridLayout_4.addWidget(self.open_34, 4, 1, 1, 1)
        self.open_35 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.open_35.setObjectName("open_35")
        self.gridLayout_4.addWidget(self.open_35, 5, 1, 1, 1)
        self.open_40 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.open_40.setObjectName("open_40")
        self.gridLayout_4.addWidget(self.open_40, 10, 1, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(1060, 240, 248, 311))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.open_button_41 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.open_button_41.setObjectName("open_button_41")
        self.gridLayout_5.addWidget(self.open_button_41, 1, 2, 1, 1)
        self.label_105 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_105.setObjectName("label_105")
        self.gridLayout_5.addWidget(self.label_105, 0, 2, 1, 1)
        self.close_button_41 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.close_button_41.setObjectName("close_button_41")
        self.gridLayout_5.addWidget(self.close_button_41, 1, 3, 1, 1)
        self.label_106 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_106.setObjectName("label_106")
        self.gridLayout_5.addWidget(self.label_106, 9, 0, 1, 1)
        self.label_107 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_107.setObjectName("label_107")
        self.gridLayout_5.addWidget(self.label_107, 10, 0, 1, 1)
        self.close_button_45 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.close_button_45.setObjectName("close_button_45")
        self.gridLayout_5.addWidget(self.close_button_45, 5, 3, 1, 1)
        self.close_button_42 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.close_button_42.setObjectName("close_button_42")
        self.gridLayout_5.addWidget(self.close_button_42, 2, 3, 1, 1)
        self.close_button_49 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.close_button_49.setObjectName("close_button_49")
        self.gridLayout_5.addWidget(self.close_button_49, 9, 3, 1, 1)
        self.label_108 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_108.setObjectName("label_108")
        self.gridLayout_5.addWidget(self.label_108, 1, 0, 1, 1)
        self.label_109 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_109.setObjectName("label_109")
        self.gridLayout_5.addWidget(self.label_109, 3, 0, 1, 1)
        self.label_110 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_110.setObjectName("label_110")
        self.gridLayout_5.addWidget(self.label_110, 2, 0, 1, 1)
        self.label_111 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_111.setObjectName("label_111")
        self.gridLayout_5.addWidget(self.label_111, 4, 0, 1, 1)
        self.label_112 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_112.setObjectName("label_112")
        self.gridLayout_5.addWidget(self.label_112, 0, 0, 1, 1)
        self.open_48 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.open_48.setObjectName("open_48")
        self.gridLayout_5.addWidget(self.open_48, 8, 1, 1, 1)
        self.close_button_46 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.close_button_46.setObjectName("close_button_46")
        self.gridLayout_5.addWidget(self.close_button_46, 6, 3, 1, 1)
        self.close_button_48 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.close_button_48.setObjectName("close_button_48")
        self.gridLayout_5.addWidget(self.close_button_48, 8, 3, 1, 1)
        self.open_49 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.open_49.setObjectName("open_49")
        self.gridLayout_5.addWidget(self.open_49, 9, 1, 1, 1)
        self.open_button_43 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.open_button_43.setObjectName("open_button_43")
        self.gridLayout_5.addWidget(self.open_button_43, 3, 2, 1, 1)
        self.label_115 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_115.setObjectName("label_115")
        self.gridLayout_5.addWidget(self.label_115, 0, 3, 1, 1)
        self.open_button_42 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.open_button_42.setObjectName("open_button_42")
        self.gridLayout_5.addWidget(self.open_button_42, 2, 2, 1, 1)
        self.label_116 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_116.setObjectName("label_116")
        self.gridLayout_5.addWidget(self.label_116, 8, 0, 1, 1)
        self.label_117 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_117.setObjectName("label_117")
        self.gridLayout_5.addWidget(self.label_117, 7, 0, 1, 1)
        self.label_118 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_118.setObjectName("label_118")
        self.gridLayout_5.addWidget(self.label_118, 6, 0, 1, 1)
        self.label_119 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_119.setObjectName("label_119")
        self.gridLayout_5.addWidget(self.label_119, 5, 0, 1, 1)
        self.open_46 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.open_46.setObjectName("open_46")
        self.gridLayout_5.addWidget(self.open_46, 6, 1, 1, 1)
        self.open_47 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.open_47.setObjectName("open_47")
        self.gridLayout_5.addWidget(self.open_47, 7, 1, 1, 1)
        self.close_button_44 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.close_button_44.setObjectName("close_button_44")
        self.gridLayout_5.addWidget(self.close_button_44, 4, 3, 1, 1)
        self.open_button_45 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.open_button_45.setObjectName("open_button_45")
        self.gridLayout_5.addWidget(self.open_button_45, 5, 2, 1, 1)
        self.open_button_47 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.open_button_47.setObjectName("open_button_47")
        self.gridLayout_5.addWidget(self.open_button_47, 7, 2, 1, 1)
        self.open_button_46 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.open_button_46.setObjectName("open_button_46")
        self.gridLayout_5.addWidget(self.open_button_46, 6, 2, 1, 1)
        self.open_button_44 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.open_button_44.setObjectName("open_button_44")
        self.gridLayout_5.addWidget(self.open_button_44, 4, 2, 1, 1)
        self.open_button_49 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.open_button_49.setObjectName("open_button_49")
        self.gridLayout_5.addWidget(self.open_button_49, 9, 2, 1, 1)
        self.open_button_48 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.open_button_48.setObjectName("open_button_48")
        self.gridLayout_5.addWidget(self.open_button_48, 8, 2, 1, 1)
        self.open_button_50 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.open_button_50.setObjectName("open_button_50")
        self.gridLayout_5.addWidget(self.open_button_50, 10, 2, 1, 1)
        self.label_122 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_122.setObjectName("label_122")
        self.gridLayout_5.addWidget(self.label_122, 0, 1, 1, 1)
        self.close_button_43 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.close_button_43.setObjectName("close_button_43")
        self.gridLayout_5.addWidget(self.close_button_43, 3, 3, 1, 1)
        self.close_button_47 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.close_button_47.setObjectName("close_button_47")
        self.gridLayout_5.addWidget(self.close_button_47, 7, 3, 1, 1)
        self.close_button_50 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.close_button_50.setObjectName("close_button_50")
        self.gridLayout_5.addWidget(self.close_button_50, 10, 3, 1, 1)
        self.open_41 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.open_41.setObjectName("open_41")
        self.gridLayout_5.addWidget(self.open_41, 1, 1, 1, 1)
        self.open_42 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.open_42.setObjectName("open_42")
        self.gridLayout_5.addWidget(self.open_42, 2, 1, 1, 1)
        self.open_43 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.open_43.setObjectName("open_43")
        self.gridLayout_5.addWidget(self.open_43, 3, 1, 1, 1)
        self.open_44 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.open_44.setObjectName("open_44")
        self.gridLayout_5.addWidget(self.open_44, 4, 1, 1, 1)
        self.open_45 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.open_45.setObjectName("open_45")
        self.gridLayout_5.addWidget(self.open_45, 5, 1, 1, 1)
        self.open_50 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.open_50.setObjectName("open_50")
        self.gridLayout_5.addWidget(self.open_50, 10, 1, 1, 1)
        self.order_box = QtWidgets.QGroupBox(self.centralwidget)
        self.order_box.setGeometry(QtCore.QRect(380, 20, 461, 161))
        self.order_box.setFlat(True)
        self.order_box.setCheckable(False)
        self.order_box.setChecked(False)
        self.order_box.setObjectName("order_box")
        self.label_129 = QtWidgets.QLabel(self.order_box)
        self.label_129.setGeometry(QtCore.QRect(20, 40, 47, 13))
        self.label_129.setObjectName("label_129")
        self.label_131 = QtWidgets.QLabel(self.order_box)
        self.label_131.setGeometry(QtCore.QRect(20, 100, 47, 13))
        self.label_131.setObjectName("label_131")
        self.label_132 = QtWidgets.QLabel(self.order_box)
        self.label_132.setGeometry(QtCore.QRect(20, 130, 47, 13))
        self.label_132.setObjectName("label_132")
        self.label_133 = QtWidgets.QLabel(self.order_box)
        self.label_133.setGeometry(QtCore.QRect(150, 20, 31, 20))
        self.label_133.setObjectName("label_133")
        self.label_134 = QtWidgets.QLabel(self.order_box)
        self.label_134.setGeometry(QtCore.QRect(250, 20, 21, 16))
        self.label_134.setObjectName("label_134")
        self.label_135 = QtWidgets.QLabel(self.order_box)
        self.label_135.setGeometry(QtCore.QRect(20, 70, 47, 13))
        self.label_135.setObjectName("label_135")
        self.label = QtWidgets.QLabel(self.order_box)
        self.label.setGeometry(QtCore.QRect(340, 20, 31, 16))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.order_box)
        self.label_4.setGeometry(QtCore.QRect(50, 20, 31, 16))
        self.label_4.setObjectName("label_4")
        self.lcdNumber = QtWidgets.QLCDNumber(self.order_box)
        self.lcdNumber.setGeometry(QtCore.QRect(40, 40, 81, 23))
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(9)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.order_box)
        self.lcdNumber_2.setGeometry(QtCore.QRect(40, 70, 81, 23))
        self.lcdNumber_2.setDigitCount(9)
        self.lcdNumber_2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.order_box)
        self.lcdNumber_3.setGeometry(QtCore.QRect(40, 100, 81, 23))
        self.lcdNumber_3.setDigitCount(9)
        self.lcdNumber_3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.order_box)
        self.lcdNumber_4.setGeometry(QtCore.QRect(40, 130, 81, 23))
        self.lcdNumber_4.setDigitCount(9)
        self.lcdNumber_4.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.order_box)
        self.lcdNumber_5.setGeometry(QtCore.QRect(130, 40, 81, 23))
        self.lcdNumber_5.setDigitCount(9)
        self.lcdNumber_5.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.order_box)
        self.lcdNumber_6.setGeometry(QtCore.QRect(130, 70, 81, 23))
        self.lcdNumber_6.setDigitCount(9)
        self.lcdNumber_6.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.lcdNumber_7 = QtWidgets.QLCDNumber(self.order_box)
        self.lcdNumber_7.setGeometry(QtCore.QRect(130, 100, 81, 23))
        self.lcdNumber_7.setDigitCount(9)
        self.lcdNumber_7.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_7.setObjectName("lcdNumber_7")
        self.lcdNumber_8 = QtWidgets.QLCDNumber(self.order_box)
        self.lcdNumber_8.setGeometry(QtCore.QRect(130, 130, 81, 23))
        self.lcdNumber_8.setDigitCount(9)
        self.lcdNumber_8.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_8.setObjectName("lcdNumber_8")
        self.lcdNumber_9 = QtWidgets.QLCDNumber(self.order_box)
        self.lcdNumber_9.setGeometry(QtCore.QRect(230, 40, 81, 23))
        self.lcdNumber_9.setDigitCount(9)
        self.lcdNumber_9.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_9.setObjectName("lcdNumber_9")
        self.lcdNumber_10 = QtWidgets.QLCDNumber(self.order_box)
        self.lcdNumber_10.setGeometry(QtCore.QRect(230, 70, 81, 23))
        self.lcdNumber_10.setDigitCount(9)
        self.lcdNumber_10.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_10.setObjectName("lcdNumber_10")
        self.lcdNumber_11 = QtWidgets.QLCDNumber(self.order_box)
        self.lcdNumber_11.setGeometry(QtCore.QRect(230, 100, 81, 23))
        self.lcdNumber_11.setDigitCount(9)
        self.lcdNumber_11.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_11.setObjectName("lcdNumber_11")
        self.lcdNumber_12 = QtWidgets.QLCDNumber(self.order_box)
        self.lcdNumber_12.setGeometry(QtCore.QRect(230, 130, 81, 23))
        self.lcdNumber_12.setDigitCount(9)
        self.lcdNumber_12.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_12.setObjectName("lcdNumber_12")
        self.lcdNumber_13 = QtWidgets.QLCDNumber(self.order_box)
        self.lcdNumber_13.setGeometry(QtCore.QRect(340, 40, 91, 23))
        self.lcdNumber_13.setDigitCount(9)
        self.lcdNumber_13.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_13.setObjectName("lcdNumber_13")
        self.lcdNumber_14 = QtWidgets.QLCDNumber(self.order_box)
        self.lcdNumber_14.setGeometry(QtCore.QRect(340, 70, 91, 23))
        self.lcdNumber_14.setDigitCount(9)
        self.lcdNumber_14.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_14.setObjectName("lcdNumber_14")
        self.lcdNumber_15 = QtWidgets.QLCDNumber(self.order_box)
        self.lcdNumber_15.setGeometry(QtCore.QRect(340, 100, 91, 23))
        self.lcdNumber_15.setDigitCount(9)
        self.lcdNumber_15.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_15.setObjectName("lcdNumber_15")
        self.lcdNumber_16 = QtWidgets.QLCDNumber(self.order_box)
        self.lcdNumber_16.setGeometry(QtCore.QRect(340, 130, 91, 23))
        self.lcdNumber_16.setDigitCount(9)
        self.lcdNumber_16.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_16.setObjectName("lcdNumber_16")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(870, 30, 361, 161))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_130 = QtWidgets.QLabel(self.groupBox_4)
        self.label_130.setGeometry(QtCore.QRect(20, 40, 47, 13))
        self.label_130.setObjectName("label_130")
        self.per_buy = QtWidgets.QLineEdit(self.groupBox_4)
        self.per_buy.setGeometry(QtCore.QRect(80, 40, 113, 20))
        self.per_buy.setObjectName("per_buy")
        self.label_136 = QtWidgets.QLabel(self.groupBox_4)
        self.label_136.setGeometry(QtCore.QRect(20, 70, 47, 13))
        self.label_136.setObjectName("label_136")
        self.label_137 = QtWidgets.QLabel(self.groupBox_4)
        self.label_137.setGeometry(QtCore.QRect(20, 100, 47, 13))
        self.label_137.setObjectName("label_137")
        self.label_138 = QtWidgets.QLabel(self.groupBox_4)
        self.label_138.setGeometry(QtCore.QRect(20, 130, 47, 13))
        self.label_138.setObjectName("label_138")
        self.sep_buy = QtWidgets.QLineEdit(self.groupBox_4)
        self.sep_buy.setGeometry(QtCore.QRect(80, 70, 113, 20))
        self.sep_buy.setObjectName("sep_buy")
        self.dec_buy = QtWidgets.QLineEdit(self.groupBox_4)
        self.dec_buy.setGeometry(QtCore.QRect(80, 100, 113, 20))
        self.dec_buy.setObjectName("dec_buy")
        self.mar_buy = QtWidgets.QLineEdit(self.groupBox_4)
        self.mar_buy.setGeometry(QtCore.QRect(80, 130, 113, 20))
        self.mar_buy.setObjectName("mar_buy")
        self.label_139 = QtWidgets.QLabel(self.groupBox_4)
        self.label_139.setGeometry(QtCore.QRect(120, 20, 47, 13))
        self.label_139.setObjectName("label_139")
        self.label_140 = QtWidgets.QLabel(self.groupBox_4)
        self.label_140.setGeometry(QtCore.QRect(240, 20, 47, 13))
        self.label_140.setObjectName("label_140")
        self.per_sell = QtWidgets.QLineEdit(self.groupBox_4)
        self.per_sell.setGeometry(QtCore.QRect(220, 40, 113, 20))
        self.per_sell.setObjectName("per_sell")
        self.sep_sell = QtWidgets.QLineEdit(self.groupBox_4)
        self.sep_sell.setGeometry(QtCore.QRect(220, 70, 113, 20))
        self.sep_sell.setObjectName("sep_sell")
        self.dec_sell = QtWidgets.QLineEdit(self.groupBox_4)
        self.dec_sell.setGeometry(QtCore.QRect(220, 100, 113, 20))
        self.dec_sell.setObjectName("dec_sell")
        self.mar_sell = QtWidgets.QLineEdit(self.groupBox_4)
        self.mar_sell.setGeometry(QtCore.QRect(220, 130, 113, 20))
        self.mar_sell.setObjectName("mar_sell")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton.setGeometry(QtCore.QRect(340, 40, 16, 17))
        self.radioButton.setCheckable(True)
        self.radioButton.setChecked(True)
        self.radioButton.setAutoRepeat(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_2.setGeometry(QtCore.QRect(340, 70, 16, 17))
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_3.setGeometry(QtCore.QRect(340, 100, 16, 17))
        self.radioButton_3.setText("")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_4.setGeometry(QtCore.QRect(340, 130, 16, 17))
        self.radioButton_4.setText("")
        self.radioButton_4.setObjectName("radioButton_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 91, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(290, 220, 81, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(560, 220, 71, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(810, 220, 71, 16))
        self.label_8.setObjectName("label_8")
        self.label_141 = QtWidgets.QLabel(self.centralwidget)
        self.label_141.setGeometry(QtCore.QRect(1060, 220, 71, 16))
        self.label_141.setObjectName("label_141")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1336, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # ให้แสดงในหน้า window หลังจากเปิดใช้งานโปรแกรม
        self.market_price()
        # self.radiobutton()
        self.radio_market()
        self.ok_button.clicked.connect(self.submitname)
        self.ok_button.clicked.connect(self.name.hide)
        self.name.isClearButtonEnabled()
        self.clear_button.clicked.connect(self.clearname)
        self.clear_button.clicked.connect(self.name.show)
        self.data_sheet()
        self.retranslateUi(MainWindow)

        # self.clear_button.clicked.connect(self.name.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # #ฟังชั่นเเลิอก product
    #
    def radio_market(self):
        self.radioButton.clicked.connect(self.market_price)
        self.radioButton_2.clicked.connect(self.market_price)
        self.radioButton_3.clicked.connect(self.market_price)
        self.radioButton_4.clicked.connect(self.market_price)
        self.radiobutton()

    def radiobutton(self):
        self.radioButton.clicked.connect(self.order_books_per)
        self.radioButton_2.clicked.connect(self.order_books_sep)
        self.radioButton_3.clicked.connect(self.order_books_dec)
        self.radioButton_4.clicked.connect(self.order_books_mar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Inset API KEY"))
        self.label_2.setText(_translate("MainWindow", "Name :"))
        self.ok_button.setText(_translate("MainWindow", "Submit"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        self.open_button_10.setText(_translate("MainWindow", "Open"))
        self.open_button_9.setText(_translate("MainWindow", "Open"))
        self.open_button_8.setText(_translate("MainWindow", "Open"))
        self.close_button_3.setText(_translate("MainWindow", "Close"))
        self.label_14.setText(_translate("MainWindow", "Open Price"))
        self.close_button_7.setText(_translate("MainWindow", "Close"))
        self.close_button_10.setText(_translate("MainWindow", "Close"))
        self.open_button_5.setText(_translate("MainWindow", "Open"))
        self.close_button_4.setText(_translate("MainWindow", "Close"))
        self.open_button_7.setText(_translate("MainWindow", "Open"))
        self.open_button_6.setText(_translate("MainWindow", "Open"))
        self.open_button_4.setText(_translate("MainWindow", "Open"))
        self.label_17.setText(_translate("MainWindow", "7"))
        self.label_18.setText(_translate("MainWindow", "6"))
        self.label_19.setText(_translate("MainWindow", "5"))
        self.label_16.setText(_translate("MainWindow", "8"))
        self.label_23.setText(_translate("MainWindow", "2"))
        self.label_24.setText(_translate("MainWindow", "Bullet"))
        self.label_20.setText(_translate("MainWindow", "4"))
        self.close_button_8.setText(_translate("MainWindow", "Close"))
        self.open_button_3.setText(_translate("MainWindow", "Open"))
        self.close_button_6.setText(_translate("MainWindow", "Close"))
        self.open_button_2.setText(_translate("MainWindow", "Open"))
        self.label_21.setText(_translate("MainWindow", "3"))
        self.label_11.setText(_translate("MainWindow", "Open"))
        self.open_button_1.setText(_translate("MainWindow", "Open"))
        self.close_button_1.setText(_translate("MainWindow", "Close"))
        self.label_15.setText(_translate("MainWindow", "9"))
        self.close_button_9.setText(_translate("MainWindow", "Close"))
        self.close_button_2.setText(_translate("MainWindow", "Close"))
        self.label_22.setText(_translate("MainWindow", "1"))
        self.label_13.setText(_translate("MainWindow", "10"))
        self.close_button_5.setText(_translate("MainWindow", "Close"))
        self.label_25.setText(_translate("MainWindow", "Close"))
        self.close_button_15.setText(_translate("MainWindow", "Close"))
        self.label_34.setText(_translate("MainWindow", "19"))
        self.close_button_11.setText(_translate("MainWindow", "Close"))
        self.label_33.setText(_translate("MainWindow", "Open"))
        self.label_35.setText(_translate("MainWindow", "20"))
        self.close_button_12.setText(_translate("MainWindow", "Close"))
        self.label_36.setText(_translate("MainWindow", "11"))
        self.label_37.setText(_translate("MainWindow", "13"))
        self.label_38.setText(_translate("MainWindow", "12"))
        self.close_button_19.setText(_translate("MainWindow", "Close"))
        self.open_button_11.setText(_translate("MainWindow", "Open"))
        self.label_44.setText(_translate("MainWindow", "18"))
        self.label_45.setText(_translate("MainWindow", "17"))
        self.open_button_12.setText(_translate("MainWindow", "Open"))
        self.open_button_13.setText(_translate("MainWindow", "Open"))
        self.close_button_14.setText(_translate("MainWindow", "Close"))
        self.label_46.setText(_translate("MainWindow", "16"))
        self.label_47.setText(_translate("MainWindow", "15"))
        self.open_button_17.setText(_translate("MainWindow", "Open"))
        self.open_button_16.setText(_translate("MainWindow", "Open"))
        self.open_button_14.setText(_translate("MainWindow", "Open"))
        self.open_button_19.setText(_translate("MainWindow", "Open"))
        self.open_button_15.setText(_translate("MainWindow", "Open"))
        self.open_button_20.setText(_translate("MainWindow", "Open"))
        self.label_50.setText(_translate("MainWindow", "Open Price"))
        self.open_button_18.setText(_translate("MainWindow", "Open"))
        self.close_button_13.setText(_translate("MainWindow", "Close"))
        self.close_button_17.setText(_translate("MainWindow", "Close"))
        self.close_button_20.setText(_translate("MainWindow", "Close"))
        self.close_button_16.setText(_translate("MainWindow", "Close"))
        self.label_40.setText(_translate("MainWindow", "Bullet"))
        self.label_39.setText(_translate("MainWindow", "14"))
        self.close_button_18.setText(_translate("MainWindow", "Close"))
        self.label_43.setText(_translate("MainWindow", "Close"))
        self.open_button_21.setText(_translate("MainWindow", "Open"))
        self.label_57.setText(_translate("MainWindow", "Open"))
        self.close_button_21.setText(_translate("MainWindow", "Close"))
        self.label_58.setText(_translate("MainWindow", "29"))
        self.label_59.setText(_translate("MainWindow", "30"))
        self.close_button_25.setText(_translate("MainWindow", "Close"))
        self.close_button_22.setText(_translate("MainWindow", "Close"))
        self.close_button_29.setText(_translate("MainWindow", "Close"))
        self.label_60.setText(_translate("MainWindow", "21"))
        self.label_61.setText(_translate("MainWindow", "23"))
        self.label_62.setText(_translate("MainWindow", "22"))
        self.label_63.setText(_translate("MainWindow", "24"))
        self.label_64.setText(_translate("MainWindow", "Bullet"))
        self.close_button_26.setText(_translate("MainWindow", "Close"))
        self.close_button_28.setText(_translate("MainWindow", "Close"))
        self.open_button_23.setText(_translate("MainWindow", "Open"))
        self.label_67.setText(_translate("MainWindow", "Close"))
        self.open_button_22.setText(_translate("MainWindow", "Open"))
        self.label_68.setText(_translate("MainWindow", "28"))
        self.label_69.setText(_translate("MainWindow", "27"))
        self.label_70.setText(_translate("MainWindow", "26"))
        self.label_71.setText(_translate("MainWindow", "25"))
        self.close_button_24.setText(_translate("MainWindow", "Close"))
        self.open_button_25.setText(_translate("MainWindow", "Open"))
        self.open_button_27.setText(_translate("MainWindow", "Open"))
        self.open_button_26.setText(_translate("MainWindow", "Open"))
        self.open_button_24.setText(_translate("MainWindow", "Open"))
        self.open_button_29.setText(_translate("MainWindow", "Open"))
        self.open_button_28.setText(_translate("MainWindow", "Open"))
        self.open_button_30.setText(_translate("MainWindow", "Open"))
        self.label_74.setText(_translate("MainWindow", "Open Price"))
        self.close_button_23.setText(_translate("MainWindow", "Close"))
        self.close_button_27.setText(_translate("MainWindow", "Close"))
        self.close_button_30.setText(_translate("MainWindow", "Close"))
        self.open_button_31.setText(_translate("MainWindow", "Open"))
        self.label_81.setText(_translate("MainWindow", "Open"))
        self.close_button_31.setText(_translate("MainWindow", "Close"))
        self.label_82.setText(_translate("MainWindow", "39"))
        self.label_83.setText(_translate("MainWindow", "40"))
        self.close_button_35.setText(_translate("MainWindow", "Close"))
        self.close_button_32.setText(_translate("MainWindow", "Close"))
        self.close_button_39.setText(_translate("MainWindow", "Close"))
        self.label_84.setText(_translate("MainWindow", "31"))
        self.label_85.setText(_translate("MainWindow", "33"))
        self.label_86.setText(_translate("MainWindow", "32"))
        self.label_87.setText(_translate("MainWindow", "34"))
        self.label_88.setText(_translate("MainWindow", "Bullet"))
        self.close_button_36.setText(_translate("MainWindow", "Close"))
        self.close_button_38.setText(_translate("MainWindow", "Close"))
        self.open_button_33.setText(_translate("MainWindow", "Open"))
        self.label_91.setText(_translate("MainWindow", "Close"))
        self.open_button_32.setText(_translate("MainWindow", "Open"))
        self.label_92.setText(_translate("MainWindow", "38"))
        self.label_93.setText(_translate("MainWindow", "37"))
        self.label_94.setText(_translate("MainWindow", "36"))
        self.label_95.setText(_translate("MainWindow", "35"))
        self.close_button_34.setText(_translate("MainWindow", "Close"))
        self.open_button_35.setText(_translate("MainWindow", "Open"))
        self.open_button_37.setText(_translate("MainWindow", "Open"))
        self.open_button_36.setText(_translate("MainWindow", "Open"))
        self.open_button_34.setText(_translate("MainWindow", "Open"))
        self.open_button_39.setText(_translate("MainWindow", "Open"))
        self.open_button_38.setText(_translate("MainWindow", "Open"))
        self.open_button_40.setText(_translate("MainWindow", "Open"))
        self.label_98.setText(_translate("MainWindow", "Open Price"))
        self.close_button_33.setText(_translate("MainWindow", "Close"))
        self.close_button_37.setText(_translate("MainWindow", "Close"))
        self.close_button_40.setText(_translate("MainWindow", "Close"))
        self.open_button_41.setText(_translate("MainWindow", "Open"))
        self.label_105.setText(_translate("MainWindow", "Open"))
        self.close_button_41.setText(_translate("MainWindow", "Close"))
        self.label_106.setText(_translate("MainWindow", "49"))
        self.label_107.setText(_translate("MainWindow", "50"))
        self.close_button_45.setText(_translate("MainWindow", "Close"))
        self.close_button_42.setText(_translate("MainWindow", "Close"))
        self.close_button_49.setText(_translate("MainWindow", "Close"))
        self.label_108.setText(_translate("MainWindow", "41"))
        self.label_109.setText(_translate("MainWindow", "43"))
        self.label_110.setText(_translate("MainWindow", "42"))
        self.label_111.setText(_translate("MainWindow", "44"))
        self.label_112.setText(_translate("MainWindow", "Bullet"))
        self.close_button_46.setText(_translate("MainWindow", "Close"))
        self.close_button_48.setText(_translate("MainWindow", "Close"))
        self.open_button_43.setText(_translate("MainWindow", "Open"))
        self.label_115.setText(_translate("MainWindow", "Close"))
        self.open_button_42.setText(_translate("MainWindow", "Open"))
        self.label_116.setText(_translate("MainWindow", "48"))
        self.label_117.setText(_translate("MainWindow", "47"))
        self.label_118.setText(_translate("MainWindow", "46"))
        self.label_119.setText(_translate("MainWindow", "45"))
        self.close_button_44.setText(_translate("MainWindow", "Close"))
        self.open_button_45.setText(_translate("MainWindow", "Open"))
        self.open_button_47.setText(_translate("MainWindow", "Open"))
        self.open_button_46.setText(_translate("MainWindow", "Open"))
        self.open_button_44.setText(_translate("MainWindow", "Open"))
        self.open_button_49.setText(_translate("MainWindow", "Open"))
        self.open_button_48.setText(_translate("MainWindow", "Open"))
        self.open_button_50.setText(_translate("MainWindow", "Open"))
        self.label_122.setText(_translate("MainWindow", "Open Price"))
        self.close_button_43.setText(_translate("MainWindow", "Close"))
        self.close_button_47.setText(_translate("MainWindow", "Close"))
        self.close_button_50.setText(_translate("MainWindow", "Close"))
        self.order_box.setTitle(_translate("MainWindow", "Name"))
        self.label_129.setText(_translate("MainWindow", "1"))
        self.label_131.setText(_translate("MainWindow", "3"))
        self.label_132.setText(_translate("MainWindow", "4"))
        self.label_133.setText(_translate("MainWindow", "Size"))
        self.label_134.setText(_translate("MainWindow", "Ask"))
        self.label_135.setText(_translate("MainWindow", "2"))
        self.label.setText(_translate("MainWindow", "Size"))
        self.label_4.setText(_translate("MainWindow", "Bid"))
        self.groupBox_4.setTitle(_translate("MainWindow", "BTC Positions"))
        self.label_130.setText(_translate("MainWindow", "Perpetual"))
        self.label_136.setText(_translate("MainWindow", "25 Sep 2020"))
        self.label_137.setText(_translate("MainWindow", "25 Dec 2020"))
        self.label_138.setText(_translate("MainWindow", "26 Mar 2020"))
        self.label_139.setText(_translate("MainWindow", "BUY"))
        self.label_140.setText(_translate("MainWindow", "SEEL"))
        self.label_5.setText(_translate("MainWindow", "RP 11000-15000"))
        self.label_6.setText(_translate("MainWindow", "RP 9000-11000"))
        self.label_7.setText(_translate("MainWindow", "RP 7000-9000"))
        self.label_8.setText(_translate("MainWindow", "RP 5000-7000"))
        self.label_141.setText(_translate("MainWindow", "RP 3000-5000"))

    def openDialog(self):
        mydialog = QDialog(self)
        mydialog.setModal(True)
        mydialog.exec()

    def order_books_per(self):
        import client
        # count_loop = 1
        # while count_loop > 0:
        _symbol = _perpetual
        orderBook = client.exchange.fetch_order_book(_symbol, 5)
        # เลือก bid กับ ask
        orderBook_bid = orderBook['bids']
        orderBook_ask = orderBook['asks']
        # data frame เพื่อง่ายต่อการระบุตำแหน่งข้อมูล
        list_bid = pd.DataFrame(orderBook_bid)
        list_ask = pd.DataFrame(orderBook_ask)

        # แยกข้อมูลออกเป็นตัว
        price_bid_1 = list_bid[0][0]
        price_bid_2 = list_bid[0][1]
        price_bid_3 = list_bid[0][2]
        price_bid_4 = list_bid[0][3]
        price_bid_5 = list_bid[0][4]

        bid_size_1 = list_bid[1][0]
        bid_size_2 = list_bid[1][1]
        bid_size_3 = list_bid[1][2]
        bid_size_4 = list_bid[1][3]
        bid_size_5 = list_bid[1][4]

        ask_price_1 = list_ask[0][0]
        ask_price_2 = list_ask[0][1]
        ask_price_3 = list_ask[0][2]
        ask_price_4 = list_ask[0][3]
        ask_price_5 = list_ask[0][4]

        ask_size_1 = list_ask[1][0]
        ask_size_2 = list_ask[1][1]
        ask_size_3 = list_ask[1][2]
        ask_size_4 = list_ask[1][3]
        ask_size_5 = list_ask[1][4]

        # เปลี่ยนตัวแปรเพื่อง่ายต่อการนำไปใช้
        bid1 = price_bid_1
        size1 = bid_size_1
        bid2 = price_bid_2
        size2 = bid_size_2
        bid3 = price_bid_3
        size3 = bid_size_3
        bid4 = price_bid_4
        size4 = bid_size_4
        # bid5 = price_bid_5
        # size5 = bid_size_5

        ask1 = ask_price_1
        size_a1 = ask_size_1
        ask2 = ask_price_2
        size_a2 = ask_size_2
        ask3 = ask_price_3
        size_a3 = ask_size_3
        ask4 = ask_price_4
        size_a4 = ask_size_4
        # ask5 = ask_price_5
        # size_a5 = ask_size_5

        # แสดงบน LED
        self.lcdNumber.display(bid1)
        self.lcdNumber_5.display(size1)
        self.lcdNumber_2.display(bid2)
        self.lcdNumber_6.display(size2)
        self.lcdNumber_3.display(bid3)
        self.lcdNumber_7.display(size3)
        self.lcdNumber_4.display(bid4)
        self.lcdNumber_8.display(size4)
        # self.lcdNumber_4.display(bid5)
        # self.lcdNumber_8.display(size5)

        self.lcdNumber_9.display(ask1)
        self.lcdNumber_13.display(size_a1)
        self.lcdNumber_10.display(ask2)
        self.lcdNumber_14.display(size_a2)
        self.lcdNumber_11.display(ask3)
        self.lcdNumber_15.display(size_a3)
        self.lcdNumber_12.display(ask4)
        self.lcdNumber_16.display(size_a4)
        # self.lcdNumber_13.display(ask5)
        # self.lcdNumber_17.display(size_a5)

        #     count_loop += 1
        #     time.sleep(delay)
        #     print(count_loop)
        # else:
        #     self.radioButton.clicked.disconnect(self.order_books_per)

    def order_books_sep(self):
        import client
        count_loop = 1
        # while (count_loop > 0) is True:
        # ดึงข้อมูล
        _symbol = _sep
        orderBook = client.exchange.fetch_order_book(_symbol, 5)
        # เลือก bid กับ ask
        orderBook_bid = orderBook['bids']
        orderBook_ask = orderBook['asks']
        # data frame เพื่อง่ายต่อการระบุตำแหน่งข้อมูล
        list_bid = pd.DataFrame(orderBook_bid)
        list_ask = pd.DataFrame(orderBook_ask)

        # แยกข้อมูลออกเป็นตัว
        price_bid_1 = list_bid[0][0]
        price_bid_2 = list_bid[0][1]
        price_bid_3 = list_bid[0][2]
        price_bid_4 = list_bid[0][3]
        price_bid_5 = list_bid[0][4]

        bid_size_1 = list_bid[1][0]
        bid_size_2 = list_bid[1][1]
        bid_size_3 = list_bid[1][2]
        bid_size_4 = list_bid[1][3]
        bid_size_5 = list_bid[1][4]

        ask_price_1 = list_ask[0][0]
        ask_price_2 = list_ask[0][1]
        ask_price_3 = list_ask[0][2]
        ask_price_4 = list_ask[0][3]
        ask_price_5 = list_ask[0][4]

        ask_size_1 = list_ask[1][0]
        ask_size_2 = list_ask[1][1]
        ask_size_3 = list_ask[1][2]
        ask_size_4 = list_ask[1][3]
        ask_size_5 = list_ask[1][4]

        # เปลี่ยนตัวแปรเพื่อง่ายต่อการนำไปใช้
        bid1 = price_bid_1
        size1 = bid_size_1
        bid2 = price_bid_2
        size2 = bid_size_2
        bid3 = price_bid_3
        size3 = bid_size_3
        bid4 = price_bid_4
        size4 = bid_size_4
        # bid5 = price_bid_5
        # size5 = bid_size_5

        ask1 = ask_price_1
        size_a1 = ask_size_1
        ask2 = ask_price_2
        size_a2 = ask_size_2
        ask3 = ask_price_3
        size_a3 = ask_size_3
        ask4 = ask_price_4
        size_a4 = ask_size_4
        # ask5 = ask_price_5
        # size_a5 = ask_size_5

        # แสดงบน LED
        self.lcdNumber.display(bid1)
        self.lcdNumber_5.display(size1)
        self.lcdNumber_2.display(bid2)
        self.lcdNumber_6.display(size2)
        self.lcdNumber_3.display(bid3)
        self.lcdNumber_7.display(size3)
        self.lcdNumber_4.display(bid4)
        self.lcdNumber_8.display(size4)
        # self.lcdNumber_4.display(bid5)
        # self.lcdNumber_8.display(size5)

        self.lcdNumber_9.display(ask1)
        self.lcdNumber_13.display(size_a1)
        self.lcdNumber_10.display(ask2)
        self.lcdNumber_14.display(size_a2)
        self.lcdNumber_11.display(ask3)
        self.lcdNumber_15.display(size_a3)
        self.lcdNumber_12.display(ask4)
        self.lcdNumber_16.display(size_a4)
        # self.lcdNumber_13.display(ask5)
        # self.lcdNumber_17.display(size_a5)
        # print(count_loop)
        # count_loop += 1
        # time.sleep(delay)

    def order_books_dec(self):
        import client
        count_loop = 1
        # while (count_loop > 0) is True:
        # ดึงข้อมูล
        _symbol = _dec
        orderBook = client.exchange.fetch_order_book(_symbol, 5)
        # เลือก bid กับ ask
        orderBook_bid = orderBook['bids']
        orderBook_ask = orderBook['asks']
        # data frame เพื่อง่ายต่อการระบุตำแหน่งข้อมูล
        list_bid = pd.DataFrame(orderBook_bid)
        list_ask = pd.DataFrame(orderBook_ask)

        # แยกข้อมูลออกเป็นตัว
        price_bid_1 = list_bid[0][0]
        price_bid_2 = list_bid[0][1]
        price_bid_3 = list_bid[0][2]
        price_bid_4 = list_bid[0][3]
        price_bid_5 = list_bid[0][4]

        bid_size_1 = list_bid[1][0]
        bid_size_2 = list_bid[1][1]
        bid_size_3 = list_bid[1][2]
        bid_size_4 = list_bid[1][3]
        bid_size_5 = list_bid[1][4]

        ask_price_1 = list_ask[0][0]
        ask_price_2 = list_ask[0][1]
        ask_price_3 = list_ask[0][2]
        ask_price_4 = list_ask[0][3]
        ask_price_5 = list_ask[0][4]

        ask_size_1 = list_ask[1][0]
        ask_size_2 = list_ask[1][1]
        ask_size_3 = list_ask[1][2]
        ask_size_4 = list_ask[1][3]
        ask_size_5 = list_ask[1][4]

        # เปลี่ยนตัวแปรเพื่อง่ายต่อการนำไปใช้
        bid1 = price_bid_1
        size1 = bid_size_1
        bid2 = price_bid_2
        size2 = bid_size_2
        bid3 = price_bid_3
        size3 = bid_size_3
        bid4 = price_bid_4
        size4 = bid_size_4
        # bid5 = price_bid_5
        # size5 = bid_size_5

        ask1 = ask_price_1
        size_a1 = ask_size_1
        ask2 = ask_price_2
        size_a2 = ask_size_2
        ask3 = ask_price_3
        size_a3 = ask_size_3
        ask4 = ask_price_4
        size_a4 = ask_size_4
        # ask5 = ask_price_5
        # size_a5 = ask_size_5

        # แสดงบน LED
        self.lcdNumber.display(bid1)
        self.lcdNumber_5.display(size1)
        self.lcdNumber_2.display(bid2)
        self.lcdNumber_6.display(size2)
        self.lcdNumber_3.display(bid3)
        self.lcdNumber_7.display(size3)
        self.lcdNumber_4.display(bid4)
        self.lcdNumber_8.display(size4)
        # self.lcdNumber_4.display(bid5)
        # self.lcdNumber_8.display(size5)

        self.lcdNumber_9.display(ask1)
        self.lcdNumber_13.display(size_a1)
        self.lcdNumber_10.display(ask2)
        self.lcdNumber_14.display(size_a2)
        self.lcdNumber_11.display(ask3)
        self.lcdNumber_15.display(size_a3)
        self.lcdNumber_12.display(ask4)
        self.lcdNumber_16.display(size_a4)
        # self.lcdNumber_13.display(ask5)
        # self.lcdNumber_17.display(size_a5)
        # print(count_loop)
        # count_loop += 1
        # time.sleep(delay)

    def order_books_mar(self):
        import client
        count_loop = 1
        # while (count_loop > 0) is True:
        # ดึงข้อมูล
        _symbol = _mar
        orderBook = client.exchange.fetch_order_book(_symbol, 5)
        # เลือก bid กับ ask
        orderBook_bid = orderBook['bids']
        orderBook_ask = orderBook['asks']
        # data frame เพื่อง่ายต่อการระบุตำแหน่งข้อมูล
        list_bid = pd.DataFrame(orderBook_bid)
        list_ask = pd.DataFrame(orderBook_ask)

        # แยกข้อมูลออกเป็นตัว
        price_bid_1 = list_bid[0][0]
        price_bid_2 = list_bid[0][1]
        price_bid_3 = list_bid[0][2]
        price_bid_4 = list_bid[0][3]
        price_bid_5 = list_bid[0][4]

        bid_size_1 = list_bid[1][0]
        bid_size_2 = list_bid[1][1]
        bid_size_3 = list_bid[1][2]
        bid_size_4 = list_bid[1][3]
        bid_size_5 = list_bid[1][4]

        ask_price_1 = list_ask[0][0]
        ask_price_2 = list_ask[0][1]
        ask_price_3 = list_ask[0][2]
        ask_price_4 = list_ask[0][3]
        ask_price_5 = list_ask[0][4]

        ask_size_1 = list_ask[1][0]
        ask_size_2 = list_ask[1][1]
        ask_size_3 = list_ask[1][2]
        ask_size_4 = list_ask[1][3]
        ask_size_5 = list_ask[1][4]

        # เปลี่ยนตัวแปรเพื่อง่ายต่อการนำไปใช้
        bid1 = price_bid_1
        size1 = bid_size_1
        bid2 = price_bid_2
        size2 = bid_size_2
        bid3 = price_bid_3
        size3 = bid_size_3
        bid4 = price_bid_4
        size4 = bid_size_4
        # bid5 = price_bid_5
        # size5 = bid_size_5

        ask1 = ask_price_1
        size_a1 = ask_size_1
        ask2 = ask_price_2
        size_a2 = ask_size_2
        ask3 = ask_price_3
        size_a3 = ask_size_3
        ask4 = ask_price_4
        size_a4 = ask_size_4
        # ask5 = ask_price_5
        # size_a5 = ask_size_5

        # แสดงบน LED
        self.lcdNumber.display(bid1)
        self.lcdNumber_5.display(size1)
        self.lcdNumber_2.display(bid2)
        self.lcdNumber_6.display(size2)
        self.lcdNumber_3.display(bid3)
        self.lcdNumber_7.display(size3)
        self.lcdNumber_4.display(bid4)
        self.lcdNumber_8.display(size4)
        # self.lcdNumber_4.display(bid5)
        # self.lcdNumber_8.display(size5)

        self.lcdNumber_9.display(ask1)
        self.lcdNumber_13.display(size_a1)
        self.lcdNumber_10.display(ask2)
        self.lcdNumber_14.display(size_a2)
        self.lcdNumber_11.display(ask3)
        self.lcdNumber_15.display(size_a3)
        self.lcdNumber_12.display(ask4)
        self.lcdNumber_16.display(size_a4)
        # self.lcdNumber_13.display(ask5)
        # self.lcdNumber_17.display(size_a5)
        # print(count_loop)
        # count_loop += 1
        # time.sleep(delay)

    def market_price(self):
        import client
        _perpetual = 'BTC-PERPETUAL'
        _sep = 'BTC-25SEP20'
        _dec = 'BTC-25DEC20'
        _mar = 'BTC-26MAR21'
        market_ticker1 = client.exchange.fetch_ticker(_perpetual)
        market_ticker2 = client.exchange.fetch_ticker(_sep)
        market_ticker3 = client.exchange.fetch_ticker(_dec)
        market_ticker4 = client.exchange.fetch_ticker(_mar)
        _bid_pep = market_ticker1['bid']
        _ask_pep = market_ticker1['ask']

        _bid_sep = market_ticker2['bid']
        _ask_sep = market_ticker2['ask']

        _bid_dec = market_ticker3['bid']
        _ask_dec = market_ticker3['ask']

        _bid_mar = market_ticker4['bid']
        _ask_mar = market_ticker4['ask']

        self.per_buy.setText(str(_bid_pep))
        self.per_sell.setText(str(_ask_pep))

        self.sep_buy.setText(str(_bid_sep))
        self.sep_sell.setText(str(_ask_sep))

        self.dec_buy.setText(str(_bid_dec))
        self.dec_sell.setText(str(_ask_dec))

        self.mar_buy.setText(str(_bid_mar))
        self.mar_sell.setText(str(_ask_mar))

    def submitname(self):
        nameCompit = self.name.text()
        print(nameCompit)
        # self.clear_button.clicked.connect(self.name.show)

    def clearname(self):
        nameCompit = None
        print(nameCompit)

    # data Sheet
    def data_sheet(self):
        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        def next_available_row(worksheet):
            str_list = list(filter(None, worksheet.col_values(1)))
            return str(len(str_list) + 1)

        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
        client = gspread.authorize(creds)
        my_list = [['1', '2', '3', '4', '5', '6', '7', '8']]
        sheet = client.open("PowersenseDatabase")
        worksheet = sheet.worksheet("Test")
        next_row = next_available_row(worksheet)
        worksheet_page = worksheet.get_all_values()

        worksheet.update("A{}".format(next_row), my_list)
        worksheet_df = pd.DataFrame(worksheet_page)
        print(worksheet_df)

    def clickopenorder(self):
        self.b

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
