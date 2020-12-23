from PyQt5.QtWidgets import QApplication, \
    QDialog, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt5 import uic, QtCore, QtGui
import BrainOfFront
import json
import WindowLoader
import base64
import pathlib


class ControllerLoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.window_loader = WindowLoader.WindowManager.get_instance()
        uic.loadUi("LoginWindow.ui", self)
        self.width = 800
        self.height = 500
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.window_h = self.screenRect.height()
        self.window_w = self.screenRect.width()
        self.vbox_left = self.findChild(QVBoxLayout, "vbox_left")
        self.logo_label = self.findChild(QLabel, "logo_label")
        self.username_field = self.findChild(QLineEdit, "username_field")
        self.fdbck_uname_label = self.findChild(QLabel, "feedback_username")
        self.fdbck_passw_label = self.findChild(QLabel, "feedback_password")
        self.password_field = self.findChild(QLineEdit, "password_field")
        self.password_field.setEchoMode(QLineEdit.Password)
        self.submit_btn = self.findChild(QPushButton, "submit_btn")
        self.init_ui()

    def init_ui(self):
        self.setGeometry((self.window_w - self.width) / 2, (self.window_h - self.height) / 2, self.width, self.height)
        self.vbox_left.setAlignment(self.logo_label, QtCore.Qt.AlignCenter)
        self.submit_btn.clicked.connect(self.on_submit)
        self.show()

    def on_submit(self):
        username = self.username_field.text()
        password = self.password_field.text()
        username_err = ""
        password_err = ""
        if not username or not password:
            if not username:
                username_err = "This field is required"
            if not password:
                password_err = "This field is required"
            self.fdbck_uname_label.setText(username_err)
            self.fdbck_passw_label.setText(password_err)
            return
        else:
            a = self.send_image()
            auth = self.authenticate(username, password)

            if auth['result'] == "ok":
                self.window_loader.load_camera_window(auth['name'])
                self.close()
            else:
                self.show_error_msg("Wrong Credentials!")
                self.username_field.setText("")
                self.password_field.setText("")
                return

    # Authentication goes here
    def authenticate(self, username, password):
        dictInput = {'action': 'login',
                     'username': username,
                     'password': password}

        BrainOfFront.SendData(json.dumps(dictInput))

        retValue = BrainOfFront.ReadData()
        dictOutput = json.loads(retValue)
        return dictOutput

    def show_error_msg(self, msg):
        msgbox = QMessageBox(self)
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setText(msg)
        msgbox.setStandardButtons(QMessageBox.Ok)
        retval = msgbox.exec_()

    def send_image(self):
        with open(pathlib.Path().absolute() / 'img/db.jpg', 'rb') as image_file:
            image_string = str(base64.b64encode(image_file.read()))

        image_string = image_string.replace("'", "")
        if image_string[0] == 'b':
            image_string = image_string.replace("b", "", 1)

        dict_input = {'action': 'face_recognition',
                      'student_id': 'u1810087',
                      'photo': image_string}

        BrainOfFront.SendData(json.dumps(dict_input))

        ret_value = BrainOfFront.ReadData()
        dict_output = json.loads(ret_value)
        return dict_output

    #
    # def closeEvent(self, event):
    #     BrainOfFront.CloseAll()
    #     event.accept()
