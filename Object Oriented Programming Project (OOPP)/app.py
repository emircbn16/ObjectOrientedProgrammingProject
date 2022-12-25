# Bu dosya uygulamamızın ana dosyasıdır.
# Burada uygulamamızın arayüzünü oluşturuyoruz.
# Ayrıca uygulamamızın içerisindeki butonlara tıklandığında hangi fonksiyonun çalışacağını belirtiyoruz.
# Qt Designer ile oluşturduğumuz arayüz dosyalarını burada çağırıyoruz.
from afet import Ui_AfetveAcil
from cevre import Ui_Cevre
from enerji import Ui_Enerji
from yasam import Ui_Yasam
from ekonomi import Ui_Ekonomi
from tarim import Ui_Tarim
#Selenium kütüphanesini import ediyoruz. Not: Selenium kütüphanesini kullanabilmek için bilgisayarımıza chromedriver.exe dosyasını indirmeniz gerekmektedir.
from selenium import webdriver # pip install selenium
#PyQt5 modülü ile uygulamamızın arayüzünü oluşturuyoruz.
from PyQt5 import QtGui, QtCore, QtWidgets   # pip install PyQt5
from PyQt5.QtWidgets import *   
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QToolTip
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import uic
# Uygulamamızda Kullanacağımız Kütüphaneleri import ediyoruz.
import time     # Uygulamamızın çalışma süresini belirlemek için kullanıyoruz.
import sys, res # sys modülü ile uygulamamızı kapatıyoruz. res modülü ile uygulamamızın içerisindeki resim dosyalarını ayarlıyoruz.  
import hashlib  # Şifrelerimizi hashleyerek veritabanına kaydediyoruz. ***pip install hashlib*** komutu ile kütüphaneyi indirmeniz gerekmektedir.
import sqlite3  # Veritabanı işlemlerimizi gerçekleştiriyoruz. ***pip install pysqlite3***  komutu ile kütüphaneyi indirmeniz gerekmektedir.
# Uygulamamızın ana arayüzünü oluşturuyoruz.
class Giris(QDialog):
    def __init__(self):
        # Giriş arayüzünü oluşturuyoruz.
        super(Giris,self).__init__()
        # Tasarım klasörümüzün içerisindeki login.ui dosyasını çağırıyoruz.
        loadUi("C:/Users/Emir/Desktop/Object Oriented Programming Project (OOPP)/Tasarim/login.ui",self) 
        # Şifre giriş alanımızın karakterlerini gizliyoruz.                        
        self.password.setEchoMode(QtWidgets.QLineEdit.Password) 
        # Giriş butonuna tıklandığında loginfunction fonksiyonunu çalıştırıyoruz.
        self.login.clicked.connect(self.loginfunction)  
        # Kayıt Ol butonuna tıklandığında gotocreate fonksiyonunu çalıştırıyoruz.        
        self.signup.clicked.connect(self.gotocreate)   
        # Çıkış butonuna tıklandığında exitfunction fonksiyonunu çalıştırıyoruz.
        self.exit.clicked.connect(self.exitfunction)  
    def loginfunction(self):
        # Giriş ekranındaki email alanını alıyoruz.
        email=self.email.text()
        # Giriş ekranındaki şifre alanını alıyoruz.                               
        password=self.password.text() 
        # Şifremizi hashleyerek veritabanında saklıyoruz.                          
        hashedpassword = hashlib.md5(password.encode()).hexdigest()
        # Veritabanımızı çağırıyoruz.
        baglanti = sqlite3.connect("kullanicilar.db")      
        # Veritabanımızı işaret ediyoruz.  
        im = baglanti.cursor()                            
        # Veritabanımızda kullanıcı tablosu yoksa oluşturuyoruz.
        t = "CREATE TABLE IF NOT EXISTS kullanicilar (email VARCHAR(255), password VARCHAR(255), userID INTEGER PRIMARY KEY AUTOINCREMENT)" 
        # Veritabanımızdaki kullanıcılar tablosuna sorgu gönderiyoruz.
        im.execute("SELECT COUNT(*) FROM kullanicilar")
        # Veritabanımızdaki kullanıcılar tablosundan gelen verileri alıyoruz.
        count = im.fetchall()
        # Veritabanımızdaki kullanıcılar tablosunda kayıt yoksa uyarı veriyoruz.
        if count[0][0] == 0:
            QMessageBox.about(self, "Hata", "Lütfen önce kayıt olun   ")
            return
        # Veritabanına admin girişi yaptırıyoruz.
        elif email == "admin":
            if password == "emir":
                time.sleep(1.7)
                arayuz = AdminMain()
                widget.addWidget(arayuz)
                widget.setCurrentIndex(widget.currentIndex()+1)
            else:
                QMessageBox.about(self, "Hata", "Girdiğiniz bilgiler yanlış  ")
        # Veritabanımızdaki kullanıcılar tablosunda kayıt varsa giriş işlemini gerçekleştiriyoruz.
        else:
            im.execute("SELECT * FROM kullanicilar WHERE email = ? AND password = ?", (email, hashedpassword))
            data = im.fetchall()
            if len(data) == 0:
                QMessageBox.about(self, "Hata", "Girdiğiniz bilgiler yanlış  ")
            else:
                time.sleep(1.7)
                arayuz = Main()
                widget.addWidget(arayuz)
                widget.setCurrentIndex(widget.currentIndex()+1)
    def gotocreate(self):
        # Kayıt Ol ekranını çağırıyoruz.
        createacc=KayitOl()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)    
    def mainfunction(self):
        # Ana ekranı çağırıyoruz.
        if self.login.clicked:
            time.sleep(1.7)
            arayuz = Main()
            widget.addWidget(arayuz)
            widget.setCurrentIndex(widget.currentIndex()+1)
    def exitfunction(self):
        # Uygulamamızı kapatıyoruz.
        sys.exit(app.exec_())
class KayitOl(QDialog):
    def __init__(self):
        # Kayıt Ol ekranını oluşturuyoruz.
        super(KayitOl,self).__init__()
        # Tasarım klasörümüzün içerisindeki signin.ui dosyasını çağırıyoruz.
        loadUi("C:/Users/Emir/Desktop/Object Oriented Programming Project (OOPP)/Tasarim/signin.ui",self)
        # Signin butonuna tıklandığında gotocreate fonksiyonunu çalıştırıyoruz.  
        self.signin.clicked.connect(self.createaccfunction)     
        # Giriş Yap butonuna tıklandığında gotologin fonksiyonunu çalıştırıyoruz.
        self.login.clicked.connect(self.gotologin)
        # Şifre giriş alanımızın karakterlerini gizliyoruz.
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        # Şifre giriş alanımızın karakterlerini gizliyoruz.
        self.password_2.setEchoMode(QtWidgets.QLineEdit.Password)
    
    def gotologin(self):
        # Giriş ekranını çağırıyoruz.
        login=Giris()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def createaccfunction(self,signin):
        # Kayıt Ol ekranındaki email alanını alıyoruz.
        email=self.email.text()
        # Kayıt Ol ekranındaki şifre alanını alıyoruz.
        password=self.password.text()
        # Kayıt Ol ekranındaki 2.şifre alanını alıyoruz.
        password_2=self.password_2.text()
        # Veritabanımızı çağırıyoruz.
        baglanti = sqlite3.connect("kullanicilar.db")
        # Veritabanımızı işaret ediyoruz.
        im = baglanti.cursor()
        # Veritabanımızda kullanıcı tablosu yoksa oluşturuyoruz.
        t = "CREATE TABLE IF NOT EXISTS kullanicilar (email VARCHAR(255), password VARCHAR(255), userID INTEGER PRIMARY KEY AUTOINCREMENT)"
        # Veritabanımızdaki kullanıcılar tablosuna veri ekliyoruz.
        im.execute(t)
        # Veritabanımızdaki kullanıcılar tablosundan gelen verileri alıyoruz.
        baglanti.commit()
        # Veritabanımızdaki email ve şifre alanlarını InsertToDb fonksiyonuna gönderiyoruz.
        self.InsertToDb(email,password)

    def InsertToDb(self,email,password):
        # Kayıt Ol ekranındaki email alanını alıyoruz.
        email = self.email.text()
        # Kayıt Ol ekranındaki email alanı için gerekli kontrolleri yapıyoruz.
        if self.email.text() == "":
            QMessageBox.about(self, "Hata", "Lütfen bir e-posta adresi girin    ")
        elif "@" not in email:
            QMessageBox.about(self, "Hata", "Lütfen geçerli bir e-posta adresi girin    ")
        elif "gmail.com" not in email:
            QMessageBox.about(self, "Hata", "Lütfen geçerli bir e-posta adresi girin    ")
        elif self.password.text() == "":
            QMessageBox.about(self, "Hata", "Lütfen bir parola girin    ")
        elif len(self.password.text()) < 4:
            QMessageBox.about(self, "Hata", "Parolanız en az 4 karakter olmalıdır    ")
        elif self.password_2.text() == "":
            QMessageBox.about(self, "Hata", "Lütfen parolanızı tekrar girin    ")
        elif self.password.text() != self.password_2.text():
            QMessageBox.about(self, "Hata", "Parolalar eşleşmiyor")
        else:    
            # Veritabanımızı çağırıyoruz.   
            baglanti = sqlite3.connect("kullanicilar.db") 
            # Şifremizi hashleyerek veritabanında saklıyoruz.   
            hashedPassword = hashlib.md5(password.encode('utf-8')).hexdigest()
            # Veritabanımızı işaret ediyoruz.
            im = baglanti.cursor()
            # Veritabanımızdaki kullanıcılar tablosuna veri ekliyoruz.
            im.execute("INSERT INTO kullanicilar (email,password) VALUES (?,?)",(email,hashedPassword))
            # Veritabanımızdaki kullanıcılar tablosundan gelen verileri alıyoruz.
            baglanti.commit()
            # Veritabanımızı kapatıyoruz.
            baglanti.close()
            # Kayıt olma işlemini başarıyla tamamladığımızı kullanıcıya bildiriyoruz.
            QMessageBox.about(self, "Başarılı", "Hesabınız oluşturuldu  ")
            # Kayıt olma ekranındaki email ve şifre alanlarını temizliyoruz.
            self.email.clear()
            self.password.clear()
            self.password_2.clear()
            # Giriş ekranını çağırıyoruz.
            login=Giris()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)

