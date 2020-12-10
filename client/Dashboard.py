from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QLabel, QToolBar, \
    QPushButton, QWidget, QSpacerItem, QDialog, QStackedWidget
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui
from models import subject_list

class DashboardWindow(QWidget):
    def __init__(self, first_name="", last_name=""):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.subject_list = []
        self.init_subject_list()
        self.stacked_widget = QStackedWidget(self)
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)
        self.init_ui()
        self.init_topbar()
        self.init_stacked_windows()

    def init_subject_list(self):
        for subject in subject_list:
            self.subject_list.append(subject["name"])

    def init_ui(self):
        desktop = QApplication.desktop()
        screen_rect = desktop.screenGeometry()
        window_w = screen_rect.width()
        window_h = screen_rect.height()
        self.setGeometry(0, 0, window_w, window_h)
        self.setWindowTitle("Dashboard")
        self.show()

    def init_topbar(self):
        hbox = QHBoxLayout()
        w_label = QLabel("Welcome, {} {}".format(self.first_name, self.last_name))
        w_label.setFont(QtGui.QFont("Sanserif", 18, 450))
        w_label.setAlignment(QtCore.Qt.AlignCenter)
        logout_btn = QPushButton("Log Out")
        logout_btn.setIcon(QtGui.QIcon("img/logout.png"))
        logout_btn.setFixedHeight(40)
        logout_btn.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        hbox.addWidget(w_label)
        hbox.addWidget(logout_btn)
        self.vbox.addLayout(hbox)

    def init_stacked_windows(self):
        self.vbox.addWidget(self.stacked_widget)
        for subject in subject_list:
            page = QWidget()
            vbox = QVBoxLayout()
            page.setLayout(vbox)

            label_header = QLabel(subject["name"].upper())
            label_header.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
            label_header.setAlignment(QtCore.Qt.AlignCenter)
            label_header.setStyleSheet("font-size: 18pt; color:blue; font-weight:bold; letter-spacing:5px;")

            label_content = QLabel("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor "
                                   "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud "
                                   "exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute "
                                   "irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
                                   "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui "
                                   "officia deserunt mollit anim id est laborum.")
            label_content.setWordWrap(True)
            close_btn = QPushButton("Close this subject")
            close_btn.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
            vbox.addWidget(label_header)
            vbox.addWidget(label_content)
            vbox.addWidget(close_btn, alignment=QtCore.Qt.AlignRight)
            self.stacked_widget.insertWidget(subject["id"], page)