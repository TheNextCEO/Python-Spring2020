from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindowAI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 60, 251, 19))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 90, 221, 20))
        self.label_2.setObjectName("label_2")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(230, 140, 321, 200))
        self.listView.setObjectName("listView")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(231, 180, 321, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.AIflappy)
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(230, 250, 321, 34))
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.clicked.connect(self.AIbreakout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def AIflappy(self):
        os.system("python3 AIflappybird.py")

    def AIbreakout(self):
        os.system("python3 AIBreakOut.py")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AI Arcade"))
        self.label.setText(_translate("MainWindow", "NoleEscape Arcade The AI Version"))
        self.label_2.setText(_translate("MainWindow", "Click below to choose a Game"))
        self.pushButton.setText(_translate("MainWindow", "Flappy Bird"))
        self.pushButton2.setText(_translate("MainWindow", "Break Out"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowAI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
