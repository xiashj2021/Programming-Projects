import re
from PyQt5 import QtCore, QtGui, QtWidgets  # Build a graphical interface

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox  # Display graphical interface
from client import TCPClient


class UserInterface(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, FIFASystem):
        FIFASystem.setObjectName("FIFASystem")
        FIFASystem.resize(1122, 734)  # Interface size settings
        FIFASystem.setMaximumSize(1122, 734)
        FIFASystem.setMinimumSize(1122, 734)
        FIFASystem.setStyleSheet("QWidget#FIFASystem{\n"
                                 "border-image: url(:/GUI Project/User Image.png);\n"
                                 "}")  # Background image settings
        """Setting of query button style"""
        self.queryButton = QtWidgets.QPushButton(FIFASystem)
        self.queryButton.setGeometry(QtCore.QRect(920, 320, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.queryButton.setFont(font)
        self.queryButton.setFlat(False)
        self.queryButton.setObjectName("queryButton")
        self.queryButton.clicked.connect(self.after_query)  # Signal for completing query
        """Setting of return button style"""
        self.returnButton = QtWidgets.QPushButton(FIFASystem)
        self.returnButton.setGeometry(QtCore.QRect(920, 250, 121, 31))
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
        """Setting of table widget style"""
        self.tableWidget = QtWidgets.QTableWidget(FIFASystem)
        self.tableWidget.setGeometry(QtCore.QRect(-5, 470, 1131, 271))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255, 0.6);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(25)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(158)
        self.tableWidget.verticalHeader().setVisible(False)
        """Setting of team name label style"""
        self.teamname_label = QtWidgets.QLabel(FIFASystem)
        self.teamname_label.setGeometry(QtCore.QRect(0, 0, 121, 151))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setItalic(True)
        self.teamname_label.setFont(font)
        self.teamname_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.teamname_label.setScaledContents(False)
        self.teamname_label.setObjectName("teamname_label")
        """Setting of team name line style"""
        self.teamname_line = QtWidgets.QLineEdit(FIFASystem)
        self.teamname_line.setGeometry(QtCore.QRect(210, 60, 331, 31))
        self.teamname_line.setStyleSheet("background-color: rgb(255, 255, 255, 0.6);")
        self.teamname_line.setText("")
        self.teamname_line.setObjectName("teamname_line")
        """Setting of date label style"""
        self.date_label = QtWidgets.QLabel(FIFASystem)
        self.date_label.setGeometry(QtCore.QRect(0, 120, 121, 151))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setItalic(True)
        self.date_label.setFont(font)
        self.date_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.date_label.setScaledContents(False)
        self.date_label.setObjectName("date_label")
        """Setting of date line style"""
        self.date_line = QtWidgets.QLineEdit(FIFASystem)
        self.date_line.setGeometry(QtCore.QRect(210, 180, 331, 31))
        self.date_line.setStyleSheet("background-color: rgb(255, 255, 255, 0.6);")
        self.date_line.setText("")
        self.date_line.setObjectName("date_line")
        """Setting of score line style"""
        self.score_line = QtWidgets.QLineEdit(FIFASystem)
        self.score_line.setGeometry(QtCore.QRect(210, 300, 331, 31))
        self.score_line.setStyleSheet("background-color: rgb(255, 255, 255, 0.6);")
        self.score_line.setObjectName("score_line")
        """Setting of score label style"""
        self.score_label = QtWidgets.QLabel(FIFASystem)
        self.score_label.setGeometry(QtCore.QRect(0, 240, 121, 151))
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
        self.racetype_label.setGeometry(QtCore.QRect(620, 120, 121, 151))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setItalic(True)
        self.racetype_label.setFont(font)
        self.racetype_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.racetype_label.setScaledContents(False)
        self.racetype_label.setObjectName("racetype_label")
        """Setting of race type line style"""
        self.racetype_line = QtWidgets.QLineEdit(FIFASystem)
        self.racetype_line.setGeometry(QtCore.QRect(770, 180, 331, 31))
        self.racetype_line.setStyleSheet("background-color: rgb(255, 255, 255, 0.6);")
        self.racetype_line.setObjectName("racetype_line")
        self.time_label = QtWidgets.QLabel(FIFASystem)
        self.time_label.setGeometry(QtCore.QRect(620, 0, 121, 151))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setItalic(True)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.time_label.setScaledContents(False)
        self.time_label.setObjectName("time_label")
        self.time_line = QtWidgets.QLineEdit(FIFASystem)
        self.time_line.setGeometry(QtCore.QRect(770, 60, 331, 31))
        self.time_line.setStyleSheet("background-color: rgb(255, 255, 255, 0.6);")
        self.time_line.setObjectName("time_line")

        self.text(FIFASystem)
        QtCore.QMetaObject.connectSlotsByName(FIFASystem)

    def text(self, FIFASystem):
        """
        Set interface element text information
        """
        _translate = QtCore.QCoreApplication.translate
        FIFASystem.setWindowTitle(_translate("FIFASystem", "FIFA World Cup System"))
        self.queryButton.setText(_translate("FIFASystem", "Query"))
        self.returnButton.setText(_translate("FIFASystem", "Return"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.teamname_label.setText(_translate("FIFASystem", "Teamname:"))
        self.date_label.setText(_translate("FIFASystem", "Date:"))
        self.score_label.setText(_translate("FIFASystem", "Score:"))
        self.racetype_label.setText(_translate("FIFASystem", "Race Type:"))
        self.time_label.setText(_translate("FIFASystem", "Time:"))

    def main_interface(self):
        """
        Slot function for jumping to the main screen
        """

        from main_interface import UIMainWindow
        self.main_interface = UIMainWindow()
        self.main_interface.show()

    def after_query(self):
        """
        Slot function for completing query
        """
        team_name_data = self.teamname_line.text()
        score_data = self.score_line.text()
        date_data = self.date_line.text()
        time_data = self.time_line.text()
        race_type_data = self.racetype_line.text()

        time_regex = re.compile(r'^(.\D+)*(\d{2}:\d{2})+(.+)*$')
        score_regex = re.compile(r'^(.\D+)*(\d · \d( [(]\d[)] · [(]\d[)])?)+(.+)*$')
        date_regex = re.compile(r'^(.\D+)*(\d{1,2} [A-Z][a-z]{2}( [0-9]{4})?)+(.+)*$')
        team_name_regex = re.compile(r'^(.\d+)*([A-Z][a-z]+(( [A-Z][a-z]+)* vs [A-Z][a-z]+( [A-Z][a-z]+)*)?)+(.+)*$')
        race_type_regex = re.compile(
            r'^(.\d+)*(Group [A-H]|Round of 16|Quarter-final|Semi-final|Play-off for third place|Final)(.+)*$')

        team_name = re.search(team_name_regex, team_name_data)
        score = re.search(score_regex, score_data)
        date = re.search(date_regex, date_data)
        race_type = re.search(race_type_regex, race_type_data)
        race_time = re.search(time_regex, time_data)

        if (team_name is None) and (score is None) and (date is None) and (race_type is None) and (race_time is None):
            try:
                QMessageBox.information(self, 'Error', 'Invalid input, please input some information you want to know.')
            except Exception as error:
                print('Input error %s' % error)

        elif (team_name is None) and (score is None) and (date is None) and (race_type is None):
            time_input = race_time.group(2)

            data_list = f'q|time|{time_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()
        elif (team_name is None) and (score is None) and (date is None) and (race_time is None):
            type_input = race_type.group(2)

            data_list = f'q|type|{type_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()
        elif (team_name is None) and (score is None) and (race_type is None) and (race_time is None):
            date_input = date.group(2)

            data_list = f'q|date|{date_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()
        elif (team_name is None) and (date is None) and (race_type is None) and (race_time is None):
            score_input = score.group(2)

            data_list = f'q|score|{score_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()
        elif (score is None) and (date is None) and (race_type is None) and (race_time is None):
            team_input = team_name.group(2)

            data_list = f'q|team|{team_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()

        elif (team_name is None) and (score is None) and (date is None):
            time_input = race_time.group(2)
            type_input = race_type.group(2)

            data_list = f'q|time_type|{time_input}_{type_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()
        elif (team_name is None) and (score is None) and (race_type is None):
            time_input = race_time.group(2)
            date_input = date.group(2)

            data_list = f'q|time_date|{time_input}_{date_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()
        elif (team_name is None) and (date is None) and (race_type is None):
            time_input = race_time.group(2)
            score_input = score.group(2)

            data_list = f'q|time_score|{time_input}_{score_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()
        elif (score is None) and (date is None) and (race_type is None):
            time_input = race_time.group(2)
            team_input = team_name.group(2)

            data_list = f'q|time_team|{time_input}_{team_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()
        elif (team_name is None) and (score is None) and (race_time is None):
            type_input = race_type.group(2)
            date_input = date.group(2)

            data_list = f'q|type_date|{type_input}_{date_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()
        elif (team_name is None) and (date is None) and (race_time is None):
            type_input = race_type.group(2)
            score_input = score.group(2)

            data_list = f'q|type_score|{type_input}_{score_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()
        elif (score is None) and (date is None) and (race_time is None):
            type_input = race_type.group(2)
            team_input = team_name.group(2)

            data_list = f'q|type_team|{type_input}_{team_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()
        elif (team_name is None) and (race_type is None) and (race_time is None):
            date_input = date.group(2)
            score_input = score.group(2)

            data_list = f'q|date_score|{date_input}_{score_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()
        elif (score is None) and (race_type is None) and (race_time is None):
            date_input = date.group(2)
            team_input = team_name.group(2)

            data_list = f'q|date_team|{date_input}_{team_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()
        elif (date is None) and (race_type is None) and (race_time is None):
            score_input = score.group(2)
            team_input = team_name.group(2)

            data_list = f'q|score_team|{score_input}_{team_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()

        elif (team_name is None) and (score is None):
            time_input = race_time.group(2)
            type_input = race_type.group(2)
            date_input = date.group(2)

            data_list = f'q|time_type_date|{time_input}_{type_input}_{date_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()

        elif (team_name is None) and (date is None):
            time_input = race_time.group(2)
            type_input = race_type.group(2)
            score_input = score.group(2)

            data_list = f'q|time_type_score|{time_input}_{type_input}_{score_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()
        elif (score is None) and (date is None):
            time_input = race_time.group(2)
            type_input = race_type.group(2)
            team_input = team_name.group(2)

            data_list = f'q|time_type_team|{time_input}_{type_input}_{team_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()
        elif (team_name is None) and (race_type is None):
            time_input = race_time.group(2)
            date_input = date.group(2)
            score_input = score.group(2)

            data_list = f'q|time_date_score|{time_input}_{date_input}_{score_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()
        elif (score is None) and (race_type is None):
            time_input = race_time.group(2)
            date_input = date.group(2)
            team_input = team_name.group(2)

            data_list = f'q|time_date_team|{time_input}_{date_input}_{team_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()
        elif (date is None) and (race_type is None):
            time_input = race_time.group(2)
            score_input = score.group(2)
            team_input = team_name.group(2)

            data_list = f'q|time_score_team|{time_input}_{score_input}_{team_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()
        elif (team_name is None) and (race_time is None):
            type_input = race_type.group(2)
            date_input = date.group(2)
            score_input = score.group(2)

            data_list = f'q|type_date_score|{type_input}_{date_input}_{score_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()
        elif (score is None) and (race_time is None):
            type_input = race_type.group(2)
            date_input = date.group(2)
            team_input = team_name.group(2)

            data_list = f'q|type_date_team|{type_input}_{date_input}_{team_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()
        elif (date is None) and (race_time is None):
            type_input = race_type.group(2)
            score_input = score.group(2)
            team_input = team_name.group(2)

            data_list = f'q|type_score_team|{type_input}_{score_input}_{team_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()
        elif (race_type is None) and (race_time is None):
            date_input = date.group(2)
            score_input = score.group(2)
            team_input = team_name.group(2)

            data_list = f'q|date_score_team|{date_input}_{score_input}_{team_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()

        elif team_name is None:
            time_input = race_time.group(2)
            type_input = race_type.group(2)
            date_input = date.group(2)
            score_input = score.group(2)

            data_list = f'q|time_type_date_score|{time_input}_{type_input}_{date_input}_{score_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()
        elif score is None:
            time_input = race_time.group(2)
            type_input = race_type.group(2)
            date_input = date.group(2)
            team_input = team_name.group(2)

            data_list = f'q|time_type_date_team|{time_input}_{type_input}_{date_input}_{team_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()
        elif date is None:
            time_input = race_time.group(2)
            type_input = race_type.group(2)
            score_input = score.group(2)
            team_input = team_name.group(2)

            data_list = f'q|time_type_score_team|{time_input}_{type_input}_{score_input}_{team_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()
        elif race_type is None:
            time_input = race_time.group(2)
            date_input = date.group(2)
            score_input = score.group(2)
            team_input = team_name.group(2)

            data_list = f'q|time_date_score_team|{time_input}_{date_input}_{score_input}_{team_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()
        elif race_time is None:
            type_input = race_type.group(2)
            date_input = date.group(2)
            score_input = score.group(2)
            team_input = team_name.group(2)

            data_list = f'q|type_date_score_team|{type_input}_{date_input}_{score_input}_{team_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()
        else:
            time_input = race_time.group(2)
            type_input = race_type.group(2)
            date_input = date.group(2)
            score_input = score.group(2)
            team_input = team_name.group(2)

            data_list = f'q|time_type_date_score_team|{time_input}_{type_input}_{date_input}_{score_input}_{team_input}'

            self.query_thread = TCPClient(data_list)
            self.query_thread.display_signal.connect(self.query_response)
            self.query_thread.start()

    def query_response(self, response):
        response = response.split('|')
        if response[0] == 'False':
            """
            If the server cannot receive the message, then it will return a list like 'False|error message'
            """
            try:
                QMessageBox.information(self, 'Error', response[-1])
            except Exception as error:
                print('Error %s' % error)
        else:
            rows = self.tableWidget.rowCount()
            columns = self.tableWidget.columnCount()
            for row in range(rows):
                for column in range(columns):
                    self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(''))
            data = response[-1]
            data_list = data.split('&')
            x = 0
            for row in data_list:
                row_data = row.split('_')
                y = 0
                for column in row_data:
                    self.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(column)))
                    y += 1
                x += 1


import Source_rc  # Load image

if __name__ == '__main__':
    app = QApplication(sys.argv)

    interface = UserInterface()
    interface.show()
    sys.exit(app.exec_())
