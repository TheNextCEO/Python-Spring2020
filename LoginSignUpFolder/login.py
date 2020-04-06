import sqlite3
from welcome import Ui_MainWindow
from signup import Ui_signUp
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def showMessageBox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    def welcomeWindowshow(self):
        self.welcomeWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.welcomeWindow)
        self.welcomeWindow.show()
    def signUpShow(self):
        self.signUpWindow=QtWidgets.QDialog()
        self.ui=Ui_signUp()
        self.ui.setupUi(self.signUpWindow)
        self.signUpWindow.show()

    #creating the function that we call when we hit the login button
    def loginCheck(self):
    #have to verify if they entered valid data
        username=self.uname_lineEdit.text() #this returns the text fromt he line
        password=self.pass_lineEdit.text()

        #check if these are valid or not
        #need a connection tot he database first
        connection = sqlite3.connect("login.db")
        #find these in database
        result=connection.execute("SELECT * FROM USERS WHERE USERNAME=? AND PASSWORD=?",(username,password))
        if(len(result.fetchall())>0):
            print("User found! ")
            self.welcomeWindowshow()
        else:
            print("User not found!")
        self.showMessageBox('Warning!','Invalid Username and Password')
        connection.close()

    def signupCheck(self):
        print("Signup Button Clicked!")
        self.signUpShow()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")

        Dialog.resize(581, 461)

        self.u_name_label = QtWidgets.QLabel(Dialog)

        self.u_name_label.setGeometry(QtCore.QRect(130, 160, 91, 31))

        self.u_name_label.setObjectName("u_name_label")

        self.pass_label = QtWidgets.QLabel(Dialog)

        self.pass_label.setGeometry(QtCore.QRect(130, 220, 91, 31))

        self.pass_label.setObjectName("pass_label")

        self.uname_lineEdit = QtWidgets.QLineEdit(Dialog)

        self.uname_lineEdit.setGeometry(QtCore.QRect(270, 160, 171, 31))

        self.uname_lineEdit.setObjectName("uname_lineEdit")

        self.pass_lineEdit = QtWidgets.QLineEdit(Dialog)

        self.pass_lineEdit.setGeometry(QtCore.QRect(270, 220, 171, 31))

        self.pass_lineEdit.setObjectName("pass_lineEdit")
        #


        #

        self.login_btn = QtWidgets.QPushButton(Dialog)

        self.login_btn.setGeometry(QtCore.QRect(200, 290, 101, 31))

        self.login_btn.setObjectName("login_btn")
        ############################### Button Event ######################
        self.login_btn.clicked.connect(self.loginCheck)
        #created a method that takes in one argument, a function that is called when you click the button
        ##################################################################
        self.signup_btn = QtWidgets.QPushButton(Dialog)

        self.signup_btn.setGeometry(QtCore.QRect(340, 290, 101, 31))

        self.signup_btn.setObjectName("signup_btn")
        ############################### Button Event ######################
        self.signup_btn.clicked.connect(self.signupCheck)
        # created a method that takes in one argument, a function that is called when you click the button
        ############################################################

        self.label = QtWidgets.QLabel(Dialog)

        self.label.setGeometry(QtCore.QRect(180, 70, 241, 41))

        font = QtGui.QFont()

        font.setPointSize(15)

        self.label.setFont(font)

        self.label.setObjectName("label")

        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate

        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        self.u_name_label.setText(_translate("Dialog", "USERNAME:"))

        self.pass_label.setText(_translate("Dialog", "PASSWORD:"))

        self.login_btn.setText(_translate("Dialog", "Login"))

        self.signup_btn.setText(_translate("Dialog", "Sign Up"))

        self.label.setText(_translate("Dialog", "NoleEscape Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())