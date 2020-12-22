from PyQt5 import QtCore
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QStyle, \
    QSlider, QHBoxLayout

class MediaPlayer(QWidget):
    def __init__(self, file):
        super().__init__()
        self.setWindowTitle("Media Player")
        self.setMaximumSize(640, 480)
        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        video_widget = QVideoWidget()

        self.play_button = QPushButton()
        self.play_button.setStyleSheet("border:none; padding:0")
        self.play_button.setEnabled(False)
        self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.play_button.clicked.connect(self.play)

        self.position_slider = QSlider(QtCore.Qt.Horizontal)
        self.position_slider.setStyleSheet("border:none; padding:0")
        self.position_slider.setRange(0, 0)
        self.position_slider.sliderMoved.connect(self.set_position)

        control_layout = QHBoxLayout()
        control_layout.setContentsMargins(0, 0, 0, 0)
        control_layout.addWidget(self.play_button)
        control_layout.addWidget(self.position_slider)

        layout = QVBoxLayout()
        layout.addWidget(video_widget)
        layout.addLayout(control_layout)

        self.setLayout(layout)

        self.media_player.setVideoOutput(video_widget)
        self.media_player.stateChanged.connect(self.media_state_changed)
        self.media_player.positionChanged.connect(self.position_changed)
        self.media_player.durationChanged.connect(self.duration_changed)
        self.init_media(file)

    def init_media(self, file):
        self.media_player.setMedia(
            QMediaContent(QtCore.QUrl.fromLocalFile(file)))
        self.play_button.setEnabled(True)

    def play(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.pause()
        else:
            self.media_player.play()

    def media_state_changed(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.play_button.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.play_button.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay))

    def position_changed(self, position):
        self.position_slider.setValue(position)

    def duration_changed(self, duration):
        self.position_slider.setRange(0, duration)

    def set_position(self, position):
        self.media_player.setPosition(position)