class AdminMain(QDialog):
    def __init__(self):
        # Admin Arayüzünü oluşturuyoruz
        super(AdminMain,self).__init__()
        # Tasarım klasörümüzün içerisindeki adminmain.ui dosyasını çağırıyoruz.
        loadUi("C:/Users/Emir/Desktop/Object Oriented Programming Project (OOPP)/Tasarim/adminmain.ui",self)
        # Butonlarımızı fonksiyonlarımıza bağlıyoruz.
        self.btn_geri.clicked.connect(self.Menufunction)
        self.btn_ekle.clicked.connect(self.Eklefunction)
        self.btn_guncelle.clicked.connect(self.Guncellefunction)
        self.btn_sil.clicked.connect(self.Silfunction)
        self.btn_goster.clicked.connect(self.Gosterfunction) 
        self.btn_icerik.clicked.connect(self.Mainfunction)  
    def mainfunction(self):
        # Ana Menü ekranını çağırıyoruz.
        if self.login.clicked:
            time.sleep(1.7)
            login=Giris()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)
    def Menufunction(self):
        # Giriş ekranını çağırıyoruz.
        menu=Giris()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Eklefunction(self):
        # Admin Ekle ekranını çağırıyoruz.
        ekle=AdminEkle()
        widget.addWidget(ekle)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Guncellefunction(self):
        # Admin Güncelle ekranını çağırıyoruz.
        guncelle=AdminGuncelle()
        widget.addWidget(guncelle)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Silfunction(self):
        # Admin Sil ekranını çağırıyoruz.
        sil=AdminSil()
        widget.addWidget(sil)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Gosterfunction(self):
        # Admin Göster ekranını çağırıyoruz.
        goster=AdminGoster()
        widget.addWidget(goster)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Mainfunction(self):
        # Arayüz ekranını çağırıyoruz.
        time.sleep(1.2)
        icerik=Main()
        widget.addWidget(icerik)
        widget.setCurrentIndex(widget.currentIndex()+1)
class AdminEkle(QDialog):
    def __init__(self):
        # Admin Ekle'yi oluşturuyoruz.
        super(AdminEkle,self).__init__()
        # Tasarım klasörümüzün içerisindeki adminekle.ui dosyasını çağırıyoruz.
        loadUi("C:/Users/Emir/Desktop/Object Oriented Programming Project (OOPP)/Tasarim/adminekle.ui",self)
        # Butonlarımızı fonksiyonlarımıza bağlıyoruz.
        self.btn_geri.clicked.connect(self.Menufunction)
        self.btn_ekle.clicked.connect(self.Eklefunction)
    def Menufunction(self):
        # Admin Menü ekranını çağırıyoruz.
        main=AdminMain()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Eklefunction(self):
        # Admin Ekle ekranındaki email alanını alıyoruz.
        email = self.line_email.text()
        # Admin Ekle ekranındaki şifre alanını alıyoruz.
        password = self.line_sifre.text()
        # Şifremizi hashleyerek veritabanında saklıyoruz. 
        hashedPassword = hashlib.md5(password.encode('utf-8')).hexdigest()
        # Veritabanı bağlantımızı oluşturuyoruz.
        baglanti = sqlite3.connect("kullanicilar.db") 
        # Veritabanı işlemleri için cursor oluşturuyoruz.
        im = baglanti.cursor()
        # Veritabanında admin tablosunda email ve şifre alanlarını kontrol ediyoruz.
        if email == "":
            QMessageBox.about(self, "Hata", "Lütfen bir e-posta adresi girin    ")
        elif "@" not in email:
            QMessageBox.about(self, "Hata", "Lütfen geçerli bir e-posta adresi girin    ")
        elif "gmail.com" not in email:
            QMessageBox.about(self, "Hata", "Lütfen geçerli bir e-posta adresi girin    ")
        elif password == "":
            QMessageBox.about(self, "Hata", "Lütfen bir parola girin    ")
        elif len(password) < 4:
            QMessageBox.about(self, "Hata", "Parolanız en az 4 karakter olmalıdır    ")
        else: 
            # Veritabanına email ve şifre alanlarını ekliyoruz.
            im.execute("INSERT INTO kullanicilar (email,password) VALUES (?,?)",(email,hashedPassword))
            # Veritabanı işlemlerimizi kaydediyoruz.
            baglanti.commit()
            QMessageBox.about(self, "Başarılı", "Kullanıcı Eklendi")
            # Admin Ekle ekranındaki email ve şifre alanlarını temizliyoruz.
            self.line_email.clear()
            self.line_sifre.clear()
class AdminGuncelle(QDialog):
    def __init__(self):
        # Admin Güncelle'yi oluşturuyoruz.
        super(AdminGuncelle,self).__init__()
        # Tasarım klasörümüzün içerisindeki adminguncelle.ui dosyasını çağırıyoruz.
        loadUi("C:/Users/Emir/Desktop/Object Oriented Programming Project (OOPP)/Tasarim/adminguncelle.ui",self)
        # Tablomuzun sütun genişliklerini ayarlıyoruz.
        self.table.setColumnWidth(0,190)
        self.table.setColumnWidth(1,114)
        self.table.setColumnWidth(2,15)
        # Butonlarımızı fonksiyonlarımıza bağlıyoruz.
        self.btn_geri.clicked.connect(self.Menufunction)
        self.btn_guncelle.clicked.connect(self.Guncellefunction)
        self.btn_goster.clicked.connect(self.Gosterfunction)
    def Menufunction(self):
        # Admin Menü ekranını çağırıyoruz.
        main=AdminMain()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Gosterfunction(self):
        # Veritabanı bağlantımızı oluşturuyoruz.
        baglanti = sqlite3.connect("kullanicilar.db")
        # Veritabanı işlemleri için cursor oluşturuyoruz.
        im = baglanti.cursor()
        # Veritabanındaki kullanicilar tablosundaki tüm verileri çekiyoruz.
        im.execute("SELECT * FROM kullanicilar")
        # Veritabanındaki tüm verileri tablomuza ekliyoruz.
        for indexSatir, kayitNumarasi in enumerate(im):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.table.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))   
            baglanti.commit()
        # Butonlarımızı fonksiyonlarımıza bağlıyoruz.
        self.btn_goster.clicked.connect(self.Gosterfunction)
    def Guncellefunction(self): # ChatGPT3 tarafından yazıldı...
        # Get the new email value from the text box
        new_email = self.email.text()

        # Get the email and password values for the selected user from the table
        selected_row = self.table.currentRow()
        old_email = self.table.item(selected_row, 0).text()
        password = self.table.item(selected_row, 1).text()

        # Prompt the user to confirm that they want to update their email
        guncelle_mesaj = QMessageBox.question(self, "Güncelleme", "E-posta adresinizi güncellemek istediğinize emin misiniz?", QMessageBox.Yes | QMessageBox.No)
        if guncelle_mesaj == QMessageBox.Yes:
            try:
                # Connect to the database and create a cursor
                baglanti = sqlite3.connect("kullanicilar.db")
                im = baglanti.cursor()

                # Validate the email value
                if new_email == "":
                    raise ValueError("Lütfen tüm alanları doldurun")

                # Execute the UPDATE statement using a parameterized query
                im.execute("UPDATE kullanicilar SET email = ? WHERE email = ? AND password = ?", (new_email, old_email, password))
                baglanti.commit()
                QMessageBox.about(self, "Başarılı", "E-posta adresiniz güncellendi")
                self.Gosterfunction()
            except Exception as error:
                QMessageBox.about(self, "Hata", "E-posta adresiniz güncellenemedi ===> " + str(error))
