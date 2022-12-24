from PyQt5 import QtCore, QtGui, QtWidgets
import sys, res

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(401, 826)
        Form.setStyleSheet("")
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
        self.label.setGeometry(QtCore.QRect(30, 30, 400, 825))
        font = QtGui.QFont()
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("border-image: url(:/images/Images/background.png);\n"
"border-radius:20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lbl_login = QtWidgets.QLabel(self.widget)
        self.lbl_login.setGeometry(QtCore.QRect(170, 100, 360, 60))
        font = QtGui.QFont()
        font.setFamily("Footlight MT Light")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_login.setFont(font)
        self.lbl_login.setStyleSheet("color:rgba(255, 255, 255, 210);")
        self.lbl_login.setObjectName("lbl_login")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(40, 780, 271, 55))
        self.label_5.setStyleSheet("color:rgba(255, 255, 255, 140);")
        self.label_5.setObjectName("label_5")
        self.btn_afet = QtWidgets.QPushButton(self.widget)
        self.btn_afet.setGeometry(QtCore.QRect(40, 210, 150, 150))
        self.btn_afet.setStyleSheet("background-image: url(:/images/Images/afet.png);")
        self.btn_afet.setText("")
        self.btn_afet.setObjectName("btn_afet")
        self.btn_enerji = QtWidgets.QPushButton(self.widget)
        self.btn_enerji.setGeometry(QtCore.QRect(40, 400, 150, 150))
        self.btn_enerji.setStyleSheet("background-image: url(:/images/C:/Users/Emir/Desktop/login/Images/enerji.png);\n"
"background-image: url(:/images/Images/enerji.png);")
        self.btn_enerji.setText("")
        self.btn_enerji.setObjectName("btn_enerji")
        self.btn_cevre = QtWidgets.QPushButton(self.widget)
        self.btn_cevre.setGeometry(QtCore.QRect(270, 210, 150, 150))
        self.btn_cevre.setStyleSheet("background-image: url(:/images/C:/Users/Emir/Desktop/login/Images/cevre.png);\n"
"background-image: url(:/images/Images/cevre.png);")
        self.btn_cevre.setText("")
        self.btn_cevre.setObjectName("btn_cevre")
        self.btn_yasam = QtWidgets.QPushButton(self.widget)
        self.btn_yasam.setGeometry(QtCore.QRect(270, 400, 150, 150))
        self.btn_yasam.setStyleSheet("background-image: url(:/images/C:/Users/Emir/Desktop/login/Images/yasam.png);\n"
"background-image: url(:/images/Images/yasam.png);")
        self.btn_yasam.setText("")
        self.btn_yasam.setObjectName("btn_yasam")
        self.btn_eko = QtWidgets.QPushButton(self.widget)
        self.btn_eko.setGeometry(QtCore.QRect(40, 590, 150, 150))
        self.btn_eko.setStyleSheet("background-image: url(:/images/C:/Users/Emir/Desktop/login/Images/ekonomi.png);\n"
"background-image: url(:/images/Images/ekonomi.png);")
        self.btn_eko.setText("")
        self.btn_eko.setObjectName("btn_eko")
        self.btn_tarim = QtWidgets.QPushButton(self.widget)
        self.btn_tarim.setGeometry(QtCore.QRect(270, 590, 150, 150))
        self.btn_tarim.setStyleSheet("background-image: url(:/images/C:/Users/Emir/Desktop/login/Images/tarim.png);\n"
"background-image: url(:/images/Images/tarim.png);")
        self.btn_tarim.setText("")
        self.btn_tarim.setObjectName("btn_tarim")
        self.btn_geri = QtWidgets.QPushButton(self.widget)
        self.btn_geri.setGeometry(QtCore.QRect(380, 780, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.btn_geri.setFont(font)
        self.btn_geri.setStyleSheet("color:rgb(0,0,0)\n"
"")
        self.btn_geri.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/geri.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_geri.setIcon(icon)
        self.btn_geri.setObjectName("btn_geri")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_login.setText(_translate("Form", "OOPP "))
        self.label_5.setText(_translate("Form", "© 2022, made with by Emir,Doğukan,Ceyhun..."))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
