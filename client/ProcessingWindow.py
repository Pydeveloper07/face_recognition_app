import os
import time

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QMessageBox

import WindowLoader
from util_funcs import face_recognition


class MyThread(QThread):

    change_value = pyqtSignal(dict)

    def __init__(self, username, name, namePic):
        self.username = username
        self.name = name
        self.namePic = namePic
        super().__init__()

    def run(self):
        time.sleep(2)
        response = face_recognition(self.username, self.namePic)
        os.remove(self.namePic)
        self.change_value.emit(response)


class ProcessingWindow(QDialog):
    def __init__(self, username, name, namePic):
        super().__init__()
        self.username = username
        self.name = name
        self.namePic = namePic

        self.window_loader = WindowLoader.WindowManager.get_instance()
        self.setWindowTitle("Your photo is being processed")
        self.setGeometry(700, 300, 600, 450)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        vbox = QVBoxLayout()
        self.label = QLabel()
        self.movie = QMovie("img/processing.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        self.show()
        self.startThread()

    def startThread(self):
        self.thread = MyThread(self.username, self.name, self.namePic)
        self.thread.change_value.connect(self.processResponse)
        self.thread.start()

    def processResponse(self, response):
        if response['result'] == "ok":
            f_name, l_name = self.name.split(' ')
            self.window_loader.load_dashboard_window(f_name, l_name, self.username)
            self.close()
        else:
            self.show_error("Authentication Error",
                            f"You are not a student with ID {self.username}. Get the fuck out of here")

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        if os.path.isfile(self.namePic):
            os.remove(self.namePic)
        super().closeEvent(a0)

    def show_error(self, text, informative_text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(text)
        msg.setInformativeText(informative_text)
        msg.setStandardButtons(QMessageBox.Close)
        retval = msg.exec_()
        self.window_loader.load_login_window()
        self.close()