class AdminSil(QDialog):
    def __init__(self):
        # Admin Sil ekranını oluşturuyoruz.
        super(AdminSil,self).__init__()
        # Tasarım klasörümüzün içerisindeki adminsil.ui dosyasını çağırıyoruz.
        loadUi("C:/Users/Emir/Desktop/Object Oriented Programming Project (OOPP)/Tasarim/adminsil.ui",self)
        # Tablomuzun sütun genişliklerini ayarlıyoruz.
        self.table.setColumnWidth(0,190)
        self.table.setColumnWidth(1,114)
        self.table.setColumnWidth(2,15)
        # Butonlarımızın fonksiyonlarını çağırıyoruz.
        self.btn_geri.clicked.connect(self.Menufunction)
        self.btn_sil.clicked.connect(self.Silfunction)
        self.btn_goster.clicked.connect(self.Gosterfunction)
    def Menufunction(self):
        # Admin Sil ekranından Admin Main ekranına geçiş yapılıyor.
        main=AdminMain()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Gosterfunction(self):
        # Veritabanımızı çağırıyoruz.
        baglanti = sqlite3.connect("kullanicilar.db")
        # Veritabanı işlemlerimiz için cursor oluşturuyoruz.
        im = baglanti.cursor()
        # Veritabanımızdaki kullanicilar tablosundaki tüm verileri çekiyoruz.
        im.execute("SELECT * FROM kullanicilar")
        # Veritabanımızdaki tüm verileri tablomuza aktarıyoruz.
        for indexSatir, kayitNumarasi in enumerate(im):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.table.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))   
            baglanti.commit()
    def Silfunction(self):
        # Kullanıcıyı silmek istediğimizde onay mesajı veriyoruz.
        sil_mesaj = QMessageBox.question(self, "Silme İşlemi", "Kullanıcıyı Silmek İstediğinize Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)
        # Kullanıcı onay verirse silme işlemi yapılıyor.
        if sil_mesaj == QMessageBox.Yes:
            secilen_kayit = self.table.selectedItems()
            silinecek_kayit = secilen_kayit[0].text()
            baglanti = sqlite3.connect("kullanicilar.db")
            im = baglanti.cursor()
            sorgu = "DELETE FROM kullanicilar WHERE email=?"
            try:
                im.execute(sorgu, (silinecek_kayit,))
                baglanti.commit()
                QMessageBox.about(self, "Başarılı", "Kullanıcı Silindi")
                self.Gosterfunction()
            except Exception as error:
                QMessageBox.about(self, "Hata", "Kullanıcı Silinemedi ===> " + str(error))
        # Kullanıcı onay vermezse silme işlemi yapmıyor.
        else:
            QMessageBox.about(self, "Başarılı", "Kullanıcı Silinmedi")
class AdminGoster(QDialog):
    def __init__(self):
        # Admin Goster ekranını oluşturuyoruz.
        super(AdminGoster,self).__init__()
        # Tasarım klasörümüzün içerisindeki admingoster.ui dosyasını çağırıyoruz.
        loadUi("C:/Users/Emir/Desktop/Object Oriented Programming Project (OOPP)/Tasarim/admingoster.ui",self)
        # Tablomuzun sütun genişliklerini ayarlıyoruz.
        self.table.setColumnWidth(0,190)
        self.table.setColumnWidth(1,114)
        self.table.setColumnWidth(2,15)
        # Butonlarımızın fonksiyonlarını çağırıyoruz.
        self.btn_geri.clicked.connect(self.Menufunction)
        self.btn_goster.clicked.connect(self.Gosterfunction)
    def Menufunction(self):
        # Admin Goster ekranından Admin Main ekranına geçiş yapılıyor.
        main=AdminMain()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Gosterfunction(self):
        # Veritabanımızı çağırıyoruz.
        baglanti = sqlite3.connect("kullanicilar.db")
        # Veritabanı işlemlerimiz için cursor oluşturuyoruz.
        im = baglanti.cursor()
        # Veritabanımızdaki kullanicilar tablosundaki tüm verileri çekiyoruz.
        im.execute("SELECT * FROM kullanicilar")
        for indexSatir, kayitNumarasi in enumerate(im):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.table.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))   
            baglanti.commit()

class Main(QDialog):
    def __init__(self):
        # Main ekranını oluşturuyoruz.
        super(Main,self).__init__()
        # Tasarım klasörümüzün içerisindeki main.ui dosyasını çağırıyoruz.
        loadUi("C:/Users/Emir/Desktop/Object Oriented Programming Project (OOPP)/Tasarim/main.ui",self)
        # Butonlarımızın fonksiyonlarını çağırıyoruz.
        self.btn_icerik.clicked.connect(self.Icerikfunction)
        self.btn_social.clicked.connect(self.Socialfunction)
        self.btn_info.clicked.connect(self.Infofunction)
        self.btn_geri.clicked.connect(self.Menufunction)
    
    def Menufunction(self):
        # Main ekranından Admin Giriş ekranına geçiş yapılıyor.
        menu=Giris()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def mainfunction(self):
        # Main ekranından Admin Giriş ekranına geçiş yapılıyor.
        login=Giris()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def Icerikfunction(self):
        # Main ekranından İçerik ekranına geçiş yapılıyor.
        time.sleep(1)
        icerik=Icerik()
        widget.addWidget(icerik)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def Socialfunction(self):
        time.sleep(1)
        # Main ekranından Social ekranına geçiş yapılıyor.
        social=Social()
        widget.addWidget(social)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Infofunction(self):
        # Main ekranından Info ekranına geçiş yapılıyor.
        time.sleep(1)
        info=Info()
        widget.addWidget(info)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Icerik(QDialog):
    def __init__(self):
        # İçerik ekranını oluşturuyoruz.
        super(Icerik,self).__init__()
        # Tasarım klasörümüzün içerisindeki icerik.ui dosyasını çağırıyoruz.
        loadUi("C:/Users/Emir/Desktop/Object Oriented Programming Project (OOPP)/Tasarim/icerik.ui",self)
        # Butonlarımızın fonksiyonlarını çağırıyoruz.
        self.btn_geri.clicked.connect(self.Menufunction)
        self.btn_afet.clicked.connect(self.Afetfunction)
        self.btn_cevre.clicked.connect(self.Cevrefunction)
        self.btn_enerji.clicked.connect(self.Enerjifunction)
        self.btn_yasam.clicked.connect(self.Yasamfunction)
        self.btn_eko.clicked.connect(self.Ekionomifunction)
        self.btn_tarim.clicked.connect(self.Tarimfunction)
    def Menufunction(self):
        # İçerik ekranından Main ekranına geçiş yapılıyor.
        main=Main()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Afetfunction(self):
        # İçerik ekranından Afet ekranına geçiş yapılıyor.
        icerik=Afet()
        widget.addWidget(icerik)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Cevrefunction(self):
        # İçerik ekranından Çevre ekranına geçiş yapılıyor.
        icerik=Cevre()
        widget.addWidget(icerik)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Enerjifunction(self):
        # İçerik ekranından Enerji ekranına geçiş yapılıyor.
        icerik=Enerji()
        widget.addWidget(icerik)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Yasamfunction(self):
        # İçerik ekranından Yaşam ekranına geçiş yapılıyor.
        icerik=Yasam()
        widget.addWidget(icerik)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Ekionomifunction(self):
        # İçerik ekranından Ekonomi ekranına geçiş yapılıyor.
        icerik=Ekonomi()
        widget.addWidget(icerik)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Tarimfunction(self):
        # İçerik ekranından Tarım ekranına geçiş yapılıyor.
        icerik=Tarim()
        widget.addWidget(icerik)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Afet(QDialog):
    def __init__(self):
        # Afet ekranını oluşturuyoruz.
        super(Afet,self).__init__()
        # Tasarım klasörümüzün içerisindeki afet.ui dosyasını çağırıyoruz.
        loadUi("C:/Users/Emir/Desktop/Object Oriented Programming Project (OOPP)/Tasarim/afet.ui",self)
        # Butonlarımızın fonksiyonlarını çağırıyoruz.
        self.btn_geri.clicked.connect(self.Menufunction)
        self.pushButton_2.clicked.connect(self.Afetfunction)
        self.pushButton_3.clicked.connect(self.Muhtarlikfunction)
        self.pushButton_4.clicked.connect(self.Itfaiyefunction)
        self.pushButton_5.clicked.connect(self.Itfaiye2function)
    def Icerikfunction(self):
        # Afet ekranından İçerik ekranına geçiş yapılıyor.
        icerik=Icerik()
        widget.addWidget(icerik)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Menufunction(self):
        # Afet ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Afetfunction(self):
        # Afet ekranından Afet ve Acil ekranına geçiş yapılıyor.
        icerik=AfetveAcil()
        widget.addWidget(icerik)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Muhtarlikfunction(self):
        # Afet ekranından Muhtarlık ekranına geçiş yapılıyor.
        icerik=Muhtarlik()
        widget.addWidget(icerik)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Itfaiyefunction(self):
        # Afet ekranından İtfaiye ekranına geçiş yapılıyor.
        icerik=Itfaiye()
        widget.addWidget(icerik)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Itfaiye2function(self):
        # Afet ekranından İtfaiye2 ekranına geçiş yapılıyor.
        icerik=Itfaiye2()
        widget.addWidget(icerik)
        widget.setCurrentIndex(widget.currentIndex()+1)
