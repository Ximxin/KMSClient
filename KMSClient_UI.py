# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KMSClient_UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(452, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ViewWindows = QtWidgets.QPushButton(self.centralwidget)
        self.ViewWindows.setGeometry(QtCore.QRect(30, 30, 111, 61))
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(8)
        self.ViewWindows.setFont(font)
        self.ViewWindows.setObjectName("ViewWindows")
        self.ActivationWindows = QtWidgets.QPushButton(self.centralwidget)
        self.ActivationWindows.setGeometry(QtCore.QRect(170, 30, 111, 61))
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(8)
        self.ActivationWindows.setFont(font)
        self.ActivationWindows.setObjectName("ActivationWindows")
        self.ActivationOffice = QtWidgets.QPushButton(self.centralwidget)
        self.ActivationOffice.setGeometry(QtCore.QRect(310, 30, 111, 61))
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(8)
        self.ActivationOffice.setFont(font)
        self.ActivationOffice.setObjectName("ActivationOffice")
        self.ActivationState = QtWidgets.QTextBrowser(self.centralwidget)
        self.ActivationState.setGeometry(QtCore.QRect(30, 180, 391, 161))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.ActivationState.setFont(font)
        self.ActivationState.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.ActivationState.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.ActivationState.setToolTip("")
        self.ActivationState.setStyleSheet("")
        self.ActivationState.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.ActivationState.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.ActivationState.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.ActivationState.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.ActivationState.setObjectName("ActivationState")
        self.ActivationTips = QtWidgets.QTextBrowser(self.centralwidget)
        self.ActivationTips.setGeometry(QtCore.QRect(30, 400, 391, 151))
        self.ActivationTips.setObjectName("ActivationTips")
        self.TipsTitle = QtWidgets.QLabel(self.centralwidget)
        self.TipsTitle.setGeometry(QtCore.QRect(30, 380, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setBold(True)
        font.setWeight(75)
        self.TipsTitle.setFont(font)
        self.TipsTitle.setObjectName("TipsTitle")
        self.StateTitle = QtWidgets.QLabel(self.centralwidget)
        self.StateTitle.setGeometry(QtCore.QRect(30, 120, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setBold(True)
        font.setWeight(75)
        self.StateTitle.setFont(font)
        self.StateTitle.setObjectName("StateTitle")
        self.AotStateBar = QtWidgets.QProgressBar(self.centralwidget)
        self.AotStateBar.setGeometry(QtCore.QRect(30, 140, 421, 23))
        self.AotStateBar.setProperty("value", 0)
        self.AotStateBar.setObjectName("AotStateBar")
        self.AotInfo = QtWidgets.QLabel(self.centralwidget)
        self.AotInfo.setGeometry(QtCore.QRect(30, 160, 391, 21))
        self.AotInfo.setObjectName("AotInfo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ViewWindows.setText(_translate("MainWindow", "查看Windows版本"))
        self.ActivationWindows.setText(_translate("MainWindow", "激活Windows"))
        self.ActivationOffice.setText(_translate("MainWindow", "激活Office"))
        self.ActivationTips.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1、此软件仅支持VOL版本Windows或Office激活，其余版本无法激活！</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2、<span style=\" font-family:\'Consolas\'; color:#000000;\">Windows</span><span style=\" font-family:\'Microsoft YaHei UI\'; color:#000000;\">的版本如何区分？</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft YaHei UI\'; color:#000000;\">答：请点击软件</span><span style=\" font-family:\'Consolas\'; color:#000000;\">Windows</span><span style=\" font-family:\'Microsoft YaHei UI\'; color:#000000;\">版本按钮！查看“产品密钥通道”。若为</span><span style=\" font-family:\'Consolas\'; color:#000000;\">OEM</span><span style=\" font-family:\'Microsoft YaHei UI\'; color:#000000;\">则是出厂系统，若为</span><span style=\" font-family:\'Consolas\'; color:#000000;\">Retail</span><span style=\" font-family:\'Microsoft YaHei UI\'; color:#000000;\">则是零售版都不支持激活！</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Microsoft YaHei UI\'; color:#000000;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Microsoft YaHei UI\'; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:100px;\"><span style=\" font-family:\'Microsoft YaHei UI\'; color:#000000;\">软件仅提供参考或交流，请勿非法使用！</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:100px;\"><span style=\" font-family:\'Microsoft YaHei UI\'; color:#000000;\">一切法律责任与作者无关！——By KMSClient</span></p></body></html>"))
        self.TipsTitle.setText(_translate("MainWindow", "软件帮助信息："))
        self.StateTitle.setText(_translate("MainWindow", "激活状态："))
        self.AotInfo.setText(_translate("MainWindow", "等待激活..."))
