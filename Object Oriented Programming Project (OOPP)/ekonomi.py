from PyQt5 import QtCore, QtGui, QtWidgets
import sys, res

class Ui_Ekonomi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(398, 826)
        Form.setStyleSheet("")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(-20, -10, 450, 867))
        self.label_2.setStyleSheet("border-radius:20px;\n"
"border-image: url(:/images/Images/background.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 360, 780))
        self.label_6.setMaximumSize(QtCore.QSize(1000, 1000))
        self.label_6.setStyleSheet("background-color:rgba(0, 0, 0, 100);\n"
"border-radius:15px;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-20, -30, 450, 900))
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
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(50, 780, 271, 55))
        self.label_5.setStyleSheet("color:rgba(255, 255, 255, 140);")
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(90, 330, 360, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(255,255,255)")
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(90, 430, 360, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgb(255,255,255)")
        self.label_7.setObjectName("label_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 300, 360, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color:rgb(0,255,255)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 400, 360, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color:rgb(0,255,255)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 480, 360, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color:rgb(0,255,255)\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(60, 510, 360, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgb(255,255,255)")
        self.label_8.setObjectName("label_8")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 560, 360, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("color:rgb(0,255,255)\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(90, 590, 360, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:rgb(255,255,255)")
        self.label_11.setObjectName("label_11")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(40, 77, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color:rgb(0,255,255)")
        self.pushButton.setObjectName("pushButton")
        self.btn_geri = QtWidgets.QPushButton(self.widget)
        self.btn_geri.setGeometry(QtCore.QRect(370, 780, 20, 20))
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
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setGeometry(QtCore.QRect(70, 610, 360, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:rgb(255,255,255)")
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setGeometry(QtCore.QRect(90, 350, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color:rgb(255,255,255)")
        self.label_14.setObjectName("label_14")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "© 2022, made with by Emir,Doğukan,Ceyhun..."))
        self.label_3.setText(_translate("Form", "Semt pazar yerlerinin listesi, günleri"))
        self.label_7.setText(_translate("Form", "Balık hal fiyatları hakkında bilgiler."))
        self.pushButton_2.setText(_translate("Form", "Semt Pazar Yerleri:"))
        self.pushButton_3.setText(_translate("Form", "Balık Hal Fiyatları:"))
        self.pushButton_4.setText(_translate("Form", "Sebze ve Meyve Hal Fiyatları:"))
        self.label_8.setText(_translate("Form", "Sebze ve meyve hal fiyatları hakkında bilgiler."))
        self.pushButton_5.setText(_translate("Form", "Otopark Ücretleri:"))
        self.label_11.setText(_translate("Form", "İzelman A.Ş.\'nin işlettiği otoparkların"))
        self.pushButton.setText(_translate("Form", "Aşağıdan İndirmek İstediğiniz Veriyi Seçiniz"))
        self.label_12.setText(_translate("Form", "saatlik ve abonelik ücretleri hakkında bilgiler."))
        self.label_14.setText(_translate("Form", "ve konumları hakkında bilgiler."))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Ekonomi()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