class AfetveAcil(QDialog,QtWidgets.QMainWindow):
    def __init__(self):
        # Afet ve Acil ekranını oluşturuyoruz.
        super(AfetveAcil, self).__init__()
        # Tasarım klasörümüzün içerisindeki afetveacil.ui dosyasını çağırıyoruz.
        self.ui = Ui_AfetveAcil()
        self.ui.setupUi(self)
        # Selenium botumuzun çalışması için gerekli ayarlamaları yapıyoruz.
        self.browserProfile = webdriver.ChromeOptions()  
        # İngilizce dil ayarını yapıyoruz.   
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        # İndirme işlemini otomatik olarak yapmasını sağlıyoruz.
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://acikveri.bizizmir.com/tr/dataset/afet-ve-acil-durum-toplanma-alanlari')
        # Tarayıcıyı tam ekran olarak açıyoruz.
        self.browser.maximize_window()
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[2]/div/a").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[2]/div/ul/li[2]/a").click()
        time.sleep(5)
        # İndirme işlemini tamamladıktan sonra tarayıcıyı simge durumuna getiriyoruz.
        self.browser.minimize_window()
        # İndirme işlemini tamamladıktan sonra tarayıcıyı kapatıyoruz.
        self.browser.quit()
        # İndirme işlemini tamamladıktan sonra bilgi mesajı veriyoruz.
        QMessageBox.information(self, "Bilgi", "İndirme Tamamlandı")

        # Butonlarımızın fonksiyonlarını çağırıyoruz.
        self.ui.btn_geri.clicked.connect(self.Menufunction)
    def Menufunction(self):
        # Afet ve Acil ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Muhtarlik(QDialog,QtWidgets.QMainWindow):
    def __init__(self):
        # Muhtarlık ekranını oluşturuyoruz.
        super(Muhtarlik, self).__init__()
        # Tasarım klasörümüzün içerisindeki muhtarlik.ui dosyasını çağırıyoruz.
        self.ui = Ui_AfetveAcil()
        self.ui.setupUi(self)
        # Selenium botumuzun çalışması için gerekli ayarlamaları yapıyoruz.
        self.browserProfile = webdriver.ChromeOptions()    
        # İngilizce dil ayarını yapıyoruz. 
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        # İndirme işlemini otomatik olarak yapmasını sağlıyoruz.
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://acikveri.bizizmir.com/tr/dataset/muhtarliklar')
        # Tarayıcıyı tam ekran olarak açıyoruz.
        self.browser.maximize_window()
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[2]/div/a").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[2]/div/ul/li[2]/a").click()
        time.sleep(5)
        # İndirme işlemini tamamladıktan sonra tarayıcıyı simge durumuna getiriyoruz.
        self.browser.minimize_window()
        # İndirme işlemini tamamladıktan sonra tarayıcıyı kapatıyoruz.
        self.browser.quit()
        # İndirme işlemini tamamladıktan sonra bilgi mesajı veriyoruz.
        QMessageBox.information(self, "Bilgi", "İndirme Tamamlandı")
        # Butonlarımızın fonksiyonlarını çağırıyoruz.
        self.ui.btn_geri.clicked.connect(self.Menufunction)
    def Menufunction(self):
        # Muhtarlık ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Itfaiye(QDialog,QtWidgets.QMainWindow):
    def __init__(self):
        # İtfaiye ekranını oluşturuyoruz.
        super(Itfaiye, self).__init__()
        # Tasarım klasörümüzün içerisindeki itfaiye.ui dosyasını çağırıyoruz.
        self.ui = Ui_AfetveAcil()
        self.ui.setupUi(self)
        # Selenium botumuzun çalışması için gerekli ayarlamaları yapıyoruz.
        self.browserProfile = webdriver.ChromeOptions()     
        # İngilizce dil ayarını yapıyoruz.
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        # İndirme işlemini otomatik olarak yapmasını sağlıyoruz.
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://acikveri.bizizmir.com/tr/dataset/itfaiye-egitim-hizmetleri')
        # Tarayıcıyı tam ekran olarak açıyoruz.
        self.browser.maximize_window()
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[1]/div/a").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[1]/div/ul/li[2]/a").click()
        time.sleep(5)
        # İndirme işlemini tamamladıktan sonra tarayıcıyı simge durumuna getiriyoruz.
        self.browser.minimize_window()
        # İndirme işlemini tamamladıktan sonra tarayıcıyı kapatıyoruz.
        self.browser.quit()
        # İndirme işlemini tamamladıktan sonra bilgi mesajı veriyoruz.
        QMessageBox.information(self, "Bilgi", "İndirme Tamamlandı")
        # Butonlarımızın fonksiyonlarını çağırıyoruz.
        self.ui.btn_geri.clicked.connect(self.Menufunction)
    def Menufunction(self):
        # İtfaiye ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Itfaiye2(QDialog,QtWidgets.QMainWindow):
    def __init__(self):
        # İtfaiye2 ekranını oluşturuyoruz.
        super(Itfaiye2, self).__init__()
        # Tasarım klasörümüzün içerisindeki itfaiye2.ui dosyasını çağırıyoruz.
        self.ui = Ui_AfetveAcil()
        self.ui.setupUi(self)
        # Selenium botumuzun çalışması için gerekli ayarlamaları yapıyoruz.
        self.browserProfile = webdriver.ChromeOptions()     
        # İngilizce dil ayarını yapıyoruz.
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        # İndirme işlemini otomatik olarak yapmasını sağlıyoruz.
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://acikveri.bizizmir.com/tr/dataset/itfaiye-acil-mudahale-sayilari')
        # Tarayıcıyı tam ekran olarak açıyoruz.
        self.browser.maximize_window()
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[1]/div/a").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[1]/div/ul/li[2]/a").click()
        time.sleep(5)
        # İndirme işlemini tamamladıktan sonra tarayıcıyı simge durumuna getiriyoruz.
        self.browser.minimize_window()
        # İndirme işlemini tamamladıktan sonra tarayıcıyı kapatıyoruz.
        self.browser.quit()
        # İndirme işlemini tamamladıktan sonra bilgi mesajı veriyoruz.
        QMessageBox.information(self, "Bilgi", "İndirme Tamamlandı")
        # Butonlarımızın fonksiyonlarını çağırıyoruz.
        self.ui.btn_geri.clicked.connect(self.Menufunction)
    def Menufunction(self):
        # İtfaiye2 ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Cevre(QDialog):
    def __init__(self):
        # Cevre ekranını oluşturuyoruz.
        super(Cevre,self).__init__()
        # Tasarım klasörümüzün içerisindeki cevre.ui dosyasını çağırıyoruz.
        loadUi("C:/Users/Emir/Desktop/Object Oriented Programming Project (OOPP)/Tasarim/cevre.ui",self)
        # Butonlarımızın fonksiyonlarını çağırıyoruz.
        self.btn_geri.clicked.connect(self.Menufunction)
        self.pushButton_2.clicked.connect(self.SuUretimfunction)
        self.pushButton_3.clicked.connect(self.GunlukSufunction)
        self.pushButton_4.clicked.connect(self.Barajfunction)
        self.pushButton_5.clicked.connect(self.Havafunction)
    def Icerikfunction(self):
        # Cevre ekranından İçerik ekranına geçiş yapılıyor.
        icerik=Icerik()
        widget.addWidget(icerik)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Menufunction(self):
        # Cevre ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def SuUretimfunction(self):
        # Cevre ekranından Su Üretim ekranına geçiş yapılıyor.
        suuretim=SuUretim()
        widget.addWidget(suuretim)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def GunlukSufunction(self):
        # Cevre ekranından Günlük Su ekranına geçiş yapılıyor.
        gunluksu=GunlukSu()
        widget.addWidget(gunluksu)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Barajfunction(self):
        # Cevre ekranından Baraj ekranına geçiş yapılıyor.
        baraj=Baraj()
        widget.addWidget(baraj)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Havafunction(self):
        # Cevre ekranından Hava ekranına geçiş yapılıyor.
        hava=Hava()
        widget.addWidget(hava)
        widget.setCurrentIndex(widget.currentIndex()+1)
class SuUretim(QDialog,QtWidgets.QMainWindow):
    def __init__(self):
        # Su Üretim ekranını oluşturuyoruz.
        super(SuUretim, self).__init__()
        # Tasarım klasörümüzün içerisindeki suuretim.ui dosyasını çağırıyoruz.
        self.ui = Ui_Cevre()
        self.ui.setupUi(self)
        # Selenium botumuzun çalışması için gerekli ayarlamaları yapıyoruz.
        self.browserProfile = webdriver.ChromeOptions()
        # İngilizce dil ayarını yapıyoruz.  
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        # İndirme işlemini otomatik olarak yapmasını sağlıyoruz.
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://acikveri.bizizmir.com/tr/dataset/su-uretiminin-aylara-ve-kaynaklara-gore-dagilimi')
        # İndirme işlemini tamamladıktan sonra tarayıcıyı kapatıyoruz.
        self.browser.maximize_window()
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[2]/div/a").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[2]/div/ul/li[2]/a").click()
        time.sleep(5)
        # İndirme işlemini tamamladıktan sonra tarayıcıyı simge durumuna alıyoruz.
        self.browser.minimize_window()
        # İndirme işlemini tamamladıktan sonra tarayıcıyı kapatıyoruz.
        self.browser.quit()
        # İndirme işlemini tamamladıktan sonra kullanıcıya bilgi veriyoruz.
        QMessageBox.information(self, "Bilgi", "İndirme Tamamlandı")
        # Butonlarımızın fonksiyonlarını çağırıyoruz.
        self.ui.btn_geri.clicked.connect(self.Menufunction)
    def Menufunction(self):
        # Su Üretim ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
