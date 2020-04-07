from PyQt5 import QtCore, QtGui, QtWidgets
from dbFolder.dbFunctions import nullEscDBClass

class Ui_signUp(object):
    def showMessageBox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def insertData(self):
        username=self.uname_lineEdit.text()
        email=self.email_lineEdit.text()
        password=self.password_lineEdit.text()
        database = nullEscDBClass()

        database.startDB("mysql.djangosfantasy.com", "djangoadmin8", "best!Group")
        database.signupUser(username,password)
        self.showMessageBox('SignUp!', 'SignUp Successful!')

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(578, 383)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 80, 68, 19))
        self.label.setText("")
        self.label.setObjectName("label")
        self.u_name_label = QtWidgets.QLabel(Dialog)
        self.u_name_label.setGeometry(QtCore.QRect(130, 110, 91, 31))
        self.u_name_label.setObjectName("u_name_label")
        self.pass_label = QtWidgets.QLabel(Dialog)
        self.pass_label.setGeometry(QtCore.QRect(130, 210, 91, 31))
        self.pass_label.setObjectName("pass_label")
        self.u_name_label_2 = QtWidgets.QLabel(Dialog)
        self.u_name_label_2.setGeometry(QtCore.QRect(130, 160, 91, 31))
        self.u_name_label_2.setObjectName("u_name_label_2")
        self.uname_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(260, 110, 141, 25))
        self.uname_lineEdit.setObjectName("uname_lineEdit")
        self.email_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.email_lineEdit.setGeometry(QtCore.QRect(260, 160, 141, 25))
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.password_lineEdit.setGeometry(QtCore.QRect(260, 210, 141, 25))
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.signup_btn = QtWidgets.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(290, 280, 81, 31))
        self.signup_btn.setObjectName("signup_btn")
        #########################Event##################
        self.signup_btn.clicked.connect(self.insertData)
        ############################################
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 30, 400, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.u_name_label.setText(_translate("Dialog", "Username:"))
        self.pass_label.setText(_translate("Dialog", "Password:"))
        self.u_name_label_2.setText(_translate("Dialog", "E-mail Address:"))
        self.signup_btn.setText(_translate("Dialog", "Sign Up"))
        self.label_2.setText(_translate("Dialog","Welcome to NoleEscape: Create a New Account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_signUp()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
