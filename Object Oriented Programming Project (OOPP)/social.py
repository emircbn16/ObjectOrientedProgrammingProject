from PyQt5 import QtCore, QtGui, QtWidgets
import sys,res

class Social(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(398, 826)
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
        self.label.setGeometry(QtCore.QRect(10, 20, 450, 867))
        font = QtGui.QFont()
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("border-image: url(:/images/Images/background.png);\n"
"\n"
"border-radius:20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(50, 120, 360, 581))
        self.label_3.setMaximumSize(QtCore.QSize(1000, 1000))
        self.label_3.setStyleSheet("background-color:rgba(0, 0, 0, 100);\n"
"border-radius:15px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.madewith = QtWidgets.QLabel(self.widget)
        self.madewith.setGeometry(QtCore.QRect(60, 780, 271, 55))
        self.madewith.setStyleSheet("color:rgba(255, 255, 255, 140);")
        self.madewith.setObjectName("madewith")
        self.btn_geri = QtWidgets.QPushButton(self.widget)
        self.btn_geri.setGeometry(QtCore.QRect(380, 790, 25, 25))
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
        self.lbl_social = QtWidgets.QLabel(self.widget)
        self.lbl_social.setGeometry(QtCore.QRect(60, 120, 331, 60))
        font = QtGui.QFont()
        font.setFamily("Footlight MT Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_social.setFont(font)
        self.lbl_social.setStyleSheet("color:rgba(255, 255, 255, 210);")
        self.lbl_social.setObjectName("lbl_social")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(50, 200, 360, 125))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color:rgba(255, 255, 255, 210);")
        self.groupBox.setObjectName("groupBox")
        self.instaD = QtWidgets.QPushButton(self.groupBox)
        self.instaD.setGeometry(QtCore.QRect(25, 30, 75, 75))
        self.instaD.setStyleSheet("\n"
"border-image: url(:/images/Images/insta.png);")
        self.instaD.setText("")
        self.instaD.setObjectName("instaD")
        self.githubD = QtWidgets.QPushButton(self.groupBox)
        self.githubD.setGeometry(QtCore.QRect(150, 30, 75, 75))
        self.githubD.setStyleSheet("border-image: url(:/images/Images/github.png);")
        self.githubD.setText("")
        self.githubD.setObjectName("githubD")
        self.inD = QtWidgets.QPushButton(self.groupBox)
        self.inD.setGeometry(QtCore.QRect(260, 30, 75, 75))
        self.inD.setStyleSheet("border-image: url(:/images/Images/in.png);")
        self.inD.setText("")
        self.inD.setObjectName("inD")
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 380, 360, 125))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("color:rgba(255, 255, 255, 210);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.instaE = QtWidgets.QPushButton(self.groupBox_2)
        self.instaE.setGeometry(QtCore.QRect(30, 30, 75, 75))
        self.instaE.setStyleSheet("border-image: url(:/images/Images/insta.png);")
        self.instaE.setText("")
        self.instaE.setObjectName("instaE")
        self.githubE = QtWidgets.QPushButton(self.groupBox_2)
        self.githubE.setGeometry(QtCore.QRect(140, 30, 75, 75))
        self.githubE.setStyleSheet("border-image: url(:/images/Images/github.png);")
        self.githubE.setText("")
        self.githubE.setObjectName("githubE")
        self.inE = QtWidgets.QPushButton(self.groupBox_2)
        self.inE.setGeometry(QtCore.QRect(260, 30, 75, 75))
        self.inE.setStyleSheet("border-image: url(:/images/Images/in.png);")
        self.inE.setText("")
        self.inE.setObjectName("inE")
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_3.setGeometry(QtCore.QRect(50, 560, 360, 125))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("color:rgba(255, 255, 255, 210);")
        self.groupBox_3.setObjectName("groupBox_3")
        self.instaC = QtWidgets.QPushButton(self.groupBox_3)
        self.instaC.setGeometry(QtCore.QRect(20, 30, 71, 71))
        self.instaC.setStyleSheet("border-image: url(:/images/Images/insta.png);")
        self.instaC.setText("")
        self.instaC.setObjectName("instaC")
        self.githubC = QtWidgets.QPushButton(self.groupBox_3)
        self.githubC.setGeometry(QtCore.QRect(140, 30, 75, 75))
        self.githubC.setStyleSheet("border-image: url(:/images/Images/github.png);")
        self.githubC.setText("")
        self.githubC.setObjectName("githubC")
        self.inC = QtWidgets.QPushButton(self.groupBox_3)
        self.inC.setGeometry(QtCore.QRect(260, 30, 75, 75))
        self.inC.setStyleSheet("border-image: url(:/images/Images/in.png);")
        self.inC.setText("")
        self.inC.setObjectName("inC")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.madewith.setText(_translate("Form", "© 2022, made with by Emir,Doğukan,Ceyhun..."))
        self.lbl_social.setText(_translate("Form", "SOSYAL MEDYA HESAPLARIMIZ"))
        self.groupBox.setTitle(_translate("Form", "Dogukan Bostancı"))
        self.groupBox_2.setTitle(_translate("Form", "Emir Çoban"))
        self.groupBox_3.setTitle(_translate("Form", "Murat Ceyhun Yalçınkaya"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Social()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