class GunlukSu(QDialog,QtWidgets.QMainWindow):
    def __init__(self):
        # Günlük Su ekranını oluşturuyoruz.
        super(GunlukSu, self).__init__()
        # Tasarım klasörümüzün içerisindeki gunluksu.ui dosyasını çağırıyoruz.
        self.ui = Ui_Cevre()
        self.ui.setupUi(self)
        # Selenium botumuzun çalışması için gerekli ayarlamaları yapıyoruz.
        self.browserProfile = webdriver.ChromeOptions()     
        # İngilizce dil ayarını yapıyoruz.
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        # İndirme işlemini otomatik olarak yapmasını sağlıyoruz.
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://acikveri.bizizmir.com/tr/dataset/gunluk-su-uretimi')
        # Tarayıcıyı tam ekran olarak açıyoruz.
        self.browser.maximize_window()
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[3]/div/a").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[3]/div/ul/li[2]/a").click()
        time.sleep(5)
        # İndirme işlemini tamamladıktan sonra tarayıcıyı simge durumuna alıyoruz.
        self.browser.minimize_window()
        QMessageBox.information(self, "Bilgi", "İndirme Tamamlandı")
        # İndirme işlemini tamamladıktan sonra tarayıcıyı kapatıyoruz.
        self.browser.quit()
        # Butonlarımızın fonksiyonlarını çağırıyoruz.
        self.ui.btn_geri.clicked.connect(self.Menufunction)
    def Menufunction(self):
        # Günlük Su ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Baraj(QDialog,QtWidgets.QMainWindow):
    def __init__(self):
        # Baraj ekranını oluşturuyoruz.
        super(Baraj, self).__init__()
        # Tasarım klasörümüzün içerisindeki baraj.ui dosyasını çağırıyoruz.
        self.ui = Ui_Cevre()
        self.ui.setupUi(self)
        # Selenium botumuzun çalışması için gerekli ayarlamaları yapıyoruz.
        self.browserProfile = webdriver.ChromeOptions()    
        # İngilizce dil ayarını yapıyoruz. 
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        # İndirme işlemini otomatik olarak yapmasını sağlıyoruz.
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://acikveri.bizizmir.com/tr/dataset/barajlarin-doluluk-oranlari')
        # Tarayıcıyı tam ekran olarak açıyoruz.
        self.browser.maximize_window()
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[2]/div/a").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[2]/div/ul/li[2]/a").click()
        time.sleep(5)
        # İndirme işlemini tamamladıktan sonra tarayıcıyı simge durumuna alıyoruz.
        self.browser.minimize_window()
        # İndirme işlemini tamamladıktan sonra tarayıcıyı kapatıyoruz.
        self.browser.quit()
        # İndirme işlemini tamamladıktan sonra kullanıcıya bilgi veriyoruz.
        QMessageBox.information(self, "Bilgi", "İndirme Tamamlandı")
        # Butonlarımızın fonksiyonlarını çağırıyoruz.
        self.ui.btn_geri.clicked.connect(self.Menufunction)
    def Menufunction(self):
        # Baraj ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Hava(QDialog,QtWidgets.QMainWindow):
    def __init__(self):
        # Hava kalitesi ekranını oluşturuyoruz.
        super(Hava, self).__init__()
        # Tasarım klasörümüzün içerisindeki hava.ui dosyasını çağırıyoruz.
        self.ui = Ui_Cevre()
        self.ui.setupUi(self)
        # Selenium botumuzun çalışması için gerekli ayarlamaları yapıyoruz.
        self.browserProfile = webdriver.ChromeOptions()  
        # İngilizce dil ayarını yapıyoruz.   
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        # İndirme işlemini otomatik olarak yapmasını sağlıyoruz.
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://acikveri.bizizmir.com/tr/dataset/hava-kalitesi-olcum-degerleri')
        # Tarayıcıyı tam ekran olarak açıyoruz.
        self.browser.maximize_window()
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[4]/div/a").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[4]/div/ul/li[2]/a").click()
        time.sleep(5)
        # İndirme işlemini tamamladıktan sonra tarayıcıyı simge durumuna alıyoruz.
        self.browser.minimize_window()
        # İndirme işlemini tamamladıktan sonra tarayıcıyı kapatıyoruz.
        self.browser.quit()
        # İndirme işlemini tamamladıktan sonra kullanıcıya bilgi veriyoruz.
        QMessageBox.information(self, "Bilgi", "İndirme Tamamlandı")
        # Butonlarımızın fonksiyonlarını çağırıyoruz.
        self.ui.btn_geri.clicked.connect(self.Menufunction)
    def Menufunction(self):
        # Hava kalitesi ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Enerji(QDialog):
    def __init__(self):
        # Enerji ekranını oluşturuyoruz.
        super(Enerji,self).__init__()
        # Tasarım klasörümüzün içerisindeki enerji.ui dosyasını çağırıyoruz.
        loadUi("C:/Users/Emir/Desktop/Object Oriented Programming Project (OOPP)/Tasarim/enerji.ui",self)
        # Butonlarımızın fonksiyonlarını çağırıyoruz.
        self.btn_geri.clicked.connect(self.Menufunction)
        self.pushButton_2.clicked.connect(self.Metrofunction)
        self.pushButton_3.clicked.connect(self.Izbanfunction)
        self.pushButton_4.clicked.connect(self.Gunesfunction)
        self.pushButton_5.clicked.connect(self.Elektrikfunction)
    def Icerikfunction(self):
        # Enerji ekranından içerik ekranına geçiş yapılıyor.
        icerik=Icerik()
        widget.addWidget(icerik)
        widget.setCurrentIndex(widget.currentIndex()+1)     
    def Menufunction(self):
        # Enerji ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Metrofunction(self):
        # Enerji ekranından Metro ekranına geçiş yapılıyor.
        metro=Metro()
        widget.addWidget(metro)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Izbanfunction(self):
        # Enerji ekranından İzban ekranına geçiş yapılıyor.
        izbansu=Izban()
        widget.addWidget(izbansu)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Gunesfunction(self):
        # Enerji ekranından Güneş ekranına geçiş yapılıyor.
        gunessu=Gunes()
        widget.addWidget(gunessu)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Elektrikfunction(self):
        # Enerji ekranından Elektrik ekranına geçiş yapılıyor.
        elektriksu=Elektrik()
        widget.addWidget(elektriksu)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Metro(QDialog,QtWidgets.QMainWindow):
    def __init__(self):
        # Metro ekranını oluşturuyoruz.
        super(Metro, self).__init__()
        # Tasarım klasörümüzün içerisindeki metro.ui dosyasını çağırıyoruz.
        self.ui = Ui_Enerji()
        self.ui.setupUi(self)
        # Selenium botumuzun çalışması için gerekli olan kodları yazıyoruz.
        self.browserProfile = webdriver.ChromeOptions()    
        # İngilizce dil ayarını yapıyoruz. 
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        # İndirme işlemini otomatik olarak yapmasını sağlıyoruz.
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://acikveri.bizizmir.com/tr/dataset/metro-ve-tramvay-enerji-tuketimi')
        # Tarayıcıyı tam ekran yaparak açıyoruz.
        self.browser.maximize_window()
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[3]/div/a").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[3]/div/ul/li[2]/a").click()
        time.sleep(5)
        # İndirme işlemini tamamladıktan sonra tarayıcıyı simge durumuna getiriyoruz.
        self.browser.minimize_window()
        # İndirme işlemini tamamladıktan sonra tarayıcıyı kapatıyoruz.
        self.browser.quit()
        # İndirme işlemini tamamladıktan sonra bilgi mesajı veriyoruz.
        QMessageBox.information(self, "Bilgi", "İndirme Tamamlandı")
        # Butonumuzun fonksiyonunu çağırıyoruz.
        self.ui.btn_geri.clicked.connect(self.Menufunction)
    def Menufunction(self):
        # Metro ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Izban(QDialog,QtWidgets.QMainWindow):
    def __init__(self):
        # İzban ekranını oluşturuyoruz.
        super(Izban, self).__init__()
        # Tasarım klasörümüzün içerisindeki izban.ui dosyasını çağırıyoruz.
        self.ui = Ui_Enerji()
        self.ui.setupUi(self)
        # Selenium botumuzun çalışması için gerekli olan kodları yazıyoruz.
        self.browserProfile = webdriver.ChromeOptions()  
        # İngilizce dil ayarını yapıyoruz.   
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        # İndirme işlemini otomatik olarak yapmasını sağlıyoruz.
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://acikveri.bizizmir.com/tr/dataset/izban-istasyonlari')
        # Tarayıcıyı tam ekran yaparak açıyoruz.
        self.browser.maximize_window()
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[4]/div/a").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[4]/div/ul/li[2]/a").click()
        time.sleep(5)
        # İndirme işlemini tamamladıktan sonra tarayıcıyı simge durumuna getiriyoruz.
        self.browser.minimize_window()
        # İndirme işlemini tamamladıktan sonra tarayıcıyı kapatıyoruz.
        self.browser.quit()
        # İndirme işlemini tamamladıktan sonra bilgi mesajı veriyoruz.
        QMessageBox.information(self, "Bilgi", "İndirme Tamamlandı")
        # Butonumuzun fonksiyonunu çağırıyoruz.
        self.ui.btn_geri.clicked.connect(self.Menufunction)
    def Menufunction(self):
        # İzban ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Gunes(QDialog,QtWidgets.QMainWindow):
    def __init__(self):
        # Güneş ekranını oluşturuyoruz.
        super(Gunes, self).__init__()
        # Tasarım klasörümüzün içerisindeki gunes.ui dosyasını çağırıyoruz.
        self.ui = Ui_Enerji()
        self.ui.setupUi(self)
        # Selenium botumuzun çalışması için gerekli olan kodları yazıyoruz.
        self.browserProfile = webdriver.ChromeOptions()     
        # İngilizce dil ayarını yapıyoruz.
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        # İndirme işlemini otomatik olarak yapmasını sağlıyoruz.
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://acikveri.bizizmir.com/tr/dataset/lisanssiz-gunes-enerji-santralleri-listesi')
        # Tarayıcıyı tam ekran yaparak açıyoruz.
        self.browser.maximize_window()
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li/div/a").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li/div/ul/li[2]/a").click()
        time.sleep(5)
        # İndirme işlemini tamamladıktan sonra tarayıcıyı simge durumuna getiriyoruz.
        self.browser.minimize_window()
        # İndirme işlemini tamamladıktan sonra tarayıcıyı kapatıyoruz.
        self.browser.quit()
        # İndirme işlemini tamamladıktan sonra bilgi mesajı veriyoruz.
        QMessageBox.information(self, "Bilgi", "İndirme Tamamlandı")
        # Butonumuzun fonksiyonunu çağırıyoruz.
        self.ui.btn_geri.clicked.connect(self.Menufunction)
    def Menufunction(self):
        # Güneş ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Elektrik(QDialog,QtWidgets.QMainWindow):
    def __init__(self):
        # Elektrik ekranını oluşturuyoruz.
        super(Elektrik, self).__init__()
        # Tasarım klasörümüzün içerisindeki elektrik.ui dosyasını çağırıyoruz.
        self.ui = Ui_Enerji()
        self.ui.setupUi(self)
        # Selenium botumuzun çalışması için gerekli olan kodları yazıyoruz. 
        self.browserProfile = webdriver.ChromeOptions() 
        # İngilizce dil ayarını yapıyoruz.    
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        # İndirme işlemini otomatik olarak yapmasını sağlıyoruz.
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://acikveri.bizizmir.com/tr/dataset/bergama-elektrik-uretim-verileri')
        # Tarayıcıyı tam ekran yaparak açıyoruz.
        self.browser.maximize_window()
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[1]/div/a").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[1]/div/ul/li[2]/a").click()
        time.sleep(5)
        # İndirme işlemini tamamladıktan sonra tarayıcıyı simge durumuna getiriyoruz.
        self.browser.minimize_window()
        # İndirme işlemini tamamladıktan sonra tarayıcıyı kapatıyoruz.
        self.browser.quit()
        # İndirme işlemini tamamladıktan sonra bilgi mesajı veriyoruz.
        QMessageBox.information(self, "Bilgi", "İndirme Tamamlandı")
        # Butonumuzun fonksiyonunu çağırıyoruz.
        self.ui.btn_geri.clicked.connect(self.Menufunction)
    def Menufunction(self):
        # Elektrik ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Yasam(QDialog):
    def __init__(self):
        # Yaşam ekranını oluşturuyoruz.
        super(Yasam,self).__init__()
        # Tasarım klasörümüzün içerisindeki yasam.ui dosyasını çağırıyoruz.
        loadUi("C:/Users/Emir/Desktop/Object Oriented Programming Project (OOPP)/Tasarim/yasam.ui",self)
        # Butonumuzun fonksiyonunu çağırıyoruz.
        self.btn_geri.clicked.connect(self.Menufunction)
        self.pushButton_2.clicked.connect(self.Pazarfunction)
        self.pushButton_3.clicked.connect(self.Eczanefunction)
        self.pushButton_4.clicked.connect(self.Sanatfunction)
        self.pushButton_5.clicked.connect(self.Toplumfunction)
    def Icerikfunction(self):
        # Yaşam ekranından İçerik ekranına geçiş yapılıyor.
        icerik=Icerik()
        widget.addWidget(icerik)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Menufunction(self):
        # Yaşam ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Pazarfunction(self):
        # Yaşam ekranından Pazar ekranına geçiş yapılıyor.
        pazar=Pazar()
        widget.addWidget(pazar)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Eczanefunction(self):
        # Yaşam ekranından Eczane ekranına geçiş yapılıyor.
        eczane=Eczane()
        widget.addWidget(eczane)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Sanatfunction(self):
        # Yaşam ekranından Sanat ekranına geçiş yapılıyor.
        sanat=Sanat()
        widget.addWidget(sanat)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Toplumfunction(self):
        # Yaşam ekranından Toplum ekranına geçiş yapılıyor.
        toplum=Toplum()
        widget.addWidget(toplum)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Pazar(QDialog,QtWidgets.QMainWindow):
    def __init__(self):
        # Pazar ekranını oluşturuyoruz.
        super(Pazar, self).__init__()
        # Tasarım klasörümüzün içerisindeki pazar.ui dosyasını çağırıyoruz.
        self.ui = Ui_Yasam()
        self.ui.setupUi(self)
        # Selenium botumuzu kullanarak gerekli olan kodları yazıyoruz.
        self.browserProfile = webdriver.ChromeOptions()     
        # İngilizce dilini seçiyoruz.
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        # İndirme işlemini otomatik olarak yapmasını sağlıyoruz.
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://acikveri.bizizmir.com/tr/dataset/semt-pazar-yerleri')
        # Tarayıcıyı tam ekran yaparak işlemi başlatıyoruz.
        self.browser.maximize_window()
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[2]/div/a").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[2]/div/ul/li[2]/a").click()
        time.sleep(5)
        # İndirme işlemini tamamladıktan sonra tarayıcıyı kapatıyoruz.
        self.browser.minimize_window()
        # İndirme işlemini tamamladıktan sonra tarayıcıyı kapatıyoruz.
        self.browser.quit()
        # İndirme işlemini tamamladıktan sonra tarayıcıyı kapatıyoruz.
        QMessageBox.information(self, "Bilgi", "İndirme Tamamlandı")
        # Butonumuzun fonksiyonunu çağırıyoruz.
        self.ui.btn_geri.clicked.connect(self.Menufunction)
    def Menufunction(self):
        # Pazar ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Eczane(QDialog,QtWidgets.QMainWindow):
    def __init__(self):
        # Eczane ekranını oluşturuyoruz.
        super(Eczane, self).__init__()
        # Tasarım klasörümüzün içerisindeki eczane.ui dosyasını çağırıyoruz.
        self.ui = Ui_Yasam()
        self.ui.setupUi(self)
        # Selenium botumuzu kullanarak gerekli olan kodları yazıyoruz.
        self.browserProfile = webdriver.ChromeOptions()     
        # İngilizce dilini seçiyoruz.
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        # İndirme işlemini otomatik olarak yapmasını sağlıyoruz.
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://acikveri.bizizmir.com/tr/dataset/nobetci-eczaneler-ve-eczane-listesi')
        # Tarayıcıyı tam ekran yaparak işlemi başlatıyoruz.
        self.browser.maximize_window()
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[3]/div/a").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[3]/div/ul/li[2]/a").click()
        time.sleep(5)
        # İndirme işlemini tamamladıktan sonra tarayıcıyı kapatıyoruz.
        self.browser.minimize_window()
        # İndirme işlemini tamamladıktan sonra tarayıcıyı kapatıyoruz.
        self.browser.quit()       
        # İndirme işlemini tamamladıktan sonra tarayıcıyı kapatıyoruz.
        QMessageBox.information(self, "Bilgi", "İndirme Tamamlandı")
        # Butonumuzun fonksiyonunu çağırıyoruz.
        self.ui.btn_geri.clicked.connect(self.Menufunction)
    def Menufunction(self):
        # Eczane ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Sanat(QDialog,QtWidgets.QMainWindow):
    def __init__(self):
        # Sanat ekranını oluşturuyoruz.
        super(Sanat, self).__init__()
        # Tasarım klasörümüzün içerisindeki sanat.ui dosyasını çağırıyoruz.
        self.ui = Ui_Yasam()
        self.ui.setupUi(self)
        # Selenium botumuzu kullanarak gerekli olan kodları yazıyoruz.
        self.browserProfile = webdriver.ChromeOptions()     
        # İngilizce dilini seçiyoruz.
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        # İndirme işlemini otomatik olarak yapmasını sağlıyoruz.
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://acikveri.bizizmir.com/tr/dataset/kultur-sanat-etkinlikleri')
        # Tarayıcıyı tam ekran yaparak işlemi başlatıyoruz.
        self.browser.maximize_window()
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[3]/div/a").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[3]/div/ul/li[2]/a").click()
        time.sleep(5)
        # İndirme işlemini tamamladıktan sonra tarayıcıyı kapatıyoruz.
        self.browser.minimize_window()
        # İndirme işlemini tamamladıktan sonra tarayıcıyı kapatıyoruz.
        self.browser.quit()
        # İndirme işlemini tamamladıktan sonra tarayıcıyı kapatıyoruz.
        QMessageBox.information(self, "Bilgi", "İndirme Tamamlandı")
        # Butonumuzun fonksiyonunu çağırıyoruz.
        self.ui.btn_geri.clicked.connect(self.Menufunction)
    def Menufunction(self): 
        # Sanat ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Toplum(QDialog,QtWidgets.QMainWindow):
    def __init__(self):
        # Toplum ekranını oluşturuyoruz.
        super(Toplum, self).__init__()
        # Tasarım klasörümüzün içerisindeki toplum.ui dosyasını çağırıyoruz.
        self.ui = Ui_Yasam()
        self.ui.setupUi(self)
        # Selenium botumuzu kullanarak gerekli olan kodları yazıyoruz.
        self.browserProfile = webdriver.ChromeOptions()  
        # İngilizce dilini seçiyoruz.   
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        # İndirme işlemini otomatik olarak yapmasını sağlıyoruz.
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://acikveri.bizizmir.com/tr/dataset/toplum-sagligi-egitimleri')
        # Tarayıcıyı tam ekran yaparak işlemi başlatıyoruz.
        self.browser.maximize_window()
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li/div/a").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li/div/ul/li[2]/a").click()
        time.sleep(5)
        # İndirme işlemini tamamladıktan sonra tarayıcıyı kapatıyoruz.
        self.browser.minimize_window()
        # İndirme işlemini tamamladıktan sonra tarayıcıyı kapatıyoruz.
        self.browser.quit()
        # İndirme işlemini tamamladıktan sonra tarayıcıyı kapatıyoruz.
        QMessageBox.information(self, "Bilgi", "İndirme Tamamlandı")
        # Butonumuzun fonksiyonunu çağırıyoruz.
        self.ui.btn_geri.clicked.connect(self.Menufunction)
    def Menufunction(self):
        # Toplum ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Ekonomi(QDialog):
    def __init__(self):
        # Ekonomi ekranını oluşturuyoruz.
        super(Ekonomi,self).__init__()
        # Tasarım klasörümüzün içerisindeki ekonomi.ui dosyasını çağırıyoruz.
        loadUi("C:/Users/Emir/Desktop/Object Oriented Programming Project (OOPP)/Tasarim/ekonomi.ui",self)
        # Butonlarımızın fonksiyonlarını çağırıyoruz.
        self.btn_geri.clicked.connect(self.Menufunction)
        self.pushButton_2.clicked.connect(self.Semtfunction)
        self.pushButton_3.clicked.connect(self.Balikfunction)
        self.pushButton_4.clicked.connect(self.Halfunction)
        self.pushButton_5.clicked.connect(self.Otoparkfunction)
    def Icerikfunction(self):
        # Ekonomi ekranından İçerik ekranına geçiş yapılıyor.
        icerik=Icerik()
        widget.addWidget(icerik)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Menufunction(self):
        # Ekonomi ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Semtfunction(self):
        # Ekonomi ekranından Semt ekranına geçiş yapılıyor.
        semt=Semt()
        widget.addWidget(semt)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Balikfunction(self):
        # Ekonomi ekranından Balık ekranına geçiş yapılıyor.
        balik=Balik()
        widget.addWidget(balik)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Halfunction(self):
        # Ekonomi ekranından Hal ekranına geçiş yapılıyor.
        hal=Hal()
        widget.addWidget(hal)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Otoparkfunction(self):
        # Ekonomi ekranından Otopark ekranına geçiş yapılıyor.
        otopark=Otopark()
        widget.addWidget(otopark)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Semt(QDialog):
    def __init__(self):
        # Semt ekranını oluşturuyoruz.
        super(Semt, self).__init__()
        # Tasarım klasörümüzün içerisindeki semt.ui dosyasını çağırıyoruz.
        self.ui = Ui_Ekonomi()
        self.ui.setupUi(self)
        # Selenium botumuzu kullanarak gerekli olan kodları yazıyoruz.
        self.browserProfile = webdriver.ChromeOptions() 
        # İngilizce dil ayarını yapıyoruz.    
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        # İndirme işlemini otomatik olarak yapmasını sağlıyoruz.
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://acikveri.bizizmir.com/tr/dataset/semt-pazar-yerleri')
        self.browser.maximize_window()
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[2]/div/a").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[2]/div/ul/li[2]/a").click()
        time.sleep(5)
        self.browser.minimize_window()
        QMessageBox.information(self, "Bilgi", "İndirme Tamamlandı")
        self.browser.quit()
        self.ui.btn_geri.clicked.connect(self.Menufunction)
    def Menufunction(self):
        # Semt ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Balik(QDialog):
    def __init__(self):
        # Balık ekranını oluşturuyoruz.
        super(Balik, self).__init__()
        # Tasarım klasörümüzün içerisindeki balik.ui dosyasını çağırıyoruz.
        self.ui = Ui_Ekonomi()
        self.ui.setupUi(self)
        # Selenium botumuzu kullanarak gerekli olan kodları yazıyoruz.
        self.browserProfile = webdriver.ChromeOptions() 
        # İngilizce dil ayarını yapıyoruz.    
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://acikveri.bizizmir.com/tr/dataset/balik-hal-fiyatlari')
        self.browser.maximize_window()
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[18]/div/a").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[18]/div/ul/li[2]/a").click()
        time.sleep(5)
        self.browser.minimize_window()
        self.browser.quit()
        QMessageBox.information(self, "Bilgi", "İndirme Tamamlandı")
        self.ui.btn_geri.clicked.connect(self.Menufunction)
    def Menufunction(self):
        # Balık ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Hal(QDialog):
    def __init__(self):
        # Hal ekranını oluşturuyoruz.
        super(Hal, self).__init__()
        # Tasarım klasörümüzün içerisindeki hal.ui dosyasını çağırıyoruz.
        self.ui = Ui_Ekonomi()
        self.ui.setupUi(self)
        # Selenium botumuzu kullanarak gerekli olan kodları yazıyoruz.
        self.browserProfile = webdriver.ChromeOptions()  
        # İngilizce dil ayarını yapıyoruz.   
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://acikveri.bizizmir.com/tr/dataset/sebze-ve-meyve-hal-fiyatlari')
        self.browser.maximize_window()
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[19]/div/a").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[19]/div/ul/li[2]/a").click()
        time.sleep(5)
        self.browser.minimize_window()
        self.browser.quit()
        QMessageBox.information(self, "Bilgi", "İndirme Tamamlandı")
        self.ui.btn_geri.clicked.connect(self.Menufunction)
    def Menufunction(self):
        # Hal ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Otopark(QDialog):
    def __init__(self):
        # Otopark ekranını oluşturuyoruz.
        super(Otopark, self).__init__()
        # Tasarım klasörümüzün içerisindeki otopark.ui dosyasını çağırıyoruz.
        self.ui = Ui_Ekonomi()
        self.ui.setupUi(self)
        # Selenium botumuzu kullanarak gerekli olan kodları yazıyoruz.
        self.browserProfile = webdriver.ChromeOptions()    
        # İngilizce dil ayarını yapıyoruz. 
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://acikveri.bizizmir.com/tr/dataset/otopark-ucretleri')
        self.browser.maximize_window()
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[1]/div/a").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[1]/div/ul/li[2]/a").click()
        time.sleep(5)
        self.browser.minimize_window()
        self.browser.quit()        
        QMessageBox.information(self, "Bilgi", "İndirme Tamamlandı")
        self.ui.btn_geri.clicked.connect(self.Menufunction)
    def Menufunction(self):
        # Otopark ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Tarim(QDialog):
    def __init__(self):
        # Tarım ekranını oluşturuyoruz.
        super(Tarim,self).__init__()
        # Tasarım klasörümüzün içerisindeki tarim.ui dosyasını çağırıyoruz.
        loadUi("C:/Users/Emir/Desktop/Object Oriented Programming Project (OOPP)/Tasarim/tarim.ui",self)
        # Butonlarımızın fonksiyonlarını çağırıyoruz.
        self.btn_geri.clicked.connect(self.Menufunction)
        self.pushButton_2.clicked.connect(self.Hayvancilikfunction)
        self.pushButton_3.clicked.connect(self.Aricilikfunction)
        self.pushButton_4.clicked.connect(self.Halfunction)
        self.pushButton_5.clicked.connect(self.KestaneKanserifunction)
    def Icerikfunction(self):
        # Tarım ekranından İçerik ekranına geçiş yapılıyor.
        icerik=Icerik()
        widget.addWidget(icerik)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Menufunction(self):
        # Tarım ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Hayvancilikfunction(self):
        # Tarım ekranından Hayvancılık ekranına geçiş yapılıyor.
        eczane=Hayvancilik()
        widget.addWidget(eczane)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Aricilikfunction(self):
        # Tarım ekranından Arıcılık ekranına geçiş yapılıyor.
        aricilik=Aricilik()
        widget.addWidget(aricilik)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Halfunction(self):
        # Tarım ekranından Hal ekranına geçiş yapılıyor.
        hal=Hal()
        widget.addWidget(hal)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def KestaneKanserifunction(self):
        # Tarım ekranından KestaneKanseri ekranına geçiş yapılıyor.
        kestaneKanseri=KestaneKanseri()
        widget.addWidget(kestaneKanseri)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Hayvancilik(QDialog):
    def __init__(self):
        # Hayvancılık ekranını oluşturuyoruz.
        super(Hayvancilik, self).__init__()
        # Tasarım klasörümüzün içerisindeki hayvancilik.ui dosyasını çağırıyoruz.
        self.ui = Ui_Tarim()
        self.ui.setupUi(self)
        # Selenium botumuzu kullanarak gerekli olan kodları yazıyoruz.
        self.browserProfile = webdriver.ChromeOptions()     
        # İngilizce dil ayarını yapıyoruz.
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        # İndirme işleminin otomatik olarak yapılmasını sağlıyoruz.
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://acikveri.bizizmir.com/tr/dataset/kucukbas-hayvan-dagitimi')
        self.browser.maximize_window()
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li/div/a").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li/div/ul/li[2]/a").click()
        time.sleep(5)
        self.browser.minimize_window()
        self.browser.quit()  
        QMessageBox.information(self, "Bilgi", "İndirme Tamamlandı")
        self.ui.btn_geri.clicked.connect(self.Menufunction)
    def Menufunction(self):
        # Hayvancılık ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)    
