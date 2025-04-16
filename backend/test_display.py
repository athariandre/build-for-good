import sys
from PyQt5.QtWidgets import QApplication
from ui.display import Display

def main():
    app = QApplication(sys.argv)
    display = Display()
    display.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()