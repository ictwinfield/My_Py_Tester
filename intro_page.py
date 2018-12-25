import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

class Intro_Page(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Introduction')
        self.lbl1 = QLabel('You can pick you topic and level')
        self.lbl2 = QLabel('If you are not sure how to do a question you can check out the video')
        self.lbl3 = QLabel('The hint will help with the format of your answer')
        self.btn = QPushButton('Next')

        self.h_box = QHBoxLayout()
        self.h_box.addStretch()
        self.h_box.addWidget(self.btn)

        self.v_box = QVBoxLayout()
        self.v_box.addWidget(self.lbl1)
        self.v_box.addWidget(self.lbl2)
        self.v_box.addWidget(self.lbl3)
        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)


app = QApplication(sys.argv)

window = Intro_Page()
window.show()

sys.exit(app.exec_())
