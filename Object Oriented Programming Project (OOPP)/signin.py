from PyQt5 import QtCore, QtGui, QtWidgets
import sys, res

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(397, 827)
        Form.setFocusPolicy(QtCore.Qt.TabFocus)
        Form.setAutoFillBackground(True)
        Form.setStyleSheet("")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-30, -30, 450, 867))
        self.widget.setMaximumSize(QtCore.QSize(1000, 1000))
        self.widget.setFocusPolicy(QtCore.Qt.TabFocus)
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
"border-image: url(:/images/Images/background.png);")
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
        self.login = QtWidgets.QPushButton(self.widget)
        self.login.setEnabled(True)
        self.login.setGeometry(QtCore.QRect(280, 520, 91, 55))
        self.login.setMaximumSize(QtCore.QSize(1000, 1000))
        self.login.setStyleSheet("background-color:rgba(255, 255, 255, 0);color: rgb(0, 0, 255)")
        self.login.setObjectName("login")
        self.lbl_login = QtWidgets.QLabel(self.widget)
        self.lbl_login.setGeometry(QtCore.QRect(108, 210, 250, 55))
        self.lbl_login.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_login.setFont(font)
        self.lbl_login.setStyleSheet("color:rgba(255, 255, 255, 210);px:25;\n"
"")
        self.lbl_login.setObjectName("lbl_login")
        self.password_2 = QtWidgets.QLineEdit(self.widget)
        self.password_2.setGeometry(QtCore.QRect(108, 420, 250, 55))
        self.password_2.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_2.setFont(font)
        self.password_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_2.setObjectName("password_2")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(108, 520, 91, 55))
        self.label_5.setMaximumSize(QtCore.QSize(1000, 1000))
        self.label_5.setStyleSheet("color:rgba(255, 255, 255, 140);")
        self.label_5.setObjectName("label_5")
        self.email = QtWidgets.QLineEdit(self.widget)
        self.email.setGeometry(QtCore.QRect(108, 285, 250, 55))
        self.email.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.email.setFont(font)
        self.email.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.email.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.email.setText("")
        self.email.setObjectName("email")
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(108, 350, 250, 55))
        self.password.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password.setFont(font)
        self.password.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.password.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.signin = QtWidgets.QPushButton(self.widget)
        self.signin.setGeometry(QtCore.QRect(108, 480, 250, 55))
        self.signin.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.signin.setFont(font)
        self.signin.setObjectName("signin")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.login.setText(_translate("Form", "Giriş Yap"))
        self.lbl_login.setText(_translate("Form", "     Kayıt Ol"))
        self.password_2.setPlaceholderText(_translate("Form", "Şifreyi Tekrarla"))
        self.label_5.setText(_translate("Form", "Şimdi Giriş Yap"))
        self.email.setPlaceholderText(_translate("Form", "E-Posta"))
        self.password.setPlaceholderText(_translate("Form", "Şifre"))
        self.signin.setText(_translate("Form", "Kayıt Ol"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
