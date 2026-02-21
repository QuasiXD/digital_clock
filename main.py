import sys
from PyQt6.QtWidgets import QWidget,QApplication,QLabel,QVBoxLayout
from PyQt6.QtCore import QTimer,QTime,Qt

class DigitalClock(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec())