import sys
import threading

from PyQt5.QtWidgets import QApplication

from ControllerLogin import ControllerLoginWindow
from Dashboard import DashboardWindow
from FaceRecognition import FaceRecognitionWindow
from teacherBoard import TeacherBoard


class WindowManager:
    __instance = None

    @staticmethod
    def get_instance():
        if not WindowManager.__instance:
            with threading.Lock():
                if not WindowManager.__instance:
                    WindowManager()
        return WindowManager.__instance

    def __init__(self):
        if WindowManager.__instance:
            raise Exception("This class is a Singleton")
        else:
            WindowManager.__instance = self
            self.app = QApplication(sys.argv)
        self.window = None

    def load_login_window(self):
        self.window = ControllerLoginWindow()

    def load_camera_window(self, username):
        self.window = FaceRecognitionWindow(username)

    def load_dashboard_window(self, name, surname, id):
        self.window = DashboardWindow(name, surname, id)

    def load_teacher_board_window(self, name, username):
        self.window = TeacherBoard(name, username)

    def start(self):
        self.load_login_window()
        sys.exit(self.app.exec_())