class Aricilik(QDialog):
    def __init__(self):
        # Arıcılık ekranını oluşturuyoruz.
        super(Aricilik, self).__init__()
        # Tasarım klasörümüzün içerisindeki aricilik.ui dosyasını çağırıyoruz.
        self.ui = Ui_Tarim()
        self.ui.setupUi(self)
        # Selenium botumuzu kullanarak gerekli olan kodları yazıyoruz.
        self.browserProfile = webdriver.ChromeOptions()   
        # İngilizce dil ayarını yapıyoruz.  
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        # İndirme işleminin otomatik olarak yapılmasını sağlıyoruz.
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://acikveri.bizizmir.com/tr/dataset/aricilik-desteginin-yillara-gore-ilce-ve-mahallere-dagilimi')
        self.browser.maximize_window()
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li/div/a").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li/div/ul/li[2]/a").click()
        time.sleep(5)
        self.browser.minimize_window()
        self.browser.quit()
        QMessageBox.information(self, "Bilgi", "İndirme Tamamlandı")
        self.ui.btn_geri.clicked.connect(self.Menufunction)
    def Menufunction(self):
        # Arıcılık ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Hal(QDialog):
    def __init__(self):
        # Hal ekranını oluşturuyoruz.
        super(Hal, self).__init__()
        # Tasarım klasörümüzün içerisindeki hal.ui dosyasını çağırıyoruz.
        self.ui = Ui_Tarim()
        self.ui.setupUi(self)
        # Selenium botumuzu kullanarak gerekli olan kodları yazıyoruz.
        self.browserProfile = webdriver.ChromeOptions()  
        # İngilizce dil ayarını yapıyoruz.   
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://acikveri.bizizmir.com/tr/dataset/sebze-ve-meyve-hal-fiyatlari')
        self.browser.maximize_window()
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[19]/div/a").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li[19]/div/ul/li[2]/a").click()
        time.sleep(5)
        self.browser.minimize_window()
        self.browser.quit()
        QMessageBox.information(self, "Bilgi", "İndirme Tamamlandı")
        self.ui.btn_geri.clicked.connect(self.Menufunction)
    def Menufunction(self):
        # Hal ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
