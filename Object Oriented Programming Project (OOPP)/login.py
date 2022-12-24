from PyQt5 import QtCore, QtGui, QtWidgets
import sys, res

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 821)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-30, -30, 450, 900))
        self.widget.setMaximumSize(QtCore.QSize(1000, 1000))
        self.widget.setStyleSheet("QPushButton#pushButton{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#pushButton:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"\n"
"QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{    \n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color:rgba(85, 98, 112, 255);\n"
"}\n"
"QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{    \n"
"    color:rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(115, 128, 142, 255);\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 20, 450, 867))
        self.label.setMaximumSize(QtCore.QSize(1000, 1000))
        self.label.setStyleSheet("border-radius:20px;\n"
"border-image: url(:/images/Images/background.png);\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 400, 825))
        self.label_2.setMaximumSize(QtCore.QSize(1000, 1000))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop:0.835227 rgba(0, 0, 0, 75));\n"
"border-radius:20px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(50, 50, 360, 780))
        self.label_3.setMaximumSize(QtCore.QSize(1000, 1000))
        self.label_3.setStyleSheet("background-color:rgba(0, 0, 0, 100);\n"
"border-radius:15px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.lbl_login = QtWidgets.QLabel(self.widget)
        self.lbl_login.setGeometry(QtCore.QRect(120, 220, 255, 55))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_login.setFont(font)
        self.lbl_login.setStyleSheet("color:rgba(255, 255, 255, 210);")
        self.lbl_login.setObjectName("lbl_login")
        self.email = QtWidgets.QLineEdit(self.widget)
        self.email.setGeometry(QtCore.QRect(100, 295, 255, 55))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.email.setFont(font)
        self.email.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.email.setText("")
        self.email.setObjectName("email")
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(100, 360, 255, 55))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.login = QtWidgets.QPushButton(self.widget)
        self.login.setGeometry(QtCore.QRect(100, 440, 255, 55))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.login.setFont(font)
        self.login.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.login.setStyleSheet("background-color:rgb(0,0,0);\n"
"color:rgb(0,0,255)\n"
"")
        self.login.setObjectName("login")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(100, 480, 111, 55))
        self.label_5.setStyleSheet("color:rgba(255, 255, 255, 140);")
        self.label_5.setObjectName("label_5")
        self.signup = QtWidgets.QPushButton(self.widget)
        self.signup.setEnabled(True)
        self.signup.setGeometry(QtCore.QRect(280, 480, 81, 55))
        self.signup.setStyleSheet("background-color:rgba(255, 255, 255, 0);color: rgb(0, 0, 255)")
        self.signup.setObjectName("signup")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_login.setText(_translate("Form", "  Giris Yap"))
        self.email.setPlaceholderText(_translate("Form", "E-Posta"))
        self.password.setPlaceholderText(_translate("Form", "Şifre"))
        self.login.setText(_translate("Form", "Giris Yap"))
        self.label_5.setText(_translate("Form", "Hesabınız Yok Mu?"))
        self.signup.setText(_translate("Form", "Kayıt Ol"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
