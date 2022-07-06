from curses import window
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QMainWindow, QApplication


class MaqinWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self);

        central_widget = QWidget()
        self.centralWidget(QWidget(self))
        


if __name__ == "__main__":
    import sys

    app = QApplication([])
    
    window = MaqinWindow()
    window.show()

    sys.exit(app.exec_())