class KestaneKanseri(QDialog):
    def __init__(self):
        # Kestane Kanseri ekranını oluşturuyoruz.
        super(KestaneKanseri, self).__init__()
        # Tasarım klasörümüzün içerisindeki kestane_kanseri.ui dosyasını çağırıyoruz.
        self.ui = Ui_Tarim()
        self.ui.setupUi(self)
        # Selenium botumuzu kullanarak gerekli olan kodları yazıyoruz.
        self.browserProfile = webdriver.ChromeOptions()     
        # İngilizce dil ayarını yapıyoruz.
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        # İndirme işleminin otomatik olarak yapılmasını sağlıyoruz.
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://acikveri.bizizmir.com/tr/dataset/kestane-kanseri-ile-mucadele-destegi')
        self.browser.maximize_window()
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li/div/a").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='dataset-resources']/ul/li/div/ul/li[2]/a").click()
        time.sleep(5)
        self.browser.minimize_window()
        self.browser.quit()
        QMessageBox.information(self, "Bilgi", "İndirme Tamamlandı")
        self.ui.btn_geri.clicked.connect(self.Menufunction)
    def Menufunction(self):
        # Kestane Kanseri ekranından Main ekranına geçiş yapılıyor.
        main=Icerik()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Social(QDialog):
    def __init__(self):
        # Social ekranını oluşturuyoruz.
        super(Social,self).__init__()
        # Tasarım klasörümüzün içerisindeki social.ui dosyasını çağırıyoruz.
        loadUi("C:/Users/Emir/Desktop/Object Oriented Programming Project (OOPP)/Tasarim/social.ui",self)
        # Butonlarımızın fonksiyonlarını çağırıyoruz.
        self.btn_geri.clicked.connect(self.Menufunction)
        self.instaD.clicked.connect(self.InstagramDfunction)
        self.instaE.clicked.connect(self.InstagramEfunction)
        self.instaC.clicked.connect(self.InstagramCfunction)
        self.githubD.clicked.connect(self.GithubDfunction) 
        self.githubE.clicked.connect(self.GithubEfunction) 
        self.githubC.clicked.connect(self.GithubCfunction)
    def mainfunction(self):
        # Social ekranından Login ekranına geçiş yapılıyor.
        login=Giris()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def Menufunction(self):
        # Social ekranından Main ekranına geçiş yapılıyor.
        main=Main()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def InstagramDfunction(self):
        # Selenium botumuzu Doğukan Bostancı'nın instagram hesabına yönlendiriyoruz.
        self.browserProfile = webdriver.ChromeOptions()     
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://www.instagram.com/dbostancii/')
        self.browser.maximize_window()
        time.sleep(3)
        self.browser.quit()
    def InstagramEfunction(self):
        # Selenium botumuzu Emir Çoban'ın instagram hesabına yönlendiriyoruz.
        self.browserProfile = webdriver.ChromeOptions()     
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://www.instagram.com/emircbn16/')
        self.browser.maximize_window()
        time.sleep(3)
        self.browser.quit()
    def InstagramCfunction(self):
        # Selenium botumuzu Ceyhun Yalçınkaya'nın instagram hesabına yönlendiriyoruz.
        self.browserProfile = webdriver.ChromeOptions()     
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://www.instagram.com/ceyhunyalcinkaya3/')
        self.browser.maximize_window()
        time.sleep(3)
        self.browser.quit()
    def GithubDfunction(self):
        # Selenium botumuzu Doğukan Bostancı'nın github hesabına yönlendiriyoruz.
        self.browserProfile = webdriver.ChromeOptions()     
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://github.com/giantgorilla')
        self.browser.maximize_window()
        time.sleep(3)
        self.browser.quit()
    def GithubEfunction(self):
        # Selenium botumuzu Emir Çoban'ın github hesabına yönlendiriyoruz.
        self.browserProfile = webdriver.ChromeOptions()     
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://github.com/emircbn16')
        self.browser.maximize_window()
        time.sleep(3)
        self.browser.quit() 

    def GithubCfunction(self):
        # Selenium botumuzu Ceyhun Yalçınkaya'nın github hesabına yönlendiriyoruz.
        self.browserProfile = webdriver.ChromeOptions()     
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.get('https://github.com/yalcinkayaceyhun')
        self.browser.maximize_window()
        time.sleep(3)
        self.browser.quit()       
class Info(QDialog):
    def __init__(self):
        # Info ekranının tasarımı ve butonlarının fonksiyonları burada tanımlanıyor.
        super(Info,self).__init__()
        loadUi("C:/Users/Emir/Desktop/Object Oriented Programming Project (OOPP)/Tasarim/info.ui",self)
        self.btn_geri.clicked.connect(self.Menufunction)
    def Menufunction(self):
        # Info ekranından Main ekranına geçiş yapılıyor.
        main=Main()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)
def show_main_window(app, widget): # ChatGPT3 tarafından yeniden düzenlenmiştir...
    # Ana ekranımızı oluşturuyoruz.
    mainwindow = Giris()
    widget.addWidget(mainwindow)
    widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    widget.setFixedSize(400, 815)
    widget.setWindowTitle("OOPP")
    widget.setWindowIcon(QtGui.QIcon("Tasarim\Images\logo.ico"))
    widget.show()
    app.exec_()
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
show_main_window(app, widget)