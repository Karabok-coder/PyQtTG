from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QMainWindow, QApplication, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class MaqinWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self);

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        gridVMain = QVBoxLayout(central_widget)
        self.btn = QPushButton('Моя первая кнопка', central_widget)
        self.btn.clicked.connect(self.print)
        gridVMain.addWidget(self.btn)

        icon = QIcon("1.png")
        self.btn.setIcon(icon)

        self.btn.setIconSize(QSize(100, 100))

    def print(self):
        print('Привет, я говорящая кнопка!')


if __name__ == "__main__":
    import sys
    app = QApplication([])
    window = MaqinWindow()
    window.show()
    sys.exit(app.exec_())


