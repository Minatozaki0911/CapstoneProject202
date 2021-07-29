# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UIZPxMjy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import os


class MainWindowUI(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 357)
        MainWindow.setStyleSheet(u"	color: rgb(220, 220, 220);\n"
"	background-color: rgb(38, 39, 58);\n"
"	border-radius: 10px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.run_script)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 160, 341, 81))
        self.pushButton.setStyleSheet(u"font-size: 25px;\n"
"font: bold;\n"
"padding-right:20px;\n"
"padding-left:20px;\n"
"text-align: center;\n"
"color: rgb(248, 251, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(97, 227, 221), stop:1 rgb(43, 176, 163));\n"
"border: 2px solid #f8fbff;\n"
"border-radius: 25px;\n"
"")
        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(-30, 100, 661, 61))
        font = QFont()
        font.setFamily(u"Sans Serif")
        font.setPointSize(24)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(1, 194, 154);")
        self.label_title.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start Application", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"<strong>HELLO</strong> USER", None))
    # retranslateUi

    def run_script(self):
        os.system("python3 ./Main.py")
