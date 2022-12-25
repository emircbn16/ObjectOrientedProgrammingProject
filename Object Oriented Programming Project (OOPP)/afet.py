# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys, res

class Ui_AfetveAcil(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(409, 814)
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
        self.label_5.setGeometry(QtCore.QRect(50, 780, 281, 55))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgba(255, 255, 255, 140);")
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(60, 280, 381, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(255,255,255)")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(40, 300, 371, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(255,255,255)")
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(50, 380, 381, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgb(255,255,255)")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(40, 500, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgb(255,255,255)")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(40, 520, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgb(255,255,255)")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(140, 540, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:rgb(255,255,255)")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(50, 650, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:rgb(255,255,255)")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setGeometry(QtCore.QRect(60, 670, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:rgb(255,255,255)")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setGeometry(QtCore.QRect(110, 690, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:rgb(255,255,255)")
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(40, 80, 360, 60))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));border-radius:21px;\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 230, 360, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_2.setStyleSheet("font: 75 10pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: darkgold;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0,128,128), stop:1 rgb(0, 255, 255));\n"
"border-style: solid;\n"
"border-radius:21px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Tasarim\\Images/Icon/afetikon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 340, 361, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_3.setStyleSheet("font: 75 10pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: darkgold;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0,128,128), stop:1 rgb(0, 255, 255));\n"
"border-style: solid;\n"
"border-radius:21px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Tasarim\\Images/Icon/muhtarikon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 450, 360, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_4.setStyleSheet("font: 75 10pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: darkgold;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0,128,128), stop:1 rgb(0, 255, 255));\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Tasarim\\Images/Icon/itfay.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 600, 360, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_5.setStyleSheet("font: 75 10pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: darkgold;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0,128,128), stop:1 rgb(0, 255, 255));\n"
"border-style: solid;\n"
"border-radius:21px;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Tasarim\\Images/Icon/itfaiyeveacil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.btn_geri = QtWidgets.QPushButton(self.widget)
        self.btn_geri.setGeometry(QtCore.QRect(340, 780, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.btn_geri.setFont(font)
        self.btn_geri.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
        self.btn_geri.setStyleSheet("border-image:url(:/images/Images/Icon/geri.png)")
        self.btn_geri.setText("")
        self.btn_geri.setObjectName("btn_geri")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "© 2022, Made With By Emir,Doğukan,Ceyhun..."))
        self.label_3.setText(_translate("Form", "Afet ve acil durum toplanma alanlarına ait"))
        self.label_4.setText(_translate("Form", " ilçe, mahalle ve konum bilgilerini içeren veri seti."))
        self.label_7.setText(_translate("Form", "Muhtarlıkların adres, telefon ve konum bilgileri."))
        self.label_8.setText(_translate("Form", "İtfaiye Dairesi Başkanlığı bünyesinde firmalara,"))
        self.label_9.setText(_translate("Form", "kurumlara verilen ilk yardım, yangın ve kurtarma "))
        self.label_10.setText(_translate("Form", "eğitimlerinin veri seti."))
        self.label_11.setText(_translate("Form", "Şehirde oluşan yangın, su basması ve benzeri"))
        self.label_12.setText(_translate("Form", "afetlere İtfaiye Dairesi Başkanlığı tarafından "))
        self.label_13.setText(_translate("Form", "yapılan müdahale sayılarını içerir."))
        self.pushButton.setText(_translate("Form", "İndirmek İstediğiniz Veriyi Seçiniz"))
        self.pushButton_2.setText(_translate("Form", "Afet Ve Acil Durum Toplanma Alanları"))
        self.pushButton_3.setText(_translate("Form", "Muhtarlıklar"))
        self.pushButton_4.setText(_translate("Form", "İtfaiye Eğitim Hizmetleri"))
        self.pushButton_5.setText(_translate("Form", "İtfaiye Acil Müdahale Sayıları"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_AfetveAcil()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
