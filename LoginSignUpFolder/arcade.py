# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arcade.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from LoginSignUpFolder.AIarcade import Ui_MainWindowAI
from LoginSignUpFolder.highscores import Ui_MainWindowHighScore
#import LoginSignUpFolder.Game.py as flappy
import LoginSignUpFolder.Gametry
import os
import pygame


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(170, 100, 421, 361))
        self.listView.setObjectName("listView")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 100, 421, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.flappy)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_5.clicked.connect(self.pong)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(self.snake)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_4.clicked.connect(self.break_out)

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.AIarcadeWindowShow)

        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_6.clicked.connect(self.HighScoreWindowShow)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 50, 241, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 70, 231, 21))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def AIarcadeWindowShow(self):
        self.arcadeWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowAI()
        self.ui.setupUi(self.arcadeWindow)
        self.arcadeWindow.show()

    def HighScoreWindowShow(self):
        self.highscoreWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowHighScore()
        self.ui.setupUi(self.highscoreWindow)
        self.highscoreWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Flappy Bird"))
        self.pushButton_5.setText(_translate("MainWindow", "Pong"))
        self.pushButton_3.setText(_translate("MainWindow", "Snake"))
        self.pushButton_4.setText(_translate("MainWindow", "Nole Escape"))
        self.pushButton.setText(_translate("MainWindow", "AI versions"))
        self.pushButton_6.setText(_translate("MainWindow", "High Scores"))

        self.label.setText(_translate("MainWindow", "NoleEscape Arcade"))
        self.label_2.setText(_translate("MainWindow", "Choose a game below!"))
    def flappy(self):
        os.system("python3 Gametry.py")
    def break_out(self):
        os.system("python3 breakout_test.py")
    def pong(self):
        os.system("python3 pypong.py")
    def snake(self):
        os.system("python3 Dsnake.py")
    def AI(self):
        self.AIarcadeWindowShow()
    def HighScore(self):
        self.HighScoreWindowShow()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
