from PyQt5 import QtCore, QtGui, QtWidgets  # Build a graphical interface

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox  # Display graphical interface


class UIMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, FIFASystem):
        FIFASystem.setObjectName("FIFASystem")
        FIFASystem.resize(1007, 634)  # Interface size settings
        FIFASystem.setMaximumSize(1007, 634)
        FIFASystem.setMinimumSize(1007, 634)
        FIFASystem.setStyleSheet("QWidget#FIFASystem{\n"
                                 "    border-image: url(:/GUI Project/FIFA Background Image.png);\n"
                                 "}")  # Background image settings
        """Setting of username line style"""
        self.username_line = QtWidgets.QLineEdit(FIFASystem)
        self.username_line.setGeometry(QtCore.QRect(550, 90, 331, 31))
        self.username_line.setStyleSheet("background-color: rgb(255, 255, 255, 0.3);")
        self.username_line.setObjectName("username_line")
        """Setting of password line style"""
        self.password_line = QtWidgets.QLineEdit(FIFASystem)
        self.password_line.setGeometry(QtCore.QRect(550, 460, 331, 31))
        self.password_line.setStyleSheet("background-color: rgb(255, 255, 255, 0.3);")
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line.setObjectName("password_line")
        """Setting of register button style"""
        self.register_button = QtWidgets.QPushButton(FIFASystem)
        self.register_button.setGeometry(QtCore.QRect(10, 520, 131, 29))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.register_button.setFont(font)
        self.register_button.setObjectName("register_button")
        self.register_button.clicked.connect(self.close)
        self.register_button.clicked.connect(self.register_interface)  # Signal for jumping to the registration screen
        """Setting of user login button style"""
        self.userlogin_button = QtWidgets.QPushButton(FIFASystem)
        self.userlogin_button.setGeometry(QtCore.QRect(10, 170, 131, 29))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.userlogin_button.setFont(font)
        self.userlogin_button.setObjectName("userlogin_button")
        self.userlogin_button.clicked.connect(self.user_interface)  # Signal for jumping to the user screen
        """Setting of administrator login button style"""
        self.managerlogin_button = QtWidgets.QPushButton(FIFASystem)
        self.managerlogin_button.setGeometry(QtCore.QRect(10, 340, 131, 49))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.managerlogin_button.setFont(font)
        self.managerlogin_button.setObjectName("managerlogin_button")
        self.managerlogin_button.clicked.connect(self.manager_interface)  # Signal for jumping to the administrator
        # screen
        """Setting of username label style"""
        self.username_label = QtWidgets.QLabel(FIFASystem)
        self.username_label.setGeometry(QtCore.QRect(350, 30, 121, 151))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setItalic(True)
        self.username_label.setFont(font)
        self.username_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.username_label.setScaledContents(False)
        self.username_label.setObjectName("username_label")
        """Setting of password label style"""
        self.password_label = QtWidgets.QLabel(FIFASystem)
        self.password_label.setGeometry(QtCore.QRect(350, 400, 121, 141))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setItalic(True)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.password_label.setScaledContents(False)
        self.password_label.setObjectName("password_label")
        """Setting of exit button style"""
        self.exit_button = QtWidgets.QPushButton(FIFASystem)
        self.exit_button.setGeometry(QtCore.QRect(850, 520, 131, 29))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.exit_button.setFont(font)
        self.exit_button.setObjectName("exit_button")
        self.exit_button.clicked.connect(self.close)  # Signal for closing the screen

        self.text(FIFASystem)
        QtCore.QMetaObject.connectSlotsByName(FIFASystem)

    def text(self, FIFASystem):
        """
        Set interface element text information
        """
        _translate = QtCore.QCoreApplication.translate
        FIFASystem.setWindowTitle(_translate("FIFASystem", "FIFA World Cup System"))
        self.register_button.setText(_translate("FIFASystem", "Register"))
        self.userlogin_button.setText(_translate("FIFASystem", "User Login"))
        self.managerlogin_button.setText(_translate("FIFASystem", "Administrator\n Login"))
        self.username_label.setText(_translate("FIFASystem", "Username:"))
        self.password_label.setText(_translate("FIFASystem", "Password:"))
        self.exit_button.setText(_translate("FIFASystem", "Exit"))

    def user_interface(self):
        """
        Slot function for jumping to the user screen
        """
        if self.username_line.text().strip() == '' or self.password_line.text().strip() == '':
            try:
                QMessageBox.information(self, 'Error', 'Invalid input, please try again.')
            except Exception as error:
                print('Input error %s' % error)
        else:
            username = self.username_line.text().strip()
            password = self.password_line.text().strip()

            data_list = f'l {username} {password} User'

            from client import TCPClient
            self.login_thread = TCPClient(data_list)
            self.login_thread.display_signal.connect(self.user_login_response)
            self.login_thread.start()

    def user_login_response(self, response):
        response = response.split(' ')
        if response[0] == 'False':
            """
            If the server cannot receive the message, then it will return a list like 'False error message'
            """
            try:
                message = ''
                for word in range(1, len(response)):
                    message += response[word] + ' '
                QMessageBox.information(self, 'Error', message)
            except Exception as error:
                print('Error %s' % error)
        else:
            try:
                QMessageBox.information(self, 'Welcome', 'Successful Login')
            except Exception as error:
                print('Database error %s' % error)
            else:
                self.close()
                from user_interface import UserInterface
                self.user_interface = UserInterface()
                self.user_interface.show()

    def manager_interface(self):
        """
        Slot function for jumping to the administrator screen
        """
        if self.username_line.text().strip() == '' or self.password_line.text().strip() == '':
            try:
                QMessageBox.information(self, 'Error', 'Invalid input, please try again.')
            except Exception as error:
                print('Input error %s' % error)
        else:
            username = self.username_line.text().strip()
            password = self.password_line.text().strip()

            data_list = f'l {username} {password} Administrator'

            from client import TCPClient
            self.login_thread = TCPClient(data_list)
            self.login_thread.display_signal.connect(self.administrator_login_response)
            self.login_thread.start()

    def administrator_login_response(self, response):
        response = response.split(' ')
        if response[0] == 'False':
            """
            If the server cannot receive the message, then it will return a list like 'False error message'
            """
            try:
                message = ''
                for word in range(1, len(response)):
                    message += response[word] + ' '
                QMessageBox.information(self, 'Error', message)
            except Exception as error:
                print('Error %s' % error)
        else:
            try:
                QMessageBox.information(self, 'Welcome', 'Successful Login')
            except Exception as error:
                print('Database error %s' % error)
            else:
                self.close()
                from administrator_interface import AdministratorInterface
                self.administrator_interface = AdministratorInterface()
                self.administrator_interface.show()

    def register_interface(self):
        """
        Slot function for jumping to the registration screen
        """

        from register_interface import RegisterInterface
        self.register_interface = RegisterInterface()
        self.register_interface.show()


import Source_rc  # Load image

if __name__ == '__main__':
    app = QApplication(sys.argv)

    interface = UIMainWindow()

    interface.show()
    sys.exit(app.exec_())
