from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QButtonGroup, QTableWidget, QTableWidgetItem, \
    QGridLayout, QGroupBox
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from datetime import datetime
import teacherBoardController
import sys


class TeacherBoard(QWidget):
    def __init__(self, fullname, username):
        super().__init__()
        self.fullname = fullname
        self.username = username
        self.controller = teacherBoardController.TeachBoardController()
        self.courses = None
        self.course_id = None
        self.student_id = None
        self.initMainUI()
        self.initTopBar()
        self.initMainWidgets()
        self.initCourses()
        self.initStudentWidgets()
        self.initDetailsWidgets()
        self.show()

    def initMainUI(self):
        self.setGeometry(200, 200, 1120, 720)
        self.setWindowTitle("Dashboard")
        self.mainVBox = QVBoxLayout()
        self.setLayout(self.mainVBox)
        self.mainVBox.setAlignment(QtCore.Qt.AlignTop)
        self.setStyleSheet("background-color: #fff8f8;")

    def initTopBar(self):
        hbox = QtWidgets.QHBoxLayout()
        self.goBackButton = QPushButton("Go Back")
        self.goBackButton.setStyleSheet("font-family: 'Sanserif'; font-size: 17px; border: 2px solid #80ADAD;")
        self.goBackButton.setIcon(QIcon("img/back_btn.png"))
        self.goBackButton.setFixedSize(100, 40)
        self.goBackButton.setHidden(True)
        self.goBackButton.clicked.connect(self.handleGoBackButton)
        self.mainLabel = QLabel(f"Welcome, {self.fullname}")
        self.mainLabel.setStyleSheet("font-family: 'Sanserif'; font-size: 35px; font-weight: 5000; color: #464A3C;")
        self.mainLabel.setAlignment(QtCore.Qt.AlignCenter)
        logout_btn = QPushButton("Log Out")
        logout_btn.setIcon(QIcon("img/logout.png"))
        logout_btn.setIconSize(QtCore.QSize(30, 30))
        logout_btn.setFixedSize(100, 40)
        logout_btn.setStyleSheet("font-family: 'Sanserif'; font-size: 17px; border: 2px solid #80ADAD;")
        logout_btn.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        logout_btn.clicked.connect(self.logOut)
        hbox.addWidget(self.goBackButton)
        hbox.addWidget(self.mainLabel)
        hbox.addWidget(logout_btn)
        self.mainVBox.addLayout(hbox)

    def initMainWidgets(self):
        self.coursesWidget = QWidget()
        self.studentsWidget = QWidget()
        self.studentsWidget.setHidden(True)
        self.detailsWidget = QWidget()
        self.detailsWidget.setHidden(True)
        self.mainVBox.addWidget(self.coursesWidget)
        self.mainVBox.addWidget(self.studentsWidget)
        self.mainVBox.addWidget(self.detailsWidget)

    def initStudentWidgets(self):
        self.studentsVBox = QVBoxLayout()
        self.studentsTable = QTableWidget()
        self.studentsVBox.addWidget(self.studentsTable)
        self.studentsWidget.setLayout(self.studentsVBox)
        self.studentsTable.setColumnCount(5)
        self.studentsTable.setStyleSheet("font-family: 'Times New Roman'; font-size: 22px;")

    def initDetailsWidgets(self):
        self.detailsVBox = QVBoxLayout()
        self.detailsTable = QTableWidget()
        self.detailsVBox.addWidget(self.detailsTable)
        self.detailsWidget.setLayout(self.detailsVBox)
        self.detailsTable.setColumnCount(4)
        self.detailsTable.setStyleSheet("font-family: 'Times New Roman'; font-size: 25px;")

    def initCourses(self):
        resp = self.controller.get_teacher_courses(self.username)
        if resp['result'] == 'error':
            return
        self.courses = resp['courses']
        self.coursesGrid = QGridLayout()
        self.coursesButtonGroup = QButtonGroup()
        self.coursesButtonGroup.buttonClicked[int].connect(self.handleGoToCourseButton)
        counter = 0
        for course in self.courses:
            grp = QGroupBox()
            vbox = QVBoxLayout()
            s_label = QLabel(course["name"])
            s_label.setStyleSheet("font-family: 'Times New Roman'; font-size: 45px;")
            p_label = QLabel("Professor: " + self.fullname)
            p_label.setStyleSheet("font-family: 'Sanserif'; font-size: 20px;")
            n_label = QLabel("Number of Students: " + str(course["student_count"]))
            n_label.setStyleSheet("font-family: 'Sanserif'; font-size: 20px;")
            btn = QPushButton("Go To Course")
            btn.setStyleSheet("font-family: 'Sanserif'; font-size: 30px; border: 1px solid #80adad; border-radius: 25px; backgorund-color: #80adad;")
            btn.setFixedSize(300, 60)
            self.coursesButtonGroup.addButton(btn, course["id"])
            vbox.addWidget(s_label)
            vbox.addWidget(p_label)
            vbox.addWidget(n_label)
            vbox.addWidget(btn)
            grp.setLayout(vbox)
            grp.setStyleSheet("background-color: #f2f7f7;")
            self.coursesGrid.addWidget(grp, counter // 2, counter % 2)
            counter += 1
        self.coursesWidget.setLayout(self.coursesGrid)

    def initStudentsTable(self):
        self.studentsTable.clear()
        resp = self.controller.get_students_of_course(self.course_id)
        if resp['result'] == 'error':
            return
        students = resp['students']
        self.studentsTable.setRowCount(len(students))
        self.studentsTable.setHorizontalHeaderLabels(['Student ID', 'FullName', 'First Access', 'Last Access', ''])

        self.detailsButtonGroup = QButtonGroup()
        self.detailsButtonGroup.buttonClicked[int].connect(self.handleDetailsButton)

        for row in range(self.studentsTable.rowCount()):
            student = students[row]
            for col in range(0, 5):
                text = "Did Not Access"
                if col == 0:
                    text = f"{student['id']}"
                elif col == 1:
                    text = f"{student['name']}"
                elif col == 2:
                    if student['first_access_date']:
                        text = f"{student['first_access_date']}"
                elif col == 3:
                    if student['last_access_date']:
                        text = f"{student['last_access_date']}"
                else:
                    btn = QPushButton("Details")
                    btn.setStyleSheet("font-size: 20px;")
                    self.detailsButtonGroup.addButton(btn, int(student['id'][1: len(student['id'])]))
                    self.studentsTable.setCellWidget(row, col, btn)
                    break
                item = QTableWidgetItem(text)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.studentsTable.setItem(row, col, item)

        self.studentsTable.setColumnWidth(0, 150)
        self.studentsTable.setColumnWidth(1, 300)
        self.studentsTable.setColumnWidth(2, 250)
        self.studentsTable.setColumnWidth(3, 250)

    def initDetailsTable(self):
        self.detailsTable.clear()
        resp = self.controller.get_students_enter_exit_times(self.course_id, self.student_id)

        if resp['result'] == 'error':
            return

        times = resp['times_list']
        self.detailsTable.setRowCount(len(times))
        self.detailsTable.setHorizontalHeaderLabels(['Date', 'Entered', 'Exited', 'Time Spent'])

        for row in range(self.detailsTable.rowCount()):
            temp = times[row]
            for col in range(0, 4):
                if col == 0:
                    text = f"{temp['enter_time'][0 : 10]}"
                elif col == 1:
                    text = f"{temp['enter_time'][11 : 19]}"
                elif col == 2:
                    text = f"{temp['exit_time'][11 : 19]}"
                else:
                    text = self.timeDiff(temp)
                item = QTableWidgetItem(text)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.detailsTable.setItem(row, col, item)

        self.detailsTable.setColumnWidth(0, 270)
        self.detailsTable.setColumnWidth(1, 320)
        self.detailsTable.setColumnWidth(2, 220)
        self.detailsTable.setColumnWidth(3, 220)

    def handleGoBackButton(self):
        # Checking which widget is not hidden. If Details Widget is open then go back to Students Widget
        if self.studentsWidget.isHidden():
            self.mainLabel.setText("Student List")
            self.student_id = None  # Setting current student to None
            self.detailsWidget.setHidden(True)  # Hide Details Widget
            self.studentsWidget.setHidden(False)  # Show Students Widget
        else:
            self.mainLabel.setText(f"Welcome, {self.fullname}")
            # Executes if the Students Widget is not hidden
            self.course_id = None  # Setting current subject to None
            self.goBackButton.setHidden(True)  # Hide Go Back button
            self.studentsWidget.setHidden(True)  # Hide Students Widget
            self.coursesWidget.setHidden(False)  # Show Courses Widget

    def handleGoToCourseButton(self, course_id):
        self.mainLabel.setText("Student List")
        self.goBackButton.setHidden(False) # Show Go Back button
        # Choosing the course
        self.course_id = course_id
        self.initStudentsTable()  # Initializing the table with students info
        self.coursesWidget.setHidden(True)  # Hide the Courses Widget
        self.studentsWidget.setHidden(False)  # Show Students Widget

    def handleDetailsButton(self, student_id):
        self.student_id = f"u{student_id}"
        self.mainLabel.setText(f"Time Logs of {self.student_id}")
        self.initDetailsTable()  # Initialing the table with chosen student's logs
        self.studentsWidget.setHidden(True)  # Hide Students Widget
        self.detailsWidget.setHidden(False)  # Show Details Widget

    # Returns the time difference between two time passed in a list
    @staticmethod
    def timeDiff(accessList):
        d1 = datetime.strptime(accessList['enter_time'], "%Y-%m-%d %H:%M:%S")
        d2 = datetime.strptime(accessList['exit_time'], "%Y-%m-%d %H:%M:%S")
        return str(d2 - d1)

    # Ends the program
    @staticmethod
    def logOut():
        sys.exit()
