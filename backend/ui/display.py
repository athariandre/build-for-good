from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPalette

class Display:
    def __init__(self):
        self.app = QApplication([])
        self.window = QWidget()
        self.palette = self.window.palette()
        self.window.setWindowTitle('Keep Going')
        self.palette.setColor(QPalette.Window, QColor('white'))
        self.window.setPalette(self.palette)
        self.window.setGeometry(100, 100, 500, 300)

        self.label = QLabel('KEEP GOING')
        self.label.setFont(QFont('Arial', 48, QFont.Bold))
        self.label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.window.setLayout(layout)

    def show(self):
        self.window.show()

    def display_message(self, speedUp=False, slowDown=False):
        if speedUp:
            self.window.setWindowTitle('Speed Up')
            self.palette.setColor(QPalette.Window, QColor('green'))
            text = 'SPEED UP'
            self.label.setStyleSheet("color: white;")
        elif slowDown:
            self.window.setWindowTitle('Slow Down')
            self.palette.setColor(QPalette.Window, QColor('red'))
            text = 'SLOW DOWN'
            self.label.setStyleSheet("color: white;")
        else:
            self.window.setWindowTitle('Keep Going')
            self.palette.setColor(QPalette.Window, QColor('white'))
            text = 'KEEP GOING'
            self.label.setStyleSheet("color: black;")

        self.label.setText(text)
        self.window.setPalette(self.palette)