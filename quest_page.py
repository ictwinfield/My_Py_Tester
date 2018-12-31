import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5 import QtGui
from PyQt5.QtCore import *

class Quest_Page(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # self.resize(500, 300)
        self.setFixedSize(700, 300)
        # Set up the look of the page
        self.vid_btn = QPushButton('Video')
        self.hnt_btn = QPushButton('Hint')
        self.lst_btn = QPushButton('Last')
        self.sub_btn = QPushButton('Submit')
        self.nxt_btn = QPushButton('Next')

        self.qu_img  = QLabel()
        self.qu_img.setPixmap(QtGui.QPixmap('quest0.png'))
        self.qu_img.setAlignment(Qt.AlignCenter)
        self.ans_txt = QLineEdit()

        self.lV_box = QVBoxLayout()
        self.lV_box.addWidget(self.vid_btn)
        self.lV_box.addWidget(self.hnt_btn)
        self.lV_box.addWidget(self.lst_btn)

        self.h_box = QHBoxLayout()
        self.h_box.addWidget(self.sub_btn)
        self.h_box.addWidget(self.nxt_btn)

        self.rV_box = QVBoxLayout()
        self.rV_box.addWidget(self.qu_img)
        self.rV_box.addWidget(self.ans_txt)
        self.rV_box.addLayout(self.h_box)

        self.page = QHBoxLayout()
        self.page.addLayout(self.lV_box)
        self.page.addLayout(self.rV_box)

        self.setLayout(self.page)

        # Set up the functionality of the page
        self.nxt_btn.setDisabled(True)
        self.sub_btn.clicked.connect(self.submit_clk)

    def submit_clk(self):
        self.nxt_btn.setDisabled(False)
app = QApplication(sys.argv)

window = Quest_Page()
window.show()

sys.exit(app.exec_())
