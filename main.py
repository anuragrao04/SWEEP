import sys 
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QLineEdit

#-----------------------------class declaration-----------------------------#
class loginregister(QMainWindow):
     def __init__(self):
         super(loginregister, self).__init__()
         loadUi("loginregister.ui", self)
         self.pushButton_login.clicked.connect(self.get_login_page)
         self.pushButton_register.clicked.connect(self.get_register_page)
        

     def get_login_page(self):
         widget.setCurrentIndex(1)
     def get_register_page(self):
         pass 
         #register page code here 




class login_page(QMainWindow):
     def __init__(self):
         super(login_page, self).__init__()
         loadUi("login_page.ui", self)
         self.pushButton_view.clicked.connect(self.pass_view_clicked)
         self.pushButton_back.clicked.connect(self.get_back)
         self.pushButton_login.clicked.connect(self.login)
     def pass_view_clicked(self):
         if self.pushButton_view.isChecked():
             self.lineEdit_password.setEchoMode(normal)
         else:
             self.lineEdit_password.setEchoMode(password)
     def get_back(self):
          widget.setCurrentIndex(0)
     def login(self):
          pass
          #on login button press

#-----------------------------indexing for stacked widget-----------------------------#

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

login_register = loginregister()
login_page = login_page()


widget.addWidget(login_register)    #0
widget.addWidget(login_page)        #1

widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")

