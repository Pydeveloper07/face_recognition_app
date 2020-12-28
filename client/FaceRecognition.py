import os
import pathlib
import time

from PyQt5 import QtGui
from PyQt5.QtMultimedia import QCamera, QCameraImageCapture, QCameraInfo
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtWidgets import QAction, QApplication, QComboBox, QErrorMessage, QMainWindow, QMessageBox, QStatusBar, \
    QToolBar

import WindowLoader
from util_funcs import face_recognition


class FaceRecognitionWindow(QMainWindow):
    def __init__(self, username):
        super().__init__()  # setting geometry
        self.username = username
        self.window_loader = WindowLoader.WindowManager.get_instance()
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.window_h = self.screenRect.height()
        self.window_w = self.screenRect.width()
        self.width = 800
        self.height = 600
        self.setGeometry((self.window_w - self.width) / 2, (self.window_h - self.height) / 2, self.width, self.height)
        self.setStyleSheet("background : lightgrey;")
        self.available_cameras = QCameraInfo.availableCameras()
        if not self.available_cameras:
            self.show_error("Camera not found!",
                            "You don't have any available webcam! Please connect one and try again!")

        self.status = QStatusBar()
        self.status.setStyleSheet("background : white;")

        # adding status bar to the main window
        # self.setStatusBar(self.status)

        self.save_path = pathlib.Path().absolute()
        self.viewfinder = QCameraViewfinder()
        self.viewfinder.show()
        self.setCentralWidget(self.viewfinder)

        self.select_camera(0)

        toolbar = QToolBar("Camera Tool Bar")
        self.addToolBar(toolbar)

        click_action = QAction("Capture", self)
        click_action.setIcon(QtGui.QIcon("img/camera-2.png"))
        click_action.triggered.connect(self.capture_photo)
        toolbar.addAction(click_action)

        # change_folder_action = QAction("Change save location", self)
        # change_folder_action.setStatusTip("Change folder where picture will be saved saved.")
        # change_folder_action.setToolTip("Change save location")
        # change_folder_action.triggered.connect(self.change_folder)
        # toolbar.addAction(change_folder_action)

        self.capture.imageCaptured.connect(self.process_captured_image)
        camera_selector = QComboBox()
        camera_selector.setToolTip("Select Camera")
        camera_selector.setToolTipDuration(2500)
        camera_selector.addItems([camera.description()
                                  for camera in self.available_cameras])
        camera_selector.currentIndexChanged.connect(self.select_camera)
        toolbar.addWidget(camera_selector)
        toolbar.setStyleSheet("background : #b3fff7;")

        self.setWindowTitle("Face verification")
        self.show()

    def process_captured_image(self, id, img):
        response = self.authenticate(self.namePic)
        os.remove(self.namePic)

        if response['result'] == "ok":
            self.window_loader.load_dashboard_window(self.username, self.username, self.username)
            self.camera.stop()
            self.close()
        else:
            # err = QErrorMessage(self)
            # err.setWindowTitle("Error")
            # err.showMessage("You are not recognized!")
            self.show_error("Authentication Error",
                            f"You are not a student with ID {self.username}. Get the fuck out of here")

    def authenticate(self, img):
        time.sleep(1)
        response = face_recognition(self.username, img)
        return response

    def select_camera(self, i):
        self.camera = QCamera(self.available_cameras[i])
        self.camera.setViewfinder(self.viewfinder)
        self.camera.setCaptureMode(QCamera.CaptureStillImage)
        self.camera.error.connect(lambda: self.alert(self.camera.errorString()))
        self.camera.start()
        self.capture = QCameraImageCapture(self.camera)
        self.capture.error.connect(lambda error_msg, error, msg: self.alert(msg))
        self.current_camera_name = self.available_cameras[i].description()
        self.save_seq = 0

    def capture_photo(self):
        timestamp = time.strftime("%d-%b-%Y-%H_%M_%S")
        self.namePic = "%s.jpg" % (timestamp)

        # capture the image and save it on the save path
        self.capture.capture(os.path.join(self.save_path,
                                          self.namePic))
        self.save_seq += 1

    def show_error(self, text, informative_text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(text)
        msg.setInformativeText(informative_text)
        msg.setStandardButtons(QMessageBox.Close)
        retval = msg.exec_()
        self.close()
        self.window_loader.load_login_window()

    # def change_folder(self):
    #     path = QFileDialog.getExistingDirectory(self, "Picture Location", "")
    #     if path:
    #         self.save_path = path
    #         self.save_seq = 0

    def alert(self, msg):
        error = QErrorMessage(self)
        error.showMessage(msg)

    # def closeEvent(self, event):
    #      BrainOfFront.CloseAll()
    #      event.accept()
