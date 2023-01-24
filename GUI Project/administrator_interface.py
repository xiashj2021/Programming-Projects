import re
from PyQt5 import QtCore, QtGui, QtWidgets  # Build a graphical interface

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox  # Display graphical interface


class AdministratorInterface(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, FIFASystem):
        FIFASystem.setObjectName("FIFASystem")
        FIFASystem.resize(1122, 734)  # Interface size settings
        FIFASystem.setMaximumSize(1122, 734)
        FIFASystem.setMinimumSize(1122, 734)
        FIFASystem.setStyleSheet("QWidget#FIFASystem{\n"
                                 "border-image: url(:/GUI Project/Administrator Image.png);\n"
                                 "}")  # Background image settings
        """Setting of date line style"""
        self.date_line = QtWidgets.QLineEdit(FIFASystem)
        self.date_line.setGeometry(QtCore.QRect(220, 200, 331, 31))
        self.date_line.setStyleSheet("background-color: rgb(255, 255, 255, 0.5);")
        self.date_line.setText("")
        self.date_line.setObjectName("date_line")
        """Setting of team name label style"""
        self.teamname_label = QtWidgets.QLabel(FIFASystem)
        self.teamname_label.setGeometry(QtCore.QRect(10, 20, 121, 151))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setItalic(True)
        self.teamname_label.setFont(font)
        self.teamname_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.teamname_label.setScaledContents(False)
        self.teamname_label.setObjectName("teamname_label")
        """Setting of race type line style"""
        self.racetype_line = QtWidgets.QLineEdit(FIFASystem)
        self.racetype_line.setGeometry(QtCore.QRect(780, 200, 331, 31))
        self.racetype_line.setStyleSheet("background-color: rgb(255, 255, 255, 0.5);")
        self.racetype_line.setObjectName("racetype_line")
        """Setting of time line style"""
        self.time_line = QtWidgets.QLineEdit(FIFASystem)
        self.time_line.setGeometry(QtCore.QRect(780, 80, 331, 31))
        self.time_line.setStyleSheet("background-color: rgb(255, 255, 255, 0.5);")
        self.time_line.setObjectName("time_line")
        """Setting of score label style"""
        self.score_label = QtWidgets.QLabel(FIFASystem)
        self.score_label.setGeometry(QtCore.QRect(10, 260, 121, 151))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setItalic(True)
        self.score_label.setFont(font)
        self.score_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.score_label.setScaledContents(False)
        self.score_label.setObjectName("score_label")
        """Setting of race type label style"""
        self.racetype_label = QtWidgets.QLabel(FIFASystem)
        self.racetype_label.setGeometry(QtCore.QRect(630, 140, 121, 151))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setItalic(True)
        self.racetype_label.setFont(font)
        self.racetype_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.racetype_label.setScaledContents(False)
        self.racetype_label.setObjectName("racetype_label")
        """Setting of score line style"""
        self.score_line = QtWidgets.QLineEdit(FIFASystem)
        self.score_line.setGeometry(QtCore.QRect(220, 320, 331, 31))
        self.score_line.setStyleSheet("background-color: rgb(255, 255, 255, 0.5);")
        self.score_line.setObjectName("score_line")
        """Setting of time label style"""
        self.time_label = QtWidgets.QLabel(FIFASystem)
        self.time_label.setGeometry(QtCore.QRect(630, 20, 121, 151))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setItalic(True)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.time_label.setScaledContents(False)
        self.time_label.setObjectName("time_label")
        """Setting of date label style"""
        self.date_label = QtWidgets.QLabel(FIFASystem)
        self.date_label.setGeometry(QtCore.QRect(10, 140, 121, 151))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setItalic(True)
        self.date_label.setFont(font)
        self.date_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.date_label.setScaledContents(False)
        self.date_label.setObjectName("date_label")
        """Setting of team name line style"""
        self.teamname_line = QtWidgets.QLineEdit(FIFASystem)
        self.teamname_line.setGeometry(QtCore.QRect(220, 80, 331, 31))
        self.teamname_line.setStyleSheet("background-color: rgb(255, 255, 255, 0.5);")
        self.teamname_line.setText("")
        self.teamname_line.setObjectName("teamname_line")
        """Setting of event label style"""
        self.event_label = QtWidgets.QLabel(FIFASystem)
        self.event_label.setGeometry(QtCore.QRect(630, 260, 121, 151))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setItalic(True)
        self.event_label.setFont(font)
        self.event_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.event_label.setScaledContents(False)
        self.event_label.setObjectName("event_label")
        """Setting of event line style"""
        self.event_line = QtWidgets.QLineEdit(FIFASystem)
        self.event_line.setGeometry(QtCore.QRect(780, 320, 331, 31))
        self.event_line.setStyleSheet("background-color: rgb(255, 255, 255, 0.5);")
        self.event_line.setObjectName("event_line")
        """Setting of status line style"""
        self.status_line = QtWidgets.QLineEdit(FIFASystem)
        self.status_line.setGeometry(QtCore.QRect(220, 430, 331, 31))
        self.status_line.setStyleSheet("background-color: rgb(255, 255, 255, 0.5);")
        self.status_line.setObjectName("status_line")
        """Setting of status label style"""
        self.status_label = QtWidgets.QLabel(FIFASystem)
        self.status_label.setGeometry(QtCore.QRect(10, 370, 121, 151))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setItalic(True)
        self.status_label.setFont(font)
        self.status_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.status_label.setScaledContents(False)
        self.status_label.setObjectName("status_label")
        """Setting of return button style"""
        self.returnButton = QtWidgets.QPushButton(FIFASystem)
        self.returnButton.setGeometry(QtCore.QRect(990, 430, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.returnButton.setFont(font)
        self.returnButton.setObjectName("returnButton")
        self.returnButton.clicked.connect(self.close)
        self.returnButton.clicked.connect(self.main_interface)  # Signal for jumping to the main screen
        """Setting of insert button style"""
        self.insertButton = QtWidgets.QPushButton(FIFASystem)
        self.insertButton.setGeometry(QtCore.QRect(990, 500, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.insertButton.setFont(font)
        self.insertButton.setFlat(False)
        self.insertButton.setObjectName("insertButton")
        self.insertButton.clicked.connect(self.after_insert)  # Signal for completing insert
        """Setting of upgrade button style"""
        self.updateButton = QtWidgets.QPushButton(FIFASystem)
        self.updateButton.setGeometry(QtCore.QRect(990, 570, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.updateButton.setFont(font)
        self.updateButton.setFlat(False)
        self.updateButton.setObjectName("upgradeButton")
        self.updateButton.clicked.connect(self.after_update)  # Signal for completing upgrade

        self.text(FIFASystem)
        QtCore.QMetaObject.connectSlotsByName(FIFASystem)

    def text(self, FIFASystem):
        _translate = QtCore.QCoreApplication.translate
        FIFASystem.setWindowTitle(_translate("FIFASystem", "FIFA World Cup System"))
        self.teamname_label.setText(_translate("FIFASystem", "Teamname:"))
        self.score_label.setText(_translate("FIFASystem", "Score:"))
        self.racetype_label.setText(_translate("FIFASystem", "Race Type:"))
        self.time_label.setText(_translate("FIFASystem", "Time:"))
        self.date_label.setText(_translate("FIFASystem", "Date:"))
        self.event_label.setText(_translate("FIFASystem", "Event:"))
        self.status_label.setText(_translate("FIFASystem", "Status:"))
        self.returnButton.setText(_translate("FIFASystem", "Return"))
        self.insertButton.setText(_translate("FIFASystem", "Insert"))
        self.updateButton.setText(_translate("FIFASystem", "Update"))

    def main_interface(self):
        """
        Slot function for jumping to the main screen
        """

        from main_interface import UIMainWindow
        self.main_interface = UIMainWindow()
        self.main_interface.show()

    def after_insert(self):
        team_name = self.teamname_line.text().strip()
        race_type_input = self.racetype_line.text()
        score = self.score_line.text().strip()
        date_input = self.date_line.text()
        race_time_input = self.time_line.text()
        event = self.event_line.text().strip()
        status_input = self.status_line.text()

        date_regex = re.compile(r'^(.\D+)*(\d{1,2} [A-Z][a-z]{2} [0-9]{4})+(.+)*$')
        time_regex = re.compile(r'^(.\D+)*(\d{2}:\d{2})+(.+)*$')
        race_type_regex = re.compile(
            r'^(.\d+)*(Group [A-H]|Round of 16|Quarter-final|Semi-final|Play-off for third place|Final)(.+)*$')
        status_regex = re.compile(r'FT|HT|I|A|ET|NS')

        date_data = re.search(date_regex, date_input)
        race_time_data = re.search(time_regex, race_time_input)
        race_type_data = re.search(race_type_regex, race_type_input)
        status_data = re.search(status_regex, status_input)

        if (date_data is None) or (race_type_data is None) or (race_time_data is None) or (status_data is None):
            try:
                QMessageBox.information(
                    self, 'Error', 'Invalid input, please input correct format information you want to insert.')
            except Exception as error:
                print('Input error %s' % error)
        else:
            date = date_data.group(2)
            race_time = race_time_data.group(2)
            race_type = race_type_data.group(2)
            status = status_data.group()
            data_list = f'i_{team_name}_{race_type}_{score}_{date}_{race_time}_{event}_{status}'

            from client import TCPClient
            self.insert_thread = TCPClient(data_list)
            self.insert_thread.display_signal.connect(self.insert_response)
            self.insert_thread.start()

    def insert_response(self, response):
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
                QMessageBox.information(self, 'Insertion', 'Successful Insertion.')
            except Exception as error:
                print('Error %s' % error)

    def after_update(self):
        team_name_input = self.teamname_line.text()
        race_type_input = self.racetype_line.text()
        score_input = self.score_line.text()
        date_input = self.date_line.text()
        race_time_input = self.time_line.text()
        event = self.event_line.text().strip()
        status_input = self.status_line.text()

        date_regex = re.compile(r'^(.\D+)*(\d{1,2} [A-Z][a-z]{2} [0-9]{4})+(.+)*$')
        time_regex = re.compile(r'^(.\D+)*(\d{2}:\d{2})+(.+)*$')
        team_name_regex = re.compile(r'(.\d+)*([A-Z][a-z]+( [A-Z][a-z]+)* vs [A-Z][a-z]+( [A-Z][a-z]+)*)+(.+)*$')
        score_regex = re.compile(r'^(.\D+)*(\d · \d( [(]\d[)] · [(]\d[)])?)+(.+)*$')
        race_type_regex = re.compile(
            r'^(.\d+)*(Group [A-H]|Round of 16|Quarter-final|Semi-final|Play-off for third place|Final)(.+)*$')
        status_regex = re.compile(r'FT|HT|I|A|ET|NS')

        date_data = re.search(date_regex, date_input)
        race_time_data = re.search(time_regex, race_time_input)
        team_name_data = re.search(team_name_regex, team_name_input)
        score_data = re.search(score_regex, score_input)
        race_type_data = re.search(race_type_regex, race_type_input)
        status_data = re.search(status_regex, status_input)

        if (date_data is None) or (race_type_data is None) or (race_time_data is None) or (status_data is None)\
                or (team_name_data is None) or (score_data is None):
            try:
                QMessageBox.information(
                    self, 'Error', 'Invalid input, please input correct format information you want to upgrade.')
            except Exception as error:
                print('Input error %s' % error)
        else:
            date = date_data.group(2)
            race_time = race_time_data.group(2)
            race_type = race_type_data.group(2)
            score = score_data.group(2)
            team_name = team_name_data.group(2)
            status = status_data.group()
            data_list = f'u_{team_name}_{race_type}_{score}_{date}_{race_time}_{event}_{status}'

            from client import TCPClient
            self.update_thread = TCPClient(data_list)
            self.update_thread.display_signal.connect(self.update_response)
            self.update_thread.start()

    def update_response(self, response):
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
                QMessageBox.information(self, 'Insertion', 'Successful Update.')
            except Exception as error:
                print('Error %s' % error)


import Source_rc  # Load image

if __name__ == '__main__':
    app = QApplication(sys.argv)

    interface = AdministratorInterface()

    interface.show()
    sys.exit(app.exec_())
