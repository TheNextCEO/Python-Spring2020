# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AIarcade.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowAI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 60, 251, 19))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 90, 221, 20))
        self.label_2.setObjectName("label_2")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(230, 140, 321, 331))
        self.listView.setObjectName("listView")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(231, 180, 321, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.AIflappy)
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(230, 250, 321, 34))
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(230, 320, 321, 34))
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 390, 321, 34))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def AIflappy(self):
        os.system("python AIflappybird.py")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "NoleEscape Arcade The AI version"))
        self.label_2.setText(_translate("MainWindow", "Click below to choose a Game"))
        self.pushButton.setText(_translate("MainWindow", "Flappy Bird"))
        self.pushButton2.setText(_translate("MainWindow", "Pong"))
        self.pushButton3.setText(_translate("MainWindow", "Break out"))
        self.pushButton_4.setText(_translate("MainWindow", "Classic Snake"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowAI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
