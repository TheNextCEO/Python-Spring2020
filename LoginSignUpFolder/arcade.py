# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arcade.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
<<<<<<< HEAD
from LoginSignUpFolder.pypong import *
=======
from pypong import *
>>>>>>> 349564f8ecf5497d4a48dea86d872b39cf440c70

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
<<<<<<< HEAD

=======
>>>>>>> 349564f8ecf5497d4a48dea86d872b39cf440c70
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
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
<<<<<<< HEAD
=======
        self.pushButton.clicked(pongGame.setuppong(self))
>>>>>>> 349564f8ecf5497d4a48dea86d872b39cf440c70
        self.verticalLayout.addWidget(self.pushButton)
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
<<<<<<< HEAD
=======

>>>>>>> 349564f8ecf5497d4a48dea86d872b39cf440c70
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Flappy Bird"))
        self.pushButton_5.setText(_translate("MainWindow", "Pong"))
        self.pushButton_3.setText(_translate("MainWindow", "Snake"))
<<<<<<< HEAD
        self.pushButton_4.setText(_translate("MainWindow", "Breakout"))
=======
        self.pushButton_4.setText(_translate("MainWindow", "Nole Escape"))
>>>>>>> 349564f8ecf5497d4a48dea86d872b39cf440c70
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "NoleEscape Arcade"))
        self.label_2.setText(_translate("MainWindow", "Choose a game below!"))


<<<<<<< HEAD
if __name__ == "__main__":
    import sys
=======
if "_name_" == "__main__":
    import sys
    hi = pongGame()
>>>>>>> 349564f8ecf5497d4a48dea86d872b39cf440c70
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
<<<<<<< HEAD
=======

>>>>>>> 349564f8ecf5497d4a48dea86d872b39cf440c70
