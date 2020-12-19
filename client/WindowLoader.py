from ControllerLogin import ControllerLoginWindow
from FaceRecognition import FaceRecognitionWindow
from Dashboard import DashboardWindow
from PyQt5.QtWidgets import QApplication
import sys
import threading
import BrainOfFront
import camera


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
        # window_2 = FaceRecognitionWindow(username)
        return camera.takePhoto()

    def load_dashboard_window(self, name, surname, id):
        self.window = DashboardWindow(name, surname, id)

    def start(self):
        self.load_login_window()
        sys.exit(self.app.exec_())
