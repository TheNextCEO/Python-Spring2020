from dbFolder.dbFunctions import nullEscDBClass

global database
database = nullEscDBClass()
database.startDB("mysql.djangosfantasy.com", "djangoadmin8", "best!Group")

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Highscores(object):
    def load(self):
        result = (database.topScores("Snake", 0, 5))
        self.tableWidget.setRowCount(0)
        for rownum, rowdata in enumerate(result):
            self.tableWidget.insertRow(rownum)
            for colnum, data in enumerate(rowdata):
                self.tableWidget.setItem(rownum, colnum, QtWidgets.QTableWidgetItem(str(data)))

    def setupUi(self, Highscores):
        Highscores.setObjectName("Highscores")
        Highscores.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Highscores)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(100, 170, 601, 211))
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.heading = QtWidgets.QTableWidget(self.centralwidget)
        self.heading.setGeometry(QtCore.QRect(100, 110, 601, 61))
        self.heading.setRowCount(1)
        self.heading.setColumnCount(3)
        self.heading.setObjectName("heading")
        self.heading.horizontalHeader().setVisible(False)
        self.heading.horizontalHeader().setDefaultSectionSize(200)
        self.heading.verticalHeader().setVisible(False)
        self.heading.verticalHeader().setDefaultSectionSize(40)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 110, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(520, 110, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 330, 161, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.load)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 110, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        Highscores.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Highscores)
        self.statusbar.setObjectName("statusbar")
        Highscores.setStatusBar(self.statusbar)

        self.retranslateUi(Highscores)
        QtCore.QMetaObject.connectSlotsByName(Highscores)

    def retranslateUi(self, Highscores):
        _translate = QtCore.QCoreApplication.translate
        Highscores.setWindowTitle(_translate("Highscores", "MainWindow"))
        self.label.setText(_translate("Highscores", "User"))
        self.label_2.setText(_translate("Highscores", "High Score"))
        self.pushButton.setText(_translate("Highscores", "Load High Scores"))
        self.label_3.setText(_translate("Highscores", "Game"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Highscores = QtWidgets.QMainWindow()
    ui = Ui_Highscores()
    ui.setupUi(Highscores)
    Highscores.show()
    sys.exit(app.exec_())