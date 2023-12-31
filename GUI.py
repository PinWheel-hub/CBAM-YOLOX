# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(982, 640)
        MainWindow.setMinimumSize(QtCore.QSize(982, 640))
        MainWindow.setMaximumSize(QtCore.QSize(982, 640))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.wgt_video = myVideoWidget(self.centralwidget)
        self.wgt_video.setGeometry(QtCore.QRect(11, 11, 960, 512))
        self.wgt_video.setMinimumSize(QtCore.QSize(960, 512))
        self.wgt_video.setMaximumSize(QtCore.QSize(960, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.wgt_video.setPalette(palette)
        self.wgt_video.setAutoFillBackground(True)
        self.wgt_video.setObjectName("wgt_video")
        self.sld_video = myVideoSlider(self.centralwidget)
        self.sld_video.setGeometry(QtCore.QRect(11, 530, 881, 20))
        self.sld_video.setMinimumSize(QtCore.QSize(410, 0))
        self.sld_video.setMaximumSize(QtCore.QSize(16777215, 20))
        self.sld_video.setMaximum(100)
        self.sld_video.setOrientation(QtCore.Qt.Horizontal)
        self.sld_video.setObjectName("sld_video")
        self.lab_video = QtWidgets.QLabel(self.centralwidget)
        self.lab_video.setGeometry(QtCore.QRect(900, 529, 71, 21))
        self.lab_video.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.lab_video.setFont(font)
        self.lab_video.setObjectName("lab_video")
        self.lab_audio = QtWidgets.QLabel(self.centralwidget)
        self.lab_audio.setGeometry(QtCore.QRect(890, 560, 81, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.lab_audio.setFont(font)
        self.lab_audio.setObjectName("lab_audio")
        self.sld_audio = QtWidgets.QSlider(self.centralwidget)
        self.sld_audio.setGeometry(QtCore.QRect(730, 560, 150, 30))
        self.sld_audio.setMinimumSize(QtCore.QSize(100, 0))
        self.sld_audio.setMaximumSize(QtCore.QSize(160, 30))
        self.sld_audio.setProperty("value", 0)
        self.sld_audio.setOrientation(QtCore.Qt.Horizontal)
        self.sld_audio.setObjectName("sld_audio")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 560, 649, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_open = QtWidgets.QPushButton(self.widget)
        self.btn_open.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.btn_open.setFont(font)
        self.btn_open.setObjectName("btn_open")
        self.horizontalLayout.addWidget(self.btn_open)
        self.btn_recognize = QtWidgets.QPushButton(self.widget)
        self.btn_recognize.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.btn_recognize.setFont(font)
        self.btn_recognize.setObjectName("btn_recognize")
        self.horizontalLayout.addWidget(self.btn_recognize)
        self.btn_result = QtWidgets.QPushButton(self.widget)
        self.btn_result.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.btn_result.setFont(font)
        self.btn_result.setObjectName("btn_result")
        self.horizontalLayout.addWidget(self.btn_result)
        self.btn_play = QtWidgets.QPushButton(self.widget)
        self.btn_play.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.btn_play.setFont(font)
        self.btn_play.setObjectName("btn_play")
        self.horizontalLayout.addWidget(self.btn_play)
        self.btn_stop = QtWidgets.QPushButton(self.widget)
        self.btn_stop.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.btn_stop.setFont(font)
        self.btn_stop.setObjectName("btn_stop")
        self.horizontalLayout.addWidget(self.btn_stop)
        self.btn_return = QtWidgets.QPushButton(self.widget)
        self.btn_return.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.btn_return.setFont(font)
        self.btn_return.setObjectName("btn_return")
        self.horizontalLayout.addWidget(self.btn_return)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 982, 26))
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
        self.lab_video.setText(_translate("MainWindow", "00:00:00"))
        self.lab_audio.setText(_translate("MainWindow", "音量:0%"))
        self.btn_open.setText(_translate("MainWindow", "选择视频文件"))
        self.btn_recognize.setText(_translate("MainWindow", "识别该视频"))
        self.btn_result.setText(_translate("MainWindow", "播放识别结果"))
        self.btn_play.setText(_translate("MainWindow", "播放"))
        self.btn_stop.setText(_translate("MainWindow", "暂停"))
        self.btn_return.setText(_translate("MainWindow", "返回"))
from myVideoWidget import myVideoWidget
from myvideoslider import myVideoSlider
