from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QButtonGroup, QFrame, QGridLayout, QHBoxLayout, QLabel, QPushButton, \
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget

import WindowLoader
import util_funcs
from MediaPlayer import MediaPlayer
from models import subject_list, video_file


# subject_list = []


class DashboardWindow(QWidget):
    def __init__(self, first_name="", last_name="", username=""):
        super().__init__()
        # uncomment when database is created
        # global subject_list
        # resp = util_funcs.get_subject_list(username)
        # if resp['status'] == 'ok':
        #     subject_list = resp['subjects']

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.window_loader = WindowLoader.WindowManager.get_instance()
        self.subject_list = []
        self.init_subject_list()
        self.stacked_widget = QStackedWidget(self)
        self.vbox = QVBoxLayout()
        self.btn_group = QButtonGroup()
        self.setLayout(self.vbox)
        self.init_ui()
        self.init_topbar()
        self.init_stacked_windows()
        self.init_home()
        self.stacked_widget.setCurrentIndex(len(subject_list))

        self.current_subject_id = -1

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
        logout_btn.clicked.connect(self.log_out)
        hbox.addWidget(w_label)
        hbox.addWidget(logout_btn)
        self.vbox.addLayout(hbox)

    def init_stacked_windows(self):
        self.vbox.addWidget(self.stacked_widget)
        for subject in subject_list:
            page = QWidget()
            page.setStyleSheet("background-color:white")
            vbox = QVBoxLayout()
            page.setLayout(vbox)
            frame = QFrame()
            frame.setStyleSheet("border: 2px solid blue; padding: 2em;")
            f_vbox = QVBoxLayout()
            frame.setLayout(f_vbox)

            label_header = QLabel(subject["name"].upper())
            label_header.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
            label_header.setAlignment(QtCore.Qt.AlignCenter)
            label_header.setStyleSheet("font-size: 18pt; color:#e0562f; font-weight:bold; letter-spacing:5px;")

            f_label_topic = QLabel("Week 11 topic {}".format(subject["name"]).upper())
            f_label_topic.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
            f_label_topic.setStyleSheet("border:none; padding:5px; border-bottom: 3px solid blue;"
                                        "font-size: 16pt; color:blue; font-weight:bold; letter-spacing:10px;")
            f_video_player = MediaPlayer(video_file)
            f_video_player.setObjectName('player')
            # f_label_content = QLabel(subject["content"])
            # f_label_content.setWordWrap(True)
            # f_label_content.setAlignment(QtCore.Qt.AlignTop)
            # f_label_content.setStyleSheet("border:none; padding:10px 100px; font-size:12pt;")

            close_btn = QPushButton("Close this subject")
            close_btn.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
            close_btn.setFixedHeight(60)
            close_btn.setIcon(QtGui.QIcon("img/close.png"))
            close_btn.setIconSize(QtCore.QSize(40, 40))
            close_btn.clicked.connect(self.close_subject_frame)

            vbox.addWidget(label_header)
            vbox.addWidget(frame)
            f_vbox.addWidget(f_label_topic, alignment=QtCore.Qt.AlignHCenter)
            f_vbox.addWidget(f_video_player, alignment=QtCore.Qt.AlignHCenter)
            # f_vbox.addWidget(f_label_content)
            vbox.addWidget(close_btn, alignment=QtCore.Qt.AlignRight)
            self.stacked_widget.insertWidget(subject["id"], page)

    def close_subject_frame(self):

        subject_id = self.stacked_widget.currentIndex()
        username = self.username
        widget = self.stacked_widget.currentWidget()
        player = widget.findChild(MediaPlayer, 'player')
        player.stop()

        # Use above variables to set how much time user spent for this subject
        util_funcs.exit_course(username, subject_id)

        self.current_subject_id = -1
        self.stacked_widget.setCurrentIndex(len(subject_list))

    def init_home(self):
        page = QWidget()
        page.setStyleSheet("background-color:white")
        vbox = QVBoxLayout()
        page.setLayout(vbox)
        label_header = QLabel("All courses".upper())
        label_header.setStyleSheet("font-weight:bold; font-size: 20pt; color:green;"
                                   "letter-spacing: 5px")
        label_header.setAlignment(QtCore.Qt.AlignCenter)
        label_header.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        vbox.addWidget(label_header)
        grid = QGridLayout()
        grid.setSpacing(20)
        vbox.addLayout(grid)
        row = 0
        col = 0
        for i in range(len(subject_list)):
            frame = QFrame()
            frame.setStyleSheet("border: 3px solid #4589ff; border-radius:10px")
            f_vbox = QVBoxLayout()
            frame.setLayout(f_vbox)
            f_hbox = QHBoxLayout()
            # pixmap = QtGui.QPixmap(subject_list[i]["image"])
            # pixmap.setDevicePixelRatio(8)
            # label_pix = QLabel()
            # label_pix.setStyleSheet("border:none")
            # label_pix.setPixmap(pixmap)
            # label_pix.setMaximumSize(120, 120)
            label_title = QLabel(subject_list[i]["name"])
            label_title.setWordWrap(True)
            label_title.setStyleSheet("border:none; font-size: 20pt; letter-spacing:3px;"
                                      "color:#e0562f; font-weight:bold")
            label_title.setAlignment(QtCore.Qt.AlignCenter)
            label_title.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
            # f_hbox.addWidget(label_pix)
            f_hbox.addWidget(label_title)
            f_vbox.addLayout(f_hbox)
            label_prof = QLabel("Professor: {}".format(subject_list[i]["professor"]))
            label_prof.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
            label_prof.setStyleSheet("border:none; border-radius: 0; border-top:1px solid #4589ff;")
            f_vbox.addWidget(label_prof)
            label_section = QLabel("Section: {:03}".format(subject_list[i]["section"]))
            label_section.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
            label_section.setStyleSheet("border:none")
            f_vbox.addWidget(label_section)
            label_desc = QLabel(subject_list[i]["description"])
            label_desc.setWordWrap(True)
            label_desc.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
            label_desc.setStyleSheet("border:none")
            f_vbox.addWidget(label_desc)
            push_btn = QPushButton("Go to the course".upper())
            push_btn.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
            push_btn.setStyleSheet("border:none; border-radius: 3px; padding: 8px; background: blue;"
                                   "color:white")
            self.btn_group.addButton(push_btn, subject_list[i]["id"])
            f_vbox.addWidget(push_btn, alignment=QtCore.Qt.AlignCenter)
            f_vspacer = QSpacerItem(20, 40, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
            f_vbox.addSpacerItem(f_vspacer)
            grid.addWidget(frame, row, col)
            if col == 1:
                col = 0
                row += 1
            else:
                col += 1
        self.btn_group.buttonClicked[int].connect(self.init_page)
        self.stacked_widget.insertWidget(len(self.subject_list), page)

    def init_page(self, id):
        username = self.username
        self.current_subject_id = id
        resp = util_funcs.enter_course(username, id)
        self.stacked_widget.setCurrentIndex(id)

    def log_out(self):
        username = self.username
        self.window_loader.load_login_window()
        util_funcs.logout(username, self.current_subject_id)
        self.close()

    def closeEvent(self, event):
        self.window_loader.CloseConnection()
        event.accept()
