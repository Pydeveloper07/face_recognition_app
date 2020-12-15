from ControllerLogin import ControllerLoginWindow
from FaceRecognition import FaceRecognitionWindow
from Dashboard import DashboardWindow
from PyQt5.QtWidgets import QApplication
import sys
import threading
import BrainOfFront

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

    def load_login_window(self):
        window_1 = ControllerLoginWindow()
        sys.exit(self.app.exec_())



    def load_camera_window(self, username):
        window_2 = FaceRecognitionWindow(username)



    def load_dashboard_window(self, name,surname, id):
        window_1 = DashboardWindow(name, surname, id)
#  sys.exit(self.app.exec_())
